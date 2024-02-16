def contar_lineas_codigo(archivo_path):
    try:
        with open(archivo_path, "r") as archivo:
            lineas = archivo.readlines()
            lineas_de_codigo = [linea.strip() for linea in lineas if not (linea.strip().startswith("#") or not linea.strip())]
            cantidad_lineas_codigo = len(lineas_de_codigo)
            return cantidad_lineas_codigo
    except FileNotFoundError:
        print(f"El archivo {archivo_path} no existe.")
        return None
    except Exception as e:
        print(f"Error al contar las líneas de código: {e}")
        return None
def main():
    archivo_path = input("Ingrese la ruta del archivo .py: ")
    if archivo_path.endswith(".py"):
        cantidad_lineas_codigo = contar_lineas_codigo(archivo_path)
        if cantidad_lineas_codigo is not None:
            print(f"El número de líneas de código en {archivo_path} es: {cantidad_lineas_codigo}")
    else:
        print("La ruta no es válida o el archivo no tiene extensión .py.")
if __name__ == "__main__":
    main()