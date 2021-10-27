#FILTRANDO_ARQUIVOS_DE_LOG_COM_EXPRESSOES_REGULARES
#O tipo de dados que podemos encontrar em diferentes tipos de arquivo como Syslog ou Log de solicitações Web

import sys
import re

#logfile = sys.argv[1]
arquivo = 'M4/logs.txt'
usersname = {}
name = "Nome do usuário"
with open(arquivo) as f:
    for line in f:
        if "CRON" not in line: #Exibiu apenas linhas que continham a String de referência CRON
            continue
        regex = r"\(user: (\w+)\)$"
        result = re.search(regex, line)
        if result is None:
            continue
        usersname[name] = usersname.get(name, 0) + 1
        print(result)
    
print(usersname)