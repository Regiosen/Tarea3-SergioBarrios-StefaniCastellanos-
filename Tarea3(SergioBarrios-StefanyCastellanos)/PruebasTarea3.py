import unittest
from BilleteraElectronica import *

class TestcalcularPrecio(unittest.TestCase):

    def testUnCreditoNingunDebito(self):
        billetera = BilleteraElectronica(1,'sergio','barrios',24101133,8)
        lista = [Creditos(5)]
        billetera.creditos = lista
        self.assertEqual(billetera.Saldo(),5,"No funciona calcular un solo credito")
        
    def testUnCreditoUnDebitoResultadoNoCero(self):
        billetera = BilleteraElectronica(1,'sergio','barrios',24101133,8)
        lista = [Creditos(5)]
        lista2 = [Creditos(7)]
        billetera.debitos = lista
        billetera.creditos = lista2
        self.assertEqual(billetera.Saldo(),2,"No funciona calcular un credito y un debito")
        
    def testUnCreditoUnDebitoResultadoCero(self):
        billetera = BilleteraElectronica(1,'sergio','barrios',24101133,8)
        lista = [Creditos(2)]
        lista2 = [Creditos(2)]
        billetera.debitos = lista
        billetera.creditos = lista2
        self.assertEqual(billetera.Saldo(),0,"No funciona calcular un credito y un debito")
        
if __name__ == "__main__":
    unittest.main()
