#Mais sobre qualificadores de repetição
#Qualificadores de repetição númerica
#       <-------------- USAR "{" e "}" para passar a quantidade de caracteres buscados.--->
import re

contLetter = re.search(r"[A-Za-z]{8}", "Olá, somos felizes por ter uma vida prospera! By Douglas.")
print(contLetter) #RETORNA O PRIMEIRO RESULTADO ENCONTRADO

contLetter = re.findall(r"[A-Za-z]{8}", "Olá, somos felizes por ter uma vida prospera! By Douglass.")
print(contLetter) # RETORNA TODOS OS RESULTADOS ENCONTRADOS COM 8 CARACTERES


#       <------- Usando "\b" no inicio e no fim nós deizemos que queremos palavras completas----->

letterComplete = re.search(r"\b[A-Za-z]{4}\b", "Test para identificar palavras com quatro letras.")
print(letterComplete) #Resulta na primeira palavra encontrada | "\b" no inicio e no fim indica palavras completas

letterComplete = re.findall(r"\b[A-Za-z]{4}\b", "Test para identificar palavras com quatro letras.")
print(letterComplete) #Resulta todas as palavras encontradas "\b" no inicio e no fim indica palavras completas

#       <----- Buscando quantidade de caracteres por intervalos usando "{" e "}" --------------->

quantIntervalo1 = re.findall(r"\w{3,5}", "Olá, como vão esses estudos em Python, buscar palavras de cinco a tres caractres é legal.")
print(quantIntervalo1) #Palavras de 3 a 5 caracteres

quantIntervalo2 = re.findall(r"\w{3,}", "Olá, como vão esses estudos em Python, buscar palavras de cinco a tres caractres é legal.")
print(quantIntervalo2) #Acima de 3 caracteres

quantIntervalo3 = re.findall(r"[^\.!, ]\w{,3}", "Olá, como vão esses estudos em Python, buscar palavras de cinco a tres caractres é legal.")
print(quantIntervalo3) #Até 3 caracteres excluindo, excluindo "." "!" "," " "

buscaAvan = re.findall(r"O[^ \.!,]\w{,4}", "Olá, como vão esses estudos em Python, buscar palavras de cinco a tres caracteres é legal.")
print(buscaAvan) #Até 4 caracteres,  excluindo "." "!" "," " " e começando com "O"
