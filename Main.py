from ContaViewPerson import *
from ContaLogicPerson import *

def principalView():

    """Método encargado de mostrar las vistas."""

    flag = True

    titleProgram()

    selection = isPersonOrCompany()

    while flag:

        if selection == 1:

            mainViewPerson()

        elif selection == 2:

<<<<<<< HEAD
            print("\nContabilidad para negocios...En desarrollo.\n")
=======
        elif menuSelection == 2:

            print("\nMaking Function...")

        elif menuSelection == 3:

            if not contabilityMatrix: 

                print("\nNo hay datos que mostrar")

            else:

                showGeneralContability()
        elif menuSelection == 4:
            opciones()
>>>>>>> 6e2ba563736525beef7340a05540e83989e4177e

        while True:

            confirm = str(input("\nDeseas Continuar? S / N: "))

            if confirm.upper() == "N":

                flag = False

                break

            elif confirm.upper() == "S":
                
                break

            else:
                print("\nIngresa Caracter Correcto!\n")

<<<<<<< HEAD

principalView()
=======
principalView()
>>>>>>> 6e2ba563736525beef7340a05540e83989e4177e
