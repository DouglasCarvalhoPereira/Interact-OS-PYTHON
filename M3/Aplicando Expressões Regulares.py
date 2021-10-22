#GREP irá imprimir qualquer satring que contenha a string pesquisada.
#Usando Grap para encontrar palavaras dentro de um arquivo de texto

#linha de comando

grep thon /usr/share/wors.txt #<--- exeplo de caminho de arquivo no termianal "thon" é a palavra pesquisada.

#Grep é sensível a MAIUSCULAS e MINUSCULAS

grep -i #  <---- Pesuisa sendo a letra correspondende Maiuscula ou Minuscula

grep l.ython #  <---- O '.' funciona como um curinga, e pode ser susbstituido por qualquer caractere na busca.
     liython # Ou seja, pode-se ter reultados como esses ao lado esquerdo.
     luython # onde o ponto substitui um caractere especifico e busca pelo resto da string
     leython


#Correspondem especificamente com o ínicio e com o fim de uma linha e não uma STRING
#Só serão exibidas linhas que contiverem os valores passados para "^" INICO e "$" FIM 
grep ^ #  <---- Indica o ínicio
grep $ #  <---- Indica o FIM da lista

grep ^fruit <caminho_arquiv> #  <---- Ele irá buscar palavras que comecem com 'fruit'
grep cat$ <caminho_arquiv> #  <---- Ele irá buscar palavras que terminem com 'cat'