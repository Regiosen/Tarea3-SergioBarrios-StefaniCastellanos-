'''
Created on 29/4/2015

@author: Sergio Luis Barrios
         Stefani Castellanos
         Francisco Sucre
'''

import sys
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
        self.saldo = 0
        
        for i in self.creditos:
            self.saldo = self.saldo + i.monto
             
        for j in self.debitos:
            self.saldo = self.saldo - j.monto
            
        if (self.saldo <0):
            sys.exit ('ERROR: Saldo negativo')
            
        elif (self.saldo >=0):     
            return self.saldo
            
    def Recargar(self,creditoEntrante):
        self.creditos.append(creditoEntrante)
        self.saldo = self.saldo + creditoEntrante.monto
        
    def Consumir(self,debitoEntrante):
        self.debitos.append(debitoEntrante)
        self.saldo = self.saldo - debitoEntrante.monto
        