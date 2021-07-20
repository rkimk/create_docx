from docxtpl import DocxTemplate
from datetime import datetime
from num2t4ru import num2text
import math
expansion = 'docx'
filename = "template"
input_file = f"{filename}.{expansion}"
doc = DocxTemplate(input_file)
nds = 20
sum = 517000
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
           'work' : "ремонту коридоров 3 и 4 этажей учебного корпуса",
           'work_name': "Ремонт коридоров 3 и 4 этажей учебного корпуса",
           'company_work' : "Общество с ограниченной ответственностью «ОПТИМУМ»",
           'company_work_schief' : "генерального директора Бурцева Сергея Владимировича",
           'na_osnovanii' : "Устава",
           'company_work_schief_sm' : "С.В. Бурцев",
           'summ' : f"{round_sum} ({num2text(sum, male_units).rsplit(' ', 1)[0].capitalize()}) {num2text(sum, male_units).rsplit(' ', 1)[-1]} {sum_kop} {num2text(int(sum_kop), female_units).rsplit(' ', 1)[-1]}",
           'nds' : f"в том числе НДС {nds}% - {'{0:,}'.format(int(sum_nds)).replace(',', ' ')} ({num2text(sum_nds, male_units).rsplit(' ', 1)[0].capitalize()}) {num2text(sum_nds, male_units).rsplit(' ', 1)[-1]} {sum_nds_kop} {num2text(int(sum_nds_kop), female_units).rsplit(' ', 1)[-1]}",
           'ist_fin' : 'Государственная программа Рязанской области "Развитие образования и молодежной политики", подпрограмма "Развитие профессионального образования" (на подготовку проектной, сметной документации, на проведение ремонтных работ, работ по благоустройству прилегающих территорий)',
           'company_work_ua' : "390046 г.Рязань пр.Машиностроителей д.7 Лит.А офис Н5",
           'company_work_fa' : "390046 г.Рязань пр.Машиностроителей д.7 Лит.А офис Н5",
           'company_work_inn': "6230087769",
           'company_work_kpp' : "623001001",
           'company_work_rs' : "40702810400000006926",
           'company_work_ks' : "30101810500000000708",
           'company_work_bank' : "ПРИО-Внешторгбанк (ПАО) г.Рязань",
           'company_work_ogrn' : "1156230000211",
           'company_work_bik' : "046126708",
           'company_work_okpo' : "12190684",
           'company_work_mail' : "-",
           'company_work_phone' : "-"
           }
if nds == 0:
    context['nds'] = "НДС не облагается"
doc.render(context)
# doc.save(f'{context["work_name"]}_{datetime.now().strftime("%d.%m.%Y_%H.%M")}.docx')
doc.save(f'{context["work_name"]}.docx')