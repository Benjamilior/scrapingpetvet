
#No olvidarse del key.json
#Buscar todos los "Cambiar" antes de usar
#En chatgpt cruzar sku_dotu con links. Pedir que te haga el json desde el info del sheets
#No olvidarse del key.json
import json
import time
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd

import gspread
from oauth2client.service_account import ServiceAccountCredentials
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.oauth2 import service_account

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException

#Google Sheets
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
KEY = 'key.json'
SPREADSHEET_ID = '1PrHE2FBeBhQnVYeCLQclLqj_tiIOq7z3JuMAG-2aAXg' #Cambiar
creds = None
creds = service_account.Credentials.from_service_account_file(KEY, scopes=SCOPES)
service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()


# PATH = "C:\\Program Files (x86)\\chromedriver.exe"
PATH = "/usr/local/bin/chromedriver"
# Configurar las opciones de Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")  # Ver el Navegador
chrome_options.add_argument("--window-size=1920x1080")
start_time = time.time()  # Tiempo de inicio de la ejecución
driver = webdriver.Chrome(options=chrome_options)

results = []

sku = {
    "petdotu66": "https://www.tusmascotas.cl/product/laveta-taurina-50ml/",
    "petdotu164": "https://www.tusmascotas.cl/product/leonardo-adulto-duck-7-5kg/",
    "petdotu152": "https://www.tusmascotas.cl/product/leonardo-gato-adulto-light/",
    "petdotu151": "https://www.tusmascotas.cl/product/leonardo-adult-senior-1-8-kg/",
    "petdotu161": "https://www.tusmascotas.cl/product/adult-senior-75-kg-leonardo/",
    "petdotu162": "https://www.tusmascotas.cl/product/meloxivet-meloxicam-1-solucion-oral-60-ml/",
    "petdotu60": "https://www.tusmascotas.cl/product/mixantip-plus-50gr/",
    "petdotu75": "https://www.tusmascotas.cl/product/jarabe-naxpet-ketoprofeno-20ml/",
    "petdotu198": "https://www.tusmascotas.cl/product/naxpet-ketoprofeno-10mg-receta-requerida/",
    "petdotu70": "https://www.tusmascotas.cl/product/nexgard-spectra-151-30kg-1-comprimidos/",
    "petdotu69": "https://www.tusmascotas.cl/product/nexgard-spectra-151-30kg-3-comprimido/",
    "petdotu189": "https://www.tusmascotas.cl/product/nexgard-spectra-36-75kg-1-comprimido/",
    "petdotu172": "https://www.tusmascotas.cl/product/nexgard-spectra-36-75kg-3-comprimidos/",
    "petdotu147": "https://www.tusmascotas.cl/product/nexgard-spectra-301-60kg-1-comprimido/",
    "petdotu138": "https://www.tusmascotas.cl/product/nexgard-spectra-301-60kg-3-comprimidos/",
    "petdotu68": "https://www.tusmascotas.cl/product/nexgard-spectra-76-15kg-1-comprimido/",
    "petdotu67": "https://www.tusmascotas.cl/product/nexgard-spectra-76-15kg-3-comprimidos/",
    "petdotu165": "https://www.tusmascotas.cl/product/nutrience-original-cat-adulto-5kg/",
    "petdotu175": "https://www.tusmascotas.cl/product/nutrience-original-cat-indoor-5kg/",
    "petdotu157": "https://www.tusmascotas.cl/product/oftavet-solucion-oftalmica-5ml/",
    "petdotu94": "https://www.tusmascotas.cl/product/ohm-pastillas-calmantes/",
    "petdotu153": "https://www.tusmascotas.cl/product/orijen-cat-and-kitten-545-kg/",
    "petdotu114": "https://www.tusmascotas.cl/product/orijen-small-breed-perro-45-kg/",
    "petdotu131": "https://www.tusmascotas.cl/product/orijen-puppy-106-kg/",
    "petdotu77": "https://www.tusmascotas.cl/product/oxtrin-30-comprimidos/",
    "petdotu206": "https://www.tusmascotas.cl/product/papainpet-suplemento-30-comprimidos/",
    "petdotu195": "https://www.tusmascotas.cl/product/paz-pet-60ml/",
    "petdotu202": "https://www.tusmascotas.cl/product/shampoo-antiseptico-150ml-petever-forte/",
    "petdotu100": "https://www.tusmascotas.cl/product/virbac-phisio-anti-olor-orejas-100-ml/",
    "petdotu192": "https://www.tusmascotas.cl/product/pro-plan-sterilized-cat-75-kg/",
    "petdotu173": "https://www.tusmascotas.cl/product/proplan-urinary-cat-7-5kg/",
    "petdotu184": "https://www.tusmascotas.cl/product/pro-plan-perro-adulto-razas-pequenas-3-kg/",
    "petdotu8": "https://www.tusmascotas.cl/product/acana-heritage-puppy-junior-1135kg/",
    "petdotu179": "https://www.tusmascotas.cl/product/regepipel-plus-150ml/",
    "petdotu5": "https://www.tusmascotas.cl/product/revolution-plus-0-25ml/",
    "petdotu4": "https://www.tusmascotas.cl/product/revolution-plus-0-50ml/",
    "petdotu27": "https://www.tusmascotas.cl/product/rimadyl-carprofeno-100mg/",
    "petdotu207": "https://www.tusmascotas.cl/product/silimadrag-suspencion-120-ml/",
    "petdotu73": "https://www.tusmascotas.cl/product/silimarina-vitanimal-30-comprimidos/",
    "petdotu74": "https://www.tusmascotas.cl/product/silimarina-90-comprimidos/",
    "petdotu203": "https://www.tusmascotas.cl/product/simparica-trio-2-5-a-5-kg-1-comprimido/",
    "petdotu169": "https://www.tusmascotas.cl/product/simparica-antiparasitario-externo-3-comprimidos-5-kg-a-10-kg/",
    "petdotu25": "https://www.tusmascotas.cl/product/simparica-antiparasitario-externo-1-comprimido-51-kg-a-10-kg/",
    "petdotu24": "https://www.tusmascotas.cl/product/simparica-antiparasitario-externo-3-comprimidos-5-kg-a-10-kg/",
    "petdotu22": "https://www.tusmascotas.cl/product/simparica-antiparasitario-externo-1-comprimido-101-kg-a-20-kg/",
    "petdotu23": "https://www.tusmascotas.cl/product/simparica-antiparasitario-externo-3-comprimidos-10-kg-a-20-kg/",
    "petdotu21": "https://www.tusmascotas.cl/product/simparica-1-comprimidos/",
    "petdotu20": "https://www.tusmascotas.cl/product/simparica-antiparasitario-externo-3-comprimidos-20-kg-a-40-kg/",
    "petdotu163": "https://www.tusmascotas.cl/product/simparica-trio-20-a-40-kg-3-comprimidos/",
    "petdotu89": "https://www.tusmascotas.cl/product/sucravet-sucralfato-100ml/",
    "petdotu210": "https://www.tusmascotas.cl/product/superpet-omega-36-gato-125ml/",
    "petdotu79": "https://www.tusmascotas.cl/product/synulox-antibiotico-10-comprimidos-receta-requerida/",
    "petdotu108": "https://www.tusmascotas.cl/product/heel-traumeel-perros-y-gatos-100-tab/",
    "petdotu92": "https://www.tusmascotas.cl/product/ursovet-suspension-oral-60ml/",
    "petdotu166": "https://www.tusmascotas.cl/product/virbac-hpm-felino-hypoallergy-3kg/",
    "petdotu146": "https://www.tusmascotas.cl/product/virbac-hpm-felino-adult-neutered-7kg/",
    "petdotu118": "https://www.tusmascotas.cl/product/virbac-hpm-canino-allergy-12kg/",
    "petdotu137": "https://www.tusmascotas.cl/product/virbac-hpm-adult-weight-loss-control-12kg/",
    "petdotu128": "https://www.tusmascotas.cl/product/virbac-hpm-adult-weight-loss-diabetes-12kg/",
    "petdotu50": "https://www.tusmascotas.cl/product/bil-jac-puppy-dog-food-13-6kg/",
    "petdotu48": "https://www.tusmascotas.cl/product/bil-jac-select-dog-food-13-6kg/",
    "petdotu33": "https://www.tusmascotas.cl/product/bravecto-antiparasitario-externo-para-gatos-12-kg-a-28-kg/",
    "petdotu31": "https://www.tusmascotas.cl/product/bravecto-gatos-250mg-28-625kg/",
    "petdotu54": "https://www.tusmascotas.cl/product/brit-perro-puppy-cordero-y-arroz-12kg/",
    "petdotu34": "https://www.tusmascotas.cl/product/pipeta-calming-spot-on-gato/",
    "petdotu35": "https://www.tusmascotas.cl/product/calming-home-spray-125-ml/",
    "petdotu38": "https://www.tusmascotas.cl/product/calming-tabletas-de-beaphar-20-und-dog-cat/",
    "petdotu36": "https://www.tusmascotas.cl/product/calming-cat-treats-35gr/",
    "petdotu88": "https://www.tusmascotas.cl/product/hills-small-paws-adulto/",
    "petdotu45": "https://www.tusmascotas.cl/product/royal-canin-anallergenic-perro/",
    "petdotu47": "https://www.tusmascotas.cl/product/royal-canin-mini-adulto/",
    "petdotu46": "https://www.tusmascotas.cl/product/royal-canin-mini-puppy-3-kg/",
    "petdotu61": "https://www.tusmascotas.cl/product/mixantip-plus-15-g/",
    "petdotu44": "https://www.tusmascotas.cl/product/mother-and-babycat-3/",
    "petdotu80": "https://www.tusmascotas.cl/product/odour-buster-original-14kg-arena-santiaria-para-gatos/",
    "petdotu62": "https://www.tusmascotas.cl/product/oven-baked-tradition-adult-2/",
    "petdotu63": "https://www.tusmascotas.cl/product/oven-baked-tradition/",
    "petdotu90": "https://www.tusmascotas.cl/product/pacifor-gotas-10ml/",
    "petdotu86": "https://www.tusmascotas.cl/product/wanpy-lamb-jerky/",
    "petdotu222": "https://www.tusmascotas.cl/product/acana-heritage-light-fit-formula-11-35kg/",
    "petdotu600": "https://www.tusmascotas.cl/product/leonardo-adulto-grain-free-3"
}

results = []

for sku_key, url in sku.items():
    driver.get(url)
    precio_oferta = "No disponible"
    precio_normal = "No disponible"
    stock= "Con Stock"
    try:
        # Intenta obtener el precio de oferta
        precio_oferta_element = driver.find_element("xpath", '/html/body/div[1]/div[1]/div/div/div/div[2]/div[1]/div[2]/div/div/div[2]/div/p[1]/ins/span') #Cambiar
        precio_oferta = precio_oferta_element.text  # Guarda el precio de oferta
        stock_element= driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/div/div/div[2]/div[1]/div[2]/div/div/div[2]/div/p[2]")
        stock = stock_element.text
    except NoSuchElementException:
        pass  # Si no se encuentra el precio de oferta, se continuará con el siguiente bloque de código

    try:
        # Intenta obtener el precio normal
        precio_normal_element = driver.find_element("xpath", '/html/body/div[1]/div[1]/div/div/div/div[2]/div[1]/div[2]/div/div/div[2]/div/p[1]/del/span[2]') #Cambiar
        precio_normal = precio_normal_element.text  # Guarda el precio normal
        stock_element= driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/div/div/div[2]/div[1]/div[2]/div/div/div[2]/div/p[2]")
        stock = stock_element.text
    except NoSuchElementException:
        pass  # Si no se encuentra el precio normal, se continuará con el siguiente bloque de código

    if precio_oferta == "No disponible" and precio_normal == "No disponible":
        try:
            # Si no se puede encontrar ni el precio de oferta ni el precio normal, intenta con el tercer XPath
            precio_normal_element = driver.find_element("xpath", '/html/body/div[1]/div[1]/div/div/div/div[2]/div[1]/div[2]/div/div/div[2]/div/p[1]/span[2]') #Cambiar
            precio_normal = precio_normal_element.text  # Guarda el precio normal
            stock_element= driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/div/div/div[2]/div[1]/div[2]/div/div/div[2]/div/p[2]")
            stock = stock_element.text
        except NoSuchElementException as e:
            print(f"No se pudo encontrar el precio en la URL {url} - {e}")

    data = {
        "SKU": sku_key,
        "Precio": precio_normal,
        "Precio_oferta": precio_oferta,
        "Stock" :stock
    }
    results.append(data)
    print(data)
    time.sleep(0.5)
driver.quit()


df = pd.DataFrame(results)

# Guardar el DataFrame en un archivo Excel
# nombre_archivo = "datos_productos.xlsx"  # Nombre del archivo Excel
# df.to_excel(nombre_archivo, index=False)  # El parámetro index=False evita que se incluyan los índices en el archivo Excel
# print(f"Datos guardados en {nombre_archivo}")


end_time = time.time()  # Tiempo de finalización de la ejecución
execution_time = end_time - start_time
print("Tiempo de ejecución: %.2f segundos" % execution_time)

#Fecha de Extraccion
now = datetime.datetime.now()
now_str = now.strftime('%Y-%m-%d %H:%M:%S')
data = {"":now_str}
json_data = json.dumps(data)
values = [[json_data]]
result = sheet.values().update(spreadsheetId=SPREADSHEET_ID,
							range='tusmascotas!k2',#CAMBIAR
							valueInputOption='USER_ENTERED',
							body={'values':values}).execute()


#Valores que se pasan a Sheets
values = [[item['SKU'], item['Precio'],item['Precio_oferta']] for item in results]
result = sheet.values().update(spreadsheetId=SPREADSHEET_ID,
							range='tusmascotas!A2:E',#CAMBIAR
							valueInputOption='USER_ENTERED',
							body={'values':values}).execute()
print(f"Datos insertados correctamente")

#Valores que se pasan a Sheets
values = [[item['Stock']] for item in results]
result = sheet.values().update(spreadsheetId=SPREADSHEET_ID,
							range='tusmascotas!M2:N',#CAMBIAR
							valueInputOption='USER_ENTERED',
							body={'values':values}).execute()
print(f"Datos insertados correctamente")


df = pd.DataFrame(results)
print(df)
print(df.head)


competitor = "Tus Mascotas"  # Cambiar 
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
values = [[row['SKU'],competitor,row["Precio_oferta"], row['Precio'], now_str] for _, row in df.iterrows()]

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
values = [[row['SKU'], competitor, row['Precio_oferta'], row['Precio'], row["Stock"]] for _, row in df.iterrows()]

# Insertar los resultados en la nueva hoja después de la última fila
update_range = f'apipets!A{last_row}:E{last_row + len(values) - 1}' #Cambiar
result = sheet.values().update(
    spreadsheetId=NEW_SPREADSHEET_ID,
    range=update_range,
    valueInputOption='USER_ENTERED',
    body={'values': values}
).execute()
