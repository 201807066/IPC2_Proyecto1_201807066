import os
import sys
import time

class Matriz(object):
    """ nombre, pos_n, pos_m, dato """
    def __init__(self, nombre, pos_n, pos_m, dato):
        self.nombre = nombre
        self.pos_n = pos_n
        self.pos_m = pos_m
        self.dato = dato

    def datos(self):
        print("Nombre: {}".format(self.nombre))
        print("Dimensiones : {}x{}".format(self.pos_n, self.pos_m))
        


class Nodo():
    
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaCircular():
    
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def Vacia(self):
        return self.primero == None
    
    def AgregarInicio(self, dato):
        if self.Vacia():
            self.primero = self.ultimo = Nodo(dato)
            self.ultimo.siguiente = self.primero
        else:
            aux = Nodo(dato)
            aux.siguiente = self.primero
            self.primero = aux
            self.ultimo.siguiente = self.primero

    def AgragarFinal(self, dato):
        if self.Vacia():
            self.primero = self.ultimo = Nodo(dato)
            self.ultimo.siguiente = self.primero
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo(dato)
            self.ultimo.siguiente = self.primero

    def Recorrer(self):
        aux = self.primero
        while aux:
            print(aux.dato)
            aux = aux.siguiente
            if aux == self.primero:
                break