print("Este es el repo del tp")

"""ESTACIONAMIENTO PARKING UADE"""

import random

"""COMPLETAR RANDOM UNA MATRIZ PARA LOS LUGARES DEL PARKING"""

def lugaresEstacionamiento():
    estacionamiento = []

    for i in range (4):
        fila = []
        fila.append(random.randint(0,1))
        estacionamiento.append(fila)

        for j in range (4):
            fila.append(random.randint(0,1))

    print(estacionamiento)
    return(estacionamiento)

"""ASIGNAR LUGARES LIBRES Y OCUPADOS, SUMAR EL TOTAL DE LUGARES Y MOSTRAR"""

def lugaresLibres(estacionamiento):

    libres = 0
    ocupados = 0

    for i in range (len(estacionamiento)):
        suma = 0
        for j in range (len(estacionamiento[i])):
            
            if estacionamiento[i][j] == 1:
                libres +=1
            if estacionamiento[i][j] == 0:
                ocupados +=1
            
            suma = libres+ocupados

    print("la suma total de lugares es", suma)
    print("la cantidad de lugares libres son: ", libres)
    print("la cantidad de lugares ocupados son:", ocupados)

est = lugaresEstacionamiento()
lugaresLibres(est)