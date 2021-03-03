from simple.Matriz import Matriz

class ListaSimple:
    def __init__(self):
        self.inicio = None

    #Insercion
    def insertar(self, pos_n, pos_m, numero):
        nuevo = Matriz(pos_n, pos_m, numero)
        if self.inicio is None:
            self.inicio = nuevo
        else:
            aux = self.inicio
            while aux.siguiente is not None:
                aux = aux.siguiente
            aux.siguiente = nuevo
    

    def mostrar(self):
        aux = self.inicio
        contador = 1
        while aux is not None:
            print(str(contador) + '. x:' + str(aux.pos_n)  + ', y: ' + str(aux.pos_m) + ', Dato: ' + str(aux.numero) + '\n')
            contador += 1
            aux = aux.siguiente

    #tamaño de la lista
    def tamaño(self):
        aux = self.inicio
        cont = 0
        while aux is not None:
            cont += 1
            aux = aux.siguiente
        return cont