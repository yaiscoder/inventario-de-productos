# Se definen variables para el funcionamiento del programa.
inventario = []
opcion = 0

# Se llaman las funciones que se encuentran en otro archivo.
from servicios import *
from archivos import *

# Se utiliza un ciclo "while" para validar la opción escogida de acuerdo a la acción a realizar en el menú 
while opcion != 9:

    # Se utilizan los condiciones "if", "elif" y "else" para cada acción del menú
    # Además que se llaman las funciones correspondiente para cada acción del menú.
    mostrar_menu()
    try:
      opcion = int(input("Ingrese el número correspondiente a la acción que desea realizar: "))
      print("-"*30)
    except ValueError:
      print("-"*30)
      print("Debe ingresar un número válido")
      print("-"*30)

    if opcion == 1:  #Se agrega un nuevo producto
     nombre = input("Ingrese el nombre del producto: ")
     precio = float(input("Ingrese el precio del producto: "))
     cantidad = int(input("Ingrese cuantos productos desea comprar: "))
     while precio <= 0 or cantidad <= 0:
        print("-"*30)
        print("¡Error! recuerda que el precio y la cantidad no pueden ser negativos")
        print("Introducelos de nuevo")
        print("-"*30)
        precio = float(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese cuántos productos desea comprar: "))

     agregar_producto(inventario, nombre, precio, cantidad)


    elif opcion == 2: #Muestra el inventario actual
      if len(inventario) == 0:
        print("-"*30)
        print("El inventario está vacio")
        print("-"*30)
      else: 
        mostrar_inventario(inventario)

    elif opcion == 3: #Busca un producto
      if len(inventario) == 0:
        print("-"*30)
        print("El inventario está vacio")
        print("-"*30)
      else:
        nombre = input("Ingrese el nombre del producto que desea buscar: ")
        p = buscar_producto(inventario, nombre)
        if p:
          print("-"*30)
          print(f"El producto que usted busco es: {p}")
          print("-"*30)
        else:
          print("-"*30)
          print("El producto que está buscando, no se encuentra disponible.")
          print("-"*30)
 

    elif opcion == 4: #Actualiza la información de un producto
      if len(inventario) == 0:
        print("-"*30)
        print("El inventario está vacio")
        print("-"*30)
      else: 
       nombre = input("Ingrese el nombre del producto que desea actualizar: ")
       precio = float(input("Ingrese el nuevo precio: "))
       cantidad = int(input("Ingrese la cantidad a comprar: "))
       if precio <= 0 or cantidad <= 0:
         print("-"*30)
         print("¡Error! recuerda que el precio y la cantidad no pueden ser negativos")
         print("Introducelos de nuevo")
         print("-"*30)
         precio = float(input("Ingrese el precio del producto: "))
         cantidad = int(input("Ingrese cuantos productos desea comprar: "))

       if actualizar_producto(inventario, nombre, nuevo_precio=precio, nueva_cantidad=cantidad):
         print("-"*30)
         print("Su producto se actualizó correctamente")
         print("-"*30)
       else:
         print("-"*30)
         print("Su producto no se encontró para actualizar")
         print("-"*30)


    elif opcion == 5: # Elimina un producto
      if len(inventario) == 0:
        print("-"*30)
        print("El inventario está vacio")
        print("-"*30)
      else:
        nombre = input("Introduzca el nombre del producto que desea eliminar: ")
        if eliminar_producto(inventario, nombre):
         print("-"*30)
         print("Su producto se eliminó correctamente")
         print("-"*30)
        else:
         print("-"*30)
         print("Su producto no se logró eliminar")
         print("-"*30) 


    elif opcion == 6: # Calcula estadisticas del inventario
      if len(inventario) == 0:
        print("-"*30)
        print("El inventario está vacio")
        print("-"*30)
      else:
       calcular_estadisticas(inventario)

    elif opcion == 7: # Guarda en CSV
      ruta = input("Ingrese la ruta y el nombre del archivo CSV: ")
      guardar_csv(inventario, ruta, incluir_header=True)
    
    elif opcion == 8: # Carga en CSV
      ruta = input("Ingrese la ruta del archivo CSV a cargar: ")
      cargado = cargar_csv(ruta)
    
      # Preguntar sobrescribir o fusionar
      decision = input("¿Desea sobrescribir el inventario actual? (S/N): ").strip().upper()
      if decision == "S":
        inventario[:] = cargado
        accion = "Reemplazo"
        print("-"*30)
        print("Inventario reemplazado por el CSV cargado.")
        print("-"*30)
      else:
        accion = "Fusión"
        for producto in cargado: 
            existente = buscar_producto(inventario, producto["Nombre"])
            if existente:
                existente["Cantidad"] += producto["Cantidad"]
                existente["Precio"] = producto["Precio"]
            else:
                inventario.append(producto)
        print("-"*30)
        print("Inventario fusionado con el CSV cargado.")
        print("-"*30)
        
    elif opcion == 9:  # Sale del programa
     print("-"*30)
     print("¡Vuelva pronto!")
     print("-"*30)
     break

    else:  # Mensaje de error sino se introduce valor entre (1-9)
     print("-"*30)
     print("¡Opción invalida, intentelo nuevamente!")
     print("-"*30)

