from View import *
from Logic import *

def principalView():

    """Método encargado de mostrar las vistas."""

    flag = True

    titleProgram()

    while flag:

        menuSelection = menu()

        if menuSelection == 1:

            addMovement()

        elif menuSelection == 2:

            print("\nMaking Function...")

        elif menuSelection == 3:

            if not contabilityMatrix: 

                print("\nNo hay datos que mostrar")

            else:

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