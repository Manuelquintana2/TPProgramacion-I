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

pedidos = []
numeroOrden = 1000

def generarNumeroOrden():
    global numeroOrden
    orden = numeroOrden
    numeroOrden += 1
    return orden

def registrarCompras():
    pass

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

        