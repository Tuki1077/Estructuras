from functions import total_creditos, agregar_credito
import unittest

class prueba_main (unittest.TestCase):

    def test_total_creditos(self):
        self.assertEqual(total_creditos(), 0)
        self.assertTrue(agregar_credito(5), True)
        self.assertTrue(agregar_credito("10"), True)
        self.assertEqual(total_creditos(), 15)
    
    def test_agregar_creditos (self):
        self.assertFalse(agregar_credito("HOLA"), False)

if __name__ == '__main__':
    unittest.main()

