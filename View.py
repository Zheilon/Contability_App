from Logic import *
from tabulate import tabulate
from datetime import datetime
import locale
import time
import os

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

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

    os.system('cls')

    while True:

<<<<<<< HEAD
        print("\n1.) Ingresar movimiento\n\n2.) Consultar utilidad Neta\n\n3.) Mostrar Contabilidad General\n")
=======
        print("\n1.) Ingresar movimiento\n\n2.) Consultar utilidad Neta\n\n3.) Mostrar Contabilidad General\n\n 4) Control de inventario")
>>>>>>> be8422a (Agrege una nueva opcion al menu control de inventario)

        try:

            option = int(input("Selecciona una opción: "))

            if option > 0 and option < 4:

                return option
            
            else:
                
                os.system('cls')

                print("\nOpciones no permitidas.")

        except ValueError as e:

            os.system('cls')

            print(f"\nSolo se Permiten valores numéricos: {e}")


def checkNetProfit() -> None:
    pass


def formatMiles(value):

    """Función encargada de darle formato de Miles a los números."""

    return locale.format_string("%d", value, grouping=True)


def showGeneralContability():
    
    """Función encargada de mostrar la tabla con los ejercicios Contables."""

    print()

    fecha = datetime.now().strftime("%B")

    print(f"| --- * LIBRO DE CAJA AUXILIAR * --- |")

    headers = ["Fecha", "Código", "Descripción", "Debe $", "Haber $", "Saldo De Caja $"]

    formated = [
        [row[0], row[1], row[2], 
         formatMiles(int(row[3])) if row[3] else '', 
         formatMiles(int(row[4])) if row[4] else '', 
         formatMiles(int(row[5])) if row[5] else ''] 
         for row in contabilityMatrix
    ]

    print(tabulate(formated, headers=headers, tablefmt="fancy_grid"))