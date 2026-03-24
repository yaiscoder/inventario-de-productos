import csv

def guardar_csv(inventario, ruta, incluir_header=True):
    if len(inventario) == 0:
        print("Inventario vacio")
        return
    
    try:
        with open(ruta, "w", encoding="utf-8") as archivo:
            campos = ["nombre", "precio", "cantidad"]
            escritor = csv.DictWriter(archivo, fieldnames=campos)

            if incluir_header:
                escritor.writeheader()
            for producto in inventario:
                escritor.writerow({
                    "nombre": producto["Nombre"],
                    "precio": producto["Precio"],
                    "cantidad": producto["Cantidad"]
                })
            print(f"Inventario guardado en {ruta}")

    except PermissionError:
        print("¡Error! No se puede escribir en la ruta especificado, verifica los permisos")
    except Exception as e:
        print(f"Error inesperado al guardar CSV: {e} ")


def cargar_csv(ruta):
    print