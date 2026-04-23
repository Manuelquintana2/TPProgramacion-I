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
                    producto = productos_remeras[i]["Nombre"]
                    productos_remeras[i]["CantidadStock"] = productos_remeras[i]["CantidadStock"] - cantidad

                    items.append({"Producto" : producto,
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
    if len(pedidos) == 0:
        print("No hay pedidos registrados.")
        return
    nro_orden_buscar = int(pedirDatos("Ingrese el número de orden que desea gestionar: ", '[0-9]+'))

    indice = 0
    encontrado = False
    
    while indice < len(pedidos) and encontrado == False:
        if pedidos[indice]["NroDeOrden"] == nro_orden_buscar:
            encontrado = True
        else:
            indice += 1 # Solo avanzamos si no lo encontramos

    if len(pedidos) == 0:
        print("No hay pedidos registrados.")
        return
    
    estado_actual = pedidos[indice]["Estado"]
    
    print(f" Gestionando Orden Nro: {nro_orden_buscar}")
    print(f"Estado actual: {estado_actual}")
    
    if estado_actual == "Pagado":
        print("Siguiente paso lógico: 'Empaquetado'")
        res = input("¿Desea cambiar el estado a 'Empaquetado'? (si/no): ")
        if res == "si" or res == "SI" or res == "Si":
            pedidos[indice]["Estado"] = "Empaquetado"
            print("¡Éxito! El pedido ahora está Empaquetado.")
            
    elif estado_actual == "Empaquetado":
        print("Siguiente paso lógico: 'Enviado'")
        res = input("¿Desea cambiar el estado a 'Enviado'? (si/no): ")
        if res == "si" or res == "SI" or res == "Si":
            pedidos[indice]["Estado"] = "Enviado"
            print("¡Éxito! El pedido ahora está Enviado.")
            
    elif estado_actual == "Enviado" or estado_actual == "Reenviado":
        print("El pedido ya fue enviado.")
        print("Opción disponible: 'Reenviado' (En caso de fallo o inconformidad del cliente)")
        res = input("¿Desea registrar un reenvío para este pedido? (si/no): ")
        if res == "si" or res == "SI" or res == "Si":
            pedidos[indice]["Estado"] = "Reenviado"
            print("¡Éxito! El pedido ha sido marcado como Reenviado.")
            
    else:
        print("El pedido tiene un estado desconocido o ya finalizó su ciclo.")

def consultarInformaciónHistorica():
    if len(pedidos) == 0:
        print("No hay pedidos cargados.")
        return

    clienteBuscado = pedirDatos("Ingrese el nombre del cliente a buscar: ", '[a-zA-Z]+')
    clienteBuscado = clienteBuscado.upper()

    pedidosCliente = list(filter(lambda pedido: pedido["Cliente"] == clienteBuscado, pedidos))

    if len(pedidosCliente) == 0:
        print("No se encontraron pedidos para ese cliente.")
        return

    print(f"\nPedidos encontrados para {clienteBuscado}:\n")

    for pedido in pedidosCliente:
        print(f"Nro de Orden: {pedido['NroDeOrden']}")
        print(f"Dirección: {pedido['Direccion']}")
        print(f"Estado: {pedido['Estado']}")
        print(f"Método de envío: {pedido['MetodoDeEnvio']}")
        print("Items:")

        for item in pedido["Items"]:
            print(f" - {item['Producto']} | Cantidad: {item['Cantidad']} | Subtotal: ${item['PrecioTotal']}")

        print("-" * 50)

def altaProducto():
    prod = {}
    prod["Id"] = len(productos_remeras)
    prod["Nombre"] = pedirDatos("Ingrese el nombre del nuevo producto: ", '[a-zA-Z]')
    prod["Color"] = pedirDatos("Ingrese el color del nuevo producto: ", '[a-zA-Z]')
    prod["Talle"] = pedirDatos("Ingrese el talle del nuevo producto: ", '[a-zA-Z]')
    prod["Precio"] = int(pedirDatos("Ingrese el precio del nuevo producto: ", '[0-9]'))
    prod["CantidadStock"] = int(pedirDatos("Ingrese la cantidad de stock del nuevo producto: ", '[0-9]'))
    productos_remeras.append(prod)

    res = pedirDatos("¿Desea listar los productos? (si/no): ", '[a-zA-Z]')
    if res == "si":
        mostrarProductos()
    else:
        print("Volviendo al menu...")
        time.sleep(1)

def bajaProducto():
    mostrarProductos()
    res = int(pedirDatos("Ingrese el numero del producto correspondiente a la baja: ", '[0-9]'))
    prod_eliminado = productos_remeras.pop(res)
    print(f'El producto eliminado fue: \n\
{prod_eliminado["Nombre"]}\n\
Talle {prod_eliminado["Talle"]}\n\
Color {prod_eliminado["Color"]}\n\
Mostrando productos actuales y volviendo al menu...')
    time.sleep(3)
    mostrarProductos()

def modificarProducto():
    mostrarProductos()
    res = int(pedirDatos("Ingrese el numero del producto correspondiente a modificar: ", '[0-9]'))
    for i in range(len(productos_remeras)):
        if res <= len(productos_remeras):
            if i == res:
                contador=0
                for key in productos_remeras[i].items():
                    contador+=1
                    print(f'{contador}: {key}')
        else:
            print("Fuera de rango")
            return
    clave = int(pedirDatos("Ingrese el numero correspondiente a la propiedad que quieras modificar: ", '[0-9]'))
    contador = 0
    for key,value in productos_remeras[res].items():
        contador+=1
        if clave == contador:
            if type(value) == int:
                nuevoValor = int(pedirDatos("Ingrese el nuevo valor: ", '[0-9]'))
                productos_remeras[res][key] = nuevoValor
            elif type(value) == str:
                nuevoValor = pedirDatos("Ingrese el nuevo valor: ", '[a-zA-Z ]')
                productos_remeras[res][key] = nuevoValor
    mostrarProductos()


"""El main solamente trabaja llamando a funciones"""
def main():

    while True:
        res = pedirDatos(
        "¿Que operación deseas realizar?\n" \
        "1: Registrar Compra \n" \
        "2: Gestionar estado de pedido\n" \
        "3: Consultar informacion Historica\n" \
        "4: Dar de Alta/Baja o Modificar un producto\n"\
        "5: Salir\n",
        '^[1-5]$'
        )

        res = int(res)

        match res:
            case 1: 
                print("Registrar Pedidos")
                registrarPedidos()
            case 2:
                print("Gestionar Estado de pedido")
                gestionarEstadoDePedido()
            case 3:
                print("Consultar Informacion Histrica")
                consultarInformaciónHistorica()
            case 4:
                res = int(pedirDatos("¿Que operacion desea hacer?\n" \
                "1: Alta\n" \
                "2: Baja\n" \
                "3: Modificar\n",'[1-3]'))
                match res:
                    case 1:
                        altaProducto()
                    case 2:
                        bajaProducto()
                    case 3:
                        modificarProducto()
                    case _:
                        print("Invalido")
            case 5:
                break
            case _:
                print("Invalido")

    print("Saliendo ...")
    time.sleep(1)

main()