from docxtpl import DocxTemplate
from datetime import datetime
expansion = 'docx'
filename = "template"
input_file = f"{filename}.{expansion}"
doc = DocxTemplate(input_file)
context = {'work' : "ремонту коридора 2-го этажа в здании главного учебного корпуса (стены)",
           'work_name': "Ремонт коридора 2-го этажа в здании главного учебного корпуса (стены)",
           'company_work' : "Общество с ограниченной ответственностью «СпецЭлектроМонтаж»",
           'company_work_schief' : "Генерального директора Варина Дмитрия Васильевича",
            'na_osnovanii' : "Устава",
           'company_work_schief_sm' : "Д.В. Варин",
           'summ' : "227 646 (Двести двадцать семь тысяч шестьсот сорок шесть) рублей 00 копеек",
           'nds' : "в том числе НДС 20% - 37 941 (Тридцать семь тысяч девятьсот сорок один) рубль 00 копеек",
           'ist_fin' : "средства от приносящей доход деятельности",
           'company_work_ua' : "390044 Рязанская обл. г.Рязань, ул. Костычева, д.6, 103",
           'company_work_fa' : "390044 Рязанская обл. г.Рязань, ул. Костычева, д.6, 103",
           'company_work_inn': "6229063805",
           'company_work_kpp' : "622901001",
           'company_work_rs' : "40702810112510000905",
           'company_work_ks' : "30101810145250000411",
           'company_work_bank' : "ФИЛИАЛ «ЦЕНТРАЛЬНЫЙ» БАНКА ВТБ (ПАО)",
           'company_work_ogrn' : "1086229003420",
           'company_work_bik' : "044525411",
           'company_work_okpo' : "86600301",
           'company_work_mail' : "-",
           'company_work_phone' : "-"
           }
doc.render(context)
# doc.save(f'{context["work_name"]}_{datetime.now().strftime("%d.%m.%Y_%H.%M")}.docx')
doc.save(f'{context["work_name"]}.docx')