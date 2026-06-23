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
    """ 
    Administra la variable global numeroOrden para asignar un ID único 
    y correlativo a cada nuevo pedido.
    """
    global numeroOrden
    orden = numeroOrden
    numeroOrden += 1
    return orden

def pedirDatos(mensaje, patron):
    """ 
    Solicita una entrada al usuario y delega la validación 
    de la misma mediante una expresión regular.
    """
    dato = input(mensaje)
    res = validaciones(patron, dato)
    return res

def validaciones(patron,valor):
    """ 
    Ejecuta un bucle de control que valida el valor ingresado contra 
    el patrón Regex proporcionado hasta que sea correcto.
    """
    while not(re.match(patron,valor)):
        print('No valido')
        valor = input('Ingrese nuevamente: ')
    return valor

def mostrarProductos():
    """ 
    Itera sobre la lista de productos_remeras para imprimir 
    el catálogo disponible en la consola.
    """
    for i in range(len(productos_remeras)):
        print(f'{i}: {productos_remeras[i]["Nombre"]} - Talle: {productos_remeras[i]["Talle"]} - Precio: {productos_remeras[i]["Precio"]}')

def elegirMetodosDeEnvio():
    """ 
    Muestra el menú de envío y gestiona la selección del usuario, 
    retornando el nombre del método seleccionado.
    """
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
    Función principal de flujo de venta. Captura datos del cliente, 
    gestiona el carrito de compras, verifica stock y almacena el pedido final.
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
                    producto_nombre = productos_remeras[i]["Nombre"]
                    productos_remeras[i]["CantidadStock"] = productos_remeras[i]["CantidadStock"] - cantidad

                    items.append({"Producto" : producto_nombre,
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
    """ 
    Busca un pedido por número de orden y permite actualizar su estado 
    (Pagado -> Empaquetado -> Enviado -> Reenviado).
    """
    if len(pedidos) == 0:
        print("No hay pedidos registrados.")
        return

    # --- NUEVA SECCIÓN: Listado de pedidos para referencia ---
    print("\n--- Listado de Pedidos Disponibles ---")
    
    for p in pedidos:
        nro = p['NroDeOrden']
        cliente = p['Cliente']
        direc = p['Direccion']
        estado = p['Estado']
        
        # Formato simple y directo
        print(f"Nro de Orden: {nro} - Nombre: {cliente} - Dirección: {direc} - Estado: {estado}")
    
    print("-" * 50 + "\n")
    # ---------------------------------------------------------
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
    
    # Lógica de cambio de estados (se mantiene igual)
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
    """ 
    Filtra los pedidos realizados buscando por nombre del cliente y 
    muestra el desglose completo de sus compras.
    """
    if len(pedidos) == 0:
        print("No hay pedidos cargados.")
        return

    clientes_disponibles = sorted(list(set(p["Cliente"] for p in pedidos)))
    
    print("\n--- Clientes con pedidos registrados ---")
    for cliente in clientes_disponibles:
        print(f"• {cliente}")
    print("----------------------------------------\n")

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
    """ 
    Registra un nuevo producto en el catálogo solicitando sus atributos 
    e incrementando el tamaño de productos_remeras.
    """
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
    """ 
    Elimina un producto del catálogo mediante su índice y 
    muestra un resumen del objeto borrado.
    """
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
    """ 
    Permite editar campos específicos (Nombre, Precio, Stock, etc.) 
    de un producto existente seleccionado por índice.
    """
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

def procesarUsuarios():
    matriz = []
    try:
        with open('./usuarios.txt', 'r') as arch:
            for linea in arch.readlines():
                if linea.strip().split(';')[0] == "nombre":
                    continue
                partes = linea.strip().split(';')
                nombre = partes[0]
                email = partes[1]
                contrasenia = partes[2]
                rol = partes[3]
                matriz.append([nombre,email,contrasenia,rol])
        return matriz
    except FileNotFoundError:
        print("Archivo no encontrado")
            
def login(email, contrasenia):
    usuarios = procesarUsuarios()
    for i in usuarios:
        if i[1] == email and i[2] == contrasenia:
            print(f'Bienvenido al sistema {i[0]} tiene permisos de {i[3]}')
            return i
    print("Usuario o contraseña incorrectas")
    return None

def altaUsuarios(nombre,email,contrasenia,rol):
    usuario = f'\n{nombre};{email};{contrasenia};{rol}'
    try:
        with open('./usuarios.txt', 'w') as arch:
            arch.write(usuario)
    except FileNotFoundError:
        print("No se encontro el archivo")
    

"""El main solamente trabaja llamando a funciones"""
def main():
    """ 
    Bucle principal que despliega el menú e invoca las 
    funcionalidades según la elección del usuario.
    """
    try:
        correo = pedirDatos("Bienvenido al sistema, ingrese su correo: ", '[a-zA-Z]')
        contrasenia = pedirDatos("Ingrese su contraseña: ", '[a-zA-Z0-9]')    
        usuario = login(correo,contrasenia)
        while not usuario:
            correo = pedirDatos("Ingrese su correo: ", '[a-zA-Z]')
            contrasenia = pedirDatos("Ingrese su contraseña: ", '[a-zA-Z0-9]')    
            usuario = login(correo,contrasenia)
        while True:  
            match(usuario[3]):
                case "administrador":
                    res = pedirDatos(

                    "¿Que operación deseas realizar?\n"

                    "1: Registrar Compra \n"

                    "2: Gestionar estado de pedido\n"

                    "3: Consultar informacion Historica\n"

                    "4: Dar de Alta/Baja o Modificar un producto\n"

                    "5: Salir\n",

                    '^[1-5]$'

                )
                    res = int(res)
                    match(res):
                        case 1:
                            print("Registrar pedidos")
                            registrarPedidos()
                        case 2:
                            print("Gestionar Estado de pedido")
                            gestionarEstadoDePedido()
                        case 3:
                            print("Consultar Informacion Historica")
                            consultarInformacionHistorica()
                        case 4:
                            subopcion = int(pedirDatos(
                            "¿Que operacion desea hacer?\n"

                            "1: Alta\n"

                            "2: Baja\n"

                            "3: Modificar\n",

                            '[1-3]'
                            ))
                            match(subopcion):
                                case 1:
                                    altaProducto()
                                case 2:
                                    bajaProducto()
                                case 3:
                                    modificarProducto()
                                case _:
                                    print("Invalido")
                        case 5:
                            print("Saliendo ...")
                            time.sleep(1)
                            break     
                        case _:
                            print("Invalido")
                            
                case "supervisor":
                    res = pedirDatos(

                    "¿Que operación deseas realizar?\n"

                    "1: Registrar Compra \n"

                    "2: Gestionar estado de pedido\n"

                    "3: Consultar informacion Historica\n"

                    "4: Modificar un producto\n"

                    "5: Salir\n",

                    '^[1-5]$'

                )
                    res = int(res)
                    match(res):
                        case 1:
                            print("Registrar pedidos")
                            registrarPedidos()
                        case 2:
                            print("Gestionar Estado de pedido")
                            gestionarEstadoDePedido()
                        case 3:
                            print("Consultar Informacion Historica")
                            consultarInformacionHistorica()
                        case 4:
                            modificarProducto()
                        case 5:    
                            print("Saliendo ...")
                            time.sleep(1)
                            break     
                        case _:
                            print("Invalido")

                case "empleado":
                    res = pedirDatos(

                    "¿Que operación deseas realizar?\n"

                    "1: Registrar Compra \n"

                    "2: Gestionar estado de pedido\n"

                    "3: Consultar informacion Historica\n"

                    "4: Salir\n",

                    '^[1-5]$'

                )
                    res = int(res)
                    match(res):
                        case 1:
                            print("Registrar pedidos")
                            registrarPedidos()
                        case 2:
                            print("Gestionar Estado de pedido")
                            gestionarEstadoDePedido()
                        case 3:
                            print("Consultar Informacion Historica")
                            consultarInformacionHistorica()
                        case 4:
                            print("Saliendo ...")
                            time.sleep(1)
                            break     
                        case _:
                            print("Invalido")
    except KeyboardInterrupt:
        print("Saliendo...")
        
main()