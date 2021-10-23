import re
#REPEATED MATCHES .* 

name = re.search(r"Do.*s", "Um grande programar Python é o Douglas") # < --- ".*" Multiplica a quantidade de vezes que o CORINGA é repetido até chegar no final
print(name)

name2 = re.search(r"Do.*s", "O Douglas é grande programar Python, isso mesmo") #Começou em "Do..." e terminou em "...s"
print(name2)

name3 = re.search(r"Do.*", "O Douglas é grande programar Python, isso mesmo") #Começou em "Do..." e temrinou ao final da linha.
print(name3)

name4 = re.search(r"Do[a-z]*s", "O Douglas é grande programar Python, isso mesmo") #Começou em "Do..." completou com caracteres entre "a-z" e finalizou com "s".
print(name4)

# <------ USANDO "+" Para repetições de letras ---->

name5 = re.search(r"D+o+u+g+l+a+s+", "Dooouuuuggglllaaasss") #O sinal de "+" retorna a String que corresponde um ou mais caracteres que antecedem o sinal de ADIÇÃO.
print(name5)

number = re.search(r"[0-9]*", "24 98821-9104")
print(number)

# <------ USANDO "?" Para possíveis letras ---->
possible = re.search(r"D?ouglas", "ouglas") #Se a letra "D" estiver presente ele imprime, se não imprime também.
print(possible)

possible2 = re.search(r"D?ougl?as", "ougas") #Se a letra "D" estiver presente ele imprime, se não imprime também.
print(possible2)

possible3 = re.search(r"D?ougl?as", "Douglas") #Imprimi normalmente caso a palavra estreja completa
print(possible3)
