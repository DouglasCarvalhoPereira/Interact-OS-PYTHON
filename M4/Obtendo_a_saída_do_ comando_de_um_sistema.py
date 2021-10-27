
#WHO comando imprimir os usuários conectados no computador

import subprocess

result = subprocess.run(["host","8.8.8.8"], shell=True, capture_output=True)
print(result.returncode)
print(result.stdout.decode()) #SAÍDA 

result2 = subprocess.run(["rm","file.txt"], shell=True, capture_output=True)
print(result2.returncode) #Número que define FAIL "1"
print(result2.stdout)
print(result2.stderr) #RETORNA O ERRO