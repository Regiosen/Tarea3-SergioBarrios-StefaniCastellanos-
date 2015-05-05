# -*- coding: UTF-8 -*-
'''
@author: Sergio Luis Barrios
         Stefani Castellanos
         Francisco Sucre
'''

import unittest
from BilleteraElectronica import *
from decimal import Decimal
from datetime import datetime

class TestcalcularPrecio(unittest.TestCase):

    def testUnCreditoCuentaVacia(self):
        billetera = BilleteraElectronica(1,'sergio','barrios',24101133,8)
        cred = Creditos(5,datetime(1997,12,2,13,43),"USB")
        billetera.Recargar(cred)
        self.assertEqual(billetera.Saldo(),5,"No funciona calcular un solo credito")       
        
    def testUnCreditoUnDebitoResultadoNoCero(self):
        billetera = BilleteraElectronica(1,'sergio','barrios',24101133,8)
        deb = Debitos(5,datetime(2001,8,1,5,20),"USB")
        cred = Creditos(7,datetime(2014,8,20,22,30),"USB")
        billetera.Recargar(cred)
        billetera.Consumir(deb)
        self.assertEqual(billetera.Saldo(),2,"No funciona calcular un credito y un debito")
        
    def testUnCreditoUnDebitoResultadoCero(self):
        billetera = BilleteraElectronica(1,'sergio','barrios',24101133,8)
        deb = Debitos(2,datetime(2014,8,20,22,30),"USB")
        cred = Creditos(2,datetime(2014,8,20,22,30),"USB")
        billetera.Recargar(cred)
        billetera.Consumir(deb)
        self.assertEqual(billetera.Saldo(),0,"No funciona calcular un credito y un debito que dejan en cero el saldo")
        
    def testRecargaUnica(self):
        billetera = BilleteraElectronica(1,'sergio','barrios',24101133,8)
        deb = Debitos(2,datetime(2014,8,20,22,30),"USB")
        cred = Creditos(2,datetime(2014,8,20,22,30),"USB")
        billetera.Recargar(cred)
        billetera.Consumir(deb)
        recarga_nueva = Creditos(6,datetime(2014,8,20,22,30),"USB")
        billetera.Recargar(recarga_nueva)
        self.assertEqual(billetera.Saldo(),6,"No funciona recargar un credito")
        
    def testConsumirConSaldoInsuficiente(self):
        billetera = BilleteraElectronica(1,'francisco','sucre',19564959,343)
        deb = Debitos(2,datetime(2014,8,20,22,30),"USB")
        self.assertRaises(Exception,billetera.Consumir, deb )
        
    def testConsumoUnicoConSuficienteCredito(self):
        billetera = BilleteraElectronica(1,'sergio','barrios',24101133,8)
        deb = Debitos(2,datetime(2014,8,20,22,30),"USB")
        cred = Creditos(9,datetime(2014,8,20,22,30),"USB")
        billetera.Recargar(cred)
        billetera.Consumir(deb)
        consumo_nuevo = Debitos(4,datetime(2014,8,20,22,30),"USB")
        billetera.Consumir(consumo_nuevo)
        self.assertEqual(billetera.Saldo(),3,"No funciona consumir credito cuando se tiene suficiente")

    def testRecargaConsumoMinimo(self):
        billetera = BilleteraElectronica(12,'sergio','barrios',24101133,8)
        cred = Creditos(0.01,datetime(2014,8,20,22,30),"USB")
        deb = Debitos(0.01,datetime(2014,8,20,22,30),"USB")
        billetera.Recargar(cred)
        billetera.Consumir(deb)
        self.assertEqual(billetera.Saldo(),0,"No funciona la operacion minima")    
        
    def testMegaRecargaMegaConsumo(self):
        billetera = BilleteraElectronica(2,'francisco','sucre',19564959,142)
        deb = Debitos(2^31,datetime(2014,8,20,22,30),"USB")
        cred = Creditos((2^31) + 1,datetime(2014,8,20,22,30),"USB")
        billetera.Recargar(cred)
        billetera.Consumir(deb)
        self.assertEqual(billetera.Saldo(), 1, "Existen Errores con la recarga/consumo grande")

    def testRecargaNoPositiva(self):
        billetera = BilleteraElectronica(3,'Stefani','Castellanos',25385981,1023)
        cred = Creditos(-1,datetime(2014,8,20,22,30),"USB")
        self.assertRaises(Exception, billetera.Recargar, cred)
        
    def testConsumoNopositivo(self):
        billetera = BilleteraElectronica(3,'Stefani','Castellanos',25385981,1023)
        deb = Debitos(-1,datetime(2014,8,20,22,30),"USB")
        self.assertRaises(Exception, billetera.Consumir, deb)
        
    def testConsumoDecimalInvalido(self):
        billetera = BilleteraElectronica(1,'sergio','barrios',24101133,8)
        deb = Debitos(2.01,datetime(2016,3,11,12,20),"USB")
        cred = Creditos(2,datetime(2014,8,20,22,30),"USB")
        billetera.Recargar(cred) 
        self.assertRaises(Exception, billetera.Consumir,deb)
        
    def testEntradaString(self):
        billetera = BilleteraElectronica(1,'sergio','barrios',24101133,8)
        self.assertRaises(Exception, Creditos, "hola", datetime(2014,8,20,22,30), "USB" )
        
    def testEntradaTrue(self):
        billetera = BilleteraElectronica(1,'sergio','barrios',24101133,8)
        self.assertRaises(Exception, Creditos, True, datetime(2014,8,20,22,30), "USB" )
        
    def testEntradaFalse(self):
        billetera = BilleteraElectronica(1,'sergio','barrios',24101133,8)
        self.assertRaises(Exception, Creditos, False, datetime(2014,8,20,22,30), "USB" )
            
    def testNombreCaracteresEspeciales(self):
        billetera = BilleteraElectronica(1024,'Ramón','Nuñez',3981023,8)
        cred = Creditos(1,datetime(2014,8,20,22,30),"USB")
        billetera.Recargar(cred)
        self.assertEqual(billetera.Saldo(), 1,"No funcionan los caracteres especiales")      
        
    def testCedulaNegativa(self):
        self.assertRaises(Exception, BilleteraElectronica, 1,'Ramón','Nuñez',-237920,8)
    
    def testFechaNoEsDateTime(self):
        self.assertRaises(Exception, Creditos, 1,"kkkaajsjjddff1212j","USB")
        
if __name__ == "__main__":
    unittest.main()
