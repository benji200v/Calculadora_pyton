import unittest

class TestDivision(unittest.TestCase):

    def test_division_exacta(self):
        #Prueba la división exacta 
        self.assertEqual(20 / 5, 4)

    def test_division_decimal(self):
        # Prueba la división con resultado decimal 
        self.assertEqual(7 / 2, 3.5)

    def test_division_periodica(self):
        #Prueba con división periódica usando assertAlmostEqual 
        self.assertAlmostEqual(10 / 3, 3.3333, places=4)

if __name__ == '_main_':
    unittest.main()