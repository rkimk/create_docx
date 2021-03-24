from docxtpl import DocxTemplate
from datetime import datetime
expansion = 'docx'
filename = "template"
input_file = f"{filename}.{expansion}"
doc = DocxTemplate(input_file)
context = {'work' : "ремонту коридора 2-го этажа в здании главного учебного корпуса (потолок амстронг)",
           'work_name': "Ремонт коридора 2-го этажа в здании главного учебного корпуса (потолок амстронг)",
           'company_work' : "Общество с ограниченной ответственностью «КОРНСТРОЙ»",
           'company_work_schief' : "Директора Корнюхина Игоря Васильевича",
            'na_osnovanii' : "Устава",
           'company_work_schief_sm' : "И.В. Корнюхин",
           'summ' : "218 964 (Двести восемнадцать тысяч девятьсот шестьдесят четыре) рубля 00 копеек",
           'nds' : "в том числе НДС 20% - 36 494 (Тридцать шесть тысяч четыреста девяносто четыре) рубля 00 копеек",
           'ist_fin' : "средства от приносящей доход деятельности",
           'company_work_ua' : "390047 Рязанская обл. г.Рязань, Куйбышевское шоссе, дом 25, стр.1, Литера В, помещение Н 2, офис 1",
           'company_work_fa' : "390047 Рязанская обл. г.Рязань, Куйбышевское шоссе, дом 25, стр.1, Литера В, помещение Н 2, офис 1",
           'company_work_inn': "6230107567",
           'company_work_kpp' : "623001001",
           'company_work_rs' : "40702810602530001846",
           'company_work_ks' : "30101810200000000593",
           'company_work_bank' : "АО «АЛЬФА БАНК»",
           'company_work_ogrn' : "1186234000897",
           'company_work_bik' : "044525593",
           'company_work_okpo' : "24126220",
           'company_work_mail' : "-",
           'company_work_phone' : "-"
           }
doc.render(context)
# doc.save(f'{context["work_name"]}_{datetime.now().strftime("%d.%m.%Y_%H.%M")}.docx')
doc.save(f'{context["work_name"]}.docx')