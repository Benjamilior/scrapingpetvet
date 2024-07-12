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
import requests
#Google Sheets
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
KEY = 'key.json'
SPREADSHEET_ID = '1PrHE2FBeBhQnVYeCLQclLqj_tiIOq7z3JuMAG-2aAXg'
creds = None
creds = service_account.Credentials.from_service_account_file(KEY, scopes=SCOPES)
service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()


#Ejecutador del Codigo

# PATH = "C:\\Program Files (x86)\\chromedriver.exe"
PATH = "/usr/local/bin/chromedriver"
# Configurar las opciones de Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")  # Ver el Navegador
chrome_options.add_argument("--window-size=1920x1080")

start_time = time.time()  # Tiempo de inicio de la ejecución

driver = webdriver.Chrome(options=chrome_options)





url = "https://petvet.cl/products/adaptil-collar-perro.js"

payload = ""
headers = {
    "cookie": "secure_customer_sig=; _tracking_consent=%257B%2522con%2522%253A%257B%2522CMP%2522%253A%257B%2522m%2522%253A%2522%2522%252C%2522a%2522%253A%2522%2522%252C%2522p%2522%253A%2522%2522%252C%2522s%2522%253A%2522%2522%257D%257D%252C%2522v%2522%253A%25222.1%2522%252C%2522region%2522%253A%2522CLRM%2522%252C%2522reg%2522%253A%2522%2522%257D; _shopify_y=6e06c95b-88fa-4ce0-b0ea-a8fba8fdf7ac; _shopify_s=a1dae16c-7a4c-468b-a001-ce827f8c08a9",
    "User-Agent": "insomnia/8.6.0"
}

response = requests.request("GET", url, data=payload, headers=headers)

print(response.text)




skus = {
    "petdotu4": "8163",
    "petdotu5": "8162",
    "petdotu8": "4159",
    "petdotu9": "9513",
    "petdotu10": "9509",
    "petdotu11": "2059",
    "petdotu12": "2054",
    "petdotu13": "4162",
    "petdotu14": "2123",
    "petdotu15": "1066",
    "petdotu16": "1396",
    "petdotu17": "917",
    "petdotu18": "2898",
    "petdotu19": "651",
    "petdotu21": "3763",
    "petdotu22": "3762",
    "petdotu24": "3954",
    "petdotu25": "3760",
    "petdotu28": "1138",
    "petdotu29": "1137",
    "petdotu30": "3954",
    "petdotu32": "1135",
    "petdotu34": "6627",
    "petdotu37": "6695",
    "petdotu39": "3941",
    "petdotu40": "1243",
    "petdotu41": "3943",
    "petdotu42": "3939",
    "petdotu43": "3942",
    "petdotu44": "2272",
    "petdotu45": "64",
    "petdotu47": "1824",
    "petdotu48": "918",
    "petdotu49": "1189",
    "petdotu50": "1215",
    "petdotu62": "3850",
    "petdotu63": "3851",
    "petdotu64": "4175",
    "petdotu65": "1840",
    "petdotu66": "2816",
    "petdotu67": "5581",
    "petdotu68": "4935",
    "petdotu69": "5582",
    "petdotu70": "4936",
    "petdotu72": "13372",
    "petdotu73": "3958",
    "petdotu74": "3940",
    "petdotu77": "1174",
    "petdotu78": "4943",
    "petdotu80": "2506",
    "petdotu81": "7473",
    "petdotu82": "10342",
    "petdotu83": "6535",
    "petdotu84": "13372",
    "petdotu88": "988",
    "petdotu89": "2078",
    "petdotu93": "4204",
    "petdotu98": "507",
    "petdotu99": "219"
}

# Headers para las solicitudes
headers = {
    "cookie": "secure_customer_sig=; _tracking_consent=%257B%2522con%2522%253A%257B%2522CMP%2522%253A%2522%2522%252C%2522a%2522%253A%2522%2522%252C%2522p%2522%253A%2522%2522%252C%2522s%2522%253A%2522%2522%257D%257D%252C%2522v%2522%253A%25222.1%2522%252C%2522region%2522%253A%2522CLRM%2522%252C%2522reg%2522%253A%2522%2522%257D; _shopify_y=6e06c95b-88fa-4ce0-b0ea-a8fba8fdf7ac; _shopify_s=a1dae16c-7a4c-468b-a001-ce827f8c08a9",
    "User-Agent": "insomnia/8.6.0"
}

# Lista para almacenar los datos extraídos
price_data = []

# Función para realizar la consulta y extraer los datos necesarios
def fetch_data(product_id, product_url):
    response = requests.get(product_url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if "variants" in data:
            for variant in data["variants"]:
                if variant["id"] == product_id:
                    price = variant["price"]
                    compare_at_price = variant.get("compare_at_price", "N/A")
                    price_data.append({
                        "SKU": product_id,
                        "Price": price,
                        "Compare_at_Price": compare_at_price
                    })
                    return
    else:
        print(f"Failed to retrieve data for ID {product_id}. Status code: {response.status_code}")

# Iterar sobre el diccionario y realizar la consulta para cada enlace
for product_id, product_url in urls.items():
    fetch_data(int(product_id), product_url)

# Crear un DataFrame con los datos extraídos
df = pd.DataFrame(price_data)
print(df)
print(df.head())

# Fecha de Extracción
now = datetime.datetime.now()
now_str = now.strftime('%Y-%m-%d %H:%M:%S')
data = {"": now_str}
json_data = json.dumps(data)

# Google Sheets API setup
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
KEY = 'key.json'
SPREADSHEET_ID = '1lLfl_jSGUEtitfsezo_zz53Bn2zAzID73VtxIi4dKRo'  # ID de la hoja de cálculo

creds = service_account.Credentials.from_service_account_file(KEY, scopes=SCOPES)
service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()

# Actualizar fecha de extracción en Google Sheets
values = [[json_data]]
result = sheet.values().update(
    spreadsheetId=SPREADSHEET_ID,
    range='superzoo!F2',  # CAMBIAR
    valueInputOption='USER_ENTERED',
    body={'values': values}
).execute()

# Valores que se pasan a Sheets
values = [[item['SKU'], item['Price']] for item in price_data]
result = sheet.values().update(
    spreadsheetId=SPREADSHEET_ID,
    range='superzoo!A2:C83',  # CAMBIAR
    valueInputOption='USER_ENTERED',
    body={'values': values}
).execute()
print(f"Datos insertados correctamente")

# Enviar datos a otro Google Sheets
competitor = "SuperZoo"  # Cambiar
NEW_SPREADSHEET_ID = '1lLfl_jSGUEtitfsezo_zz53Bn2zAzID73VtxIi4dKRo'  # ID de la nueva hoja de cálculo

# Obtener la última fila con datos en la nueva hoja
result = sheet.values().get(spreadsheetId=NEW_SPREADSHEET_ID, range='petvet!A:A').execute()  # Cambiar donde llega la info
values = result.get('values', [])
last_row = len(values) + 1  # Obtener el índice de la última fila vacía

# Convertir resultados a la lista de valores
values = [[row['SKU'], competitor, "No Disponible", row['Price'], now_str] for _, row in df.iterrows()]

# Insertar los resultados en la nueva hoja después de la última fila
update_range = f'petvet!A{last_row}:E{last_row + len(values) - 1}'  # Cambiar
result = sheet.values().update(
    spreadsheetId=NEW_SPREADSHEET_ID,
    range=update_range,
    valueInputOption='USER_ENTERED',
    body={'values': values}
).execute()

print(f"Datos insertados correctamente en la nueva hoja de Google Sheets en el rango {update_range}")