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