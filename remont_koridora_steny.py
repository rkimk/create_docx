from docxtpl import DocxTemplate
from datetime import datetime
expansion = 'docx'
filename = "template"
input_file = f"{filename}.{expansion}"
doc = DocxTemplate(input_file)
context = {'work' : "ремонту коридора 2-го этажа в здании главного учебного корпуса (стены)",
           'work_name': "Ремонт коридора 2-го этажа в здании главного учебного корпуса (стены)",
           'company_work' : "Общество с ограниченной ответственностью «РПК СТРОЙ»",
           'company_work_schief' : "Исполнительного директора Кошелевой Светланы Евгеньевны",
           'company_work_schief_sm' : "С.Е. Кошелева",
           'summ' : "227 646 (Двести двадцать семь тысяч шестьсот сорок шесть) рублей 00 копеек",
           'nds' : "в том числе НДС 20% - 37 941 (Тридцать семь тысяч девятьсот сорок один) рубль 00 копеек",
           'ist_fin' : "средства от приносящей доход деятельности",
           'company_work_ua' : "390044 Рязанская обл. г.Рязань, Московское шоссе дом 20, офис 532",
           'company_work_fa' : "390044 Рязанская обл. г.Рязань, Московское шоссе дом 20, офис 532",
           'company_work_inn': "6229092838",
           'company_work_kpp' : "622901001",
           'company_work_rs' : "40702810220300012049",
           'company_work_ks' : "30101810800000000388",
           'company_work_bank' : "Операционный офис «Рязанский» ТКБ БАНК ПАО",
           'company_work_ogrn' : "1196234006451",
           'company_work_bik' : "044525388",
           'company_work_okpo' : "40738477",
           'company_work_mail' : "-",
           'company_work_phone' : "-"
           }
doc.render(context)
# doc.save(f'{context["work_name"]}_{datetime.now().strftime("%d.%m.%Y_%H.%M")}.docx')
doc.save(f'{context["work_name"]}.docx')