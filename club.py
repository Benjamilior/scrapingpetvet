
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
    "petdotu97": "https://www.clubdeperrosygatos.cl/shop/salud-y-bienestar/farmacia-perros-y-gatos/adaptil-collar-perros-reductor-estres-s-m/",
    "petdotu96": "https://www.clubdeperrosygatos.cl/shop/salud-y-bienestar/farmacia-perros-y-gatos/adaptil-collar-perros-reductor-estres-s-m/",
    "petdotu9": "https://www.clubdeperrosygatos.cl/shop/alimento/alimento-para-gatos/acana-para-gatos/comecan-acana-bountiful-catch-cat-4-5-kg/",
    "petdotu82": "https://www.clubdeperrosygatos.cl/shop/salud-y-bienestar/farmacia-perros-y-gatos/artri-tabs-para-articulaciones-60-comprimidos/",
    "petdotu93": "https://www.clubdeperrosygatos.cl/shop/salud-y-bienestar/farmacia-perros-y-gatos/adaptil-reductor-estres-difusor-repuesto-48-ml/",
    "petdotu42": "https://www.clubdeperrosygatos.cl/shop/salud-y-bienestar/entrenamiento-salud-y-bienestar/feliway-difusor-repuesto-feromonas-48-ml/",
    "petdotu43": "https://www.clubdeperrosygatos.cl/shop/salud-y-bienestar/farmacia-perros-y-gatos/feliway-friends-difusor-repuesto-feromonas-48-ml-2/",
    "petdotu4": "https://www.clubdeperrosygatos.cl/shop/salud-y-bienestar/control-parasitario/pipeta-revolution-gatos-plus-2-5-5-kg/",
    "petdotu5": "https://www.clubdeperrosygatos.cl/shop/salud-y-bienestar/control-parasitario/pipeta-revolution-gatos-plus-1-25-2-5-kg/",
    "petdotu66": "https://www.clubdeperrosygatos.cl/shop/salud-y-bienestar/farmacia-perros-y-gatos/laveta-taurina-50ml/",
    "petdotu65": "https://www.clubdeperrosygatos.cl/shop/salud-y-bienestar/farmacia-perros-y-gatos/laveta-carnitina-50ml/",
    "petdotu40": "https://www.clubdeperrosygatos.cl/shop/salud-y-bienestar/anti-estres-y-relajacion/feliway-spray-60ml/",
    "petdotu39": "https://www.clubdeperrosygatos.cl/shop/salud-y-bienestar/entrenamiento-salud-y-bienestar/feliway-difusor-repuesto-feromonas-48-ml-2/",
    "petdotu47": "https://www.clubdeperrosygatos.cl/shop/alimento/alimento-para-perros/royal-canin/royal-canin-mini-adult-8-3kg/",
    "petdotu83": "https://www.clubdeperrosygatos.cl/shop/salud-y-bienestar/farmacia-perros-y-gatos/condrovet-de-30-comprimidos/",
    "petdotu84": "https://www.clubdeperrosygatos.cl/shop/regalos/cat-lovers/america-litter-ultra-odor-seal/",
    "petdotu77": "https://www.clubdeperrosygatos.cl/shop/salud-y-bienestar/farmacia-perros-y-gatos/oxtrin-30-comprimidos/",
    "petdotu98": "https://www.clubdeperrosygatos.cl/shop/salud-y-bienestar/higiene-y-belleza/virbac-shampo-medicado-250ml-allercalm-avena/",
    "petdotu10": "https://www.clubdeperrosygatos.cl/shop/alimento/alimento-para-gatos/acana-para-gatos/comecan-acana-first-feast-cat-1-8-kg/",
    "petdotu41": "https://www.clubdeperrosygatos.cl/shop/salud-y-bienestar/farmacia-perros-y-gatos/feliway-friends-difusor-repuesto-feromonas-48-ml/",
    "petdotu34": "https://www.clubdeperrosygatos.cl/shop/salud-y-bienestar/farmacia-perros-y-gatos/calming-spot-on-gatos/",
    "petdotu86": "https://www.clubdeperrosygatos.cl/shop/alimento/snacks-perros-y-gatos/snacks-para-perros/masticables-perro/wanpy-beef-jerky/",
    "petdotu27": "https://www.clubdeperrosygatos.cl/shop/salud-y-bienestar/farmacia-perros-y-gatos/farmacia-con-receta/rimadyl-anti-inflamatorio-14-comprimidos/",
    "petdotu18": "https://www.clubdeperrosygatos.cl/shop/alimento/alimento-para-perros/fit-formula-para-perros/fit-formula-alimento-perro-cachorro/",
    "petdotu44": "https://www.clubdeperrosygatos.cl/shop/alimento/alimento-para-gatos/royal-canin-para-gatos/royal-canin-mother-babycat-1-5-kg/",
    "petdotu36": "https://www.clubdeperrosygatos.cl/shop/alimento/snacks-perros-y-gatos/snacks-para-gatos/masticables-gato/beaphar-calming-cat-treats/",
    "petdotu94": "https://www.clubdeperrosygatos.cl/shop/salud-y-bienestar/anti-estres-y-relajacion/holliday-ohm-modulador-de-ansiedad/",
    "petdotu81": "https://www.clubdeperrosygatos.cl/shop/salud-y-bienestar/farmacia-perros-y-gatos/vetarom-calmer-efecto-ansiolitico-natural/",
    "petdotu72": "https://www.clubdeperrosygatos.cl/shop/salud-y-bienestar/arenas-sanitarias/arena-america-litter-lavanda-15-kg/",
    "petdotu15": "https://www.clubdeperrosygatos.cl/shop/alimento/alimento-para-gatos/fit-formula/fit-formula-alimento-gato-adulto/",
    "petdotu89": "https://www.clubdeperrosygatos.cl/shop/salud-y-bienestar/farmacia-perros-y-gatos/farmacia-con-receta/sucravet-antiacido-100-ml/",
    "petdotu37": "https://www.clubdeperrosygatos.cl/shop/salud-y-bienestar/anti-estres-y-relajacion/calming-collar-gato/",
    "petdotu16": "https://www.clubdeperrosygatos.cl/shop/alimento/alimento-para-perros/fit-formula-para-perros/fit-formula-alimento-perro-senior-20-kg/",
    "petdotu79": "https://www.clubdeperrosygatos.cl/shop/salud-y-bienestar/farmacia-perros-y-gatos/farmacia-con-receta/synulox-200-mg-amox-50-mg-ac-clv-10-comp/",
    "petdotu92": "https://www.clubdeperrosygatos.cl/shop/salud-y-bienestar/farmacia-perros-y-gatos/farmacia-con-receta/ursovet-susp-oral-60-ml/",
    "petdotu17": "https://www.clubdeperrosygatos.cl/shop/alimento/alimento-para-perros/fit-formula-para-perros/fit-formula-alimento-perro-adulto-20-kg/",
    "petdotu38": "https://www.clubdeperrosygatos.cl/shop/salud-y-bienestar/farmacia-perros-y-gatos/calming-tablets-20-comp/",
    "petdotu71": "https://www.clubdeperrosygatos.cl/shop/salud-y-bienestar/farmacia-perros-y-gatos/flora-fix-pet/",
    "petdotu75": "https://www.clubdeperrosygatos.cl/shop/salud-y-bienestar/farmacia-perros-y-gatos/naxpet-suspension-oral-20ml/",
    "petdotu26": "https://www.clubdeperrosygatos.cl/shop/salud-y-bienestar/farmacia-perros-y-gatos/farmacia-con-receta/rimadyl-anti-inflamatorio-60-comprimidos/",
    "petdotu87": "https://www.clubdeperrosygatos.cl/shop/salud-y-bienestar/farmacia-perros-y-gatos/farmacia-con-receta/itraskin-2-susp-oral-120-ml/",
    "petdotu91": "https://www.clubdeperrosygatos.cl/shop/salud-y-bienestar/farmacia-perros-y-gatos/farmacia-con-receta/dermisolona-susp-oral-0-4-x-30ml/",
    "petdotu95": "https://www.clubdeperrosygatos.cl/shop/salud-y-bienestar/farmacia-perros-y-gatos/farmacia-con-receta/dermisolona-20-mg-10-comprimidos/",
    "petdotu100": "https://www.clubdeperrosygatos.cl/shop/salud-y-bienestar/farmacia-perros-y-gatos/virbac-phisio-anti-olor-para-orejas-100ml/"
}

sku2 = { "petdotu4": "https://www.clubdeperrosygatos.cl/shop/salud-y-bienestar/farmacia-perros-y-gatos/artri-tabs-para-articulaciones-60-comprimidos/"}
results = []

for sku_key, url in sku.items():
    driver.get(url)
    precio_oferta = "No disponible"
    precio_normal = "No disponible"
    time.sleep(3)
    try:
        # Intenta obtener el precio de oferta
        precio_oferta_element = driver.find_element("xpath", '/html/body/div[1]/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div/div[2]/div/p/del/span') #Cambiar
        precio_oferta = precio_oferta_element.text  # Guarda el precio de oferta
    except NoSuchElementException:
        pass  # Si no se encuentra el precio de oferta, se continuará con el siguiente bloque de código

    try:
        # Intenta obtener el precio normal
        precio_normal_element = driver.find_element("xpath", '/html/body/div[1]/div[1]/div/div/div/div[2]/div[1]/div[2]/div/div/div[2]/div/p[1]/ins/span') #Cambiar
        precio_normal = precio_normal_element.text  # Guarda el precio normal
    except NoSuchElementException:
        pass  # Si no se encuentra el precio normal, se continuará con el siguiente bloque de código

    if precio_oferta == "No disponible" and precio_normal == "No disponible":
        try:
            # Si no se puede encontrar ni el precio de oferta ni el precio normal, intenta con el tercer XPath
            precio_normal_element = driver.find_element("xpath", '/html/body/div[3]/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div/div[2]/div/p') #Cambiar
            precio_normal = precio_normal_element.text  # Guarda el precio normal
        except NoSuchElementException as e:
            print(f"No se pudo encontrar el precio en la URL {url} - {e}")

    data = {
        "SKU": sku_key,
        "Precio": precio_normal,
        "Precio_oferta": precio_oferta
    }
    results.append(data)
    print(data)
    time.sleep(0.5)
driver.quit()


df = pd.DataFrame(results)

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
							range='club!k2',#CAMBIAR
							valueInputOption='USER_ENTERED',
							body={'values':values}).execute()


#Valores que se pasan a Sheets
values = [[item['SKU'], item['Precio'],item['Precio_oferta']] for item in results]
result = sheet.values().update(spreadsheetId=SPREADSHEET_ID,
							range='club!A2:C',#CAMBIAR
							valueInputOption='USER_ENTERED',
							body={'values':values}).execute()
print(f"Datos insertados correctamente")

df = pd.DataFrame(results)
print(df)
print(df.head)


competitor = "Club"  # Cambiar 
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
values = [[row['SKU'], "No disponible",competitor, row['Precio'], now_str] for _, row in df.iterrows()]

# Insertar los resultados en la nueva hoja después de la última fila
update_range = f'petvet!A{last_row}:E{last_row + len(values) - 1}' #Cambiar
result = sheet.values().update(
    spreadsheetId=NEW_SPREADSHEET_ID,
    range=update_range,
    valueInputOption='USER_ENTERED',
    body={'values': values}
).execute()

print(f"Datos insertados correctamente en la nueva hoja de Google Sheets en el rango {update_range}")