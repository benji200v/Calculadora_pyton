import unittest

class TestMultiplicacion(unittest.TestCase):

    def test_multiplicacion_positivos(self):
        # Prueba la multiplicación de dos números positivos 
        self.assertEqual(6 * 3, 18)

    def test_multiplicacion_cero(self):
        #Prueba la multiplicación por cero (debe dar cero) 
        self.assertEqual(9 * 0, 0)

    def test_multiplicacion_negativo(self):
        #Prueba la multiplicación de un número negativo por uno positivo 
        self.assertEqual(-4 * 2, -8)

if __name__ == '_main_':
    unittest.main()