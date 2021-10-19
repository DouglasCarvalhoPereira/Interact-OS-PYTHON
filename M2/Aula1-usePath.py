#Existem inúmeras funções em OS e OSPATH a serem exploradas.
import os
import datetime

file = open('old.csv')
tamanhoDoArquivo = os.path.getsize('words.txt') #Retorna o tamanho do arquivo
ultimaModificacao = os.path.getmtime('words.txt') #Retorna aúltima alteração segundo o horário UNIX
dateExat = datetime.datetime.fromtimestamp(ultimaModificacao) #Converta é tempo legível
caminhoDoArquivo = os.path.abspath('text.txt') #TRANSFORMA O ARQUIVO EM UM CAMINHO ABSOLUTO


print(tamanhoDoArquivo)
print(ultimaModificacao)
print(dateExat) 
print(caminhoDoArquivo)

file = open(caminhoDoArquivo) #POSSO USAR O CAMINHO ABSOLUTO PARA EDTAR, EXCLUIR E CRIAR O ARQUIVO.
print(file.read())
file.close()
os.remove(caminhoDoArquivo)