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
    
    #prueba de TDD
    
    def testUnCreditoCuentaVacia(self):
        billetera = BilleteraElectronica(1,'sergio','barrios',24101133,"8")
        cred = Creditos(5, "USB")
        billetera.Recargar(cred)
        self.assertEqual(billetera.Saldo(),5,"No funciona calcular un solo credito")
        
    #prueba de TDD
        
    def testUnCreditoUnDebitoResultadoNoCero(self):
        billetera = BilleteraElectronica(1,'sergio','barrios',24101133,"8")
        deb = Debitos(5, "USB")
        cred = Creditos(7, "USB")
        billetera.Recargar(cred)
        billetera.Consumir(deb, "8")
        self.assertEqual(billetera.Saldo(),2,"No funciona calcular un credito y un debito")
        
    #prueba de TDD
        
    def testUnCreditoUnDebitoResultadoCero(self):
        billetera = BilleteraElectronica(1,'sergio','barrios',24101133, "8")
        deb = Debitos(2, "USB")
        cred = Creditos(2, "USB")
        billetera.Recargar(cred)
        billetera.Consumir(deb, "8")
        self.assertEqual(billetera.Saldo(),0,"No funciona calcular un credito y un debito que dejan en cero el saldo")
        
    #prueba de TDD
            
    def testRecargaUnica(self):
        billetera = BilleteraElectronica(1,'sergio','barrios',24101133, "8")
        deb = Debitos(2, "USB")
        cred = Creditos(2, "USB")
        billetera.Recargar(cred)
        billetera.Consumir(deb, "8")
        recarga_nueva = Creditos(6, "USB")
        billetera.Recargar(recarga_nueva)
        self.assertEqual(billetera.Saldo(),6,"No funciona recargar un credito")
        
    #prueba de TDD
    
    def testConsumirConSaldoInsuficiente(self):
        billetera = BilleteraElectronica(1,'francisco','sucre',19564959, "343")
        deb = Debitos(2, "USB")
        self.assertRaises(Exception,billetera.Consumir, deb )
        
    #prueba de TDD
        
    def testConsumoUnicoConSuficienteCredito(self):
        billetera = BilleteraElectronica(1,'sergio','barrios',24101133, "8")
        deb = Debitos(2, "USB")
        cred = Creditos(9, "USB")
        billetera.Recargar(cred)
        billetera.Consumir(deb, "8")
        consumo_nuevo = Debitos(4, "USB")
        billetera.Consumir(consumo_nuevo, "8")
        self.assertEqual(billetera.Saldo(),3,"No funciona consumir credito cuando se tiene suficiente")
        
    #prueba de frontera
    
    def testRecargaConsumoMinimo(self):
        billetera = BilleteraElectronica(12,'sergio','barrios',24101133, "8")
        cred = Creditos(0.01 ,"USB")
        deb = Debitos(0.01, "USB")
        billetera.Recargar(cred)
        billetera.Consumir(deb, "8")
        self.assertEqual(billetera.Saldo(),0,"No funciona la operacion minima")
        
    #prueba de frontera

    def testMegaRecargaMegaConsumo(self):
        billetera = BilleteraElectronica(2,'francisco','sucre',19564959,"142")
        deb = Debitos(2^31, "USB")
        cred = Creditos((2^31) + Decimal(0.01), "USB")
        billetera.Recargar(cred)
        billetera.Consumir(deb, "142")
        self.assertEqual(billetera.Saldo(), Decimal(0.01).quantize(Decimal("1.00")), "Existen Errores con la recarga/consumo grande")
        
    #TDD

    def testRecargaNoPositiva(self):
        billetera = BilleteraElectronica(3,'Stefani','Castellanos',25385981, "1023")
        cred = Creditos(-0.01, "USB")
        self.assertRaises(Exception, billetera.Recargar, cred)
        
    #TDD y frontera

    def testConsumoNopositivo(self):
        billetera = BilleteraElectronica(3,'Stefani','Castellanos',25385981,"1023")
        deb = Debitos(-0.01, "USB")
        self.assertRaises(Exception, billetera.Consumir, deb)

    #TDD y malicia

    def testConsumoDecimalInvalido(self):
        billetera = BilleteraElectronica(1,'sergio','barrios',24101133, "8")
        deb = Debitos(2.01, "USB")
        cred = Creditos(2, "USB")
        billetera.Recargar(cred)
        self.assertRaises(Exception, billetera.Consumir,deb)
        
    #malicia

    def testEntradaStringCred(self):
        billetera = BilleteraElectronica(1,'sergio','barrios',24101133, "8")
        self.assertRaises(Exception, Creditos, "hola", "USB" )
        
    #malicia
    
    def testEntradaStringDeb(self):
        billetera = BilleteraElectronica(1,'sergio','barrios',24101133, "8")
        self.assertRaises(Exception, Debitos, "hola", "USB" )
        
    #malicia

    def testEntradaBooleanoCreditos(self):
        billetera = BilleteraElectronica(1,'sergio','barrios',24101133, "8")
        self.assertRaises(Exception, Creditos, True, "USB" )
        
    #malicia
        
    def testEntradaBooleanoDebitos(self):
        billetera = BilleteraElectronica(1,'sergio','barrios',24101133, "8")
        self.assertRaises(Exception, Debitos, True, "USB" )
        
    #malicia
    
    def testNombreCaracteresEspeciales(self):
        billetera = BilleteraElectronica(1024,'Ramón','Nuñez',3981023, "8")
        cred = Creditos(1,"USB")
        billetera.Recargar(cred)
        self.assertEqual(billetera.Saldo(), 1,"No funcionan los caracteres especiales")
        
    #malicia

    def testCedulaNegativa(self):
        self.assertRaises(Exception, BilleteraElectronica, 1,'Ramón','Nuñez',-237920, "8")
        
    #malicia

    def testFechaNoEsDateTime(self):
        self.assertRaises(Exception, Creditos, 1,"kkkaajsjjddff1212j","USB")
        
    #frontera y esquina
        
    def testBilleteraStringsVacios(self):
        billetera = BilleteraElectronica(1024,'','',3981023, "")
        cred = Creditos(1,"USB")
        billetera.Recargar(cred)
        self.assertEqual(billetera.Saldo(), 1,"Hay un error con entradas de string vacios")
        
    #frontera

    def testCreditoStringVacio(self):
        billetera = BilleteraElectronica(1024,'Ramón','Nuñez',237920, "8")
        cred = Creditos(1,"")
        billetera.Recargar(cred)
        self.assertEqual(billetera.Saldo(), 1,"Hay un error con entradas de string vacios")
        
    #frontera
        
    def testDebitoStringVacio(self):
        billetera = BilleteraElectronica(1024,'Ramón','Nuñez',237920, "8")
        cred = Creditos(1,"")
        billetera.Recargar(cred)
        deb = Debitos(1,"")
        billetera.Consumir(deb, "8")
        self.assertEqual(billetera.Saldo(), 0,"Hay un error con entradas de string vacios")
        
    #TDD

    def testPINIncorrecto(self):
        billetera = BilleteraElectronica(1024,'Fallo','Oh no!',3981023, "1024")
        cred = Creditos(10.01,"USB")
        deb = Debitos(2.99, "USB")
        self.assertRaises(Exception, billetera.Consumir, deb, "2" )
        
    
if __name__ == "__main__":
    unittest.main()