#!/usr/bin/env python3

import sys
import csv
import os

def process_csv(csv_file):
    """#Transforma o CSV em uma lista de listas"""
    print("Processando {}".format(csv_file))
    with open(csv_file, "r") as datafile:
        data = list(csv.reader(datafile))
    
    return data

def data_to_html(title, data):
    """Transforma a lista tabela HTML"""

    # HTML Header
    html_content = """
    
    <html>
<head>
<style>
table {
  width: 25%;
  font-family: arial, sans-serif;
  border-collapse: collapse;
}
tr:nth-child(odd) {
  background-color: #dddddd;
}
td, th {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}
</style>
</head>
<body>
"""

    html_content += "<h2>{}</h2><table>".format(title)

    #Adiciona cada linha de dados como uma linha da tabela
    #A primeria linha é tratada separadamente por ser especial
    for i, row in enumerate(data):
        html_content += "<tr>"
        for column in row:
            if i == 0:
                html_content += "<th>{}</th>".format(column)
            else:
                html_content += "<td>{}</td>".format(column)
        html_content += "</tr>"
    
        html_content += "</tr>"
    html_content += """</tr></table></body></html>"""
    return html_content

def write_html_file(html_string, html_file):

    #Saber se o arquivo HTML que estamos escrevendo existe ou não
    if os.path.exists(html_file):
        print("{} Esse arquivo já existe!")
    
    with open(html_file, 'w') as htmlfile:
        htmlfile.write(html_string)
    print("Tabela {} criada com sucesso.".format(html_file))

def main():
    """Verifica todos os argumentos e chama a função de processamento"""
    #Verifica se os arquivos da linha de comando estão incluídos
    if len(sys.argv) < 3:
        print("ERROR: Argumento de linha de comando não encontrado!")
        print("Saindo do programa...")
        sys.exit(1)

    csv_file = sys.argv[1]
    html_file = sys.argv[2]


    # Verifica se está incluído o arquivo com as extenções
    if ".csv" not in csv_file:
        print("Arquivo CSV não encontrado")
        print("Saindo do sistema!")
        sys.exit(1)

    if not os.path.exists(csv_file):
        print("Caminho para o arquivo {} inexistente".format(csv_file))
        print("Saino do sistema!")
        sys.exit(1)

    data = process_csv(csv_file)
    title = os.path.splitext(os.path.basename(csv_file))[0].replace("_", " ").title()
    html_string = data_to_html(title, data)
    write_html_file(html_string, html_file)

if __name__ =="__main__":
    main()