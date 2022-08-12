"""
Собираем данные об экспертах в системе добровольной сертификации ИНТЕРГАЗСЕРТ
https://www.intergazcert.ru
Вдохновлялся этим видео с youtube:

"""

import getinfo, xlsxwriter

def certificateWriter(certificate_info):
    book = xlsxwriter.Workbook(r'Intergazcert.xlsx')
    page = book.add_worksheet('Certificates')

    page.set_column('A:A', 20)
    page.set_column('B:B', 20)
    page.set_column('C:C', 40)
    page.set_column('D:D', 40)
    page.set_column('E:E', 20)
    page.set_column('F:F', 20)
    page.set_column('G:G', 20)
    page.set_column('H:H', 20)
    page.set_column('I:I', 40)
    page.set_column('J:J', 10)
    page.set_column('K:K', 10)
    page.set_column('L:L', 5)
    page.set_column('M:M', 5)
    page.set_column('N:N', 40)
    page.set_column('O:O', 30)
    page.set_column('P:P', 20)

    page.write(0,0,'№ сертификата')
    page.write(0,1,'№ бланка')
    page.write(0,2,'Заявитель')
    page.write(0,3,'Адрес')
    page.write(0,4,'Контакты')
    page.write(0,5,'Изготовитель')
    page.write(0,6,'Адрес')
    page.write(0,7,'Контакты')
    page.write(0,8,'Продукция')
    page.write(0,9,'с')
    page.write(0,10,'по')
    page.write(0,11,'класс')
    page.write(0,12,'схема')
    page.write(0,13,'ОС')
    page.write(0,14,'ЦОС')
    page.write(0,15,'Примечание')

    row = 1
    column = 0
    for item in certificate_info:
        page.write(row, column, item[0])
        page.write(row, column+1, item[1])
        page.write(row, column+2, item[2])
        page.write(row, column+3, item[3])
        page.write(row, column+4, item[4])
        page.write(row, column+5, item[5])
        page.write(row, column+6, item[6])
        page.write(row, column+7, item[7])
        page.write(row, column+8, item[8])
        page.write(row, column+9, item[9])
        page.write(row, column+10, item[10])
        page.write(row, column+11, item[11])
        page.write(row, column+12, item[12])
        page.write(row, column+13, item[13])
        page.write(row, column+14, item[14])
        page.write(row, column+15, item[15])
        row+=1
        completed_percent = int((((row - 1) / getinfo.cert_quantity) * 100))
        print(f'\r{completed_percent}% completed', end='')
    book.close()

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
    page.write(0,3,'Область')
    page.write(0,4,'ОКПД')
    page.write(0,5,'ЦОС')
    page.write(0,6,'Примечание')

    row = 1
    column = 0
    counter = 0
    for item in experts_info:
        page.write(row, column, item[0])
        page.write(row, column+1, item[1])
        page.write(row, column+2, item[2])
        page.write(row, column+3, item[3])
        page.write(row, column+4, item[4])
        page.write(row, column+5, item[5])
        page.write(row, column+6, item[6])
        row+=1
        completed_percent = int((((row-1) / getinfo.experts_quantity) * 100))
        print(f'\r{completed_percent}% completed',end='')
    book.close()

expertsWriter(getinfo.getExpertData(expert_number_of_lines = 500))
print('\r100% completed', end='')
print('\nИнформация об экспертах сохранена!')
certificateWriter(getinfo.getCertificateData(cert_number_of_lines = 2000))
print('\r100% completed', end='')
print('\nИнформация о действующих сертификатах сохранена!')
print('COMPLETED')


