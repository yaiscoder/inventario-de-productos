def mostrar_menu():
    print("-"*30)
    print(" ======== MENÚ ======== ")
    print("-"*30)
    print("1. Agregar")
    print("2. Mostrar")
    print("3. Buscar")
    print("4. Actualizar")
    print("5. Eliminar")
    print("6. Estadísticas")
    print("7. Guardar CSV")
    print("8. Cargar CSV")
    print("9. Salir")
    print("-"*30)


def agregar_producto(inventario, nombre, precio, cantidad):
    """
    Agrega un producto al inventario.

    Parámetros:
    inventario (list): lista de productos
    nombre (str): nombre del producto
    precio (float): precio
    cantidad (int): cantidad

    Retorna:
    None
    """
    producto = {     # Diccionario para cada producto
        'Nombre': nombre,
        'Precio': precio,
        'Cantidad': cantidad
       }
    
    inventario.append(producto) # Se agrega el diccionario a la lista
    print("-"*30)
    print("¡El producto se agregó correctamente!")
    print("-"*30)


def mostrar_inventario(inventario):
    """
    Muestra todos los productos del inventario.

    Parámetros:
    inventario (list): Lista de productos.
    
    Retorna:
    None
    """

    for producto in inventario:
        print(f"Producto: {producto['Nombre']} | Precio: {producto['Precio']} | Cantidad: {producto['Cantidad']}")


def buscar_producto(inventario, nombre):
    """
    Busca un producto por nombre.

    Parámetros:
    inventario (list): Lista de productos.
    nombre (str): Nombre del producto a buscar.

    Retorna:
    dict: Producto encontrado.
    None: Si no se encuentra el producto.
    """

    for producto in inventario:
        if producto['Nombre'].strip().lower() == nombre.strip().lower():
            return producto
    return None
    

def actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):
    """
    Actualiza el precio o cantidad de un producto.

    Parámetros:
    inventario (list): Lista de productos.
    nombre (str): Nombre del producto a actualizar.
    nuevo_precio (float): Nuevo precio del producto.
    nueva_cantidad (int): Nueva cantidad del producto.

    Retorna:
    bool: True si el producto fue actualizado.
    bool: False si el producto no fue encontrado.
    """
    producto = buscar_producto(inventario, nombre)

    if producto:
        if nuevo_precio is not None:
            producto['Precio'] = nuevo_precio
        if nueva_cantidad is not None:
            producto['Cantidad'] = nueva_cantidad
        return True
    return False


def eliminar_producto(inventario, nombre):
    """
    Elimina un producto del inventario.

    Parámetros:
    inventario (list): Lista de productos.
    nombre (str): Nombre del producto a eliminar.

    Retorna:
    bool: True si el producto fue eliminado.
    bool: False si el producto no fue encontrado.
    """

    p = buscar_producto(inventario, nombre)

    if p:
        inventario.remove(p)
        return True
    return False


def calcular_estadisticas(inventario):
    """
    Calcula estadísticas del inventario.

    Parámetros:
    inventario (list): Lista de productos.

    Retorna:
    - unidades_totales (int)
    - valor_total (float)
    - producto_mas_caro (dict)
    - producto_mayor_stock (dict)
    None: Si el inventario está vacío.
    """

    valor_total = 0
    unidades_totales = 0

    for item in inventario:
        cost = item["Precio"]
        amount = item["Cantidad"]
        subtotal = cost * amount
        valor_total += subtotal
        unidades_totales = len(inventario)
    mas_caro = max(inventario, key=lambda p: p["Precio"])
    mayor_stock = max(inventario, key=lambda p: p["Cantidad"])
   
    print("-"*30)
    print(f"El total es: ${valor_total}")
    print(f"Hay un total de {unidades_totales} productos")
    print(f"El producto más caro es: {mas_caro}")
    print(f"El producto con mayor stock en el inventario es: {mayor_stock}")

    return unidades_totales, valor_total, mas_caro, mayor_stock