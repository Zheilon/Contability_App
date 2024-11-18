from Utils import *
from datetime import datetime
from tabulate import tabulate
import pandas as pd
import os
import time

contabilityMatrixPerson = []


def getDate():

    """Esta función obtiene la fecha actual."""

    os.system('cls')

    printTextEfect("Fecha obtenida Automáticamente!", 0.03)

    time.sleep(1)

    return datetime.now().strftime("%d/%m/%Y")


def getContabilityCodes():

    """Esta función se encarga de primero mostrar y luego, 
    retornar el código seleccionado."""
    
    os.system('cls')

    while True:

        print("Codigos Disponibles: \n")

        #* INT = INGRESOS, CM = COMPRAS, GST = GASTOS #*

        listOfCodes = ["ING", "CM", "GST"]

        listCodesDescription = ["ING (Ingreso)", "CM (Compra)", "GST (Gasto)"]
    
        for z in range(len(listCodesDescription)):

            print(f"{z + 1}. {listCodesDescription[z]}\n")

        try:

            code = int(input("Selecciona Código: "))

            if code > 0 and code < 4:

                return listOfCodes[code - 1]
            
            else:

                os.system('cls')
                
                print("\nRangos no permitidos.\n")

        except ValueError as vl:

            os.system('cls')    

            print(f"\nSolo se permiten valores númericos: {vl}.\n")


def getDescription():

    """Esta función obtiene la descripción escrita por el usuario."""

    os.system('cls')

    return str(input("Ingresa Descripción: "))



def registerMovement(fecha, code, description):

    """Esta función se encarga de obtener un valor 'n', para luego adicionarlo
    en una lista, que se añadirá a la matriz principal"""

    os.system('cls')

    value = int(input("Ingresa Valor: "))

    if code == "ING":

        saveAll(fecha, code, description, value, "", getBalance(value, code=code))

    elif code == "CM":
        
        saveAll(fecha, code, description, "", value, getBalance(value, code=code))

    elif code == "GST":
        
        saveAll(fecha, code, description, "", value, getBalance(value, code=code))


def saveAll(date, code, description, debe, haber , saldo):

    """Esta función se encarga de guardar en la matriz principal una lista con 
    todos los elementos necesarios que componen un ejercicio contable."""

    contabilityMatrixPerson.append([date, code, description, debe, haber, saldo])
    

def getBalance(value, code):

    """Función encargada de determinar y retornar el saldo, 
    despues de cada ejercicio contable."""

    for z in range(len(contabilityMatrixPerson)):

        for w in range(len(contabilityMatrixPerson[0])):

            if z == len(contabilityMatrixPerson) - 1 and w == 5 and code == "ING":

                return contabilityMatrixPerson[z][w] + value
            
            elif z == len(contabilityMatrixPerson) - 1 and w == 5 and code == "CM":

                return contabilityMatrixPerson[z][w] - value
    
            elif z == len(contabilityMatrixPerson) - 1 and w == 5 and code == "GST":

                return contabilityMatrixPerson[z][w] - value
            

def getCurrentCashBalance():

    """Función encargada de obtener el saldo de caja actual."""

    for z in range(len(contabilityMatrixPerson)):

        for w in range(len(contabilityMatrixPerson[0])):

            if z == len(contabilityMatrixPerson) - 1 and w == 5:

                return contabilityMatrixPerson[z][w]
                

def addMovement():

    """Función encargada añadir un nuevo movimiento contable."""

    fecha = getDate()

    code = getContabilityCodes()

    description = getDescription()

    registerMovement(fecha, code, description)


def functionExample() -> list[list]:

    df = pd.read_excel("work.xlsx", sheet_name="Hoja 1")

    listExcel = df.values.tolist()

    return listExcel
