import requests, gc
from bs4 import BeautifulSoup

headers = {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36 OPR/56.0.3051.104'}

def getExpertData(experts_url = 'https://www.intergazcert.ru/register/members/certification-experts/',
                  expert_number_of_lines=450):
    global experts_quantity
    experts_quantity = expert_number_of_lines
    response = requests.get(experts_url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')

    del response
    gc.collect()

    search_lines = ['tr-'+str(i) for i in range(1, expert_number_of_lines + 1)]

    for _ in search_lines:
        line1 = soup.find('tbody')
        line2 = line1.find(class_=_)
        if line2 == None:
            experts_quantity = search_lines.index(_)
            break
        name = line2.find(class_='td-0').text
        date_since = line2.find(class_='td-1').text
        date_until = line2.find(class_='td-2').text
        sphere = line2.find(class_='td-3').text
        okpd_codes = line2.find(class_='td-4').text
        department = line2.find(class_='td-5').text
        extra = line2.find(class_='td-6').text
        yield name,date_since, date_until, sphere, okpd_codes, department, extra

    del soup, line2, search_lines, name, date_since, date_until, sphere, okpd_codes, department, extra
    gc.collect()

def getCertificateData(certificate_url = 'https://www.intergazcert.ru/register/certificates/active/products/',
                       cert_number_of_lines=1700):
    global cert_quantity
    cert_quantity = cert_number_of_lines
    response = requests.get(certificate_url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')

    del response
    gc.collect()

    search_lines = ['tr-'+str(i) for i in range(1, cert_number_of_lines + 1)]

    for _ in search_lines:
        line1 = soup.find('tbody')
        line2 = line1.find(class_=_)
        del line1
        gc.collect
        if line2 == None:
            cert_quantity = search_lines.index(_)
            break

        cert_no = line2.find(class_='td-0').text
        cert_blank = line2.find(class_='td-1').text
        cert_holder_name = line2.find(class_='td-2').text
        cert_holder_adress = line2.find(class_='td-3').text
        cert_holder_contacts = line2.find(class_='td-4').text
        cert_producer_name = line2.find(class_='td-5').text
        cert_producer_adress = line2.find(class_='td-6').text
        cert_producer_contacts = line2.find(class_='td-7').text
        cert_product_name = line2.find(class_='td-8').text
        cert_date_since = line2.find(class_='td-9').text
        cert_date_until = line2.find(class_='td-10').text
        cert_klass = line2.find(class_='td-11').text
        cert_scheme = line2.find(class_='td-12').text
        cert_givenby = line2.find(class_='td-13').text
        cert_dept = line2.find(class_='td-14').text
        cert_extra = line2.find(class_='td-15').text

        yield cert_no, cert_blank, cert_holder_name, cert_holder_adress, \
               cert_holder_contacts, cert_producer_name, cert_producer_adress, \
               cert_producer_contacts, cert_product_name, cert_date_since, \
               cert_date_until, cert_klass, cert_scheme, cert_givenby, cert_dept, cert_extra