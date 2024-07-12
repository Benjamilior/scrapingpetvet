#Codigo para sacar el precio de producto donde la pagina no tiene boton

#NO USARRRR NO USARRRR
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

url = "https://www.superzoo.cl/on/demandware.store/Sites-SuperZoo-Site/es_CL/Product-GetById"
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
    "petdotu18": "2998",
    "petdotu19": "1065",
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
    "petdotu99": "219",
    "petdotu6":"5016",
    "petdotu7":"5019",
    "petdotu4":"8163",
    "petdotu20":"12714",
    "petdotu23":"3955",
    "petdotu33":"14068",
    "petdotu97":"5336",
    "petdotu96":"5334",
    "petdotu86":"10222",
 
    
}
headers = {
    "cookie": "__cq_dnt=1; dw_dnt=1; sid=aNszqMqPjS6bdyk64ACSoAI6n_68Nciu_x0; dwsid=cjZj0XNDE02Mz8o5mheOZxjXz4cF-VbN6KUV6Msolr23rKPCi3Ra-KwDxbMNhU-B9aodz9yTyIZIUkORfsNC8A%3D%3D",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:124.0) Gecko/20100101 Firefox/124.0",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "en-US,es-CL;q=0.7,en;q=0.3",
    "Accept-Encoding": "gzip, deflate, br",
    "X-Requested-With": "XMLHttpRequest",
    "Connection": "keep-alive",
    "Referer": "https://www.superzoo.cl/perro/alimentos/alimentos-seco/acana-heritage-puppy-and-junior-formula-alimento-para-perro/2440_m.html",
    "Cookie": "dwanonymous_d0dc502116cb8dbe645f9cfd4de7a41c=abJO6BX3dDhWBOkJQ6Kc1S7xBK; _gcl_au=1.1.432189164.1711992849; _ga_F6KXZHLE3N=GS1.1.1712622773.10.1.1712622897.59.0.0; _ga=GA1.2.251015063.1711992850; _ga_NX6YD1WY8Q=GS1.2.1712622774.7.1.1712622897.60.0.0; _fbp=fb.1.1711992850744.1025892230; _gid=GA1.2.1783016410.1712531264; _gcl_aw=GCL.1712599357.CjwKCAiA_aGuBhACEiwAly57Ma3whRvQ74YJVrZD0wjsjqAGIgtA5PH7NaB5XB-MRKeBw9e6cplxsBoC_LkQAvD_BwE; _gac_UA-16091283-48=1.1712599357.CjwKCAiA_aGuBhACEiwAly57Ma3whRvQ74YJVrZD0wjsjqAGIgtA5PH7NaB5XB-MRKeBw9e6cplxsBoC_LkQAvD_BwE; sid=zzWTNYWgPr2fcXZ469kqO9oqxQmmxA0xW-Q; __cq_dnt=1; dw_dnt=1; dwsid=Q4Wea-dXYy5aSdwhBe76UVaayFfEM1Cintz7tPhwBg85nAxnKGZuMylzum0_LyrN3Ns9mcqZsGihgw3BMI5E4g==; _gat_UA-16091283-48=1",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "TE": "trailers"
}

skus2 = {"petdotu111":"4159"}

price_data=[]
for sku, product_id in skus.items():
    querystring = {"id": product_id}
    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    price = data['product']['price']
    # price_offer = data['product']['price']['sales']
    price_data.append({"SKU": sku, "Price": price})
    print(f"SKU: {sku}, Price: {price}")


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
values = [[item['SKU'], item['Price']] for item in price_data]
result = sheet.values().update(spreadsheetId=SPREADSHEET_ID,
							range='superzoo!A2:C83',#CAMBIAR
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