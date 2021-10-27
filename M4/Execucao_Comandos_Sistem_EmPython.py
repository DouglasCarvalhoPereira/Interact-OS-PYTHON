#!/usr/bin/env python

import subprocess
# "shutdown" FUNÇÕES INTERNAS DO SISTEMA OPERACIONAL


#subprocess.run(["date"], shell=True) #COMANDO INTERNO "date"
#subprocess.run("time", shell=True) #COMANDO INTERNO "time"
#subprocess.run(["shutdown", ""], shell=True) #COMANDO "shutdown" funções de desligar, reiniciar e etc.
subprocess.run(["sleep", "2"], shell= True)


print(subprocess.run(["date", "20-12-2019"], shell= True))
#return CompletedProcess(args=['date', '20-12-2019'], returncode=1) SEM PERMISSÕES 

# >  O que relalmente importa é o que o "returncode=1" resulta, 0 = Sucess ou 1 = Fail  <
#O resultado determinará se precisaremos tomar novas ações para resolver os erros, entender por que não concluiu a execução do script como deveria.


