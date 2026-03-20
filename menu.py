# Se definen uas variables para el funcionamiento del programa, una lista llamada "inventario" para guardar la información de cada producto
# Y una variable llamada "opcion" que tiene un valor por defecto 0 para que más adelante en la ejecución, de acuerdo a la acción realizada por el usuario
#Se modifique según corresponda.

inventario = []
opcion = 0
total = 0
t_unidad = 0

# Se llaman las funciones que se encunetran en otro archivo para hacer del codigo más limpio y organizado.
from funciones import *


# Se utiliza un ciclo "while" para validar la opción escogida de acuerdo a la acción a realizar en el menú y así el programa se repita 
# mostrando el menú hasta que el propio usuario sea quien decida si quiere salirse del programa.
while opcion != 4:

    # Aqui se utilizan los condiciones "if", "elif" y "else" para condicionar que según sea la opción escogida por el usuario
    # Se cumpla la acción correspondiente a cada opción.
    # Además que se llaman las funciones correspondiente a cada opción del menú
    mostrar_menu()
    opcion = int(input("Ingrese el número correspondiente a la acción que desea realizar: "))
    print("-"*30)

    if opcion == 1:
     agregar_producto(inventario)

    elif opcion == 2:
      mostrar_inventario(inventario)

    elif opcion == 3:
      calcular_estadisticas(inventario, total, t_unidad)
        
    elif opcion == 4:
     print("-"*30)
     print("¡Vuelva pronto!")
     break

    else:
     print("-"*30)
     print("¡Opción invalida, intentelo nuevamente!")

# El objetivo de esta semana fue el implemntar el uso de ciclos y condiciones en el programa para poder añadir un menú con cada acción que el programa realiza.
# Además de importar funciones ya definidas en otro archivo para hacer del documento más limpio.