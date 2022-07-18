import csv

# Genera file Comuni
dati_csv = open('Elenco-comuni-italiani.csv', encoding='iso-8859-1', newline='')
parsed_csv = csv.reader(dati_csv, delimiter=';', quotechar='"')

comuni_json = open('../comuni.json', 'w', encoding='utf-8')
comuni_json.write('[\n')
next(parsed_csv)
for com in parsed_csv:
    comune = ('  {'
            '"id": ' + str(int(com[4])).strip() + ', '
            '"nome": "' + com[6] + '", '
            '"regione": "' + com[10] + '", '
            '"idRegione": ' + str(int(com[0])) + ', '
            '"provincia": "' + com[11] + '", '
            '"siglaProvincia": "' + com[14] + '", '
            '"idProvincia": ' + str(int(com[1])) + '},\n'
        )
    comuni_json.write(comune)
comuni_json.write(']')


# Genera file Province
dati_csv = open('Elenco-comuni-italiani.csv', encoding='iso-8859-1', newline='')
parsed_csv = csv.reader(dati_csv, delimiter=';', quotechar='"')

next(parsed_csv)
first_row = next(parsed_csv)

province = []
province.append([
    first_row[1], #idProvincia
    first_row[11], #provincia
    first_row[14], #siglaProvincia
    first_row[10], #regione
    first_row[0], #idRegione
    ])

for row in parsed_csv:
    ins = False
    for i in range(0, len(province)):
        if row[14] in province[i]:
            ins = True
            break
    if not ins:
        province.append([
            row[1], #idProvincia
            row[11], #provincia
            row[14], #siglaProvincia
            row[10], #regione
            row[0], #idRegione
        ])

province_json = open('../province.json', 'w', encoding='utf-8')
province_json.write('[\n')
for prov in province:
    provincia = ('  {'
            '"id": ' + str(int(prov[0])).strip() + ', '
            '"nome": "' + prov[1] + '", '
            '"regione": "' + prov[3] + '", '
            '"idRegione": ' + str(int(prov[4])) + ', '
            '"siglaProvincia": "' + prov[2] + '"},\n'
        )
    province_json.write(provincia)
province_json.write(']')


