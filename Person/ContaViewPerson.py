from Person.ContaLogicPerson import *
from Utils import *
from tabulate import tabulate
from datetime import datetime, date
import locale
import time
import os

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

locale.setlocale(locale.LC_TIME, "es_ES")

saldoInicial = True


def mainViewPerson():

    global saldoInicial

    if saldoInicial:

        saldoInicial = False

        initBalanceToMonth()

    selectedMenu = menuPerson()

    if selectedMenu == 1:

        addMovement()

    elif selectedMenu == 2:

        if not contabilityMatrixPerson: 

            printTextEfect("\nTabla vacia\n", timer=0.03)

            time.sleep(1)
        
        else:

            showGeneralContability()


def titleProgram():

    """Método encargado de mostrar título principal
    del programa."""

    os.system('cls')

    printTextEfect("Bienvenido a ContalApp!", timer=0.03)

    time.sleep(1.1)

    os.system('cls')


def initBalanceToMonth():

    month = datetime.now().strftime("%B")

    fecha = date.today()

    os.system('cls')

    printTextEfect("\nAntes de seguir...\n", timer=0.03)

    printTextEfect(f"\nPrimero necesitas establecer el efectivo de caja inicial para el mes {month:}!\n\n", timer=0.03)

    while True:

        efectivoInicial = int(input("Ingresa efectivo de caja inicial: "))

        if efectivoInicial > 0:

            saveAll(fecha, "EFI", "Efectivo de caja inicial", "", "", efectivoInicial)

            printTextEfect(f"\nPerfecto! estableciste un efectivo inicial de: $ {efectivoInicial:,.0f}.\n", timer=0.03)

            printTextEfect("\nContinuemos!\n", timer=0.03)

            time.sleep(1.1)

            break

        else:

            printTextEfect("\nNo puedes Ingresar Unidades Negativas!\n", timer=0.03)

            time.sleep(1.1)

            os.system('cls')


def menuPerson():

    """Método encargado de mostrar el menú."""

    os.system('cls')

    while True:

        print("ContalApp® Personas")

        print("\n1.) Ingresar movimiento\n\n2.) Mostrar Contabilidad General\n")

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

    month = datetime.now().strftime("%B").upper()

    year = datetime.now().year

    print(f"| --- * LIBRO AUXILIAR DE CAJA - MES {month} AÑO {year} * --- |")

    headers = ["Fecha", "Código", "Descripción", "Debe $", "Haber $", "Saldo De Caja $"]

    formated = [[row[0], row[1], row[2], 
        formatMiles(int(row[3])) if row[3] else '', 
        formatMiles(int(row[4])) if row[4] else '', 
        formatMiles(int(row[5])) if row[5] else ''] 
        for row in contabilityMatrixPerson
    ]

    print(tabulate(formated, headers=headers, tablefmt="fancy_grid"))


def isPersonOrCompany():

    printTextEfect("Hola!", 0.03)

    time.sleep(1.1)

    os.system('cls')

    print("ContalApp®\n")

    printTextEfect("Vas a manejar esta aplicación para: \n", 0.03)

    printTextEfect("\n1.) Uso personal.\n", 0.03)

    printTextEfect("\n2.) Negocio y/o Emprendimiento.\n\n", 0.03)

    while True:

        try: 
            
            return int(input("Selecciona opción: "))
        
        except ValueError as vl:

            print(f"\nSolo se permiten valores numéricos: {vl}\n")