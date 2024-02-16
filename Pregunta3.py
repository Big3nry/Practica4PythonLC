import requests
from io import BytesIO
import zipfile
from PIL import Image

def descargar_imagen(url):
    try:
        response = requests.get(url)
        response.raise_for_status() 
        return response.content
    except requests.RequestException as e:
        print(f"Error al descargar la imagen: {e}")
        return None

def guardar_imagen_como_zip(imagen_data, image_zip):
    with zipfile.ZipFile(image_zip, 'w') as zip_file:
        zip_file.writestr('imagen.jpg', imagen_data)

def descomprimir_zip(archivo_zip, carpeta_destino):
    with zipfile.ZipFile(archivo_zip, 'r') as zip_file:
        zip_file.extractall(carpeta_destino)

def main():
    url = "https://images.unsplash.com/photo-1546527868-ccb7ee7dfa6a?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"

    imagen_data = descargar_imagen(url)

    if imagen_data:
        image_zip = "imagen.zip"
        guardar_imagen_como_zip(imagen_data, image_zip)
        print(f"Imagen descargada y guardada como {image_zip}")

        carpeta_destino = "imagen_descomprimida"
        descomprimir_zip(image_zip, carpeta_destino)
        print(f"Archivo zip descomprimido en la carpeta {}")

        imagen_descomprimida_path = f"{carpeta_destino}/imagen.jpg"
        Image.open(imagen_descomprimida_path).show()

if __name__ == "__main__":
    main()