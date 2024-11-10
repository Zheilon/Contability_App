from Logic import *
from tabulate import tabulate
from prettytable import PrettyTable
import pandas as ps
import time
import os

def titleProgram():

    """Método encargado de mostrar título principal
    del programa."""

    listLetters = ['C','u','e','n','t','a','l','A','p','p']
    for z in listLetters:
        print(f"{z}")
        time.sleep(0.2)

    time.sleep(0.6)
    os.system('cls')
    

def menu():

    """Método encargado de mostrar el menú."""

    print("\n1.) Ingresar movimiento\n2.) Consultar utilidad Neta\n3.) Mostrar Contabilidad General")

    while True:

        option = int(input("Selecciona una opción: "))
        if option >= 1 and option <= 3:
            return option
        
        else:
            print("\nOpciones no permitidas.\n")


def checkNetProfit() -> None:
    pass

def showGeneralContability():

    print(tabulate(listN, headers=["Nombre", "Edad"], tablefmt="grid"))