import time
import re
# Descripción del sistema
# El sistema está hecho para gestionar pedidos de un e-commerce,
# incluyendo la carga de productos comprados, cantidades, 
# métodos de envío y el seguimiento del estado de cada orden.

productos_remeras = [
    {
        "id": 1,
        "Nombre": "Remera Basic Oversize",
        "Color": "Negro",
        "Talle": "L",
        "Precio": 6000,
        "CantidadStock": 50
    },
    {
        "id": 2,
        "Nombre": "Remera Basic Oversize",
        "Color": "Blanco",
        "Talle": "M",
        "Precio": 8000,
        "CantidadStock": 35
    },
    {
        "id": 3,
        "Nombre": "Remera Estampada Rock",
        "Color": "Gris Melange",
        "Talle": "XL",
        "Precio": 3250,
        "CantidadStock": 15
    },
    {
        "id": 4,
        "Nombre": "Remera Deportiva Dry-Fit",
        "Color": "Azul Francia",
        "Talle": "S",
        "Precio": 13000,
        "CantidadStock": 0
    },
    {
        "id": 5,
        "Nombre": "Remera Polo Clásica",
        "Color": "Verde Oliva",
        "Talle": "XXL",
        "Precio": 13000,
        "CantidadStock": 10
    }
]

def pedirDatos(mensaje, patron):
    dato = input(mensaje)
    res = validaciones(patron, dato)
    return res

def validaciones(patron,valor):
    while not(re.match(patron,valor)):
        print('No valido')
        valor = input('Ingrese nuevamente: ')
    return valor

def mostrarProductos():
    for i in range(len(productos_remeras)):
        print(f'{i}: {productos_remeras[i]["Nombre"]}')

def registrarCompras():
    cliente = pedirDatos("Ingrese el nombre del cliente: ", '[a-zA-Z]')
    mostrarProductos()
    producto = pedirDatos("Ingrese el producto que desea comprar (Seleccione un numero)", '[0-9]')




def gestionarEstadoDePedido():
    pass

def consultarInformaciónHistorica():
    pass

def main():

    while True:
        res = int(input("¿Que operación deseas realizar?\n" \
        "1: Registrar Compra \n" \
        "2: Gestionar estado de pedido\n" \
        "3: Consultar informacion Historica\n" \
        "4: Salir\n" \
        ))
        match res:
            case 1: 
                print("Registrar compras")
                registrarCompras()
            case 2:
                print("Gestionar Estado de pedido")
                gestionarEstadoDePedido()
            case 3:
                print("Consultar Informacion Histrica")
            case 4:
                print("Saliendo...")
                time.sleep(1)
                break
            case _:
                print("Invalido")

    print("Saliendo ...")
    time.sleep(1)

main()

        
