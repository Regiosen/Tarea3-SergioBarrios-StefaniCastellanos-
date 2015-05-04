'''
Created on 29/4/2015
@author: Sergio Luis Barrios
         Stefani Castellanos
         Francisco Sucre
'''

# -*- coding: UTF-8 -*-

class Creditos(object):
    def __init__(self, monto, fecha_transaccion, id_establecimiento):
        self.monto = monto
        self.fecha_transaccion = fecha_transaccion
        self.id_establecimiento = id_establecimiento

class Debitos(object):
    def __init__(self, monto, fecha_transaccion, id_establecimiento):
        self.monto = monto
        self.fecha_transaccion = fecha_transaccion
        self.id_establecimiento = id_establecimiento
        
class BilleteraElectronica(object):
    '''
    classdocs
    '''

    def __init__(self, ID, nombre, apellido, CI, PIN):
        self.ID = ID
        self.nombre = nombre
        self.apellido = apellido
        self.CI= CI
        self.PIN = PIN
        self.creditos = []
        self.debitos = []
        self.saldo = 0
        
    def Saldo(self):
        return self.saldo
            
    def Recargar(self,creditoEntrante):
        if (creditoEntrante.monto <= 0):
            raise Exception("No es posible recargar una cantidad no positiva")     

        self.creditos.append(creditoEntrante)
        self.saldo = self.saldo + creditoEntrante.monto
        
    def Consumir(self,debitoEntrante):
        
        if (debitoEntrante.monto <= 0):
            raise Exception("No es posible consumir una cantidad no positiva")     

        if (self.saldo - debitoEntrante.monto < 0):
            raise Exception("No tiene sufieciente fondos para efectuar la operacion")     

        self.debitos.append(debitoEntrante)
        self.saldo = self.saldo - debitoEntrante.monto