#Extraindo um PID usando regexes em Python
import re

# <----------- EXTRAIR VALOR QUANDO EXISTIR, E QUANDO NÃO RETORNA ALGO ----------->
log = "July 31 07:51:48 [cage] mycomputer bad_process [12345]: ERROR Performaing package upgrade"
# FUNÇÃO QUE EXTRAI O "PID" ou "ID" QUANDO EXISTIR
def extract_PID(log_line):
    regex4 = r"\[(\d+)\]"
    resultado4 = re.search(regex4, log_line)
    if resultado4 is None:
        return "Vazio" #ESSE É O PID, um reaultado retornardo quando um valor não for encontrado.
    
    return resultado4[1]

print(extract_PID(log))




log = "July 31 07:51:48 [1827382KWA] mycomputer bad_process[12345]: ERROR Performaing package upgrade"
regex = r"\[(\d+)\]" # O "+" é usado para encontrar qualquer número que se repita.
resultado = re.search(regex, log)
print(resultado[1])

log2 = "July 31 07:51:48 [1827382KWA] mycomputer bad_process[12345]: ERROR Performaing package upgrade"
regex2 = r"\[(\d+\w+?)\]" # Nessa condição é encontrado 1 ou mais opções com letras ou números
resultado2 = re.findall(regex2, log2)
print(resultado2) 

log3 = "July 31 07:51:48 [1827382KWA] mycomputer bad_process[12345]: ERROR Performaing package upgrade"
regex3 = r"\[(\d+\w+?)\]" # Nessa condição é encontrado 1 ou mais opções com letras ou números
resultado3 = re.findall(regex3, log3)
print(resultado3[0], resultado3[0][::-1]) #Acessando o caractere por index! 

