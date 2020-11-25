from docxtpl import DocxTemplate
from datetime import datetime
expansion = 'docx'
filename = "template"
input_file = f"{filename}.{expansion}"
doc = DocxTemplate(input_file)
context = {'work' : 'замене окон на ПВХ',
           'work_name': 'Замена окон на ПВХ',
           'company_work' : "Общество с ограниченной ответственностью «ДЕЛЮКС»",
           'company_work_schief' : "Королева Евгения Александровича",
           'company_work_schief_sm' : "Е.А. Королев",
           'summ' : "79 800 (Семьдесят девять тысяч восемьсот) рублей 00 копеек",
           'nds' : "в том числе НДС 20% - 9 154 (Девять тысяч сто пятьдесят четыре) рубля 83 копейки",
           'ist_fin' : "средства от приносящей доход деятельности",
           'company_work_ua' : "390013, г. Рязань, переулок Шоссейный, д.5, здание Лит.А., офис 4",
           'company_work_fa' : "390013, г. Рязань, переулок Шоссейный, д.5, здание Лит.А., офис 4",
           'company_work_inn': "6234175800",
           'company_work_kpp' : "623401001",
           'company_work_rs' : "440702810553000005458",
           'company_work_ks' : "30101810500000000614",
           'company_work_bank' : "ПАО Сбербанк",
           'company_work_ogrn' : "1186234002855",
           'company_work_bik' : "046126614",
           'company_work_okpo' : "26030062",
           'company_work_mail' : "olga_rgsha@mail.ru",
           'company_work_phone' : "-"
           }
doc.render(context)
# doc.save(f'{context["work_name"]}_{datetime.now().strftime("%d.%m.%Y_%H.%M")}.docx')
doc.save(f"{context['work_name']}.docx")