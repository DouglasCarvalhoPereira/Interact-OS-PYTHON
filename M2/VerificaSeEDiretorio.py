import os

dirAtual = os.getcwd()
os.mkdir('DiretorioTeste')
for item in os.listdir(dirAtual):
    fullname = os.path.join(dirAtual, item) #Usar JOIN permite usar esse comando em multiplos OS
    if os.path.isdir(fullname):
        print(f"{item} é um diretório. Diretório completo {fullname}")
    else:
        print(f'{item} é um arquivo.')