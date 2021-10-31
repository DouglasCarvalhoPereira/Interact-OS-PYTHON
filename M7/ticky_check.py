#!/usr/bin/env python3
# > A classificação dos erros gerados pelo sistema
# > As estatísticas de uso do usuário para o serviço 
import re

arquivoLog = 'M7/syslog.log'

#Número de erros, do mais comum ao menos comum
error = {'Error': 0}

#Nome do usuário e erros do mesmo
per_user = {
            'Username': [],
            'INFO': [], 
            'ERROR':[]
            }

with open(arquivoLog) as file:
    for line in file:
        if re.search(r"ticky: ERROR: ([\w ]*)", line):
            per_user['ERROR'].append(line.strip())
            username = re.search(r"\([\w \.]*\)$", line)
            per_user['Username'].append(username.group())
        if re.search(r"ticky: INFO: ([\w ]*)", line):
            per_user['INFO'].append(line.strip())
            username = re.search(r"\(\b[\w \.]*\b\)$", line)
            per_user['Username'].append(username.group())


for nameuser, datas in per_user.items():
    print("="*50)
    print(nameuser)
    print("="*50)
    for user in datas:
        print(user)
