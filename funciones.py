def mostrar_menu():
    print("-"*30)
    print("MENÚ")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Calcular estadísticas")
    print("4. Salir")
    print("-"*30)


def agregar_producto(inventario):
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese cuantos productos desea comprar: "))
    if precio <= 0 and cantidad <= 0:
        print("¡Error! recuerda que el precio y la cantidad no pueden ser negativos")
        print("Introducelos de nuevo")
        precio = float(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese cuantos productos desea comprar: "))
       
    producto = {
        "Nombre": nombre,
        "Precio": precio,
        "Cantidad": cantidad
       }
    inventario.append(producto)
    print("-"*30)
    print("¡El producto se agregó correctamente!")
    print("-"*30)


def mostrar_inventario(inventario):
    if len(inventario) == 0:
        print("-"*30)
        print("El inventario está vacio")
    else:
       for producto in inventario:
          print(f"Producto: {producto["Nombre"]} | Precio: {producto["Precio"]} | Cantidad: {producto["Cantidad"]}")

def calcular_estadisticas(inventario, total, t_unidad):
   if len(inventario) == 0:
        print("-"*30)
        print("El inventario está vacio, no hay estadisticas para calcular")
   else: 
      for item in inventario:
         cost = item["Precio"]
         amount = item["Cantidad"]
         subtotal = cost * amount
         total += subtotal
         t_unidad = len(inventario)
      print("-"*30)
      print(f"El total de su compra completa es {total}")
      print(f"Y usted compró en total {t_unidad} productos")