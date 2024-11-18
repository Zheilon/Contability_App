import os
import sys
import time


def printTextEfect(text, timer):

    """Método encargado de generar efecto de escritura
    a una cadena de texto."""

    for z in text:

        sys.stdout.write(z)

        sys.stdout.flush()

        time.sleep(timer)


def isPersonOrCompany():

    """Función encargada de determinar el tipo de cuenta a usar."""

    os.system('cls')

    print("ContalApp®\n")

    printTextEfect("Vas a manejar esta aplicación para: \n", 0.01)

    printTextEfect("\n1.) Uso personal.\n", 0.01)

    printTextEfect("\n2.) Negocio y/o Emprendimiento.\n\n", 0.01)

    while True:

        try: 

            selection = int(input("Selecciona opción: "))

            if selection > 0 and selection < 3:

                return selection
            
            else:
                
                printTextEfect("\nRango de valores no permitidos!\n\n", 0.01)

                time.sleep(1)
        
        except ValueError as vl:

            print(f"\nSolo se permiten valores numéricos: {vl}\n")

        
def decorationProfile(info: str):

    for z in range(len(info)): 
    
        if z == 0:

            print(end="+")

        elif info[z] == '|':

            print(end="+")

        elif z == len(info):

            print(end="+")
        
        else: 

            print(end="-")


def informationProfile(user, account, type, cashBalance):

    """Muestra la información del usuario."""

    info = f"| ContalApp® {type} | Username: {user} | Cuentas Creadas: {account} | Saldo Caja: $ {cashBalance:,.0f} |" 

    decorationProfile(info)
    
    print()

    print(info)

    decorationProfile(info)

    return info


