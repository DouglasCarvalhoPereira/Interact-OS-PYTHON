import csv
import string
import os, sys, stat

contatos = open('leads.csv','w')
read_csv = csv.reader(contatos, delimiter=';')
point = string.punctuation
for lead in read_csv:
    nome, email, whatsapp = lead
    whatsapp = [newNum.replace(point, '') for newNum in whatsapp]
    new_whats = ''.join(whatsapp)
    contatos.close()

    with open('newContatos', 'w') as newLeads:
        newLeads.writer(lead)

    #CONTINUAÇÃO


    print('Nome: {} | Email: {} | Whatsapp: {}'.format(nome, email, new_whats))