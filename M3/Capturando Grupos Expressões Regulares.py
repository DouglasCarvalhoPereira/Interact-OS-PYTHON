import re
#Captruando Grupos com ES

names = re.search(r"^(\w*), (\w*), (\w*)$", "Pereira, Carvalho, Douglas") 
print(names.groups()) # COMO FORAM DEFINIDOS 4 GRUPOS USANDO "(" e ")" É RETORNADO UMA TUPL
print(names[0]) #Grupo inteiro
print(names[1]) #Parte 1 do grupo
print(names[2]) #Parte 2 do grupo
print(names[3]) #Parte 3 do grupo

def consertando_nome(nome):
    search = re.search(r"^([\w\.  ]*), ([\w\. ]*).?([\w\. ]*)$", nome)
    if search is None:
        return print("ERROR")
    
    return print(f"{search[3]} {search[2]} {search[1]}")

consertando_nome("Pereira, C. Douglas") #SOLUCIONADO
consertando_nome("Junior, Evangelista, Lucas") 
consertando_nome("Pereira, Carvalho, Clayton")