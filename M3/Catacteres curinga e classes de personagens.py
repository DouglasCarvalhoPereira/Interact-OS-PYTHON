import re
#A FUNÇÃO "SEARCH" SÓ BUSCA A PRIMEIRA OPÇÃO DA FRASE

#Usando Character Classes
names = ["Douglas", "douglas", "souglas", "Souglas", "Touglas", "touglas", "@ouglas"]
for name in names:
    result = re.search(r"[DdSsTt@]ouglas", name) #Buscando o nome Douglas, podendo ele começar com as letras dentro das chaves.
    print(result)

names = ["viuva", "aricanduva", "soluva", "tuva", "VIUVA", "ARICANDUVA", "SOLUVA", "TUVA"]
for name in names:
    result = re.search(r"[A-Z]uva", name, re.IGNORECASE) #Buscando nomes, podendo ele começar com as letras dentro das chaves. Ignorando caracteres maiusculos ou minusculos
    print(result)

names = ["Mateus", "Hebreus"]
for name in names:
    result = re.search(r"..[a-z]eus", name) #Buscando o nomes, podendo ele começar com as letras dentro das chaves e se anteceder de qualquer outra letra.
    print(result)

#  <--------------------- BUSCANDO QUALQUER COISA QUE NÃO SEJA UMA LETRA, NÚMERO E ETC ------------------->
#                                       USA-SE "^" DENTRO DA CHAVE []

teste = re.search(r"[^a-zA-z0-9]", "Testando testo para verificar o buscador. Quantas vezes ele encontrará o resultado. 10, 20, 0" )
print(teste) #Resultado contabilizando o SPACE na busca

teste = re.search(r"[^a-zA-z0-9.á, ]", "Testando testo para verificar o buscador. Quantas vezes ele encontrará o resultado. 10, 20, 0" )
print(teste) #Resultado NÃO contabilizando o SPACE, nem ".", "á", "," na busca RETORNA NONE


# <-------------------------- BUSCANDO POR OPÇÕES ------------------------>
#                             USANDO " | "

busca = re.search(r"A|E|I", "Sempre sempres aquilo que cultivarmos, é uma cErteza.")
busca1 = re.search(r"A|E|I", "Sempre sempres aquilo que cultivarmos, é uma cArteza.")
busca2 = re.search(r"A|E|I", "Sempre sempres aquilo que cultivarmos, é uma cIrteza.")
print(busca) #DEVOLVE INTERVALO
print(busca1) #DEVOLVE INTERVALO
print(busca2) #DEVOLVE INTERVALO

#  <---------------------------- USANDO "FINDALL" PARA BUSCAR MAIS DE UM VALOR NA MESMA LINHA ------------>

buscaValues = re.findall(r"A|E|I", "Sempre sempres aquIlo que cultivArmos, é uma cErtezA.")
print(buscaValues) #DEVOLVE OS VALORES ENCONTRADOS
