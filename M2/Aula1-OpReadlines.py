#Para arquivos muito grandes o ideal é processar linha por linha usando o readlines(), assim economiza a memória do computador e mantém o desempenho.
file = open('words.txt').readlines()
text = file.sort()

#Para arquivos mais curtos, usar o read() pode ser boa ideia.
with open('words.txt') as file:
    print(file.readlines())