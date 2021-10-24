#DIVIDINDO E SUBSTITUINDO COM EXPRESSÕES REGULARES 
# "split()" Separar qualquer expressão regular
# "sub()" Para substituir strings com REGEX

import re

texto = "Texto base que será usado como separador. Esse texto inclui pontuação com um único objetivo! Ser separado por eles. Você já imaginou isso?"
regex = r"[.!?]" #Nesse caso, os sinais são excluidos ao se tornarem separadores.
result = re.split(regex, texto)
print(result[0])#ACESSANDO PARTES DO TEXTO
print(result[1])#ACESSANDO PARTES DO TEXTO
print(result[2])#ACESSANDO PARTES DO TEXTO
print(result[3])#ACESSANDO PARTES DO TEXTO
 
texto2 = "Texto base que será usado como separador. Esse texto inclui pontuação com um único objetivo! Ser separado por eles. Você já imaginou isso?"
regex2 = r"([.!?])" #Nesse caso os sinais estão inclusos na separção a partir dos sinais
result2 = re.split(regex2, texto2)
print(result2)


# <----------- SUBSTITUINDO AS PARTES POR UMA STRING DIFERENTE USANDO "SUB" ----------------->

result3 = re.sub(r"[\w.%+-]+@[\w.+-]+", "[REDACTED]", "Received an email for teste@site.com") #SUBSTITUI O PADRÃO Por "[REDACTED]"
print(result3)

resultNew = re.sub(r"\d+", "[NÚM]", "Esse texto contém 1, 2, 3 ou até quatro números.")
print(resultNew) #Substitui números por [NÚM]


 