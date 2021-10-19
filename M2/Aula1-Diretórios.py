#NAVEGAR, CRIAR E EXCLUIR DIRETÓRIOS E ARQUIVOS
import os

print(os.getcwd()) #Mostra o diretório atual, onde o arquivo está sendo executado.
os.mkdir('New_diretório') #Cria um diretório localizado no local de trabalho atual.
os.chdir("Diretório que desejamos mudar como parametro") #Alteea diretórios
os.rmdir('new_diretório') #Remove diretórios vazios
os.listdir('M2') #Retorna a lista de diretórios, sub-diretórios e arquivos no diretório