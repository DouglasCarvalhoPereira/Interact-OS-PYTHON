import os
#VÁRIAVEIS DE AMBIENTE
#O aplicativo que lê e executa os comandos se chama SHEL, seja um máquina local ou remota.
#Uma interface de linha de comando usada para interagir com o sistema operacional BASH, ZSH e FISH


# ACESSAR AS VARIAVEIS DE AMBIENTE VIA SHELL NO WINDOWS
#DIGITE NO TERMINAL

# 1° - python
# 2° - import os
# 3° - os.environ

#O Shell usa as variáveis de ambiente para encontrar o caminho dos arquivos executaveis e onde procura-los.

print("HOME: " + os.environ.get("USERPROFILE", "")) #Estou dizendo usando ".get", encontro o valor da chave, mas se não encontrar retorne STRING VAZIA
print("SHELL: " + os.environ.get("USERDOMAIN", "")) #Estou dizendo usando ".get", encontro o valor da chave, mas se não encontrar retorne STRING VAZIA
print("FRUIT: " + os.environ.get("FRUIT", "VARIÁVEL VAZIA")) #Estou dizendo usando apenas "os.environ("PATH")", se não houver um valor para retornar recebemos um ERROR