import os

listFecha = []

listCodigo = []

listDescripcion = []

listDebe = []

listHaber = []

listSaldo = []

listN = [["Juan", 32], ["Camila", 12]]

def valueSaldo(a, b):
    return a - b

def getDate():

    os.system('cls')

    return str(input("Ingresa Fecha: "))


def getContabilityCodes():

    os.system('cls')

    print("Codigos Disponibles: \n")

    listOfCodes = ["VT", "CM", "GST"]

    for z in range(len(listOfCodes)):

        print(f"{z + 1}. {listOfCodes[z]}")

    code = int(input("Selecciona Código: "))

    return listOfCodes[code - 1]


def getDescription():

    return str(input("Ingresa Descripción: "))


def registerMovement(code):

    value = int(input("Ingresa Valor: "))

    if code == "VT":
        
        listDebe.append(value)

        listHaber.append(0)

    elif code == "CM":

        listDebe.append(0)

        listHaber.append(value)

    elif code == "GST":
        
        listDebe.append(0)

        listHaber.append(value)


def getSaldo():

    debe = 0 
    haber = 0

    for z in range(len(listDebe)):

        if listDebe[z] != 0:

            debe += listDebe[z]

    for z in range(len(listHaber)):

        if listHaber[z] != 0:

            haber += listHaber[z]

    print(f"Saldo: {valueSaldo(debe, haber)}")


def addMovement():

    fecha = getDate()

    code = getContabilityCodes()

    description = getDescription()

    listFecha.append(fecha)

    listCodigo.append(code)

    listDescripcion.append(description)

    registerMovement(code)

    getSaldo()