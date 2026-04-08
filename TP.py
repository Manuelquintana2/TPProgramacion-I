import random

"""Completa una matriz random con 0 y 1"""

def lugaresEstacionamiento():
    estacionamiento = []

    for i in range (4):
        fila = []

        for j in range (5):
            fila.append(random.randint(0,1))
        estacionamiento.append(fila)
            
    return(estacionamiento)

"""Mostrar la matriz del estacionamiento"""

def mostrarEstacionamiento(estacionamiento):
    for i in range(len(estacionamiento)):
        print(estacionamiento[i])

"""Asignar lugares libres y ocupados, mostrarlos, y sumarlos para mostrar el total de lugares """

def lugaresLibres(estacionamiento):

    libres = 0
    ocupados = 0

    for i in range (len(estacionamiento)):
        for j in range (len(estacionamiento[i])):
            
            if estacionamiento[i][j] == 1:
                libres +=1
            else:
                ocupados +=1
            
    suma = libres+ocupados

    print("la suma total de lugares es", suma)
    print("la cantidad de lugares libres son: ", libres)
    print("la cantidad de lugares ocupados son:", ocupados)

"""Muestra el menú principal"""

def menuPrincipal ():

    print (f"BIENVENIDOS A PARKING CODE. SELECCIONE UNA OPCIÓN")
    print("1- Mostrar Estacionamiento")
    print("2- Mostrar lugares")
    print("0- Salir")

    return input("Opción: ")

"""Función principal, basado en llamado a funciones"""

def main():

    est = lugaresEstacionamiento()

    while True:

        opcion = menuPrincipal()

        if opcion == "1":
            mostrarEstacionamiento(est)

        elif opcion == "2":
            lugaresLibres(est)

        elif opcion == "0":
            print (f"Saliendo xd")
            break

        else:
            print("Opción inválida")

main()
