from docxtpl import DocxTemplate
from datetime import datetime
expansion = 'docx'
filename = "template"
input_file = f"{filename}.{expansion}"
doc = DocxTemplate(input_file)
context = {'title' : "Областное государственное бюджетное профессиональное образовательное учреждение «Рязанский колледж имени Героя Советского Союза Н.Н. Комарова»",
           'dir' : "Т.В. Мастюкова",
           'dirfi' : "Мастюкова Татьяна Вячеславовна",
           'dirfr' : "Мастюковой Татьяны Вячеславовны",
           'io_dir' : "В.Н. Бутова",
           'adress_osn' : "390526, Рязанская область, Рязанский район, п.Варские, ул.Юбилейная, д.6",
           'adress_strukt' : "Рязанская область, Старожиловский район, рабочий поселок Старожилово, ул. Денисова, д.37",
           'inn' : "6215001527",
           'kpp' : "621501001",
           'rs' : "40601810145251000059",
           'ls' : "21596У85140",
           'ogrn' : "1026200702340",
           'bik' : "046126001",
           'okpo' : "00564292",
           'mail' : "rat68@yandex.ru",
           'bank' : "УФК по Рязанской области Отделение Рязань г. Рязань",
           'phone' : "+7(4912) 26-12-18, 26-12-46",
           'block' : ""}
doc.render(context)
doc.save(f'{filename}_{datetime.now().strftime("%d.%m.%Y_%H.%M")}.docx')