#1 /usr/bin/bash

# -le verifica se n é menor que 5, e itera até chegar.

n=1
while [ $n -le 5 ]; do
    echo "Interation number $n"
    ((n+=1))
done