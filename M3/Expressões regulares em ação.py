import re

country = re.search(r"A.*a", "Argentina") #Começa com "A" e termina com "a"
country2 = re.search(r"A.*a", "Azerbaijan") #Ele para em "a"
country2_1 = re.search(r"^A.*a$", "Azerbaijan") #Especifica começo e fim com "^" e "$"
country3 = re.search(r"^A.*a$", "Australia") #Especificado o inicio e o fim da String que procuro

print(country)
print(country2)
print(country2_1)
print(country3)


# < ----------------- VALIDA SE É UMA VARIAVEL VÁLIDA ----------->
# Pode conter letras, números e sublinhados, mas não pode começar com números.

variavel = re.search(r"^[^0-9]\w*$", "_teste_de_variavel_1") #Começou com número a variavel é NONE
variavel2 = re.search(r"^[a-zA-Z_][a-zA-Z0-9_]*$", "_teste_de_variavel_1") #Começou com número a variavel é NONE

print(variavel)
print(variavel2)