import os
import sys
import time
#import xml.ElementTree as ET
#from obj_matriz import *


def cls():
    os.system("cls")

def cargar():
    cls()
    try:
        print("********* Cargar archivo *********\n")
        datos = input("Ingrese la ruta del archivo xml: ")
        archivo = open(datos, 'r', encoding='UTF-8')
        lienas = archivo.readlines()
        archivo.close()

        for liena in lienas:
            print(liena)
            time.sleep(0.05)
        print("\nArchivo cargado correctamente")
        time.sleep(1)
        cls()
    except:
        input("Ruta del archivo no encontrado...")
        cargar()

def procesar_archivo():
    cls()
    print("********* Procesar archivo *********\n")
    input()

def escribir_archivo():
    cls()
    print("********* Escribir Archivo de salida *********\n")
    input("Escribir la ruta especifica: ")
    

def generar_grafica():
    cls()
    print("********* Generar gráfica *********\n")
    input("Nombre de la matriz que desea generar su gráfica: ")
    