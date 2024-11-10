from View import *
from Logic import *

def principalView():

    """Método encargado de mostrar las vistas."""

    flag = True

    titleProgram()

    while flag:

        if menu() == 1:

            addMovement()

        elif menu() == 3:

            showGeneralContability()

        while True:

            confirm = str(input("\nDeseas Continuar? S / N: "))

            if confirm.upper() == "N":
                flag = False
                break

            elif confirm.upper() == "S":
                break

            else:
                print("\nIngresa Caracter Correcto!\n")

principalView()