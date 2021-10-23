#Escaping Characters
#Combinado os caracteres especiais para obter expressões regulares incríveis e poderosas
#CONULTAS: regex101.com


import re
# .*+?$[] Caracteres especiais que podemos usar nas expressões regulares
#Agora usaremos \ \w \d 

teste = re.search(r".com", "welcome") #Essa busca está usando "." como coringa, e a respota será 'lcom'
print(teste) 

#Para utilizar de forma efizar usaremos o "\"
teste2 = re.search(r"\.com", "mkt@site.com") #Essa busca está usando "." como coringa, e a respota será NONE
print(teste2) # "\" A barra invertida é um caractere de escape, assi é possível usar o \.


#   \w Corresponde a qualquer caractere alphanumerico, incluindo letras, números e sublinhados, mas não SPACES
teste3 = re.search(r"\w*", "Essa é um aula poderosa para programadores")
print(teste3) #Só exibe até "ESSA", pois espaço não está incluso

teste4 = re.search(r"\w*", "Essa_é_um_aula_poderosa_para_programadores")
print(teste4) #Exibe toda a String, pois "_" Esão inclusos.


#   \d Para digitos correspondentes
#   \s Para espaços em branco, como SPACE, TAB ou NOVA LINHA
#   \b Para limits de palavras


