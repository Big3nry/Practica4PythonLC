from pyfiglet import Figlet
import random

def imprimir_texto_con_figlet():
    fuentes_disponibles = Figlet().getFonts()

    fuente_seleccionada = input(f"Ingrese el nombre de una fuente ({', '.join(fuentes_disponibles)}): ").strip()
    if not fuente_seleccionada:
        fuente_seleccionada = random.choice(fuentes_disponibles)

    texto_imprimir = input("Ingrese el texto a imprimir: ")

    figlet = Figlet(font=fuente_seleccionada)

    print(figlet.renderText(texto_imprimir))

if __name__ == "__main__":
    imprimir_texto_con_figlet()
