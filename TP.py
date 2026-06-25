import time
import re
import json

""" 
Descripción del sistema
El sistema está hecho para gestionar pedidos de un e-commerce,
incluyendo la carga de productos comprados, cantidades, 
métodos de envío y el seguimiento del estado de cada orden.
"""

def cargarProductos():
    """ 
    Lee el archivo productos.json y devuelve la lista de productos 
    para trabajar con el catálogo desde el programa.
    """
    try:
        """ Abre el archivo en modo lectura ('r') """
        with open('./productos.json', 'r') as arch:
            """ Convierte el contenido JSON a una estructura de Python (lista/diccionario) """
            return json.load(arch)
    except FileNotFoundError:
        """ Si el archivo no existe, avisa por consola y devuelve una lista vacía """
        print("No se pudo cargar productos.json")
        return []

def cargarPedidos():
    try:
        """ Abre el archivo de pedidos en modo lectura """
        with open('./pedidos.json', 'r') as arch:
            return json.load(arch)
    except FileNotFoundError:
        """ Manejo de error si no se encuentra el historial de pedidos """
        print("No se pudo cargar pedidos.json")
        return []
    
def guardarProductos():
    """ 
    Guarda la lista actual de productos_remeras en productos.json 
    para conservar los cambios realizados en el catálogo.
    """
    try:
        """ Abre el archivo en modo escritura ('w'), sobreescribiendo el anterior """
        with open('./productos.json', 'w') as arch:
            """ Vuelca la lista 'productos_remeras' al JSON con indentación para legibilidad """
            json.dump(productos_remeras, arch, indent=4, ensure_ascii=False)
    except:
        print("No se pudo guardar productos.json")

def guardarPedidos():
    try:
        """ Abre y sobreescribe el historial de pedidos con los datos actuales en memoria """
        with open('./pedidos.json', 'w') as arch:
            json.dump(pedidos, arch, indent=4, ensure_ascii=False)
    except:
        print("No se pudo guardar pedidos.json")
    

""" Carga inicial de datos al arrancar el programa """
productos_remeras = cargarProductos()
pedidos = cargarPedidos()

""" Inicializa el número de orden base """
def generarNumeroOrden():
    numeroOrden = 1000
    """ 
    Administra la variable global numeroOrden para asignar un ID único 
    y correlativo a cada nuevo pedido.
    """
    """ Llama a la variable global definida arriba """
    for i in pedidos:
        numeroOrden = i["NroDeOrden"]
    """ Incrementa el contador para el próximo pedido """
    return numeroOrden+1

def pedirDatos(mensaje, patron):

    """ 
    Solicita una entrada al usuario y delega la validación 
    de la misma mediante una expresión regular.
    """
    """ Muestra el mensaje por consola y captura lo que escribe el usuario """
    dato = input(mensaje)
    """ Llama a la función validadora pasándole el regex y el dato ingresado """
    res = validaciones(patron, dato)
    return res

def validaciones(patron,valor):
    """ 
    Ejecuta un bucle de control que valida el valor ingresado contra 
    el patrón Regex proporcionado hasta que sea correcto.
    """
    """ Mientras el valor no coincida con la expresión regular (patrón)... """
    while not(re.match(patron,valor)):
        print('No valido')
        """ ...vuelve a pedir el ingreso del dato """
        valor = input('Ingrese nuevamente: ')
    """ Retorna el valor solo cuando pasa la validación """
    return valor

def contadorSalida(numero):
    """ 
    Realiza una cuenta regresiva recursiva desde el número recibido 
    hasta llegar a cero.
    """
    """ Condición de corte de la recursividad """
    if numero == 0:
        return
    print(numero)
    """ Pausa la ejecución por 1 segundo """
    time.sleep(1)
    """ Se llama a sí misma restando 1 al número """
    contadorSalida(numero - 1)

def mostrarProductos():
    """ 
    Itera sobre la lista de productos_remeras para imprimir 
    el catálogo disponible en la consola.
    """
    """ Recorre la lista por índice para mostrar la posición (ID temporal) y los datos del producto """
    for i in range(len(productos_remeras)):
        print(f'{i}: {productos_remeras[i]["Nombre"]} - Talle: {productos_remeras[i]["Talle"]} - Precio: {productos_remeras[i]["Precio"]}')

def elegirMetodosDeEnvio():
    """ 
    Muestra el menú de envío y gestiona la selección del usuario, 
    retornando el nombre del método seleccionado.
    """
    """ Despliega las opciones de envío """
    print("\nMétodos de envío:")
    print("1 - Retiro en sucursal")
    print("2 - Envío estándar")
    print("3 - Envío express")

    opcion = input("Seleccione una opción: ")

    """ Bucle de validación manual (sin regex) para asegurar que elija 1, 2 o 3 """
    while opcion != "1" and opcion != "2" and opcion != "3":
        print("Opción inválida.")
        opcion = input("Seleccione una opción: ")

    """ Retorna un string descriptivo según la opción numérica elegida """
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
    """ Bandera para controlar el bucle de compras """
    flag = "si"
    """ Pide y valida nombre y dirección, convirtiéndolos a mayúsculas """
    cliente = pedirDatos("Ingrese el nombre del cliente: ", '[a-zA-Z]')
    cliente = cliente.upper()
    direccion = pedirDatos("Ingrese su dirección: ", '[A-Za-z0-9]')
    direccion = direccion.upper()
    """ Lista local para guardar los productos de esta compra específica (carrito) """
    items = []

    """ Inicia el ciclo de selección de productos """
    while flag == "si":
        mostrarProductos()

        """ Pide el índice del producto y lo convierte a entero """
        producto = int(pedirDatos("Ingrese el producto que desea comprar (Seleccione un numero): ", '^[0-9]+$'))

        """ Valida que el índice seleccionado exista dentro de la lista de productos """
        while producto < 0 or producto >= len(productos_remeras):
            print("Opción inválida")
            producto = int(pedirDatos("Ingrese el producto que desea comprar (Seleccione un numero): ", '^[0-9]+$'))

        """ Pide la cantidad deseada """
        cantidad = int(pedirDatos("Ingrese la cantidad que desea comprar: ", '^[0-9]+$'))

        """ Busca el producto seleccionado en el catálogo """
        for i in range(len(productos_remeras)):
            if producto == i:
                """ Verifica si hay suficiente stock disponible """
                if cantidad < productos_remeras[i]["CantidadStock"]:
                    """ Calcula precios y actualiza el stock restando la cantidad comprada """
                    precioUnitario = productos_remeras[i]["Precio"]
                    precioTotal = cantidad * productos_remeras[i]["Precio"]
                    producto_nombre = productos_remeras[i]["Nombre"]
                    productos_remeras[i]["CantidadStock"] = productos_remeras[i]["CantidadStock"] - cantidad

                    """ Agrega el detalle del producto al carrito (lista 'items') """
                    items.append({"Producto" : producto_nombre,
                                "PrecioUnitario" : precioUnitario,
                                "Cantidad" : cantidad,
                                "PrecioTotal" : precioTotal
                                })
                else:
                    print("No tenemos la cantidad de stock suficiente para la compra")

        """ Pregunta si desea agregar otro producto al carrito """
        flag = pedirDatos("¿Quiere seguir comprando?: (si/no)\n", '^(si|no)$')

    """ Llama a la función para elegir cómo se entregará el pedido """
    metodoDeEnvio = elegirMetodosDeEnvio()

    """ Arma el diccionario del pedido final con todos los datos recopilados """
    pedido = {}
    pedido["Cliente"] = cliente
    pedido["Direccion"] = direccion
    pedido["Items"] = items
    pedido["NroDeOrden"] = generarNumeroOrden() 
    pedido["Estado"] = "Pagado" 
    pedido["MetodoDeEnvio"] = metodoDeEnvio

    """ Imprime el ticket o resumen general """
    print(f'\
            -------Resumen de compra:--------\
    \nCliente : {pedido["Cliente"]}\
    \nDireccion : {pedido["Direccion"]}\
    \nNro De Orden: {pedido["NroDeOrden"]}\
    \nEstado: {pedido["Estado"]}\
    \nMetodoDeEnvio : {pedido["MetodoDeEnvio"]}')

    total_compra = 0
    print("--- DETALLE DE COMPRA ---")
    
    """ Recorre el carrito para imprimir el detalle y sumar el costo total """
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
    
    """ Guarda el pedido en la lista global """
    pedidos.append(pedido)
    """ Persiste los cambios de stock en el JSON """
    guardarProductos()
    """ Persiste el nuevo pedido en el JSON """
    guardarPedidos()
            
    input("Presione cualquier tecla para continuar...")


def gestionarEstadoDePedido():
    """ 
    Busca un pedido por número de orden y permite actualizar su estado 
    (Pagado -> Empaquetado -> Enviado -> Reenviado).
    """
    """ Verifica que existan pedidos cargados """
    if len(pedidos) == 0:
        print("No hay pedidos registrados.")
        return

    print("\n--- Listado de Pedidos Disponibles ---")
    
    """ Muestra un resumen rápido de todos los pedidos para facilitar la búsqueda """
    for p in pedidos:
        nro = p['NroDeOrden']
        cliente = p['Cliente']
        direc = p['Direccion']
        estado = p['Estado']
        
        """ Formato simple y directo """
        print(f"Nro de Orden: {nro} - Nombre: {cliente} - Dirección: {direc} - Estado: {estado}")
    
    print("-" * 50 + "\n")
    """ Solicita el número de orden a modificar """
    nro_orden_buscar = int(pedirDatos("Ingrese el número de orden que desea gestionar: ", '[0-9]+'))

    indice = 0
    encontrado = False
    
    """ Búsqueda secuencial (While) del pedido por su número de orden """
    while indice < len(pedidos) and encontrado == False:
        if pedidos[indice]["NroDeOrden"] == nro_orden_buscar:
            encontrado = True
        else:
            indice += 1

    """ Si recorre toda la lista y no lo encuentra, sale de la función """
    if not encontrado:
        print(f"No se encontró la orden Nro {nro_orden_buscar}.")
        return
    
    """ Extrae el estado actual del pedido encontrado """
    estado_actual = pedidos[indice]["Estado"]
    
    print(f"\n> Gestionando Orden Nro: {nro_orden_buscar}")
    print(f"> Cliente: {pedidos[indice]['Cliente']}")
    print(f"> Estado actual: {estado_actual}")
    
    """ Máquina de estados lineal: evalúa el estado actual y ofrece pasar al siguiente lógico """
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
    
    """ Guarda los cambios de estado en el JSON """
    guardarPedidos()

def consultarInformacionHistorica():
    """ 
    Filtra los pedidos realizados buscando por nombre del cliente y 
    muestra el desglose completo de sus compras.
    """
    """ Verifica que haya pedidos en el sistema """
    if len(pedidos) == 0:
        print("No hay pedidos cargados.")
        return

    """ Crea una lista única (set) de nombres de clientes y la ordena alfabéticamente """
    clientes_disponibles = sorted(list(set(p["Cliente"] for p in pedidos)))
    
    """ Imprime la lista de clientes para ayudar al usuario a saber a quién buscar """
    print("\n--- Clientes con pedidos registrados ---")
    for cliente in clientes_disponibles:
        print(f"• {cliente}")
    print("----------------------------------------\n")

    """ Solicita y formatea el nombre del cliente a buscar """
    clienteBuscado = pedirDatos("Ingrese el nombre del cliente a buscar: ", '[a-zA-Z]+')
    clienteBuscado = clienteBuscado.upper()

    """ Usa filter y lambda para crear una nueva lista solo con los pedidos de ese cliente """
    pedidosCliente = list(filter(lambda pedido: pedido["Cliente"] == clienteBuscado, pedidos))

    """ Si el cliente no tiene pedidos, avisa y sale """
    if len(pedidosCliente) == 0:
        print("No se encontraron pedidos para ese cliente.")
        return

    print(f"\nPedidos encontrados para {clienteBuscado}:\n")

    """ Recorre todos los pedidos de ese cliente e imprime los detalles """
    for pedido in pedidosCliente:
        print(f"Nro de Orden: {pedido['NroDeOrden']}")
        print(f"Dirección: {pedido['Direccion']}")
        print(f"Estado: {pedido['Estado']}")
        print(f"Método de envío: {pedido['MetodoDeEnvio']}")
        print("Items:")

        """ Recorre los productos dentro de cada pedido específico """
        for item in pedido["Items"]:
            print(f" - {item['Producto']} | Cantidad: {item['Cantidad']} | Subtotal: ${item['PrecioTotal']}")

        print("-" * 50)
        input("Presione cualquier tecla para continuar...")

def altaProducto():

    """ 
    Registra un nuevo producto en el catálogo solicitando sus atributos 
    e incrementando el tamaño de productos_remeras.
    """

    prod = {}
    """ Asigna como ID la longitud actual de la lista (lo pone al final) """
    prod["Id"] = len(productos_remeras)
    """ Solicita y valida todas las propiedades del nuevo producto """
    prod["Nombre"] = pedirDatos("Ingrese el nombre del nuevo producto: ", '[a-zA-Z]')
    prod["Color"] = pedirDatos("Ingrese el color del nuevo producto: ", '[a-zA-Z]')
    prod["Talle"] = pedirDatos("Ingrese el talle del nuevo producto: ", '[a-zA-Z]')
    prod["Precio"] = int(pedirDatos("Ingrese el precio del nuevo producto: ", '[0-9]'))
    prod["CantidadStock"] = int(pedirDatos("Ingrese la cantidad de stock del nuevo producto: ", '[0-9]'))
    
    """ Agrega el diccionario del nuevo producto a la lista general """
    productos_remeras.append(prod)
    guardarProductos()

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
    try:
        """ Pide el índice numérico del producto a eliminar """
        res = int(pedirDatos("Ingrese el numero del producto correspondiente a la baja: ", '[0-9]'))
        """ Utiliza .pop() para quitar el elemento de la lista y lo guarda en una variable """
        prod_eliminado = productos_remeras.pop(res)
        guardarProductos()
    except IndexError:
        """ Si el usuario ingresa un número mayor a la cantidad de productos, ataja el error """
        print("No existe un producto con ese número.")
        return

    """ Imprime el detalle del producto que acaba de ser eliminado """
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
    """ Pide el índice numérico del producto que se quiere editar """
    res = int(pedirDatos("Ingrese el numero del producto correspondiente a modificar: ", '[0-9]'))
    try:
        """ Intenta acceder al producto en esa posición """
        producto = productos_remeras[res]
    except:
        """ Si el índice no existe, corta la ejecución """
        print("Fuera de rango")
        return

    contador=0
    """ Muestra todas las propiedades (claves) del producto para que el usuario elija cuál editar """
    for key in producto.items(): 
        contador+=1
        print(f'{contador}: {key}')

    """ Pide el número de la propiedad seleccionada """
    clave = int(pedirDatos("Ingrese el numero correspondiente a la propiedad que quieras modificar: ", '[0-9]'))
    contador = 0
    
    """ Vuelve a recorrer las propiedades para encontrar la que coincide con el número elegido """
    for key,value in producto.items():
        contador+=1
        if clave == contador:
            """ Valida el tipo de dato original para saber qué tipo de ingreso solicitar """
            if type(value) == int:
                nuevoValor = int(pedirDatos("Ingrese el nuevo valor: ", '[0-9]'))
                productos_remeras[res][key] = nuevoValor
            elif type(value) == str:
                nuevoValor = pedirDatos("Ingrese el nuevo valor: ", '[a-zA-Z ]')
                productos_remeras[res][key] = nuevoValor
    
    """ Guarda los cambios y muestra cómo quedó """
    guardarProductos()
    mostrarProductos()

def procesarUsuarios():
    """ 
    Lee el archivo usuarios.txt, separa los datos de cada usuario 
    y los guarda en una matriz para poder validar el acceso.
    """
    matriz = []
    try:
        """ Abre el archivo de texto donde están los usuarios """
        with open('./usuarios.txt', 'r') as arch:
            for linea in arch:
                """ Si la línea es el encabezado de las columnas, la ignora """
                if linea.strip().split(';')[0] == "nombre":
                    continue
                """ Separa los datos por punto y coma (;) y quita los saltos de línea """
                partes = linea.strip().split(';')
                """ Agrega la lista de datos del usuario como una nueva fila en la matriz """
                matriz.append(partes)
        return matriz
    except:
        print("Archivo no encontrado")
        return matriz

def login(email, contrasenia):
    """ 
    Busca un usuario por email y contraseña dentro de la matriz 
    generada desde usuarios.txt para permitir el ingreso al sistema.
    """
    """ Llama a procesarUsuarios para obtener la matriz actualizada """
    usuarios = procesarUsuarios()
    """ Recorre fila por fila buscando coincidencia de email y clave """
    for i in usuarios:
        if i[1] == email and i[2] == contrasenia:
            """ Si coincide, devuelve la lista con los datos completos del usuario (incluyendo el rol) """
            print(f'Bienvenido al sistema {i[0]} tiene permisos de {i[3]}')
            return i
    """ Si termina de recorrer y no hay coincidencias, falla el login """
    print("Usuario o contraseña incorrectas")
    return None

def altaUsuarios(nombre,email,contrasenia,rol):
    """ 
    Registra un nuevo usuario agregando sus datos al archivo 
    usuarios.txt con el formato correspondiente.
    """
    """ Formatea el string con la estructura esperada separada por ; y un salto de línea """
    usuario = f'{nombre};{email};{contrasenia};{rol}\n'
    try:
        """ Abre el archivo en modo 'append' ('a') para agregar texto al final sin borrar el contenido """
        with open('./usuarios.txt', 'a') as arch:
            arch.write(usuario)
    except:
        print("No se encontro el archivo")
    
def bajaUsuarios(email):
    """ 
    Elimina un usuario según su email y reescribe el archivo 
    usuarios.txt con la lista actualizada.
    """
    usuarios = procesarUsuarios()
    """ Busca al usuario por su email y lo remueve de la matriz en memoria """
    for i in usuarios:
        if i[1] == email:
            usuarios.remove(i)
    try:
        """ Vuelve a abrir el archivo en modo escritura ('w') para sobreescribirlo todo """
        with open('./usuarios.txt', 'w') as arch:
            """ Escribe primero el encabezado de las columnas """
            arch.write('nombre;email;contrasenia;rol\n')
            """ Escribe línea por línea los usuarios restantes en la matriz """
            for i in usuarios:
                arch.write(f'{i[0]};{i[1]};{i[2]};{i[3]}\n')
    except:
        print("El archivo no se encontro")
            
""" El main solamente trabaja llamando a funciones """
def main():
    """ 
    Bucle principal que despliega el menú e invoca las 
    funcionalidades según la elección del usuario.
    """
    try:
        """ Proceso de autenticación inicial """
        correo = pedirDatos("Bienvenido al sistema, ingrese su correo: ", '[a-zA-Z]')
        contrasenia = pedirDatos("Ingrese su contraseña: ", '[a-zA-Z0-9]')    
        usuario = login(correo,contrasenia)
        
        """ Bucle infinito hasta que el usuario ingrese credenciales válidas """
        while not usuario:
            correo = pedirDatos("Ingrese su correo: ", '[a-zA-Z]')
            contrasenia = pedirDatos("Ingrese su contraseña: ", '[a-zA-Z0-9]')    
            usuario = login(correo,contrasenia)
            
        """ Bucle principal de ejecución de los menús """
        while True:  
            """ Evalúa el rol del usuario (posición 3 de la lista devuelta por login) """
            match(usuario[3]):
                
                
                case "administrador":
                    res = pedirDatos(
                        "¿Que operación deseas realizar?\n"
                        "1: Registrar Compra \n"
                        "2: Gestionar estado de pedido\n"
                        "3: Consultar informacion Historica\n"
                        "4: Dar de Alta/Baja o Modificar un producto\n"
                        "5: Salir\n"
                        "6: Dar de Alta/Baja un usuario\n",
                        '^[1-6]$'
                    )
                    res = int(res)
                    """ Selector de sub-menú para el administrador """
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
                            """ Submenú específico para gestionar productos en el catálogo """
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
                            contadorSalida(5)
                            time.sleep(1)
                            """ Cierra la ejecución de la función main utilizando return """
                            return     
                        case 6:
                            """ Submenú específico para gestionar usuarios del sistema """
                            subopcion_usuario = int(pedirDatos(
                                "¿Que operacion desea hacer?\n"
                                "1: Dar de alta un usuario\n"
                                "2: Dar de baja un usuario\n",
                                '^[1-2]$'
                            ))
                            match(subopcion_usuario):
                                case 1:
                                    nombre = pedirDatos("Ingrese el nombre del empleado: ", '^[a-zA-Z ]+$')
                                    email = pedirDatos("Ingrese el email: ", '^.+$')
                                    contrasenia = pedirDatos("Ingrese la contraseña: ", '^.+$')
                                    rol = pedirDatos("Ingrese el rol: ", '^[a-zA-Z]+$')
                                    altaUsuarios(nombre, email, contrasenia, rol)
                                case 2:
                                    email = pedirDatos("Ingrese el email del empleado que vas a dar de baja: ", '^.+$')
                                    bajaUsuarios(email)     
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
                    """ El supervisor tiene menos permisos (no puede dar altas o bajas) """
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
                            contadorSalida(5)
                            """ Sale del bucle para terminar el programa """
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
                    """ El empleado tiene el nivel de acceso más básico (solo opera ventas y estados) """
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
                            contadorSalida(5)
                            break     
                        case _:
                            print("Invalido")
    except:
        """ Atrapa excepciones generales durante la ejecución del programa para cerrarlo de forma controlada """
        print("Saliendo...")
        contadorSalida(5)
        
""" Punto de entrada de la aplicación """
main()