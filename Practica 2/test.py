from main import total_creditos, agregar_credito
import unittest

class prueba_main (unittest.TestCase):

    def Test_total_creditos(self):
        self.assertEqual(total_creditos(), 0)
        self.assertTrue(agregar_credito(5), True)
        self.assertTrue(agregar_credito("10"), True)
        self.assertFalse(agregar_credito("HOLA"), False)
        self.assertEqual(total_creditos(), 15)

