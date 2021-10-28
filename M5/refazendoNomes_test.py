from refazendoNomes import refazendo_nomes
import unittest

#Classe de testes unitários
class TestRefazendoNomes(unittest.TestCase):
    def test_case(self):
        testecase = "Douglas, Carvalho" #Entrada que estou testando
        expectativa = "Douglas Carvalho" #O que eu espero no resultado
        self.assertEqual(refazendo_nomes(testecase), expectativa)

    def test_vazio(self):
        testecase = ""
        expectativa = ""
        self.assertEqual(refazendo_nomes(testecase), expectativa)

    def test_nomeDuplo(self):
        testecase = "Douglas, C. Pereira"
        expectativa = "Douglas C. Pereira"
        self.assertEqual(refazendo_nomes(testecase), expectativa)

    def test_UmNome(self):
        testecase = "Douglas"
        expectativa = "Douglas"
        self.assertEqual(refazendo_nomes(testecase), expectativa)

unittest.main()