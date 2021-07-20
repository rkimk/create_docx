from docxtpl import DocxTemplate
from datetime import datetime
from num2t4ru import num2text
import math
expansion = 'docx'
filename = "template"
input_file = f"{filename}.{expansion}"
doc = DocxTemplate(input_file)
nds = 20
sum = 536500.80
round_sum = '{0:,}'.format(int(sum)).replace(',', ' ')
sum_kop = (math.floor(sum*100)%100)
if sum_kop == 0:
    sum_kop = str(sum_kop) + '0'
sum_nds = round(sum*nds/100/(1+nds/100), 2)
sum_nds_kop = (math.floor(sum_nds*100)%100)
if sum_nds_kop == 0:
    sum_nds_kop = str(sum_nds_kop) + '0'
male_units = ((u'рубль', u'рубля', u'рублей'), 'm')
female_units = ((u'копейка', u'копейки', u'копеек'), 'f')
context = {'ikz':"212621500152762150100100480000000244",
           'work' : "сантехнические и отделочные работы в кабинетах 4-го этажа",
           'work_name': "Сантехнические и отделочные работы в кабинетах 4-го этажа",
           'company_work' : "Общество с ограниченной ответственностью «РПК СТРОЙ»",
           'company_work_schief' : "Генерального директора Кошелевой Светланы Евгеньевны",
           'na_osnovanii' : "Приказа №2 от 11.04.2019 г. с правом первой подписи",
           'company_work_schief_sm' : "С.Е. Кошелева",
           'summ' : f"{round_sum} ({num2text(sum, male_units).rsplit(' ', 1)[0]}) {num2text(sum, male_units).rsplit(' ', 1)[-1]} {sum_kop} {num2text(int(sum_kop), female_units).rsplit(' ', 1)[-1]}",
           'nds' : f"в том числе НДС {nds}% - {'{0:,}'.format(int(sum_nds)).replace(',', ' ')} ({num2text(sum_nds, male_units).rsplit(' ', 1)[0]}) {num2text(sum_nds, male_units).rsplit(' ', 1)[-1]} {sum_nds_kop} {num2text(int(sum_nds_kop), female_units).rsplit(' ', 1)[-1]}",
           'ist_fin' : 'Государственная программа Рязанской области "Развитие образования и молодежной политики", подпрограмма "Развитие профессионального образования" (на подготовку проектной, сметной документации, на проведение ремонтных работ, работ по благоустройству прилегающих территорий)',
           'company_work_ua' : "390044 Рязанская обл. г.Рязань, Московское шоссе дом 20, офис 532",
           'company_work_fa' : "390044 Рязанская обл. г.Рязань, Московское шоссе дом 20, офис 532",
           'company_work_inn': "6229092838",
           'company_work_kpp' : "622901001",
           'company_work_rs' : "40702810202000106598",
           'company_work_ks' : "30101810300000000760",
           'company_work_bank' : "Ярославский филиал ПАО «Промсвязьбанк» г.Ярославль",
           'company_work_ogrn' : "1196234006451",
           'company_work_bik' : "047888760",
           'company_work_okpo' : "40738477",
           'company_work_mail' : "rpks2019@mail.ru",
           'company_work_phone' : "-"
           }
if nds == 0:
    context['nds'] = "НДС не облагается"
doc.render(context)
# doc.save(f'{context["work_name"]}_{datetime.now().strftime("%d.%m.%Y_%H.%M")}.docx')
doc.save(f'{context["work_name"]}.docx')