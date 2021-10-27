#Gerenciando_Subprocessos_Avancados
#Esses comandos alteram o caminho de um variável de ambiente ou seja, onde o programa encontra programas executaveis.

import subprocess
import os

my_env = os.environ.copy() #COPIEI VARIAVEIS DE AMBIENTE
my_env["PATH"] = os.pathsep.join(["/opt/myapp/", my_env["PATH"]]) #"pathsep" une elementos com um separador de caminho conforme o sistema operacional atual

#result = subprocess.run(["myapp"], env=my_env, shell=True)
 