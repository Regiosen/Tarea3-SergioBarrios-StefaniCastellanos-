# -*- coding: UTF-8 -*-
'''
@author: Sergio Luis Barrios
         Stefani Castellanos
         Francisco Sucre
'''

import unittest
from BilleteraElectronica import *
from decimal import Decimal

class TestcalcularPrecio(unittest.TestCase):

    def testUnCreditoCuentaVacia(self):
        billetera = BilleteraElectronica(1,'sergio','barrios',24101133,8)
        cred = Creditos(5,"25/4/2015","USB")
        billetera.Recargar(cred)
        self.assertEqual(billetera.Saldo(),5,"No funciona calcular un solo credito")       
        
    def testUnCreditoUnDebitoResultadoNoCero(self):
        billetera = BilleteraElectronica(1,'sergio','barrios',24101133,8)
        deb = Debitos(5,"2/5/2015","USB")
        cred = Creditos(7,"1/5/2015","USB")
        billetera.Recargar(cred)
        billetera.Consumir(deb)
        self.assertEqual(billetera.Saldo(),2,"No funciona calcular un credito y un debito")
        
    def testUnCreditoUnDebitoResultadoCero(self):
        billetera = BilleteraElectronica(1,'sergio','barrios',24101133,8)
        deb = Debitos(2,"1/5/2015","USB")
        cred = Creditos(2,"2/5/2015","USB")
        billetera.Recargar(cred)
        billetera.Consumir(deb)
        self.assertEqual(billetera.Saldo(),0,"No funciona calcular un credito y un debito que dejan en cero el saldo")
        
    def testRecargaUnica(self):
        billetera = BilleteraElectronica(1,'sergio','barrios',24101133,8)
        deb = Debitos(2,"2/5/2015","USB")
        cred = Creditos(2,"2/5/2015","USB")
        billetera.Recargar(cred)
        billetera.Consumir(deb)
        recarga_nueva = Creditos(6,"2/5/2015","USB")
        billetera.Recargar(recarga_nueva)
        self.assertEqual(billetera.Saldo(),6,"No funciona recargar un credito")
        
    def testConsumirConSaldoInsuficiente(self):
        billetera = BilleteraElectronica(1,'francisco','sucre',19564959,343)
        deb = Debitos(2,"2/5/2015","USB")
        self.assertRaises(Exception,billetera.Consumir, deb )
        
    def testConsumoUnicoConSuficienteCredito(self):
        billetera = BilleteraElectronica(1,'sergio','barrios',24101133,8)
        deb = Debitos(2,"2/5/2015","USB")
        cred = Creditos(9,"2/5/2015","USB")
        billetera.Recargar(cred)
        billetera.Consumir(deb)
        consumo_nuevo = Debitos(4,"2/5/2015","USB")
        billetera.Consumir(consumo_nuevo)
        self.assertEqual(billetera.Saldo(),3,"No funciona consumir credito cuando se tiene suficiente")

    def testRecargaConsumoMinimo(self):
        billetera = BilleteraElectronica(12,'sergio','barrios',24101133,8)
        cred = Creditos(0.01,"25/4/2015","USB")
        deb = Debitos(0.01,"25/4/2015","USB")
        billetera.Recargar(cred)
        billetera.Consumir(deb)
        self.assertEqual(billetera.Saldo(),0,"No funciona la operacion minima")    
        
    def testMegaRecargaMegaConsumo(self):
        billetera = BilleteraElectronica(2,'francisco','sucre',19564959,142)
        deb = Debitos(2^31,"2/5/2015","USB")
        cred = Creditos((2^31) + 1,"3/5/2015","USB")
        billetera.Recargar(cred)
        billetera.Consumir(deb)
        self.assertEqual(billetera.Saldo(), 1, "Existen Errores con la recarga/consumo grande")

    def testRecargaNoPositiva(self):
        billetera = BilleteraElectronica(3,'Stefani','Castellanos',25385981,1023)
        cred = Creditos(-1,"2/5/2015","USB")
        self.assertRaises(Exception, billetera.Recargar, cred)
        
    def testConsumoNopositivo(self):
        billetera = BilleteraElectronica(3,'Stefani','Castellanos',25385981,1023)
        deb = Debitos(-1,"2/5/2015","USB")
        self.assertRaises(Exception, billetera.Consumir, deb)
        
    def testConsumoDecimalInvalido(self):
        billetera = BilleteraElectronica(1,'sergio','barrios',24101133,8)
        deb = Debitos(2.01,"1/5/2015","USB")
        cred = Creditos(2,"2/5/2015","USB")
        billetera.Recargar(cred) 
        self.assertRaises(Exception, billetera.Consumir,deb)
        
    def testEntradaString(self):
        billetera = BilleteraElectronica(1,'sergio','barrios',24101133,8)
        self.assertRaises(Exception, Creditos, "hola", "2/5/2015", "USB" )
        
    def testEntradaTrue(self):
        billetera = BilleteraElectronica(1,'sergio','barrios',24101133,8)
        self.assertRaises(Exception, Creditos, True, "2/5/2015", "USB" )
        
    def testEntradaFalse(self):
        billetera = BilleteraElectronica(1,'sergio','barrios',24101133,8)
        self.assertRaises(Exception, Creditos, False, "2/5/2015", "USB" )
            
    def testNombreCaracteresEspeciales(self):
        billetera = BilleteraElectronica(1024,'Ramón','Nuñez',3981023,8)
        cred = Creditos(1,"25/4/2015","USB")
        billetera.Recargar(cred)
        self.assertEqual(billetera.Saldo(), 1,"No funcionan los caracteres especiales")      
        
    def testNombreCaracteresEspeciales(self):
        self.assertRaises(Exception, BilleteraElectronica, 1,'Ramón','Nuñez',-237920,8)
        
if __name__ == "__main__":
    unittest.main()
