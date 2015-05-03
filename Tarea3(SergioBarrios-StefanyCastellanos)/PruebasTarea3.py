import unittest
from BilleteraElectronica import *

class TestcalcularPrecio(unittest.TestCase):
    
    def testUnCreditoNingunDebito(self):
        billetera = BilleteraElectronica(1,'sergio','barrios',24101133,8)
        lista = [Creditos(5)]
        billetera.creditos = lista
        self.assertEqual(billetera.Saldo(),5,"wat")
        
#if __name__ == "__main__":
#    unittest.main()
