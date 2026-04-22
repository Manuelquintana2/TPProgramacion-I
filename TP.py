import time
# Descripción del sistema
# El sistema está hecho para gestionar pedidos de un e-commerce,
# incluyendo la carga de productos comprados, cantidades, 
# métodos de envío y el seguimiento del estado de cada orden.

productos = []
producto = {}
producto["Cantidad"] = "a"
producto["Precio"] = "a"
producto["MetodoDeEnvio"] = "a"
producto["NroDeOrden"] = {"Estados" : ["Pagados", "Empaquetados", "Enviados", "Reenviado"]}

def registrarCompras():
    pass

def gestionarEstadoDePedido():
    pass

pedidos = []
numeroOrden = 1000

def generarNumeroOrden():
    global numeroOrden
    orden = numeroOrden
    numeroOrden += 1
    return orden

def elegirMetodoDeEnvio():
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


def registrarCompras():
    cliente = input("\nIngrese el nombre del cliente: ")

    while cliente == "":
        print("El nombre no puede estar vacío.")
        cliente = input("Ingrese el nombre del cliente: ")

    cantidadProductos = int(input("¿Cuántos productos desea cargar? "))

    while cantidadProductos <= 0:
        print("Debe ingresar al menos 1 producto.")
        cantidadProductos = int(input("¿Cuántos productos desea cargar? "))

    productos = []

    for i in range(cantidadProductos):
        print("\nProducto", i + 1)

        nombreProducto = input("Nombre del producto: ")
        while nombreProducto == "":
            print("El nombre no puede estar vacío.")
            nombreProducto = input("Nombre del producto: ")

        cantidad = int(input("Cantidad: "))
        while cantidad <= 0:
            print("La cantidad debe ser mayor a 0.")
            cantidad = int(input("Cantidad: "))

        precio = float(input("Precio: "))
        while precio <= 0:
            print("El precio debe ser mayor a 0.")
            precio = float(input("Precio: "))

        producto = {}
        producto["Nombre"] = nombreProducto
        producto["Cantidad"] = cantidad
        producto["Precio"] = precio

        productos.append(producto)

    metodoDeEnvio = elegirMetodoDeEnvio()
    nroDeOrden = generarNumeroOrden()

    pedido = {}
    pedido["Cliente"] = cliente
    pedido["Productos"] = productos
    pedido["MetodoDeEnvio"] = metodoDeEnvio
    pedido["NroDeOrden"] = nroDeOrden
    pedido["Estado"] = "Pagado"

    pedidos.append(pedido)

    print("\nCompra registrada correctamente.")
    print("Número de orden generado:", nroDeOrden)
    print("Estado inicial:", pedido["Estado"])


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