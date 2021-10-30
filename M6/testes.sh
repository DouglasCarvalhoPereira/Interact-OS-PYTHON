#!/usr/bin/bash

line='==================================================='  #Variável

echo "Starting at: $(date)" ; echo $line    #Dessa forma ($line) a variável é exibida como se fosse "print"

echo "UPTIME" ; uptime ; echo $line

echo "FREE" ; free ; echo $line

echo "WHO" ; who ; echo $line

echo "Finishing at: $(date)"