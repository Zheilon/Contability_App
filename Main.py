from Person.ContaViewPerson import *
from Person.ContaLogicPerson import *
from Company.contaViewNegocio import *
from Company.contaLogicNegocio import *

def principalView():

    """Método encargado de mostrar las vistas."""

    flag = True

    titleProgram()

    selection = isPersonOrCompany()

    while flag:

        if selection == 1:

            mainViewPerson()

        elif selection == 2:
            mainViewCompany()

        

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
