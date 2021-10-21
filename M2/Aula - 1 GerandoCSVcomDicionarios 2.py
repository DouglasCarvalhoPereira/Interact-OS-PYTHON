#GERAR UM ARQUIVO CSV USANDO DictWriter a partir de uma list de dicionários
#Para funcionar também pé preciso passar a lista de chave de cada coluna

import csv


dict = [{'Nome': 'Millena', 'Email': 'millenaalvarenga99@gmail.com', 'WhatsApp': '24999791393'},
{'Nome': 'Dário', 'Email': 'dariocassiano.vr.rt@gmail.com', 'WhatsApp': '24-988312952'},
{'Nome': 'GILBERTO NASCIMENTO SILVA', 'Email': 'gilbertopuc@gmail.com', 'WhatsApp': '(24) 99831-987'},
{'Nome': 'Priscila Pacheco', 'Email': 'priscilapacheco11@gmail.com', 'WhatsApp': '24999593640'},
{'Nome': 'Licia', 'Email': 'licia.almeida@gmail.com', 'WhatsApp': '24 992713815'}]

keys = ['Nome', 'Email', 'WhatsApp']
with open('leadsDict.csv', 'w') as file_inCSV:
    writer = csv.DictWriter(file_inCSV, fieldnames=keys) #Passo o arquivo e as chaves como parametro
    writer.writeheader() #Cria a primeira linha com as chaves
    writer.writerows(dict) #Escreve a lista em CSV


