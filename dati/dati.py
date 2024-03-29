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
            '"regione": "' + com[10].replace('/Vallée d\'Aoste', '').replace('/Südtirol', '') + '", '
            '"idRegione": ' + str(int(com[0])) + ', '
            '"provincia": "' + com[11].replace('Valle d\'Aosta/Vallée d\'Aoste', 'Aosta').replace('/Bozen', '') + '", '
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
            '"nome": "' + prov[1].replace('Valle d\'Aosta/Vallée d\'Aoste', 'Aosta').replace('/Bozen', '') + '", '
            '"regione": "' + prov[3].replace('/Vallée d\'Aoste', '').replace('/Südtirol', '') + '", '
            '"idRegione": ' + str(int(prov[4])) + ', '
            '"siglaProvincia": "' + prov[2] + '"},\n'
        )
    province_json.write(provincia)
province_json.write(']')



# Genera file Regioni
dati_csv = open('Elenco-comuni-italiani.csv', encoding='iso-8859-1', newline='')
parsed_csv = csv.reader(dati_csv, delimiter=';', quotechar='"')

next(parsed_csv)
first_row = next(parsed_csv)

regioni = []
regioni.append([
    first_row[0], #idRegione
    first_row[10], #regione
    ])

for row in parsed_csv:
    ins = False
    for i in range(0, len(regioni)):
        if row[0] in regioni[i]:
            ins = True
            break
    if not ins:
        regioni.append([
            row[0], #idRegione
            row[10], #regione
        ])

regioni_json = open('../regioni.json', 'w', encoding='utf-8')
regioni_json.write('[\n')
for reg in regioni:
    regione = ('  {'
            '"id": ' + str(int(reg[0])).strip() + ', '
            '"nome": "' + reg[1].replace('/Vallée d\'Aoste', '').replace('/Südtirol', '') + '"},\n'
        )
    regioni_json.write(regione)
regioni_json.write(']')

