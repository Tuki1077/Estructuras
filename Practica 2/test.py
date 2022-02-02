import functions as fc
import unittest

class prueba_main (unittest.TestCase):

    def test_agregar_creditos (self):
        self.assertFalse(fc.agregar_credito("HOLA"), False)

    def test_agregar_debitos(self):
        self.assertFalse(fc.agregar_debito("HOLA"), False)

    def test_total_creditos(self):
        self.assertEqual(fc.total_creditos(), 0)
        self.assertTrue(fc.agregar_credito(5), True)
        self.assertTrue(fc.agregar_credito("10"), True)
        self.assertEqual(fc.total_creditos(), 15)
    
    def test_total_debitos(self):
        self.assertEqual(fc.total_debitos(), 0)
        self.assertTrue(fc.agregar_debito(5), True)
        self.assertTrue(fc.agregar_debito("20"), True)
        self.assertEqual(fc.total_debitos(), 25)
    
    def test_saldo(self):
        self.assertFalse(fc.saldo(), 0)  



if __name__ == '__main__':
    unittest.main()

