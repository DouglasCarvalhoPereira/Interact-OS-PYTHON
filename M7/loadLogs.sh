#!/bin/bash

#Pesquisando Logs "ticky"
grep ticky syslog.log

#Pesquisando Logs "ERROR"
grep "ERROR" syslog.log

#Busca pela frase "ERROR Tried to add information to closed ticket"
grep "ERROR Tried to add information to closed ticket" syslog.log 