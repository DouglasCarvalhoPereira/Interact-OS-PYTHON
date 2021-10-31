import csv
import pandas as pd

paginaArmazenamento = '/var/www/html/index.html'
arquivo = 'M7/user_emails.csv'

df = pd.read_csv(arquivo)
table = df.to_html()

with open('M7/index.html', 'w+') as file:
    file.write(table)