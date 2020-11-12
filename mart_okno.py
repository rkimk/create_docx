from docxtpl import DocxTemplate
from datetime import datetime
expansion = 'docx'
filename = "template"
input_file = f"{filename}.{expansion}"
doc = DocxTemplate(input_file)
context = {'work' : "замене окна на ПВХ в общежитии",
           'work_name': "Замена окна на ПВХ в общежитии",
           'company_work' : "Общество с ограниченной ответственностью «МАРТ»",
           'company_work_schief' : "Зарубина Алексея Валерьевича",
           'company_work_schief_sm' : "А.В. Зарубин",
           'summ' : "19 600 (Девятнадцать тысяч шестьсот) рублей 00 копеек",
           'nds' : "НДС не облагается",
           'ist_fin' : "средства от приносящей доход деятельности",
           'company_work_ua' : "391962, Рязанская обл, Ряжский р-н, г. Ряжск, ул. Свободы, д. 2а",
           'company_work_fa' : "391962, Рязанская обл, Ряжский р-н, г. Ряжск, ул. Свободы, д. 2а",
           'company_work_inn': "6214007269",
           'company_work_kpp' : "621401001",
           'company_work_rs' : "40702810700010004375",
           'company_work_ks' : "30101810500000000708",
           'company_work_bank' : "Прио-Внешторгбанк (ПАО) г.Рязань",
           'company_work_ogrn' : "1136214000262",
           'company_work_bik' : "046126708",
           'company_work_okpo' : "12200394",
           'company_work_mail' : "okna62-kers82@yandex.ru",
           'company_work_phone' : "8 (4912) 77-79-14, 8 (920) 960-66-60"
           }
doc.render(context)
# doc.save(f'{context["work_name"]}_{datetime.now().strftime("%d.%m.%Y_%H.%M")}.docx')
doc.save(f'{context["work_name"]}.docx')