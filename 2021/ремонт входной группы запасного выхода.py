from docxtpl import DocxTemplate
from datetime import datetime
from num2t4ru import num2text
import math
expansion = 'docx'
filename = "template"
input_file = f"{filename}.{expansion}"
doc = DocxTemplate(input_file)
nds = 20
sum = 421000
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
           'work' : "ремонту входной группы запасного выхода",
           'work_name': "Ремонт входной группы запасного выхода",
           'company_work' : "Общество с ограниченной ответственностью «АРСЕНАЛСТРОЙ»",
           'company_work_schief' : "директора Корнюхина Игоря Васильевича",
           'na_osnovanii' : "Устава",
           'company_work_schief_sm' : "И.В. Корнюхин",
           'summ' : f"{round_sum} ({num2text(sum, male_units).rsplit(' ', 1)[0]}) {num2text(sum, male_units).rsplit(' ', 1)[-1]} {sum_kop} {num2text(int(sum_kop), female_units).rsplit(' ', 1)[-1]}",
           'nds' : f"в том числе НДС {nds}% - {'{0:,}'.format(int(sum_nds)).replace(',', ' ')} ({num2text(sum_nds, male_units).rsplit(' ', 1)[0]}) {num2text(sum_nds, male_units).rsplit(' ', 1)[-1]} {sum_nds_kop} {num2text(int(sum_nds_kop), female_units).rsplit(' ', 1)[-1]}",
           'ist_fin' : 'Государственная программа Рязанской области "Развитие образования и молодежной политики", подпрограмма "Развитие профессионального образования" (на подготовку проектной, сметной документации, на проведение ремонтных работ, работ по благоустройству прилегающих территорий)',
           'company_work_ua' : "390043 Рязанская обл. г.Рязань, проезд Шабулина, офис 8",
           'company_work_fa' : "390043 Рязанская обл. г.Рязань, проезд Шабулина, офис 8",
           'company_work_inn': "6229097748",
           'company_work_kpp' : "622901001",
           'company_work_rs' : "40702810720300012219",
           'company_work_ks' : "30101810800000000388",
           'company_work_bank' : "ТКБ БАНК ПАО г.Москва",
           'company_work_ogrn' : "1216200003480",
           'company_work_bik' : "044525388",
           'company_work_okpo' : "54975991",
           'company_work_mail' : "-",
           'company_work_phone' : "+7(910)6410493"
           }
if nds == 0:
    context['nds'] = "НДС не облагается"
doc.render(context)
# doc.save(f'{context["work_name"]}_{datetime.now().strftime("%d.%m.%Y_%H.%M")}.docx')
doc.save(f'{context["work_name"]}.docx')