import sys
import time

def printTextEfect(text, timer):

    """Método encargado de generar efecto de escritura
    a una cadena de texto."""

    for z in text:

        sys.stdout.write(z)

        sys.stdout.flush()

        time.sleep(timer)