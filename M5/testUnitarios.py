# Testes unitários são usados para identificar se pequenas partes isoladas de um programa estão corretas.
#São escritos ao lado do código para testar seu comportamento, como funções ou métodos.
#Ajuda a testar se cada pedaço do código faz o que deveria fazer

import re

def refazendo_nome(name):
    result = re.search(r"^([\w .]*), ([\w .]*)$", name)
    return "{} {}".format(result[2], result[1])