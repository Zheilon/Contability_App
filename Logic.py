import os
import time
from datetime import date
from datetime import datetime
from tabulate import tabulate

contabilityMatrix = []

firstMov = True

everyMov = False


def getDate():

    """Esta función obtiene la fecha actual."""

    os.system('cls')

    print("Fecha obtenida Automaticamente!")

    time.sleep(1.5)

    return date.today()


def getContabilityCodes():

    """Esta función se encarga de primero mostrar y luego, 
    retornar el código seleccionado."""
    
    os.system('cls')

    while True:

        print("Codigos Disponibles: \n")

        #* VT = VENTAS, CM = COMPRAS, GST = GASTOS #*

        listOfCodes = ["VT", "CM", "GST"]

        listCodesDescription = ["VT (Venta)", "CM (Compra)", "GST (Gasto)"]
    
        for z in range(len(listCodesDescription)):

            print(f"{z + 1}. {listCodesDescription[z]}\n")

        try:

            code = int(input("Selecciona Código: "))

            if code > 0 and code < 4:

                return listOfCodes[code - 1]
            
            else:

                os.system('cls')
                
                print("\nRangos no permitidos.\n")

        except ValueError as vl:

            os.system('cls')    

            print(f"\nSolo se permiten valores númericos: {vl}.\n")


def getDescription():

    """Esta función obtiene la descripción escrita por el usuario."""

    os.system('cls')

    return str(input("Ingresa Descripción: "))



def registerMovement(fecha, code, description):

    """Esta función se encarga de obtener un valor 'n', para luego adicionarlo
    en una lista, que se añadirá a la matriz principal"""

    os.system('cls')

    value = int(input("Ingresa Valor: "))

    if code == "VT":

        saveAll(fecha, code, description, value, "", getBalance(value, code=code))

    elif code == "CM":
        
        saveAll(fecha, code, description, "", value, getBalance(value, code=code))

    elif code == "GST":
        
        saveAll(fecha, code, description, "", value, getBalance(value, code=code))


def saveAll(date, code, description, debe, haber , saldo):

    """Esta función se encarga de guardar en la matriz principal una lista con 
    todos los elementos necesarios que componen un ejercicio contable."""

    contabilityMatrix.append([date, code, description, debe, haber, saldo])
    

def getBalance(value, code):

    """Función encargada de determinar y retornar el saldo, 
    despues de cada ejercicio contable."""

    global firstMov

    global everyMov

    if firstMov:

        firstMov = False

        everyMov = True

        return abs(value)
    
    if everyMov:

        for z in range(len(contabilityMatrix)):

            for w in range(len(contabilityMatrix[0])):

                if z == len(contabilityMatrix) - 1 and w == 5 and code == "VT":

                    return contabilityMatrix[z][w] + value
                
                elif z == len(contabilityMatrix) - 1 and w == 5 and code == "CM":

                    return contabilityMatrix[z][w] - value
        
                elif z == len(contabilityMatrix) - 1 and w == 5 and code == "GST":

                    return contabilityMatrix[z][w] - value
                

def addMovement():

    """Función encargada añadir un nuevo movimiento contable."""

    fecha = getDate()

    code = getContabilityCodes()

    description = getDescription()

<<<<<<< HEAD
    registerMovement(fecha, code, description)
=======
    registerMovement(fecha, code, description)

# CONTROL DE INVENTARIO
inventari=[]
#primero se creo una lista para almacenar la informacion del inventario
def addProduct ():
    code = input(f"Ingrese el codigo del producto")
    article = input(f"Ingrese el nombre del articulo")
    price = input(f"Ingrese el precio por unidad del producto")
    output =0
    entry = input(f"Ingrese las entradas del producto")
#el stock es la variable donde se muestra lo que queda en bodega
    stock= entry-output
#revision del producto para saber si ya esta documentado en el inventrio
    estored=False
    for product in inventari:
        #si codigo es igual al producto
        if product["Codigo"] == code:
            product["Entradas"] += entry
            product["Salidas"] += output
            product["Stock"] += product["Entradas"]-product["Salidas"]
            product["Precio"] = price
            estored=True
            print(f"Producto {product["Articulo"]} Actualizado")

#Control de inventario

#lista para almacenar los registros del inventario
inventario = []

# Agregar productos
def agregar_o_actualizar_producto():
    # Pedir al usuario que ingrese los datos
    codigo = input("Ingrese el código del producto: ")
    articulo = input("Ingrese el nombre del artículo: ")
    precio_unitario = float(input("Ingrese el precio por unidad: ")) 
    salidas = 0
    entradas = int(input("Ingrese las entradas del producto: "))
    #El stock son los productos que quedan almacenados en bodega
    stock = entradas - salidas  
# Revision
    encontrado = False
    for producto in inventario:
        if producto['Código'] == codigo:
            # Si el producto ya existe, actualizar el stock, el precio y las salidas/entradas
            producto['Entradas'] += entradas
            producto['Salidas'] += salidas
            producto['Stock'] = producto['Entradas'] - producto['Salidas']
            producto['Precio'] = precio_unitario 
            encontrado = True
            print(f"Producto {producto['Artículo']} actualizado.")
            break

    # Si el producto no existe, agregar uno nuevo
    if not encontrado:
        producto = {
            'Código': codigo,
            'Artículo': articulo,
            'Precio': precio_unitario,
            'Entradas': entradas,
            'Salidas': salidas,
            'Stock': stock,
            'Movimientos': []  
        }
        inventario.append(producto)
        print(f"Producto {articulo} agregado al inventario.")
# registrar una entrada de producto
def registrar_entrada():
    codigo = input("Ingrese el código del producto para la entrada: ")
    cantidad = int(input("Ingrese la cantidad de entradas: "))
    fecha = datetime.now().strftime('%d/%m/%Y')  
    
    for producto in inventario:
        if producto['Código'] == codigo:
            producto['Entradas'] += cantidad
            producto['Stock'] += cantidad
            producto['Movimientos'].append({'Tipo': 'Entrada', 'Cantidad': cantidad, 'Fecha': fecha})
            print(f"Entrada registrada para el producto {producto['Artículo']}.")
            return
    print("Producto no encontrado.")

#  salida de producto
def registrar_salida():
    codigo = input("Ingrese el código del producto para la salida: ")
    cantidad = int(input("Ingrese la cantidad de salidas: "))
    fecha = datetime.now().strftime('%d/%m/%Y') 
    
    for producto in inventario:
        if producto['Código'] == codigo:
            if cantidad > producto['Stock']:
                print("No hay suficiente stock para realizar la salida.")
                return
            producto['Salidas'] += cantidad
            producto['Stock'] -= cantidad
            producto['Movimientos'].append({'Tipo': 'Salida', 'Cantidad': cantidad, 'Fecha': fecha})
            print(f"Salida registrada para el producto {producto['Artículo']}.")
            return
    print("Producto no encontrado.")

# inventario con los movimientos registrados
def mostrar_inventario():
    # Preparar los encabezados y datos para la tabla
    encabezados = ['Código', 'Artículo', 'Entradas', 'Salidas', 'Stock', 'Precio Unitario', 'Total Entradas', 'Total Salidas']
    tabla = []

    # Generar los datos para la tabla
    for producto in inventario:
        total_entradas = producto['Entradas'] * producto['Precio']
        total_salidas = producto['Salidas'] * producto['Precio']
        tabla.append([
            producto['Código'],
            producto['Artículo'],
            producto['Entradas'],
            producto['Salidas'],
            producto['Stock'],
            f"${producto['Precio']:.2f}",
            f"${total_entradas:.2f}",
            f"${total_salidas:.2f}"
        ])
    
    # Mostrar la tabla con tabulate
    if inventario:
        print("\nInventario actualizado:")
        print(tabulate(tabla, headers=encabezados, tablefmt='grid'))
        
        # entradas y salidas de cada producto
        for producto in inventario:
            if producto['Movimientos']:
                print(f"\nMovimientos para el producto {producto['Artículo']} ({producto['Código']}):")
                for movimiento in producto['Movimientos']:
                    print(f"  Tipo: {movimiento['Tipo']} | Cantidad: {movimiento['Cantidad']} | Fecha: {movimiento['Fecha']}")
    else:
        print("El inventario está vacío.")

# Menú principal
def menu1():
    while True:
        print("\nMenu:")
        print("1. Agregar o actualizar producto")
        print("2. Registrar entrada de producto")
        print("3. Registrar salida de producto")
        print("4. Mostrar inventario")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            agregar_o_actualizar_producto()
        elif opcion == '2':
            registrar_entrada()
        elif opcion == '3':
            registrar_salida()
        elif opcion == '4':
            mostrar_inventario()
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida, por favor intente de nuevo.")






>>>>>>> be8422a (Agrege una nueva opcion al menu control de inventario)
