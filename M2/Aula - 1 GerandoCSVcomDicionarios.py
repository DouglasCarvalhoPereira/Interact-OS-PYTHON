import csv

with open('leads.csv') as file:
    reader = csv.DictReader(file, delimiter=';')
    for row in reader:
        name = row['Nome']
        email = row['E mail']
        tel = row['WhatsApp']
        print(row)
        #print(("{} - {} - {} ").format(row['Nome'], row['Email'], row['WhatsApp']))
        #Ou
        #print(("{} - {} - {} ").format(name, email, tel))
        #APREDNER A MOSTRA SOMENTE AS CHAVES DE ACESSO DA PRIMEIRA LINHA