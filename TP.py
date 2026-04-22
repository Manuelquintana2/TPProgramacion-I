import time
import re
# Descripción del sistema
# El sistema está hecho para gestionar pedidos de un e-commerce,
# incluyendo la carga de productos comprados, cantidades, 
# métodos de envío y el seguimiento del estado de cada orden.
pedidos = []
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
        "Nombre": "Remera Classic Oversize",
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
        "CantidadStock": 15
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

numeroOrden = 1000

def generarNumeroOrden():
    global numeroOrden
    orden = numeroOrden
    numeroOrden += 1
    return orden

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
        print(f'{i}: {productos_remeras[i]["Nombre"]} - Talle: {productos_remeras[i]["Talle"]} - Precio: {productos_remeras[i]["Precio"]}')

def elegirMetodosDeEnvio():
    print("\nMétodos de envío:")
    print("1 - Retiro en sucursal")
    print("2 - Envío estándar")
    print("3 - Envío express")

    opcion = input("Seleccione una opción: ")

    while opcion != "1" and opcion != "2" and opcion != "3":
        print("Opción inválida.")
        opcion = input("Seleccione una opción: ")

    if opcion == "1":
        return "Retiro en sucursal"
    elif opcion == "2":
        return "Envío estándar"
    else:
        return "Envío express"
    

def registrarPedidos():
    flag = "si"
    cliente = pedirDatos("Ingrese el nombre del cliente: ", '[a-zA-Z]')
    cliente = cliente.upper()
    direccion = pedirDatos("Ingrese su dirección: ", '[A-Za-z0-9]')
    direccion = direccion.upper()
    items = []
    while flag == "si":
        mostrarProductos()
        producto = int(pedirDatos("Ingrese el producto que desea comprar (Seleccione un numero): ", '[0-9]'))
        cantidad = int(pedirDatos("Ingrese la cantidad que desea comprar: ", '[0-9]'))
        for i in range(len(productos_remeras)):
            if producto == i:
                if cantidad < productos_remeras[i]["CantidadStock"]:
                    precioUnitario = productos_remeras[i]["Precio"]
                    precioTotal = cantidad * productos_remeras[i]["Precio"]
                    producto = productos_remeras[i]["Nombre"]
                    productos_remeras[i]["CantidadStock"] = productos_remeras[i]["CantidadStock"] - cantidad

                    items.append({"Producto" : producto,
                                "PrecioUnitario" : precioUnitario,
                                "Cantidad" : cantidad,
                                "PrecioTotal" : precioTotal
                                })
                else:
                    print("No tenemos la cantidad de stock suficiente para la compra")

    
        flag = input("¿Quiere seguir comprando?: (si/no)\n")

    metodoDeEnvio = elegirMetodosDeEnvio()

    pedido = {}
    pedido["Cliente"] = cliente
    pedido["Direccion"] = direccion
    pedido["Items"] = items
    pedido["NroDeOrden"] = generarNumeroOrden()
    pedido["Estado"] = "Pagado"
    pedido["MetodoDeEnvio"] = metodoDeEnvio

    print(f'\
            -------Resumen de compra:--------\
    \nCliente : {pedido["Cliente"]}\
    \nDireccion : {pedido["Direccion"]}\
    \nNro De Orden: {pedido["NroDeOrden"]}\
    \nEstado: {pedido["Estado"]}\
    \nMetodoDeEnvio : {pedido["MetodoDeEnvio"]}')

    print(f"{'Producto':<30} | {'Cant.':<5} | {'Subtotal':<10}")
    total_compra = 0
    for item in pedido["Items"]:
        nombre_prod = item["Producto"]
        cant = item["Cantidad"]
        subtotal = item["PrecioTotal"]
        total_compra += subtotal
        print(f"{nombre_prod:<30} | {cant:<5} | ${subtotal:>8}")
    
    print(f"{'-'*50}")
    print(f"{'TOTAL A PAGAR:':<28} ${total_compra:>20}")
    print(f"{'='*50}\n")
    pedidos.append(pedido)

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
        "4: Dar de Alta/Baja/Modificar un producto\n"\
        "4: Salir\n" \
        ))
        match res:
            case 1: 
                print("Registrar Pedidos")
                registrarPedidos()
            case 2:
                print("Gestionar Estado de pedido")
                gestionarEstadoDePedido()
            case 3:
                print("Consultar Informacion Histrica")
            case 4:
                break
            case _:
                print("Invalido")

    print("Saliendo ...")
    time.sleep(1)

main()

        
