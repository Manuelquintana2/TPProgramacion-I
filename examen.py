"""1) Generar una matriz n x m con valores aleatorios entre 10 y 99. Contar cuántos números son mayores a 50.

2) Pedir mínimo y máximo. Crear por comprensión una lista con los números impares que no sean múltiplos de 5.

3) Crear una lista de enteros positivos y negativos. Crear una lista con los negativos y otra con los números elevados al cuadrado.

4) Registrar películas en un diccionario: título, director, año y duración. Mostrar películas estrenadas después de 2010. Mostrar la película con mayor duración.

"""
import random

n = 3
m = 3

def generarMatriz(n,m):

    matriz = []

    for i in range (n):
        fila = []
        for j in range (m):
            columnas = random.randint (10,99)
            fila.append(columnas)
            matriz.append(fila)

    contador = 0

    for i in range (len(matriz)):

        for j in range (len(matriz[i])):
            if matriz [i][j] > 50:
                contador +=1

    print (matriz)
    print (contador)

    return matriz

generarMatriz(n, m)

def listaNumerosImpares():
    minimo = int(input("Ingrese el valor mínimo"))
    maximo = int (input("Ingrese el máximo"))

    lista = [i for i in range (minimo, maximo, +1) if i % 5 == 0 and i % 2 != 0]
    print (lista)

listaNumerosImpares()

def listasPositivasyNegativas():

    list = [10, 20, 30, -40, -50]

    listanegativa = [i for i in list if i <0]

    print (listanegativa)

    return list

listasPositivasyNegativas()

def listasCuadrado():

    list = [10, 20, 30, -40, -50]
    cuadrado = []

    for i in list:
        suma = i ** 2
        cuadrado.append(suma)

    print (cuadrado)
listasCuadrado()

diccionary = {}
cantidad = int(input("Ingrese la cantidad de películas"))





