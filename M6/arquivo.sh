#!/usr/bin/bash

#O comando "Test" avalia as condicionais retornando "0" para True e "1" para False

# "-n" verifica se uma string está vazia ou não

if test -n "$PATH"; then echo "Seu teste está vazio"; fi
#ou
#Atenção ao espaçamento, ou receberá um ERROR
if [ -n "$PATH" ]; then echo "Seu caminho está vazio"; fi


if grep "127.0.0.1" /etc/hosts; then
        echo "Everything Ok"
else
        echo "ERROR! 127.0.0.1 is not in /etc/hosts"

fi