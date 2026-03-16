# ==========================================================
# Sistema Básico de Gestión de Inventario y Pedidos
# Uso de arreglos (listas) y funciones
# ==========================================================


# Listas para almacenar datos
inventario = []
pedidos = []


# ==========================================================
# FUNCIONES INVENTARIO
# ==========================================================

def registrar_producto():
    nombre = input("Nombre del producto: ")
    cantidad = int(input("Cantidad: "))
    precio = float(input("Precio: "))

    producto = {
        "nombre": nombre,
        "cantidad": cantidad,
        "precio": precio
    }

    inventario.append(producto)
    print("Producto registrado correctamente.\n")


def mostrar_inventario():

    if not inventario:
        print("Inventario vacío.\n")
        return

    print("Inventario actual:")
    for i, producto in enumerate(inventario):
        print("Codigo:",i, "|", producto["nombre"], "| Cantidad:", producto["cantidad"], "| Precio:", producto["precio"])
    print()


def editar_producto():

    mostrar_inventario()

    if not inventario:
        return

    indice = int(input("Seleccione el codigo del producto a editar: "))

    if 0 <= indice < len(inventario):

        nombre = input("Nuevo nombre: ")
        cantidad = int(input("Nueva cantidad: "))
        precio = float(input("Nuevo precio: "))

        inventario[indice]["nombre"] = nombre
        inventario[indice]["cantidad"] = cantidad
        inventario[indice]["precio"] = precio

        print("Producto actualizado.\n")

    else:
        print("Producto no válido.\n")


def eliminar_producto():

    mostrar_inventario()

    if not inventario:
        return

    indice = int(input("Seleccione el codigo del producto a eliminar: "))

    if 0 <= indice < len(inventario):

        inventario.pop(indice)
        print("Producto eliminado.\n")

    else:
        print("Producto no válido.\n")


# ==========================================================
# FUNCIONES PEDIDOS
# ==========================================================

def registrar_pedido():

    cliente = input("Nombre del cliente: ")
    producto = input("Producto pedido: ")
    cantidad = int(input("Cantidad: "))

    pedido = {
        "cliente": cliente,
        "producto": producto,
        "cantidad": cantidad
    }

    pedidos.append(pedido)
    print("Pedido registrado correctamente.\n")


def mostrar_pedidos():

    if not pedidos:
        print("No hay pedidos registrados.\n")
        return

    print("Lista de pedidos:")

    for i, pedido in enumerate(pedidos):
        print("Codigo:",i, "|", pedido["cliente"], "| Producto:", pedido["producto"], "| Cantidad:", pedido["cantidad"])

    print()


def editar_pedido():

    mostrar_pedidos()

    if not pedidos:
        return

    indice = int(input("Seleccione el codigo del pedido a editar: "))

    if 0 <= indice < len(pedidos):

        cliente = input("Nuevo cliente: ")
        producto = input("Nuevo producto: ")
        cantidad = int(input("Nueva cantidad: "))

        pedidos[indice]["cliente"] = cliente
        pedidos[indice]["producto"] = producto
        pedidos[indice]["cantidad"] = cantidad

        print("Pedido actualizado.\n")

    else:
        print("Pedido no válido.\n")


def eliminar_pedido():

    mostrar_pedidos()

    if not pedidos:
        return

    indice = int(input("Seleccione el codigo del pedido a eliminar: "))

    if 0 <= indice < len(pedidos):

        pedidos.pop(indice)
        print("Pedido eliminado.\n")

    else:
        print("Pedido no válido.\n")


# ==========================================================
# MENÚ PRINCIPAL
# ==========================================================

def menu():

    while True:

        print("=================================")
        print(" SISTEMA DE INVENTARIO Y PEDIDOS ")
        print("=================================")

        print("1. Registrar producto")
        print("2. Mostrar inventario")
        print("3. Editar producto")
        print("4. Eliminar producto")
        print("5. Registrar pedido")
        print("6. Mostrar pedidos")
        print("7. Editar pedido")
        print("8. Eliminar pedido")
        print("9. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_producto()

        elif opcion == "2":
            mostrar_inventario()

        elif opcion == "3":
            editar_producto()

        elif opcion == "4":
            eliminar_producto()

        elif opcion == "5":
            registrar_pedido()

        elif opcion == "6":
            mostrar_pedidos()

        elif opcion == "7":
            editar_pedido()

        elif opcion == "8":
            eliminar_pedido()

        elif opcion == "9":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida.\n")


# ==========================================================
# EJECUCIÓN DEL PROGRAMA
# ==========================================================

menu()