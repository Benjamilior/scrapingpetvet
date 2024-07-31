import requests
import pandas as pd

# URL del endpoint
url = 'https://script.googleusercontent.com/macros/echo?user_content_key=xQkdDmw35jiSDDSmxSScZlr0pgNFjM9D8Jz1FkUd7oHZlg4ck1xu9gwALuHZuvXyNqxqP_-zMdQXYY-oh-_GfokSR7pXw-WYm5_BxDlH2jW0nuo2oDemN9CCS2h10ox_1xSncGQajx_ryfhECjZEnIzGumioN7qoCfe8ajqxd-u7R-2JNAcT7b30BqGxYusw7zVZ8FUFbFq5SttUL60FvVnMBidYx-OSkuRkfb4AbqWkd4xJLH4V-w&lib=Mruxvl4KDFUxguH-OYvWh81hwL89NOhPq'

# Realiza la solicitud GET al endpoint
response = requests.get(url)

# Asegúrate de que la solicitud fue exitosa
if response.status_code == 200:
    # Cargar los datos JSON en una lista de listas
    data = response.json()

    # Verificar si el JSON contiene datos
    if len(data) > 0:
        # La primera lista contiene los encabezados de las columnas
        headers = data[0]
        # Las siguientes listas contienen los datos de las filas
        rows = data[1:]

        # Crear un DataFrame con los datos
        df = pd.DataFrame(rows, columns=headers)

        # Imprimir el DataFrame completo
        print(df)
    else:
        print("No se encontraron datos en el JSON.")
else:
    print(f"Error al obtener datos: {response.status_code}")
