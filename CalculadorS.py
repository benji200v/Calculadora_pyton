import unittest

class TestResta(unittest.TestCase):

    def test_resta_positivos(self):
        # Prueba la resta de dos números positivos 
        self.assertEqual(15 - 5, 10)

    def test_resta_iguales(self):
        # Prueba la resta de dos números iguales (debe dar cero) 
        self.assertEqual(8 - 8, 0)

if __name__ == '_main_':
    unittest.main()