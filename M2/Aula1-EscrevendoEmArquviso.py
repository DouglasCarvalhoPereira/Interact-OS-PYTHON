with open('text.txt', 'w') as file:
    file.write("Texto escrito em arquvio de Log")

with open('text.txt', 'a') as file:
    file.write("\nO parametro modificador 'a' funciona como APPEND, adiciona ao arquivo já existente, ao invés de escluir e criar um novo.")

#USANDO "W" como modificador eu deleto todo o textoo anterior e escrevo um novo.