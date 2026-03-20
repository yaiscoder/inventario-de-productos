def mostrar_menu():
    print("-"*30)
    print("MENÚ")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Calcular estadísticas")
    print("4. Salir")
    print("-"*30)


def agregar_producto(c_producto, inventario):
    for i in range(c_producto):
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
       print("¡El producto se agregó correctamente!")
       print(f"{inventario}")

def mostrar_inventario(inventario):
    if len(inventario) == 0:
        print("-"*30)
        print("El inventario está vacio")
    else:
       for producto in inventario:
          print(producto)

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
         unidad = item["Cantidad"]
         t_unidad += unidad 
         print("-"*30)
         print(f"El total de su compra completa es {total}")
         print(f"Y usted compró en total {t_unidad} productos")