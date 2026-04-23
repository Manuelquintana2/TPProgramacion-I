"""Ejercicio 1: Una tienda registra las ventas de los últimos 7 días
El programa debe
Guardar las ventas en una lista
Mostrar el total vendido, el día con mayor venta y el promedio de ventas"""

ventas = []
total = 0


for i in range (7):
    ventadia = float(input("Ingrese el valor de la venta "))
    ventas.append(ventadia)
    total += ventadia

max = (ventas[0])

if max < ventas[i]:
    ventas[i] = max


promedio = total/(len(ventas))

print (f"la lista de ventas es {ventas}")
print (f"el total vendido es {total}")
print (f"el valor promedio de las ventas es {promedio}")
print (f"el mayor valor de ventas es {max}")


"""Ejercicio 2: Un sistema meteorológico registra 10 temperaturas diarias
El programa debe
Guardar las temperaturas en una lista
Informar cuantas temperaturas superan los 30c
La temperatura mínima
La temperatura máxima"""

temperaturas = []
temperaturas30 = 0

for i in range (10):
    temperaturasDiarias = float(input("Ingrese la temperatura "))
    temperaturas.append(temperaturasDiarias)

    if temperaturasDiarias >30:
        temperaturas30 +=1

min = temperaturas[0]
max = temperaturas[0]
 
for i in range (10):
    if min > temperaturas[i]:
        min = temperaturas[i]

for i in range (10):
    if max < temperaturas[i]:
        max = temperaturas[i]


print (f"La lista de temperaturas es{temperaturas}")
print (f"La temperatura mínima es {min}")
print (f"La temperatura máxima es {max}")
print (f"La cantidad de temperaturas que superan los 30 grados son {temperaturas30}")


"""Un cine tiene 3 filas y 5 asientos por fila
Se registran con 0 libre y 1 ocupado
el programa debe cargar la matriz
Mostrar total de asientos libres y ocupados"""

import random

matriz = []
ocupados = 0
libres = 0

for i in range (3):

    fila = []
    fila.append(random.randint(0,1))
    matriz.append(fila)

    for j in range (4):
        fila.append(random.randint(0,1))


for i in range (len(matriz)):
    for j in range (len(matriz[i])):
        
        if matriz [i][j] == 1:
            libres += 1
            
        if matriz [i][j] == 0:
            ocupados += 1

print (matriz)
print (libres)
print (ocupados)


"""Una escuela registra las notas de 4 estudiantes en 3 materias
Las notas se guardan en una matriz
El programa debe calcular
El promedio de cada estudiante"""

estudiantes = ["Pepe", "Juan", "Alejo", "Leandro"]
matriz = []
promedio= []

for i in range (len(estudiantes)):
    fila = []
    nota = float(input(f"Ingrese la nota del estudiante {estudiantes[i]} "))
    fila.append(nota)
    matriz.append(fila)

    for j in range (2):
        nota = float(input(f"Ingrese la nota del estudiante {estudiantes[i]} "))
        fila.append(nota)

for i in range (len(matriz)):
    suma = 0
    for j in range(len(matriz [i])):
       suma += matriz[i][j]

    promedio = suma/(len(matriz[i]))
    print (f"el promedio de {estudiantes[i]} es, {promedio}")

print(matriz)
print(promedio)


"""Un supermercado registra el stock de 4 productos en 3 sucursales
Los datos se muestran en una matriz
Crear una función que reciba una lista y calcule el stock total de un producto
El programa debe mostrar el stock total de cada producto"""

productos = ["Leche", "Azucar", "Sal", "Yogurt"]
matriz = []

for i in range (len(productos)):
    fila = []

    for j in range (3):
        stock = int(input(f"Ingrese el stock de {productos[i]}"))
        fila.append(stock)

    matriz.append(fila)

for i in range (len(matriz)):

    suma = 0

    for j in range (len(matriz[i])):

        suma += matriz[i][j]


    total = suma + (len(matriz[i]))
    print(f"la suma total de {productos[i]} es {suma}")


print(matriz)



    

