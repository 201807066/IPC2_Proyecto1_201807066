import os
import sys
import time
import funciones

def cls():
    os.system('cls')

def menuPrincipal():
    cls()
    while True:
        print("************* PROYECTO 1 *************\n")
        print("Menú Principal")
        print("1) Cargar archivo de entrada")
        print("2) Procesar archivo")
        print("3) Escribir archivo salida")
        print("4) Mostrar datos del estudiante")
        print("5) Generar gráfica")
        print("6) Salir")
        opc = input("\nOpción a realizar: ")

        if opc == "1":
            funciones.cargar()
            menuPrincipal()
            break
        elif opc == "2":
            funciones.procesar_archivo()
            menuPrincipal()
            break
        elif opc == "3":
            funciones.escribir_archivo()
            menuPrincipal()
            break
        elif opc == "4":
            cls()
            print("****************************************")
            print("**** Introducción a la Programación ****")
            print("****        y Computación 2         ****")
            print("****          Sección A             ****")
            print("****                                ****")
            print("****      Ciencias y sistemas       ****")
            print("****         4to Semestre           ****")
            print("****   Brayan Andrés Cholotio Tum   ****")
            print("****           201807066            ****")
            print("****************************************\n")
            input("Presione cualquier tecla para continuar...")
            menuPrincipal()
            cls()
            break
        elif opc == "5":
            funciones.generar_grafica()
            menuPrincipal()
            break
        elif opc == "6":
            cls()
            print("Saliendo del sistema...")
            time.sleep(2)
            os.system("exit")
            break
        else:
            print("Opción incorrecta...")
            time.sleep(1)
            cls() 

menuPrincipal()