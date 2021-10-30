#!/usr/bin/bash
#Condicionais em BASH

if grep "127.0.0.1" /etc/hosts; then
        echo "Everything Ok"

else       
        echo "ERROR! 127.0.01 is not in /etc/hosts"

fi