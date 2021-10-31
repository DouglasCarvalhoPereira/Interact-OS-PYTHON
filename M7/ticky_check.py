#!/usr/bin/env python3
import sys
import re
import operator
import csv

#Dicionário que conta a entrada de números no Log para cada usuário
per_user = {} #Dividido entre INFO e ERROR
#Dicionário com número de erros diferentes por messages
errors = {}

# Ler o arquivo e criar os dicionários

with open('syslog.log') as file:
    #Leio todas as linhas
    for line in file.readlines():
        #Regex de busca
        # Linha que mostra o arquivo de log
        #Ex - "May 27 11:45:40 ubuntu.local ticky: INFO: Created ticket [#1234] (username)"
        match = re.search(r"ticky: ([\w+]*):? ([\w' ]*)[\[[#0-9]*\]?]? ?\((.*)\)$", line)
        code, error_msg, user = match.group(1), match.group(2), match.group(3)

        #Preenchendo o dicionário "error" com a mensgaem de ERRO do arquivo
        if error_msg not in errors.keys():
            errors[error_msg] = 1
        else:
            errors[error_msg] += 1

        #Preenchendo o dicionário "per_user" com os logs
        if user not in per_user.keys():
            per_user[user] = {}
            per_user[user]['INFO'] = 0
            per_user[user]['ERROR'] = 0
        
        #Preenchendo "per_user" com usuparios dos logs
        if code == 'INFO':
            if user not in per_user.keys():
                per_user[user] = {}
                per_user[user]['INFO'] = 0
            else:
                per_user[user]['INFO'] += 1
            
        elif code == 'ERROR':
            if user not in per_user.keys():
                per_user[user] = {}
                per_user[user]['ERROR'] = 0
            else:
                per_user[user]['ERROR'] += 1

# Classificar valores do mais comum até o menos comum (VALUE)
errors_list = sorted(errors.items(), key=operator.itemgetter(1), reverse=True)

# Classificando por Nome de usupario
per_user_list = sorted(per_user.items(), key=operator.itemgetter(0))

file.close()

#Inserir no inicio da lista
errors_list.insert(0, ('Error','Count'))

# Gerando arquivo CSV para users_static
with open('user_stattics.csv', 'w', newline='') as user_csv:
    for key, value in per_user_list:
        user_csv.write(str(key) + ',' + 
                        str(value['INFO']) + ',' + str(value['ERROR']) + '\n')

with open('error_message.csv', 'w', newline = '') as error_csv:
    for key, value in errors_list:
        error_csv.write(str(key) + ' ' + str(value))

