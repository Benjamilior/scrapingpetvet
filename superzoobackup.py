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


#Ejecutador del Codigo

# PATH = "C:\\Program Files (x86)\\chromedriver.exe"
PATH = "/usr/local/bin/chromedriver"
# Configurar las opciones de Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")  # Ver el Navegador
chrome_options.add_argument("--window-size=1920x1080")

start_time = time.time()  # Tiempo de inicio de la ejecución

driver = webdriver.Chrome(options=chrome_options)

import requests

skus = {
    "petdotu33":"14068",
    "petdotu86":"10222",
    "petdotu6":"2054",
    "petdotu20":"12714",
    "petdotu23":"3955",
    "petdotu197": "9510",
    "petdotu172": "5580",
    "petdotu189": "4934",
    "petdotu181": "1139",
    "petdotu203": "3759",
    "petdotu169": "12708",
    "petdotu163": "12714",
    "petdotu164": "4114",
    "petdotu185": "566",
    "petdotu188": "563",
    "petdotu177": "7665",
    "petdotu196": "7666",
    "petdotu199": "7667",
    "petdotu171": "4132",
    "petdotu173": "913",
    "petdotu175": "2917",
    "petdotu179": "1600",
    "petdotu180": "180",
    "petdotu187": "912",
    "petdotu190": "924",
    "petdotu191": "923",
    "petdotu192": "1838",
    "petdotu193": "2084",
    "petdotu195": "3565",
    "petdotu201": "6533",
    "petdotu202": "544",
    "petdotu205": "5426",
    "petdotu210": "1355",
    "petdotu184": "183",
    "petdotu12": "2054",
    "petdotu8": "4159",
    "petdotu9": "9513",
    "petdotu14": "2123",
    "petdotu11": "2059",
    "petdotu13": "4162",
    "petdotu10": "9509",
    "petdotu44": "2272",
    "petdotu45": "64",
    "petdotu68": "4935",
    "petdotu67": "5581",
    "petdotu70": "4936",
    "petdotu69": "5582",
    "petdotu138": "5583",
    "petdotu147": "4937",
    "petdotu148": "14070",
    "petdotu32": "1135",
    "petdotu30": "3954",
    "petdotu29": "1137",
    "petdotu28": "1138",
    "petdotu84": "13372",
    "petdotu72": "13372",
    "petdotu5": "8162",
    "petdotu4": "8163",
    "petdotu119": "14318",
    "petdotu48": "918",
    "petdotu99": "219",
    "petdotu22": "3762",
    "petdotu24": "3954",
    "petdotu25": "3760",
    "petdotu21": "3763",
    "petdotu88": "988",
    "petdotu50": "1215",
    "petdotu97": "5336",
    "petdotu96": "5334",
    "petdotu63": "3851",
    "petdotu62": "3850",
    "petdotu64": "4175",
    "petdotu78": "4943",
    "petdotu73": "3958",
    "petdotu74": "3940",
    "petdotu18": "2998",
    "petdotu15": "1066",
    "petdotu82": "10342",
    "petdotu93": "4204",
    "petdotu42": "3939",
    "petdotu43": "3942",
    "petdotu40": "1243",
    "petdotu39": "3941",
    "petdotu66": "2816",
    "petdotu65": "1840",
    "petdotu49": "1189",
    "petdotu83": "6535",
    "petdotu77": "1174",
    "petdotu98": "507",
    "petdotu41": "3943",
    "petdotu34": "6627",
    "petdotu81": "7473",
    "petdotu89": "2078",
    "petdotu37": "6695",
    "petdotu17": "917",
    "petdotu16": "1396",
    "petdotu19": "1065",
    "petdotu160": "2053",
    "petdotu121": "3086",
    "petdotu151": "4122",
    "petdotu152": "4120",
    "petdotu131": "4165",
    "petdotu153": "3367",
    "petdotu146": "1898",
    "petdotu125": "13374",
    "petdotu105": "7481",
    "petdotu142": "1250",
    "petdotu135": "1602",
    "petdotu149": "6490",
    "petdotu115": "6491",
    "petdotu80": "2506",
    "petdotu46": "2970",
    "petdotu47": "1824",
    "petdotu161":"4123",
    "petdotu13":"5820",
    "petdotu194":"5017",
    "petdotu176":"7084",
    "petdotu128":"2592",
    "petdotu132":"5138"
   
}
url = "https://www.superzoo.cl/on/demandware.store/Sites-SuperZoo-Site/es_CL/Product-Variation"
headers = {
    "cookie": "dwanonymous_d0dc502116cb8dbe645f9cfd4de7a41c=bcMOVoozmTsaCnopmAfqnOFYdA; sid=uisfiyZAjKB6kyrlYredoTkMQimFmMBcKfo; __cq_dnt=1; dw_dnt=1; dwsid=GuTXqtD4VymkY-qv5Zx93JnDighzIBvV9wrfyljSk3IY_BUNChw2Ws6jK10_LB1pNasK-Y5GpS0AW2iq_6suUg%3D%3D",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "en-US,es-CL;q=0.7,en;q=0.3",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "X-Requested-With": "XMLHttpRequest",
    "Connection": "keep-alive",
    "Referer": "https://www.superzoo.cl/perro/alimentos/alimentos-seco/acana-heritage-puppy-and-junior-formula-alimento-para-perro/2440_m.html",
    "Cookie": "dwanonymous_d0dc502116cb8dbe645f9cfd4de7a41c=abJO6BX3dDhWBOkJQ6Kc1S7xBK; _gcl_au=1.1.432189164.1711992849; _ga_F6KXZHLE3N=GS1.1.1718132347.22.1.1718132387.20.0.0; _ga=GA1.1.251015063.1711992850; _ga_NX6YD1WY8Q=GS1.2.1718132347.18.1.1718132379.28.0.0; _fbp=fb.1.1711992850744.1025892230; _gcl_aw=GCL.1717534440.Cj0KCQjw9vqyBhCKARIsAIIcLMHVvFDImQTRT2a1V55uFu5xkdKDhTZDr5k-RGFBWksG92cB6gYxAGsaArplEALw_wcB; _gac_UA-16091283-48=1.1717534425.Cj0KCQjw9vqyBhCKARIsAIIcLMHVvFDImQTRT2a1V55uFu5xkdKDhTZDr5k-RGFBWksG92cB6gYxAGsaArplEALw_wcB; _gcl_gs=2.1.k1$i1717534435; sid=Q8elh4xKnj8nmnRX_NzLdThOTF4whDVCM4A; __cq_dnt=1; dw_dnt=1; dwsid=SXsAkxLDywQFtR3zHq_QyjLy6UquDWB5Ea9DklGenmVgKodeoS2UeX7gqnhxPSj36gtMopZwiZMO5Y-BVJqMcQ==; _gid=GA1.2.1717175473.1718125883; _gat_UA-16091283-48=1",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "TE": "trailers"
}


price_data = []
payload = ""
skus2 = {"petdotu105": "7481"}

for sku, product_id in skus.items():
    querystring = {"pid": product_id}
    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    data = response.json()
   
    
    price = data['product']['price']['sales']['value']
    price_offer = data['product']['price']['list']['value'] if data['product']['price']['list'] is not None else None
    availability = data['product']['availability']['messages'][0] if 'messages' in data['product']['availability'] else "Información no disponible"

    price_data.append({
        "SKU": sku,
        "Price": price,
        "Price_Offer": price_offer,
        "Availability": availability
    })
    
    print(f"SKU: {sku}, Price: {price}, Price_Offer: {price_offer}, Availability: {availability}")

    if price_offer is None:
        print(f"SKU: {sku}, Price Offer: No disponible")



end_time = time.time()  # Tiempo de finalización de la ejecución

execution_time = end_time - start_time

print("Tiempo de ejecución: %.2f segundos" % execution_time)

df = pd.DataFrame(price_data)
print(df)
print(df.head)

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
values = [[item['SKU'], item['Price'], item["Price_Offer"]] for item in price_data]
result = sheet.values().update(spreadsheetId=SPREADSHEET_ID,
							range='superzoo!A2:C1000',#CAMBIAR
							valueInputOption='USER_ENTERED',
							body={'values':values}).execute()
print(f"Datos insertados correctamente")  

#Valores que se pasan a Sheets
values = [[item['Availability']] for item in price_data]
result = sheet.values().update(spreadsheetId=SPREADSHEET_ID,
							range='superzoo!M2:N',#CAMBIAR
							valueInputOption='USER_ENTERED',
							body={'values':values}).execute()
print(f"Datos insertados correctamente")  




df = pd.DataFrame(price_data)
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
values = [[row['SKU'], competitor, "No Disponible",row['Price'], now_str] for _, row in df.iterrows()]

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
values = [[now_str, competitor,row['SKU'], row['Availability']] for _, row in df.iterrows()]

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
values = [[row['SKU'], competitor, row['Price'],"Nada", row["Availability"]] for _, row in df.iterrows()]

# Insertar los resultados en la nueva hoja después de la última fila
update_range = f'apipets!A{last_row}:E{last_row + len(values) - 1}' #Cambiar
result = sheet.values().update(
    spreadsheetId=NEW_SPREADSHEET_ID,
    range=update_range,
    valueInputOption='USER_ENTERED',
    body={'values': values}
).execute()
