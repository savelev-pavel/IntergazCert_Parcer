"""Собираем данные об экспертах в системе добровольной сертификации ИНТЕРГАЗСЕРТ
    https://www.intergazcert.ru"""

import requests, xlsxwriter
from bs4 import BeautifulSoup

headers = {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36 OPR/56.0.3051.104'}

page_url = 'https://www.intergazcert.ru/register/members/certification-experts/'
search_lines = []

def getExpertData(number_of_lines):
    response = requests.get(page_url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')

    search_lines = ['tr-'+str(i) for i in range(1, number_of_lines + 1)]

    for i in search_lines:
        line1 = soup.find('tbody')
        line2 = line1.find(class_=i)
        if line2 == None: break

        name = line2.find(class_='td-0').text
        date_since = line2.find(class_='td-1').text
        date_until = line2.find(class_='td-2').text
        sphere = line2.find(class_='td-3').text
        okpd_codes = line2.find(class_='td-4').text
        department = line2.find(class_='td-5').text
        extra = line2.find(class_='td-6').text

        #print(f'{name}, аттестат эксперта с {date_since} по {date_until}, область деятельности: {sphere}'
        #     f'\nкоды ОКПД: {okpd_codes}, \nЦОС: {department},\nПримечание:{extra}\n')

        yield name,date_since, date_until, sphere, okpd_codes, department, extra

def expertsWriter(experts_info):
    book = xlsxwriter.Workbook(r'Intergazcert.xlsx')
    page = book.add_worksheet('Experts')

    page.set_column('A:A', 40)
    page.set_column('B:B', 11)
    page.set_column('C:C', 10)
    page.set_column('D:D', 20)
    page.set_column('E:E', 50)
    page.set_column('F:F', 30)
    page.set_column('G:G', 20)

    page.write(0,0,'ФИО')
    page.write(0,1,'с')
    page.write(0,2,'по')
    page.write(0,3,'область')
    page.write(0,4,'ОКПД')
    page.write(0,5,'ЦОС')
    page.write(0,6,'Примечание')

    row = 1
    column = 0
    for item in experts_info:
        page.write(row, column, item[0])
        page.write(row, column+1, item[1])
        page.write(row, column+2, item[2])
        page.write(row, column+3, item[3])
        page.write(row, column+4, item[4])
        page.write(row, column+5, item[5])
        page.write(row, column+6, item[6])
        row+=1
    book.close()

expertsWriter(getExpertData(414))          #number of lines to collect
print('Parcing successful!')



