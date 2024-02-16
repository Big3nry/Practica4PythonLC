import requests

def obtener_precio_bitcoin():
    try:
        cantidad_bitcoins = float(input("Ingrese la cantidad de bitcoins que posee: "))
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()  
        precio_bitcoin = response.json()["bpi"]["USD"]["rate_float"]
        costo_en_usd = cantidad_bitcoins * precio_bitcoin
        print(f"El costo actual de {cantidad_bitcoins} bitcoins es: ${costo_en_usd:,.4f}")

        guardar_en_archivo(cantidad_bitcoins, costo_en_usd)

    except ValueError:
        print("Por favor, ingrese un valor numérico válido para la cantidad de bitcoins.")
    except requests.RequestException as e:
        print(f"Error al consultar la API de CoinDesk: {e}")

def guardar_en_archivo(cantidad_bitcoins, costo_en_usd):
    with open("bitcoin_prices.txt", "a") as archivo:
        archivo.write(f"Cantidad de Bitcoins: {cantidad_bitcoins}, Costo en USD: {costo_en_usd:,.4f}\n")

if __name__ == "__main__":
    obtener_precio_bitcoin()
