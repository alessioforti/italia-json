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


