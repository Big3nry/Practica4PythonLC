def guardar_tabla_multiplicar(numero):
    try:
        if 1 <= numero <= 10:
            with open(f"tabla-{numero}.txt", "w") as archivo:
                for i in range(1, 11):
                    archivo.write(f"{numero} x {i} = {numero * i}\n")
            print(f"La tabla de multiplicar del {numero} se ha guardado en tabla-{numero}.txt")
        else:
            print("Por favor, ingrese un número entre 1 y 10.")
    except Exception as e:
        print(f"Error al guardar la tabla de multiplicar: {e}")

def mostrar_tabla_multiplicar(numero):
    try:
        if 1 <= numero <= 10:
            with open(f"tabla-{numero}.txt", "r") as archivo:
                contenido = archivo.read()
                print(f"Tabla de multiplicar del {numero}:\n{contenido}")
        else:
            print("Por favor, ingrese un número entre 1 y 10.")
    except FileNotFoundError:
        print(f"El archivo tabla-{numero}.txt no existe.")
    except Exception as e:
        print(f"Error al leer la tabla de multiplicar: {e}")

def mostrar_linea_tabla_multiplicar(numero, linea):
    try:
        if 1 <= numero <= 10:
            with open(f"tabla-{numero}.txt", "r") as archivo:
                lineas = archivo.readlines()
                if 1 <= linea <= len(lineas):
                    print(f"Línea {linea} de la tabla de multiplicar del {numero}:\n{lineas[linea - 1]}")
                else:
                    print(f"Línea {linea} fuera de rango. La tabla tiene {len(lineas)} líneas.")
        else:
            print("Por favor, ingrese un número entre 1 y 10.")
    except FileNotFoundError:
        print(f"El archivo tabla-{numero}.txt no existe.")
    except Exception as e:
        print(f"Error al leer la línea de la tabla de multiplicar: {e}")

def menu():
    while True:
        print("\nMenu:")
        print("1. Guardar tabla de multiplicar")
        print("2. Mostrar tabla de multiplicar")
        print("3. Mostrar línea de la tabla de multiplicar")
        print("4. Salir")

        opcion = input("Seleccione una opción (1-4): ")

        if opcion == "1":
            numero = int(input("Ingrese un número entre 1 y 10: "))
            guardar_tabla_multiplicar(numero)
        elif opcion == "2":
            numero = int(input("Ingrese un número entre 1 y 10: "))
            mostrar_tabla_multiplicar(numero)
        elif opcion == "3":
            numero = int(input("Ingrese un número entre 1 y 10: "))
            linea = int(input("Ingrese el número de línea a mostrar: "))
            mostrar_linea_tabla_multiplicar(numero, linea)
        elif opcion == "4":
            print("Programa finalizado.")
            break
        else:
            print("Opción no válida. Por favor, ingrese una opción del 1 al 4.")

if __name__ == "__main__":
    menu()
