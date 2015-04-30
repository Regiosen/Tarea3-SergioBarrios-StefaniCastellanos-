'''
Created on 29/4/2015

@author: Sergio Luis Barrios
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
        
#Caso de Prueba 1 (un credito y ningun debito), saldo de 5 = 5
        
billetera = BilleteraElectronica(1,'sergio','barrios',24101133,8)
lista = [Creditos(5)]
billetera.creditos = lista
print('heloo')
if (billetera.Saldo() == 5):
    print('caso 1 Pasado ')
    
#Caso de Prueba 2 (un credito y un debito)

billetera = BilleteraElectronica(1,'sergio','barrios',24101133,8)
lista = [Creditos(7)]
lista = [Creditos(5)]
billetera.debitos = lista
print('heloo')
if (billetera.Saldo() == 2):
    print('caso 1 Pasado ')
