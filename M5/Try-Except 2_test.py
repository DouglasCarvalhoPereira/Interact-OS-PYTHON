import unittest
from try_except_2 import valida_usuario

class TesteValidaUser(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(valida_usuario('', 3), True)

    def teste_nome(self):
        self.assertEqual(valida_usuario(2, 6), True)
    
    def teste_tam_nome(self):
        self.assertEqual(valida_usuario('douglas', 1), False)

unittest.main()