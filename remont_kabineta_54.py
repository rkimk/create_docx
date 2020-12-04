from docxtpl import DocxTemplate
from datetime import datetime
expansion = 'docx'
filename = "template"
input_file = f"{filename}.{expansion}"
doc = DocxTemplate(input_file)
context = {'work' : "ремонту кабинета №54",
           'work_name': "Ремонт кабинета №54",
           'company_work' : "Общество с ограниченной ответственностью «Стальные конструкции – Сервис»",
           'company_work_schief' : "Бурцева Сергея Владимировича",
           'company_work_schief_sm' : "С.В. Бурцев",
           'summ' : "109 000 (Сто девять тысяч) рублей 00 копеек",
           'nds' : "в том числе НДС 20% - 18 166 (Восемнадцать тысяч сто шестьдесят шесть) рублей 67 копеек",
           'ist_fin' : "средства от приносящей доход деятельности",
           'company_work_ua' : "390046, г. Рязань, проезд Машиностроителей, д.7, Литера А, помещение Н5, офис 2",
           'company_work_fa' : "390046, г. Рязань, проезд Машиностроителей, д.7, Литера А, помещение Н5, офис 2",
           'company_work_inn': "6230086660",
           'company_work_kpp' : "623001001",
           'company_work_rs' : "40702810402020001831",
           'company_work_ks' : "30101810200000000593",
           'company_work_bank' : "АО «АЛЬФА БАНК»",
           'company_work_ogrn' : "1146230005239",
           'company_work_bik' : "044525593",
           'company_work_okpo' : "44893849",
           'company_work_mail' : "-",
           'company_work_phone' : "-"
           }
doc.render(context)
# doc.save(f'{context["work_name"]}_{datetime.now().strftime("%d.%m.%Y_%H.%M")}.docx')
doc.save(f'{context["work_name"]}.docx')