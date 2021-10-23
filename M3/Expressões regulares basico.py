import re
#A FUNÇÃO "SEARCH" SÓ BUSCA A PRIMEIRA OPÇÃO DA FRASE

#ESSE É O MODO TRADICIONAL DE EXTRAIR USANDO SOMENTE PYTHON
log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performaing package upgrade"
index = log.index("[")
print(log[index+1:index+6])

#AGORA USAREMOS REGEX ou EXPRESSÕES REGULARES PARA ISSSO
log = "July 31 07:51:48 mycomputer bad_process [12345]: ERROR Performaing package upgrade"

#NÃO IMPORTA ONDE O ID DE PROCESSO APAREÇA NO PROCESSO OU QUANTO TEMPO OU CURTA A LINHA SEJA
#Enquanto houver uma única sequência de números entre colchetes ele ira retornar.
regex = r"\[(\d+)\]" #DIZ O QUE PROCURAR
restult = re.search(regex, log) #DIZ PARA PROCURAR COM A FUNÇÃO def search():
print(restult[1])