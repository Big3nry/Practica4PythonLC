import requests
import sqlite3

url_api = "https://apis.net.pe/api-tipo-cambio/v1/tipo-cambio"

params = {
    "mes": "01",
    "anho": "2023",
    "moneda": "USD"
}

response = requests.get(url_api, params=params)

if response.status_code == 200:
    data = response.json()

    compra_dolar = data["compra"]
    venta_dolar = data["venta"]

    conn = sqlite3.connect("base.db")
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sunat_info (
            fecha TEXT PRIMARY KEY,
            compra_dolar REAL,
            venta_dolar REAL
        )
    ''')

    cursor.execute('''
        INSERT INTO sunat_info (fecha, compra_dolar, venta_dolar)
        VALUES (?, ?, ?)
    ''', (params["anho"] + "-" + params["mes"], compra_dolar, venta_dolar))

    conn.commit()
    conn.close()

    conn = sqlite3.connect("base.db")
    cursor = conn.cursor()

    cursor.execute('''
        SELECT * FROM sunat_info
    ''')

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    conn.close()

else:
    print(f"Error en la solicitud al API: {response.status_code}")