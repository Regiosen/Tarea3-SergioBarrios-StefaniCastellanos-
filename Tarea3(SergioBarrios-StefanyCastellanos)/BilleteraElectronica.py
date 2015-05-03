'''
Created on 29/4/2015

@author: Sergio Luis Barrios
         Stefani Castellanos
'''

import sys

class Creditos(object):
    def __init__(self,mont):
        self.monto = mont

class Debitos(object):
    def __init__(self,mont):
        self.monto = mont        

class BilleteraElectronica(object):
    '''
    classdocs
    '''

    def __init__(self, Identificador,Nombre,Apellido, Cedula, PIN):
        self.ID = Identificador
        self.nombre = Nombre
        self.apellido = Apellido
        self.ci= Cedula
        self.pin = PIN
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
            