file = open("words.txt") #USANDO ESRE MÉTODO É PRECISO FECHAR O ARQUIVO COM file.close() Esse método
#é usado para trabalhar com o arquivo em outras partes do sistema.

with open('words.txt') as file: #Com o método WITH ele é fechado automáticamente.
    for line in file:
        print(line.upper().strip())