from Person.ContaLogicPerson import *
from Utils import *
from tabulate import tabulate
from datetime import datetime
import locale
import time
import os

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

locale.setlocale(locale.LC_TIME, "es_ES")

saldoInicial = True

presentacion = True


def mainViewPerson(user, account):

    global saldoInicial

    if saldoInicial:

        saldoInicial = False

        initBalanceToMonth(user)

    selectedMenu = menuPerson(user, account)

    if selectedMenu == 1:

        addMovement()

    elif selectedMenu == 2:

        if not contabilityMatrixPerson: 

            printTextEfect("\nTabla vacia\n", timer=0.03)

            time.sleep(1)
        
        else:

            showGeneralContability()

    elif selectedMenu == 3:

        return 3
    
    elif selectedMenu == 4:

        os.system('cls')

        printTextEfect("Saliendo del Programa!\n", 0.02)

        time.sleep(2)

        return 4


def titleProgram():

    """Método encargado de mostrar título principal
    del programa."""

    os.system('cls')

    printTextEfect("Bienvenido a ContalApp!", timer=0.03)

    time.sleep(1.1)

    os.system('cls')


def initBalanceToMonth(user):

    month = datetime.now().strftime("%B")

    fecha = datetime.now().strftime("%d/%m/%Y")

    os.system('cls')

    printTextEfect(f"\n{user}! Antes de seguir...\n", timer=0.03)

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


def presentProgram():
        
    global presentacion
    
    if presentacion:

        printTextEfect("\nIngresaste a ContalApp® Personas, con nuestras herramientas,\n", timer=0.03)

        printTextEfect("\npodras llevar un seguimiento más claro de tu contabilidad diaria.\n", timer=0.03)

        printTextEfect("\nD i s f r u t a !\n", timer=0.02)

        time.sleep(1.5)

        os.system('cls')

        presentacion = False


def menuPerson(user, account):

    """Método encargado de mostrar el menú."""

    charOne = "+"

    os.system('cls')

    while True:

        presentProgram()

        information = informationProfile(user, account, "Personas", getCurrentCashBalance())

        distance = len(information) - 1

        print()

        for z in range(len(information)):

            if z == 0: 
                
                print(end="+")

            elif z == len(information) - 1:

                print(end="+")

            else:

                print(end="-")

        print()

        listOptions = ["1.) Ingresar movimiento", "2.) Mostrar Contabilidad General", "3.) Retornar al menú de selección.", "4.) Salir del Programa."]

        for z in range(len(listOptions)):

            if z < len(listOptions) - 1:

                print(f"| {listOptions[z]:<{distance - 2}}|\n{charOne:<{distance}}+")

            else: 
                
                print(f"| {listOptions[z]:<{distance - 2}}|")

        for z in range(len(information)):

            if z == 0: 
                
                print(end="+")

            elif z == len(information) - 1:

                print(end="+")

            else:

                print(end="-")

        print()

        try:

            option = int(input("Selecciona una opción: "))

            if option > 0 and option < 5:

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


def setNameUser():

    """Función encargada de establecer el nombre del usuario."""

    os.system('cls')

    printTextEfect("Establece un nombre de usuario!\n", 0.03)

    time.sleep(1.1)

    os.system('cls')

    return str(input("Username: "))

def showExcelTable():

    print(tabulate(functionExample(), tablefmt="fancy_grid"))