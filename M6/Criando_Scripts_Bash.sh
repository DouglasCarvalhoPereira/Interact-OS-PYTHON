#! /usr/bin/bash
#Criando_Scripts_Bash
#Esse script possui uma extenção ".sh" Bash, sendo possível executar no terminal

#Usando Variáveis e Globais
#Bash é uma linguagem completamente estruturada e pode ser usada semelhantemente ao Python

#> "Globs" em Bash são caracteres que nos permitem criar listas de arquivos. (*) e (?) são os mais comuns.

#===> *.py imprimi na tela todos os arquivos com extensões .py do diretório atual, da mesma forma que usado em expressões regulares.
#===> capta* semelhante a expressões regulares, nesse caso imprimira arquivos e do diretório atual que sejam coerentes com o nome "capta..."
#===> * usando somente asterisco, será impresso todos os arquivos do diretório atual


#===> ? já o simbolo de interrogação é usado para corresponder um caractere de cada vez, por exemplo um arquivo com 5 caracteres usaria ?????.py

>>>>> ESSE MESMO COMANDO PODERIA ESTAR ESCRITO ASSIM <<<<<


line='==================================================='  #Variável

echo "Starting at: $(date)" ; echo $line    #Dessa forma ($line) a variável é exibida como se fosse "print"

echo "UPTIME" ; uptime ; echo $line

echo "FREE" ; free ; echo $line

echo "WHO" ; who ; echo $line

echo "Finishing at: $(date)"

