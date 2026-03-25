import csv

def guardar_csv(inventario, ruta, incluir_header=True):
    """
    Guarda el inventario en un archivo CSV.
    
    Parámetros:
    - inventario (list): lista de diccionarios con productos
    - ruta (str): ruta del archivo CSV a guardar
    - incluir_header (bool): si True, incluye encabezado con 'nombre,precio,cantidad'

    Retorna:
    - None
    """

    if len(inventario) == 0:
        print("Inventario vacio")
        return
    
    try:
        with open(ruta, "w", newline="", encoding="utf-8") as archivo:
            campos = ["Nombre", "Precio", "Cantidad"]
            escritor = csv.DictWriter(archivo, fieldnames=campos)

            if incluir_header:
                escritor.writeheader()
            for producto in inventario:
                escritor.writerow({
                    "Nombre": producto["Nombre"],
                    "Precio": producto["Precio"],
                    "Cantidad": producto["Cantidad"]
                })
            print("-"*30)
            print(f"Inventario guardado en {ruta}")
            print("-"*30)

    except PermissionError:
        print("¡Error! No se puede escribir en la ruta especificada, verifica los permisos")
    except Exception as e:
        print(f"Error inesperado al guardar CSV: {e} ")


def cargar_csv(ruta):
    """
    Carga un inventario desde un archivo CSV.

    Parámetros:
    - ruta (str): ruta del archivo CSV a cargar

    Retorna:
    - lista de diccionarios con los productos cargados
    """
    inventario_cargado = []
    filas_invalidas = 0

    try:
        with open(ruta, newline='', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            
            header_esperados = ["Nombre", "Precio", "Cantidad"]
            if lector.fieldnames != header_esperados:
                print("Encabezado inválido. Se esperaba:", header_esperados)
                return []

            for fila in lector:
                try:
                    if len(fila) != 3:
                        filas_invalidas += 1
                        continue

                    nombre = fila["Nombre"].strip()
                    precio = float(fila["Precio"])
                    cantidad = int(fila["Cantidad"])

                    if precio <= 0 or cantidad <= 0:
                        filas_invalidas += 1
                        continue

                    inventario_cargado.append({
                        "Nombre": nombre,
                        "Precio": precio,
                        "Cantidad": cantidad
                    })
                except (ValueError, KeyError):
                    filas_invalidas += 1
                    continue
        print("-"*30)
        print(f"{len(inventario_cargado)} productos cargados desde el CSV.")
        print(f"{filas_invalidas} filas inválidas omitidas.")
        print("-"*30)

        return inventario_cargado

    except FileNotFoundError:
        print("Archivo no encontrado. Verifica la ruta.")
        return []
    except UnicodeDecodeError:
        print("Error de codificación al leer el archivo.")
        return []
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return []