import unittest
from BilleteraElectronica import *

class TestcalcularPrecio(unittest.TestCase):

    def testUnCreditoNingunDebito(self):
        billetera = BilleteraElectronica(1,'sergio','barrios',24101133,8)
        deb = [Creditos(5,"25/4/2015","USB")]
        billetera.creditos = deb
        self.assertEqual(billetera.Saldo(),5,"No funciona calcular un solo credito")
        
    def testUnCreditoUnDebitoResultadoNoCero(self):
        billetera = BilleteraElectronica(1,'sergio','barrios',24101133,8)
        deb = [Debitos(5,"2/5/2015","USB")]
        cred = [Creditos(7,"1/5/2015","USB")]
        billetera.debitos = deb
        billetera.creditos = cred
        self.assertEqual(billetera.Saldo(),2,"No funciona calcular un credito y un debito")
        
    def testUnCreditoUnDebitoResultadoCero(self):
        billetera = BilleteraElectronica(1,'sergio','barrios',24101133,8)
        deb = [Debitos(2,"1/5/2015","USB")]
        cred = [Creditos(2,"2/5/2015","USB")]
        billetera.debitos = deb
        billetera.creditos = cred
        self.assertEqual(billetera.Saldo(),0,"No funciona calcular un credito y un debito que dejan en cero el saldo")
        
    def testRecargaUnica(self):
        billetera = BilleteraElectronica(1,'sergio','barrios',24101133,8)
        deb = [Debitos(2,"2/5/2015","USB")]
        cred = [Creditos(2,"2/5/2015","USB")]
        billetera.debitos = deb
        billetera.creditos = cred
        recarga_nueva = Creditos(6,"2/5/2015","USB")
        billetera.Recargar(recarga_nueva)
        self.assertEqual(billetera.Saldo(),6,"No funciona recargar un credito")
        
    def testConsumoUnicoConSuficienteCredito(self):
        billetera = BilleteraElectronica(1,'sergio','barrios',24101133,8)
        deb = [Debitos(2,"2/5/2015","USB")]
        cred = [Creditos(9,"2/5/2015","USB")]
        billetera.debitos = deb
        billetera.creditos = cred
        consumo_nuevo = Debitos(4,"2/5/2015","USB")
        billetera.Consumir(consumo_nuevo)
        self.assertEqual(billetera.Saldo(),3,"No funciona consumir credito cuando se tiene suficiente")

if __name__ == "__main__":
    unittest.main()
