from Company.contaLogicNegocio import *
from Utils import *
from tabulate import tabulate
from datetime import datetime, date
import pandas
import locale
import time
import os

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

locale.setlocale(locale.LC_TIME, "es_ES")

caja = True

presentacion = True


def mainViewCompany(user, account):

    global caja

    if caja:

        caja = False

        initBalanceToMonth(user)

    selectedMenu = menuInventory(user, account)

    if selectedMenu == 1:

        addMovement()

    elif selectedMenu == 2:

        if not contabilityMatrix: 

            printTextEfect("\nTabla vacia\n", timer=0.03)

            time.sleep(1)
        
        else:

            showGeneralContability()

    elif selectedMenu == 3:

        menu1()

    elif selectedMenu == 4:

        return 4
    
    elif selectedMenu == 5:

        return 5


def titleProgram():

    """Método encargado de mostrar título principal
    del programa."""

    os.system('cls')

    printTextEfect("Bienvenido a ContalApp!", timer=0.03)

    time.sleep(1.1)

    os.system('cls')


def initBalanceToMonth(user):

    month = datetime.now().strftime("%B")

    fecha = date.today()

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


def menuInventory(user, account):

    """Método encargado de mostrar el menú."""

    os.system('cls')

    while True:

        presentProgram()

        information = informationProfile(user, account, "Empresas", getCurrentCashBalance())

        print("\n1.) Ingresar movimiento\n\n2.) Mostrar Contabilidad General\n\n3.) Control de inventario.\n\n4.) Retornar al menú de selección.\n\n5.) Salir\n")

        try:

            option = int(input("Selecciona una opción: "))

            if option > 0 and option < 6:

                return option
            
            else:
                
                os.system('cls')

                print("\nOpciones no permitidas.")

        except ValueError as e:

            os.system('cls')

            print(f"\nSolo se Permiten valores numéricos: {e}")


def presentProgram():
        
    global presentacion
    
    if presentacion:

        printTextEfect("\nIngresaste a ContalApp® Empresas, con nuestras herramientas,\n", timer=0.03)

        printTextEfect("\npodras llevar un seguimiento más claro y detallado de los moviemientos\n", timer=0.03)

        printTextEfect("\ngenerados por tu empresa.\n", timer=0.03)

        printTextEfect("\nD i s f r u t a !\n", timer=0.02)

        time.sleep(1.5)

        os.system('cls')

        presentacion = False


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
        for row in contabilityMatrix
    ]

    print(tabulate(formated, headers=headers, tablefmt="fancy_grid"))
    