#Codigo para sacar el precio de producto donde la pagina no tiene boton 
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.oauth2 import service_account
import pandas as pd
import json
import datetime
#Google Sheets
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
KEY = 'key.json'
SPREADSHEET_ID = '1PrHE2FBeBhQnVYeCLQclLqj_tiIOq7z3JuMAG-2aAXg'
creds = None
creds = service_account.Credentials.from_service_account_file(KEY, scopes=SCOPES)
service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()

start_time = time.time()  # Tiempo de inicio de la ejecución


# URL del endpoint
url = "https://www.superzoo.cl/on/demandware.store/Sites-SuperZoo-Site/es_CL/Product-GetById"

import requests

skus = {
    "petdotu194": "5017",
    "petdotu160": "2053",
    "petdotu197": "no stock",
    "petdotu121": "3087",
    "petdotu176": "no stock",
    "petdotu6": "5016",
    "petdotu97": "5336",
    "petdotu96": "5334",
    "petdotu93": "4204",
    "petdotu205": "5426",
    "petdotu135": "1602",
    "petdotu142": "1250",
    "petdotu149": "6490",
    "petdotu115": "6491",
    "petdotu199": "7667",
    "petdotu177": "7665",
    "petdotu196": "7666",
    "petdotu98": "507",
    "petdotu125": "13374",
    "petdotu84": "13372",
    "petdotu72": "13372",
    "petdotu78": "4943",
    "petdotu82": "10342",
    "petdotu132": "2950_m",
    "petdotu170": "4084",
    "petdotu49": "1189",
    "petdotu9": "9513",
    "petdotu181": "1139",
    "petdotu28": "1138",
    "petdotu32": "1135",
    "petdotu30": "3954",
    "petdotu29": "1137",
    "petdotu148": "14070",
    "petdotu171": "4132",
    "petdotu81": "7473",
    "petdotu37": "6695",
    "petdotu83": "6535",
    "petdotu193": "2084",
    "petdotu188": "563",
    "petdotu185": "566",
    "petdotu14": "2123",
    "petdotu190": "924",
    "petdotu191": "923",
    "petdotu105": "7481",
    "petdotu42": "3939",
    "petdotu43": "3942",
    "petdotu41": "3943",
    "petdotu39": "3941",
    "petdotu40": "1243",
    "petdotu10": "9509",
    "petdotu19": "1065",
    "petdotu18": "2998",
    "petdotu17": "917",
    "petdotu15": "1066",
    "petdotu126": "1689",
    "petdotu16": "1396",
    "petdotu71": "15654",
    "petdotu12": "2054",
    "petdotu11": "2059",
    "petdotu183": "no stock",
    "petdotu65": "1840",
    "petdotu66": "2816",
    "petdotu164": "4114",
    "petdotu152": "4120",
    "petdotu151": "4122",
    "petdotu161": "4123",
    "petdotu13": "5820",
    "petdotu60": "890",
    "petdotu70": "4936",
    "petdotu69": "5582",
    "petdotu189": "4934",
    "petdotu172": "5580",
    "petdotu147": "4937",
    "petdotu138": "5583",
    "petdotu68": "4935",
    "petdotu67": "5581",
    "petdotu175": "2917",
    "petdotu153": "3367",
    "petdotu131": "4165",
    "petdotu77": "1174",
    "petdotu195": "3565",
    "petdotu202": "544",
    "petdotu192": "1838",
    "petdotu187": "912",
    "petdotu173": "913",
    "petdotu184": "183",
    "petdotu180": "180",
    "petdotu8": "4159",
    "petdotu179": "1600",
    "petdotu5": "8162",
    "petdotu4": "8163",
    "petdotu119": "14318",
    "petdotu201": "6533",
    "petdotu73": "3958",
    "petdotu74": "3940",
    "petdotu203": "3759",
    "petdotu169": "12708",
    "petdotu25": "3760",
    "petdotu24": "3954",
    "petdotu22": "3762",
    "petdotu23": "3955",
    "petdotu21": "3763",
    "petdotu20": "12714",
    "petdotu163": "12714",
    "petdotu89": "2078",
    "petdotu210": "1355",
    "petdotu92": "445",
    "petdotu146": "1898",
    "petdotu128": "2590",
    "petdotu48": "918",
    "petdotu33": "14068",
    "petdotu34": "6627",
    "petdotu88": "988",
    "petdotu85": "no stock",
    "petdotu45": "64",
    "petdotu47": "1824",
    "petdotu46": "2970",
    "petdotu99": "219",
    "petdotu44": "2272",
    "petdotu80": "2506",
    "petdotu62": "3850",
    "petdotu63": "3851",
    "petdotu64": "4175",
    "petdotu86": "10222",
    "petdotu222": "4162"
}

# Encabezados de la solicitud
headers = {
    "cookie": "dwanonymous_d0dc502116cb8dbe645f9cfd4de7a41c=bcMOVoozmTsaCnopmAfqnOFYdA; sid=I5m0lb08bfRr1IZd-AGpLIewqr6SH52xkBU; __cq_dnt=1; dw_dnt=1; dwsid=4nSsmpJ2_8RY_L_RBnLeHkZdsrG9VQ-Boz3nGFJtQqM6J6OU1Rx3ppeUOHQm3CEj_PLgGdVaWDVOtJBmIKtvrg%3D%3D",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:130.0) Gecko/20100101 Firefox/130.0",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "en-US,es-CL;q=0.7,en;q=0.3",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "X-Requested-With": "XMLHttpRequest",
    "Connection": "keep-alive",
    "Referer": "https://www.superzoo.cl/gato/alimentos/alimento-seco/hills-feline-adult-mature-hairball-control-7-1.58-kg-alimento-para-gato/2017.html",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "TE": "trailers"
}

results = []

# Función para obtener datos por SKU
def get_product_by_sku(sku_key, sku_id):
    querystring = {"id": sku_id}
    try:
        response = requests.get(url, headers=headers, params=querystring, timeout=10)
        response.raise_for_status()  # Verifica si hubo un error en la respuesta
        data = response.json()  # Asumiendo que la respuesta es JSON
        
        # Extraer solo el 'price' y 'quantity'
        product = data.get('product', {})
        price = product.get('price', 'No disponible')
        quantity = product.get('quantity', 'No disponible')
        
        # Guardar los datos en un diccionario y añadirlo a 'results'
        data = {
            "SKU": sku_key,
            "Precio": price,
            "Stock": quantity
        }
        results.append(data)
        
        # Imprimir el resultado actual
        print(f"SKU: {sku_key} (ID: {sku_id}) - Precio: {price}, Cantidad: {quantity}")
    
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred para SKU {sku_key} (ID: {sku_id}): {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Error de conexión para SKU {sku_key} (ID: {sku_id}): {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout para SKU {sku_key} (ID: {sku_id}): {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Error en la solicitud para SKU {sku_key} (ID: {sku_id}): {req_err}")
    except ValueError as json_err:
        print(f"Error al parsear JSON para SKU {sku_key} (ID: {sku_id}): {json_err}")

# Medir el tiempo de ejecución
start_time = time.time()

# Iterar sobre todos los SKUs y obtener sus datos
for sku_key, sku_id in skus.items():
    get_product_by_sku(sku_key, sku_id)
    time.sleep(1)  # Pausa de 1 segundo entre solicitudes para evitar sobrecargar el servidor

# Calcular el tiempo total de ejecución
end_time = time.time()
execution_time = end_time - start_time

# Convertir los resultados en un DataFrame y mostrarlo
df = pd.DataFrame(results)
print(df)

# Mostrar las primeras filas del DataFrame
print(df.head())

# Imprimir el tiempo de ejecución
print(f"Tiempo de ejecución: {execution_time} segundos")

# Mostrar el contenido de la lista 'results'
print(results)

print("Tiempo de ejecución: %.2f segundos" % execution_time)


#Fecha de Extraccion
now = datetime.datetime.now()
now_str = now.strftime('%Y-%m-%d %H:%M:%S')
data = {"":now_str}
json_data = json.dumps(data)
values = [[json_data]]
result = sheet.values().update(spreadsheetId=SPREADSHEET_ID,
							range='superzoo!F2',#CAMBIAR
							valueInputOption='USER_ENTERED',
							body={'values':values}).execute()


#Valores que se pasan a Sheets
values = [[item['SKU'], item['Precio']] for item in results]
result = sheet.values().update(spreadsheetId=SPREADSHEET_ID,
							range='superzoo!A2:C1000',#CAMBIAR
							valueInputOption='USER_ENTERED',
							body={'values':values}).execute()
print(f"Datos insertados correctamente")  

#Valores que se pasan a Sheets
values = [[item['Stock']] for item in results]
result = sheet.values().update(spreadsheetId=SPREADSHEET_ID,
							range='superzoo!M2:N',#CAMBIAR
							valueInputOption='USER_ENTERED',
							body={'values':values}).execute()
print(f"Datos insertados correctamente")  




df = pd.DataFrame(results)
print(df)
print(df.head) 

competitor = "SuperZoo"  # Cambiar 
# Enviar datos a otro Google Sheets
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
KEY = 'key.json'
NEW_SPREADSHEET_ID = '1lLfl_jSGUEtitfsezo_zz53Bn2zAzID73VtxIi4dKRo'  # ID de la nueva hoja de cálculo

creds = service_account.Credentials.from_service_account_file(KEY, scopes=SCOPES)
service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()

# Obtener la última fila con datos en la nueva hoja
result = sheet.values().get(spreadsheetId=NEW_SPREADSHEET_ID, range='petvet!A:A').execute() #Cambiar donde llega la info
values = result.get('values', [])
last_row = len(values) + 1  # Obtener el índice de la última fila vacía

# Convertir resultados a la lista de valores
values = [[row['SKU'], competitor, "No Disponible",row['Precio'], now_str] for _, row in df.iterrows()]

# Insertar los resultados en la nueva hoja después de la última fila
update_range = f'petvet!A{last_row}:E{last_row + len(values) - 1}' #Cambiar
result = sheet.values().update(
    spreadsheetId=NEW_SPREADSHEET_ID,
    range=update_range,
    valueInputOption='USER_ENTERED',
    body={'values': values}
).execute()

print(f"Datos insertados correctamente en la nueva hoja de Google Sheets en el rango {update_range}")

# Obtener la última fila con datos en la nueva hoja
result = sheet.values().get(spreadsheetId=NEW_SPREADSHEET_ID, range='Stock!A:A').execute()  # Cambiar donde llega la info
values = result.get('values', [])
last_row = len(values) + 1  # Obtener el índice de la última fila vacía
# Convertir resultados a la lista de valores
values = [[now_str, competitor,row['SKU'], row['Stock']] for _, row in df.iterrows()]

# Insertar los resultados en la nueva hoja después de la última fila
print(values)
update_range = f'Stock!A{last_row}:E{last_row + len(values) - 1}'  # Cambiar
result = sheet.values().update(
    spreadsheetId=NEW_SPREADSHEET_ID,
    range=update_range,
    valueInputOption='USER_ENTERED',
    body={'values': values}
).execute()

# MANDAR DATOS A LA API ----------------------------------------------------------------------------------------------------
# Obtener la última fila con datos en la nueva hoja
result = sheet.values().get(spreadsheetId=NEW_SPREADSHEET_ID, range='apipets!A:A').execute() #Cambiar donde llega la info
values = result.get('values', [])
last_row = len(values) + 1  # Obtener el índice de la última fila vacía

# Convertir resultados a la lista de valores
values = [[row['SKU'], competitor, row['Precio'],"Nada", row["Stock"]] for _, row in df.iterrows()]

# Insertar los resultados en la nueva hoja después de la última fila
update_range = f'apipets!A{last_row}:E{last_row + len(values) - 1}' #Cambiar
result = sheet.values().update(
    spreadsheetId=NEW_SPREADSHEET_ID,
    range=update_range,
    valueInputOption='USER_ENTERED',
    body={'values': values}
).execute()
