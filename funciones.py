#from circularSimple import ListaCircular
import os, sys, time

from simple.ListaSimple import ListaSimple
from circularSimple.ListaCircular import  ListaCircular

import xml.etree.ElementTree as ET

matriz = ListaCircular()



def cls():
    os.system("cls")


def cargar():
    cls()

    try:
        
        posiciones = ListaSimple()
        print("********* Cargar archivo *********\n")
        datos = input("Ingrese la ruta del arxhivo xml:")
        archivo = ET.parse(datos)
        root = archivo.getroot()

        nodo_principal = root.tag
        if nodo_principal == "matrices":
            for elemento in root:               
                nombre = elemento.attrib['nombre']
                n = elemento.attrib['n']
                m = elemento.attrib['m']
                for sub in elemento:
                    x = sub.attrib['x']
                    y = sub.attrib['y']
                    numero = sub.text
                    posiciones.insertar(x, y, numero)
                p = posiciones
                matriz.AgragarFinal(nombre, n, m, p)
            print("Archivo cargado exitosamente")
            input()
        else:
            print("\n-*-*-*-*-*-*-*-*-*ERROR-*-*-*-*-*-*-*-*-*")
            input("El archivo que desea cargar no especifica el nodo pricipal 'matrices'....")
        
    except:
        input("Ruta del archivo no encontrado...")
        cargar()


    
def procesar_archivo():
    cls()
    print("********* Procesar archivo *********\n")
    matriz.Recorrer()
    input()

def escribir_archivo():
    cls()
    print("********* Escribir Archivo de salida *********\n")
    input("Escribir la ruta especifica: ")
    

def generar_grafica():
    cls()
    print("********* Generar gráfica *********\n")
    input("Nombre de la matriz que desea generar su gráfica: ")
    