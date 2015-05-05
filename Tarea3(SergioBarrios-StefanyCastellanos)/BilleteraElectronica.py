# -*- coding: UTF-8 -*-
'''
Created on 29/4/2015
@author: Sergio Luis Barrios
         Stefani Castellanos
         Francisco Sucre
'''

from decimal import Decimal
from datetime import datetime
import hashlib

class Creditos(object):
    
    def __init__(self, monto, id_establecimiento):
        
        if (isinstance(monto, str) or isinstance(monto, bool) ):
            raise Exception("Debe ingresar un monto numerico")
        
        self.monto = Decimal(monto).quantize(Decimal('1.00'))
        self.fecha_transaccion = datetime.today()
        self.id_establecimiento = id_establecimiento

class Debitos(object):
    def __init__(self, monto, id_establecimiento):
        
        if (isinstance(monto, str) or isinstance(monto, bool) ):
            raise Exception("Debe ingresar un monto numerico de tipo Decimal")
        
        self.monto = Decimal(monto).quantize(Decimal('1.00'))
        self.fecha_transaccion = datetime.today()
        self.id_establecimiento = id_establecimiento
        
class BilleteraElectronica(object):

    def __init__(self, ID, nombre, apellido, CI, PIN):
        
        if (not isinstance(CI, int) or (CI <= 0)):
            raise Exception("Debe ingresar un monto numerico")
        
        self.ID = ID 
        self.nombre = nombre
        self.apellido = apellido
        self.CI = CI 
        self.PIN = hashlib.sha512(PIN)
        self.creditos = []
        self.debitos = []
        self.saldo = 0
        
    def Saldo(self):
        return Decimal(self.saldo).quantize(Decimal('1.00'))
            
    def Recargar(self,creditoEntrante):
        
        if (creditoEntrante.monto <= 0):
            raise Exception("No es posible recargar una cantidad no positiva")       

        self.creditos.append(creditoEntrante)
        self.saldo += creditoEntrante.monto
        
    def Consumir(self,debitoEntrante):
        
        if (debitoEntrante.monto <= 0):
            raise Exception("No es posible consumir una cantidad no positiva")     

        if (self.saldo - debitoEntrante.monto < 0):
            raise Exception("No tiene sufieciente fondos para efectuar la operacion")  
        
        self.debitos.append(debitoEntrante)
        self.saldo -= debitoEntrante.monto