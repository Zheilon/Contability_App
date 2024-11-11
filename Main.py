from View import *
from Logic import *

def principalView():

    """Método encargado de mostrar las vistas."""

    flag = True

    # Lugar para insertar la funcion: titleProgram()

    while flag:

        if menu() == 1:

            addMovement()

        elif menu() == 3:

            if not contabilityMatrix: 

                print("No hay datos que mostrar")

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