import os

file = open('new.txt','w')
file.close()
os.remove("new.txt") #DELETA O ARQUIVO

file2 = open('new.txt','w')
file2.close()
os.rename('new.txt', 'old.csv') #RENOMEA o arquivo, inclusive a extenção
print(os.path.exists('new.txt')) #VERIFICA SE OS ARQUIVOS EXISTEM E RETORNA TRUE OU FALSE
print(os.path.exists('old.txt')) #VERIFICA SE OS ARQUIVOS EXISTEM E RETORNA TRUE OU FALSE

