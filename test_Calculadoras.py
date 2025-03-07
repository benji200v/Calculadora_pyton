# Importación del módulo unittest para poder realizar pruebas unitarias
import unittest
# Importación de la clase calculadora desde el archivo calculadora.py
from Calculadora import Calculadora

# Definir de la clase de pruebas que heredará de unittest.TestCase
class TestCalculadora(unittest.TestCase):
    # Método que se ejecuta antes de cada prueba
    def setUp(self):
        self.calc = Calculadora()

    # Pruebas de método suma
    def test_Multiplicacion(self):
        # Prueba la suma de dos números positivos
        self.assertEqual(self.calc.multiplicacion(5, 2), 10)
        # Prueba la suma de dos ceros
        self.assertEqual(self.calc.multiplicacion(0, 0), 0)

# Bloque condicional que permite ejecutar las pruebas directamente
if __name__ == '_main_':
    # Inicializar la ejecución de todas las pruebas definidas en la clase
    unittest.main()