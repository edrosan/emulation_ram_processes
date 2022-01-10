import os
import random

ejecutar = True
# ejecutar = False

tamMemoria = 10
ram = [0] * tamMemoria

contador = 0
proceso = 281


def addProceso(ram, tamProceso):
    global contador, proceso
    proceso += 1
    for i in  range(tamProceso):
        ram[contador] = proceso
        contador += 1
    return True

def subProceso(ram):
    global contador
    procesoEnCola = ram[contador-1]
    print(f'Proceso : {procesoEnCola}')
    while (ram[contador-1] == procesoEnCola):
        ram[contador-1] = 0
        contador -= 1

def validacion(tamMemoria, contador, tamProceso):
    #*  1 = tamaño valido
    #?  0 = tamaño no valido
    #!  -1 = proceso supera tamaño de memoria
    #!  -2 = memoria llena 
    #!  -3 = dato no valido
    if( isinstance(tamProceso, int)):
        if( (tamProceso <= (tamMemoria - contador)) and (tamProceso > 0) ):
            return 1 
        elif (tamProceso <= 0):
            print(f'Tamaño de proceso no valido: {tamProceso}, valores permitidos: 1 - {tamMemoria}')
            return 0
        elif(tamProceso >tamMemoria):
            print(f'Tamaño del proceso: {tamProceso}, supera el tamaño de memoria total: {tamMemoria}')
            return -1
        elif(tamProceso > (tamMemoria-contador)):
            print(f'Error: Tamaño del proceso: {tamProceso}, excede tamaño disponible: {tamMemoria-contador}')
            return -2
    else:
        print(f'Entrada no valida: "{tamProceso}", {type(tamProceso)}')
        return -3

def convertir(tamProceso):
    ascii = list(tamProceso.encode('ascii'))
    if(ascii[0] >= 48 and ascii[0] <= 59):
        return int(tamProceso)
    else:
        return tamProceso
    
def printRam(ram):
    global contador
    procesoEnCola = ram[0] 
    n = random.randrange(105,229)   
    print(f'Memoria RAM:')
    print(ram)
    print()
    print ('[','\033[30m', end='')
    col= '\x1b[48;5;'
    for element in ram:
        if(element == 0):
            n= 46
            col += str(n) + 'm'
            print (col, element, end="") 
        elif (element == procesoEnCola):
            col += str(n) + 'm'
            print (col, element, end="")
        else:
            n = random.randrange(105,229)   
            procesoEnCola = element 
            col += str(n) + 'm'
            print (col, element, end="")
        col= '\x1b[48;5;'

    print('\x1b[0m',']')


while(ejecutar):
    print(f'---------------------')
    print(f'Menu:')
    print(f'[1] Agregar proceso')
    print(f'[2] Ejecutar proceso')
    print(f'[3] Mostrar procesos en memoria')
    print(f'[4] Salir')

    opc = input('Seleccione una opcion: [ ]\033[2D')
    print(f'---------------------')
    if( opc == '1'):
        tamProceso = input('Ingrese tamaño de proceso: [   ]\033[4D')
        tamProceso = convertir(tamProceso)
        respuesta = validacion(tamMemoria, contador, tamProceso)
        if( respuesta == 1 ):
            if( addProceso(ram, tamProceso)):
                print(f'Proceso agregado con exito: {proceso}')
            else:
                print(f'Error no se pudo agregar el proceso')
        elif ( (respuesta == 0) or (respuesta == -3) ):
            print(f'Valor no valido: "{tamProceso}", ingrese un valor valido')
        elif (respuesta == -2):
            print(f'Memoria llena, ¿que desea hacer?:')
            print(f'[1] ¿Ejecutar un proceso?')
            print(f'[2] No crear el proceso')

            opc = input('Seleccione una opcion: [ ]\033[2D')
            if(opc == '1'):
                subProceso(ram)
                print(f'Proceso ejecutado')
    elif(opc == '2'):
        if (contador == 0):
            print(f'Memoria vacia, no hay procesos a ejecutar')
        else:
            print(f'Proceso ejecutado')
            subProceso(ram)
    
    elif(opc == '3'):
        printRam(ram)
    elif(opc == '4'):
        ejecutar = False




