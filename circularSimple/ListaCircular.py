#from Proyecto1.circularsimple.Clase import  Clase
from circularSimple.Clase import Clase

class ListaCircular():
    
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def Vacia(self):
        return self.primero == None
    
    def AgragarInicio(self, nombre, tam_n, tam_m, dato):
        if self.Vacia():
            self.primero = self.ultimo = Clase(nombre, tam_n, tam_m, dato)
            self.ultimo.siguiente = self.primero
        else:
            aux = Clase(nombre, tam_n, tam_m, dato)
            aux.siguiente = self.primero
            self.primero = aux
            self.ultimo.siguiente = self.primero
    
    def AgragarFinal(self, nombre, tam_n, tam_m, dato):
        if self.Vacia():
            self.primero = self.ultimo = Clase(nombre, tam_n, tam_m, dato)
            self.ultimo.siguiente = self.primero
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Clase(nombre, tam_n, tam_m, dato)
            self.ultimo.siguiente = self.primero

    def Recorrer(self):
        aux = self.primero
        while aux:
            print('Nombre: ' + str(aux.nombre) + '    n: ' + str(aux.tam_n) + '   m: ' + str(aux.tam_m) + '\n')
            print('Posiciones: ' + str(aux.dato.mostrar()))
            aux = aux.siguiente
            if aux == self.primero:
                break