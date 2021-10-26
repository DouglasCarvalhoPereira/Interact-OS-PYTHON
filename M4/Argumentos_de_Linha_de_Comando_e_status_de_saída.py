#ARGUMENTOS DE LINHA DE COMANDO E STATUS DE SAÍDA
#Passando argumento através da linha de comando

#VERIRICAR "Exit Status" ou "Return Code" deve ser 0 para Sucesso ou != 0 para FALHA.

import sys
print(sys.argv)

#    > COMANDO SHEELL PARA TESTAR SE FOI EXECUTADO COM SUCESSO <
# python script.py && echo '0' || echo '1'


#EXUCUTAR PROGRAM > python Argumentos_de_Linha_de_Comando_e_status_de_saída.py
#EXUCUTAR PROGRAM > python Argumentos_de_Linha_de_Comando_e_status_de_saída.py argumento1
#EXUCUTAR PROGRAM > python Argumentos_de_Linha_de_Comando_e_status_de_saída.py argumento1 argumento2
#EXUCUTAR PROGRAM > python Argumentos_de_Linha_de_Comando_e_status_de_saída.py argumento1 argumento2 argumento3

# >IMPRESSO NA LINHA DE COMANDO<

#['Argumentos_de_Linha_de_Comando_e_status_de_saída.py', 'argumento1', 'argumento2', 'argumento3']

#Os parâmetros são armazenados em SYS

#Aprender a passar parâmetros pela linha de comando para programas PYTHON e como fazer programas retornaram com sucesso ou não

#Usarei parâmetros de linha de comando para dizer aos meus programas PYTHON o que fazer sem ter que interagir com eles.

#Usarei valores de saída para saber se o comando foi bem sucedido ou não.

#Em seguida registrar LOGS de falahas em um arquivo e tentar automaticamento os comandos se for necesseário.