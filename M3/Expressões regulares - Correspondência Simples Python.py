import re
#A FUNÇÃO "SEARCH" SÓ BUSCA A PRIMEIRA OPÇÃO DA FRASE



result = re.search(r"glas", "Douglas") #Nesse caso <span=(3,7)> retorna a posição que se encontra "glas" de 3 até 7 
print(result)

numbers = "763274627372839120219937487483"
result2 = re.search(r"6", numbers) #Nesse caso só retorna a primeria popsição que foi encontrado o número "6"
print(result2)

result3 = re.search(r"glass", "dougl")
print(result3) #O retorno para uma string não encontrada é NONE

search_1 = re.search("^Douglas", "Douglas Carvalho Pereira") # "^" para buscar Douglas no começo da linha
search_2 = re.search("Carvalho", "Douglas Carvalho Pereira") # Sem sinal para buscar Carvalho em toda a linha
search_3 = re.search("Pereira$", "Douglas Carvalho Pereira") # "$" Para buscar Pereira no final da linha

print(search_1) # SEMPRE RETORNA O INTERVALO ONDE FOI ENCONTRADA A STRING
print(search_2) # SEMPRE RETORNA O INTERVALO ONDE FOI ENCONTRADA A STRING
print(search_3) # SEMPRE RETORNA O INTERVALO ONDE FOI ENCONTRADA A STRING


search_4 = re.search("^......s", "Douglas Carvalho Pereira") # "^" para buscar Douglas no começo da linha Utilizando CORINGA
search_5 = re.search(".......o", "Douglas Carvalho Pereira") # Sem sinal para buscar Carvalho em toda a linha Utilizando CORINGA
search_6 = re.search("......a$", "Douglas Carvalho Pereira") # "$" Para buscar Pereira no final da linha Utilizando CORINGA

print(search_4) # SEMPRE RETORNA O INTERVALO ONDE FOI ENCONTRADA A STRING
print(search_5) # SEMPRE RETORNA O INTERVALO ONDE FOI ENCONTRADA A STRING
print(search_6) # SEMPRE RETORNA O INTERVALO ONDE FOI ENCONTRADA A STRING


# <-------------- PARA IGNORAR MAIUSCULAS E MINUSCULAS ------------->

res = re.search(r"doug", "dOuGlas", re.IGNORECASE) #Ignora letras maiusculas e minusculas na busca
print(res)
