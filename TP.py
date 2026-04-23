import time
import re

# Descripción del sistema
# El sistema está hecho para gestionar pedidos de un e-commerce,
# incluyendo la carga de productos comprados, cantidades, 
# métodos de envío y el seguimiento del estado de cada orden.

pedidos = [] 
productos_remeras = [
    {
        "id": 0,
        "Nombre": "Remera Basic Oversize",
        "Color": "Negro",
        "Talle": "L",
        "Precio": 6000,
        "CantidadStock": 50
    },
    {
        "id": 1,
        "Nombre": "Remera Classic Oversize",
        "Color": "Blanco",
        "Talle": "M",
        "Precio": 8000,
        "CantidadStock": 35
    },
    {
        "id": 2,
        "Nombre": "Remera Estampada Rock",
        "Color": "Gris Melange",
        "Talle": "XL",
        "Precio": 3250,
        "CantidadStock": 15
    },
    {
        "id": 3,
        "Nombre": "Remera Deportiva Dry-Fit",
        "Color": "Azul Francia",
        "Talle": "S",
        "Precio": 13000,
        "CantidadStock": 15
    },
    {
        "id": 4,
        "Nombre": "Remera Polo Clásica",
        "Color": "Verde Oliva",
        "Talle": "XXL",
        "Precio": 13000,
        "CantidadStock": 10
    }
]

numeroOrden = 1000

def generarNumeroOrden():
    """ Incrementa el contador global y devuelve el número de orden para el nuevo pedido. """
    global numeroOrden
    orden = numeroOrden
    numeroOrden += 1
    return orden

def pedirDatos(mensaje, patron):
    """ Solicita un dato al usuario y lo valida llamando a la función validaciones. """
    dato = input(mensaje)
    res = validaciones(patron, dato)
    return res

def validaciones(patron, valor):
    """ Compara el valor ingresado contra un patrón Regex. Si no coincide, solicita reingreso. """
    while not(re.match(patron, valor)):
        print('No valido')
        valor = input('Ingrese nuevamente: ')
    return valor

def mostrarProductos():
    """ Recorre la lista de remeras e imprime el índice, nombre, talle y precio. """
    for i in range(len(productos_remeras)):
        print(f'{i}: {productos_remeras[i]["Nombre"]} - Talle: {productos_remeras[i]["Talle"]} - Precio: {productos_remeras[i]["Precio"]}')

def elegirMetodosDeEnvio():
    """ Muestra opciones de envío, valida la selección y retorna el nombre del método. """
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
    """ 
    Gestiona la toma de datos del cliente, la selección de productos múltiples, 
    el control de stock y el cálculo de totales para guardar un nuevo pedido. 
    """
    flag = "si"
    cliente = pedirDatos("Ingrese el nombre del cliente: ", '[a-zA-Z]')
    cliente = cliente.upper()
    direccion = pedirDatos("Ingrese su dirección: ", '[A-Za-z0-9]')
    direccion = direccion.upper()
    items = []

    while flag == "si":
        mostrarProductos()

        producto = int(pedirDatos("Ingrese el producto que desea comprar (Seleccione un numero): ", '^[0-9]+$'))

        while producto < 0 or producto >= len(productos_remeras):
            print("Opción inválida")
            producto = int(pedirDatos("Ingrese el producto que desea comprar (Seleccione un numero): ", '^[0-9]+$'))

        cantidad = int(pedirDatos("Ingrese la cantidad que desea comprar: ", '^[0-9]+$'))

        for i in range(len(productos_remeras)):
            if producto == i:
                if cantidad < productos_remeras[i]["CantidadStock"]:
                    precioUnitario = productos_remeras[i]["Precio"]
                    precioTotal = cantidad * productos_remeras[i]["Precio"]
                    nombre_prod = productos_remeras[i]["Nombre"]
                    productos_remeras[i]["CantidadStock"] = productos_remeras[i]["CantidadStock"] - cantidad

                    items.append({"Producto" : nombre_prod,
                                "PrecioUnitario" : precioUnitario,
                                "Cantidad" : cantidad,
                                "PrecioTotal" : precioTotal
                                })
                else:
                    print("No tenemos la cantidad de stock suficiente para la compra")

        flag = pedirDatos("¿Quiere seguir comprando?: (si/no)\n", '^(si|no)$')

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

    total_compra = 0
    print("--- DETALLE DE COMPRA ---")
    
    for item in pedido["Items"]:
        nombre_prod = item["Producto"]
        cant = item["Cantidad"]
        subtotal = item["PrecioTotal"]
        total_compra += subtotal
        
        print(f"Producto: {nombre_prod}")
        print(f"Cantidad: {cant}")
        print(f"Subtotal: ${subtotal}")
        print("-" * 20) 

    print(f"TOTAL A PAGAR: ${total_compra}")
    print("=" * 30 + "\n")
    
    pedidos.append(pedido)

def gestionarEstadoDePedido():
    """ Permite listar pedidos existentes y actualizar su estado siguiendo el flujo logístico. """
    if len(pedidos) == 0:
        print("No hay pedidos registrados.")
        return

    print("\n--- Listado de Pedidos Disponibles ---")
    for p in pedidos:
        nro = p['NroDeOrden']
        cliente = p['Cliente']
        direc = p['Direccion']
        estado = p['Estado']
        print(f"Nro de Orden: {nro} - Nombre: {cliente} - Dirección: {direc} - Estado: {estado}")
    
    print("-" * 50 + "\n")

    nro_orden_buscar = int(pedirDatos("Ingrese el número de orden que desea gestionar: ", '[0-9]+'))

    indice = 0
    encontrado = False
    
    while indice < len(pedidos) and encontrado == False:
        if pedidos[indice]["NroDeOrden"] == nro_orden_buscar:
            encontrado = True
        else:
            indice += 1

    if not encontrado:
        print(f"No se encontró la orden Nro {nro_orden_buscar}.")
        return
    
    estado_actual = pedidos[indice]["Estado"]
    
    print(f"\n> Gestionando Orden Nro: {nro_orden_buscar}")
    print(f"> Cliente: {pedidos[indice]['Cliente']}")
    print(f"> Estado actual: {estado_actual}")
    
    if estado_actual == "Pagado":
        print("Siguiente paso lógico: 'Empaquetado'")
        res = input("¿Desea cambiar el estado a 'Empaquetado'? (si/no): ").lower()
        if res == "si":
            pedidos[indice]["Estado"] = "Empaquetado"
            print("¡Éxito! El pedido ahora está Empaquetado.")
            
    elif estado_actual == "Empaquetado":
        print("Siguiente paso lógico: 'Enviado'")
        res = input("¿Desea cambiar el estado a 'Enviado'? (si/no): ").lower()
        if res == "si":
            pedidos[indice]["Estado"] = "Enviado"
            print("¡Éxito! El pedido ahora está Enviado.")
            
    elif estado_actual == "Enviado" or estado_actual == "Reenviado":
        print("El pedido ya fue enviado.")
        print("Opción disponible: 'Reenviado'")
        res = input("¿Desea registrar un reenvío para este pedido? (si/no): ").lower()
        if res == "si":
            pedidos[indice]["Estado"] = "Reenviado"
            print("¡Éxito! El pedido ha sido marcado como Reenviado.")
    else:
        print("El pedido tiene un estado desconocido o ya finalizó su ciclo.")

def consultarInformacionHistorica():
    """ Filtra la lista global de pedidos por cliente y muestra el detalle de cada compra encontrada. """
    if len(pedidos) == 0:
        print("No hay pedidos cargados.")
        return 

    clientes_disponibles = sorted(list(set(p["Cliente"] for p in pedidos)))
    
    print("\n--- Clientes con pedidos registrados ---")
    for cliente in clientes_disponibles:
        print(f"• {cliente}")
    print("----------------------------------------\n