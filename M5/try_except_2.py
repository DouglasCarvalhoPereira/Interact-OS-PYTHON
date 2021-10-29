#!/usr/bin/env python

def valida_usuario(nome, mintam):
    assert type(nome) == str, "Sim, é uma string"
    if mintam < 1:
        raise ValueError("Digite mais caracteres")
    if len(nome) < mintam:
        return False
    if not nome.isalnum():
        return False
        
    return True

print(valida_usuario("Douglas", 3))