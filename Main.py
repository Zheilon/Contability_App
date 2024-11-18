from Utils import *
from Person.ContaViewPerson import *    
from Person.ContaLogicPerson import *   
from Company.contaViewNegocio import *
from Company.contaLogicNegocio import *

flagOne = True

flagTwo = True

currentAccount = 0

titleProgram()    

nameUser = setNameUser()

def principalView():

    """Método encargado de mostrar las vistas."""

    personAcc = True

    companyAcc = True

    global flagOne

    global flagTwo

    while flagOne:

        global currentAccount

        selection = isPersonOrCompany()

        flagTwo = True

        while flagTwo:

            if selection == 1:

                if personAcc:

                    personAcc = False

                    currentAccount += 1

                returnPrincipalMenu = mainViewPerson(nameUser, currentAccount)

                if returnPrincipalMenu == 3:

                    flagTwo = False

                    break

                elif returnPrincipalMenu == 4:

                    flagOne = False

                    flagTwo = False

                    break

            elif selection == 2:

                if companyAcc:

                    companyAcc = False

                    currentAccount += 1

                returnPrincipalMenu = mainViewCompany(nameUser, currentAccount)

                if returnPrincipalMenu == 4:

                    flagTwo = False

                    break

                if returnPrincipalMenu == 5:

                    flagOne = False

                    flagTwo = False

                    break
                
            while True:

                confirm = str(input("\nDeseas Continuar? S / N: "))

                if confirm.upper() == "N":

                    flagOne = False

                    flagTwo = False

                    break

                elif confirm.upper() == "S":

                    os.system('cls')
                    
                    break

                else:
                    print("\nIngresa Caracter Correcto!\n")


principalView()