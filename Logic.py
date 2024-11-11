import os
import time
from datetime import date
contabilityMatrix = []

firstMov = True

everyMov = False

def valueSaldo(a, b):

    """Función encargada de calcular el saldo."""

    return a - b

def getDate():

    """Esta función obtiene la fecha escrita por el usuario."""

    os.system('cls')

    print("Fecha obtenida Automaticamente!")

    time.sleep(1.5)

    return date.today()


def getContabilityCodes():

    """Esta función se encarga de primero mostrar y luego, 
    retornar el código seleccionado."""

    os.system('cls')

    print("Codigos Disponibles: \n")

    #* VT = VENTAS, CM = COMPRAS, GST = GASTOS #*

    listOfCodes = ["VT", "CM", "GST"]

    for z in range(len(listOfCodes)):

        print(f"{z + 1}. {listOfCodes[z]}")

    return listOfCodes[(int(input("Selecciona Código: "))) - 1]


def getDescription():

    """Esta función obtiene la descripción escrita por el usuario."""

    return str(input("Ingresa Descripción: "))


def registerMovement(fecha, code, description):

    """Esta función se encarga de obtener un valor 'n', para luego adicionarlo
    en una lista, que se añadirá a la matriz principal"""

    value = int(input("Ingresa Valor: "))

    if code == "VT":

        saveAll(fecha, code, description, value, "", getBalance(value, code=code))

    elif code == "CM":
        
        saveAll(fecha, code, description, "", value, getBalance(value, code=code))

    elif code == "GST":
        
        saveAll(fecha, code, description, "", value, getBalance(value, code=code))


def saveAll(date, code, description, debe, haber , saldo):

    """Esta función se encarga de guardar en una lista, todos los elementos
    necesarios que componen un ejercicio contable."""

    contabilityMatrix.append([date, code, description, debe, haber, saldo])
    

def getBalance(value, code):

    """Función encargada de determinar y retornar los 
    saldos, despues de cada ejercicio contable."""

    global firstMov

    global everyMov

    if firstMov:

        firstMov = False

        everyMov = True

        return abs(value)
    
    if everyMov:

        for z in range(len(contabilityMatrix)):

            for w in range(len(contabilityMatrix[0])):

                if z == len(contabilityMatrix) - 1 and w == 5 and code == "VT":

                    return contabilityMatrix[z][w] + value
                
                elif z == len(contabilityMatrix) - 1 and w == 5 and code == "CM":

                    return contabilityMatrix[z][w] - value
        
                elif z == len(contabilityMatrix) - 1 and w == 5 and code == "GST":

                    return contabilityMatrix[z][w] - value
                

def addMovement():

    """Función encargada añadir un nuevo movimiento contable."""

    fecha = getDate()

    code = getContabilityCodes()

    description = getDescription()

    registerMovement(fecha, code, description)
