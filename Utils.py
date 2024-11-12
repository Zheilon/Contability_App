import sys
import time

def printTextEfect(text, timer):

    for z in text:

        sys.stdout.write(z)

        sys.stdout.flush()

        time.sleep(timer)