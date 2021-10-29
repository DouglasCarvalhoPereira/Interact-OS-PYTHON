#!/usr/bin/env python

def frequencia_caractere(filename):

    try:
        f = open(filename)
    except OSError: #Except só é executado se TRY retornar ERROR
        return None

    caracteres = {}
    for line in f:
        for caract in line:
            caracteres[caract] = caracteres.get(caract, 0 ) + 1
    
    f.close()
    return caracteres

print(frequencia_caractere('arquivo.txt'))

