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
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException

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

sku = {
    "petdotu10": "https://www.amigales.cl/acana-first-feas-gatitos.html",
    "petdotu15": "https://www.amigales.cl/fit-formula-gato-adulto-10kg.html",
    "petdotu16": "https://www.amigales.cl/fit-formula-perro-senior.html",
    "petdotu17": "https://www.amigales.cl/fit-formula-perro-adulto-20kg.html",
    "petdotu18": "https://www.amigales.cl/fit-formula-cachorro-10kg.html",
    "petdotu27": "https://www.amigales.cl/rimadyl-anti-inflamatorio-100-mg.html",
    "petdotu32": "https://www.amigales.cl/bravecto-perros.html",
    "petdotu34": "https://www.amigales.cl/beaphar-calmingspot-gatos.html",
    "petdotu36": "https://www.amigales.cl/snacks-calmantes-gatos.html",
    "petdotu37": "https://www.amigales.cl/collar-calmante-gatos.html",
    "petdotu38": "https://www.amigales.cl/tabletas-calmantes-beaphar.html",
    "petdotu39": "https://www.amigales.cl/feliway-classic-repuesto.html",
    "petdotu40": "https://www.amigales.cl/feliway-classic-spray.html",
    "petdotu41": "https://www.amigales.cl/feliway-friends-repuesto.html",
    "petdotu42": "https://www.amigales.cl/feliway-classic-difusor-repuesto.html",
    "petdotu43": "https://www.amigales.cl/feliway-friends-difusor-repuesto.html",
    "petdotu44": "https://www.amigales.cl/royal-canin-mother-baby-cat-1-5kg.html",
    "petdotu45": "https://www.amigales.cl/royal-canin-hypoallergenic-perros-razas-pequenas.html",
    "petdotu47": "https://www.amigales.cl/royal-canin-mini-perro-adulto.html",
    "petdotu49": "https://www.amigales.cl/bil-jac-small-breed-para-perros.html",
    "petdotu61": "https://www.amigales.cl/catalog/product/view/id/5199/s/mixantip-plus-crema/category/2/",
    "petdotu62": "https://www.amigales.cl/oven-baked-pollo-perros-11-34-kg.html",
    "petdotu63": "https://www.amigales.cl/oven-baked-pescado-perros-11-34-kg.html",
    "petdotu64": "https://www.amigales.cl/oven-baked-pollo-perros-senior-11-34-kg.html",
    "petdotu65": "https://www.amigales.cl/beaphar-laveta-carnitina.html",
    "petdotu66": "https://www.amigales.cl/beaphar-laveta-taurina.html",
    "petdotu68": "https://www.amigales.cl/nexgard-spectra-antiparasitario-1-tableta.html",
    "petdotu70": "https://www.amigales.cl/nexgard-spectra-antiparasitario-1-tableta.html",
    "petdotu71": "https://www.amigales.cl/florafix-15g.html",
    "petdotu74": "https://www.amigales.cl/silimavet-silimarina-vitanimal.html",
    "petdotu75": "https://www.amigales.cl/naxpet-solucion-oral.html",
    "petdotu77": "https://www.amigales.cl/oxtrin.html",
    "petdotu79": "https://www.amigales.cl/synulox-250mg.html",
    "petdotu81": "https://www.amigales.cl/calmer-calma.html",
    "petdotu82": "https://www.amigales.cl/artri-tabs-60-tabletas.html",
    "petdotu83": "https://www.amigales.cl/condrovet-30-comprimidos.html",
    "petdotu85": "https://www.amigales.cl/hills-metabolic-perros.html",
    "petdotu86": "https://www.amigales.cl/wanpy-jerky-cordero.html",
    "petdotu87": "https://www.amigales.cl/itraskin-suspension-oral.html",
    "petdotu88": "https://www.amigales.cl/hills-small-paws-cachorros.html",
    "petdotu89": "https://www.amigales.cl/sucravet.html",
    "petdotu91": "https://www.amigales.cl/dermisolona-30-ml-solucion-oral.html",
    "petdotu92": "https://www.amigales.cl/ursovet-drag-pharma.html",
    "petdotu93": "https://www.amigales.cl/adaptil-difusor-repuesto.html",
    "petdotu94": "https://www.amigales.cl/ohm-comprimidos-calmantes-perros-gatos.html",
    "petdotu95": "https://www.amigales.cl/dermisolona-20mg-10-comprimidos.html",
    "petdotu96": "https://www.amigales.cl/collar-adaptil.html",
    "petdotu97": "https://www.amigales.cl/collar-adaptil.html",
    "petdotu98": "https://www.amigales.cl/virbac-allercalm-shampoo.html",
    "petdotu100": "https://www.amigales.cl/phisio-anti-olor-auricular.html",
    "petdotu13":"https://www.amigales.cl/fit-formula-perro-adulto-light-20kg.html"
}
sku2 = {"petdotu5": "https://www.amigales.cl/revolution-plus-antiparasitario-gatos.html"}


results = []

for sku_key, url in sku.items():
    driver.get(url)
    precio_oferta = "No disponible"
    precio_normal = "No disponible"
    try:
        # Intenta obtener el precio de oferta
        precio_oferta_element = driver.find_element_by_class_name("product-info-price2") #Cambiar
        precio_oferta = precio_oferta_element.text  # Guarda el precio de oferta
    except NoSuchElementException:
        pass  # Si no se encuentra el precio de oferta, se continuará con el siguiente bloque de código

    try:
        # Intenta obtener el precio normal
        precio_normal_element = driver.find_element("xpath", '/html/body/div[2]/main/div[3]/div/div[1]/div[4]/div[1]') #Cambiar
        precio_normal = precio_normal_element.text  # Guarda el precio normal
    except NoSuchElementException:
        pass  # Si no se encuentra el precio normal, se continuará con el siguiente bloque de código

    if precio_oferta == "No disponible" and precio_normal == "No disponible":
        try:
            # Si no se puede encontrar ni el precio de oferta ni el precio normal, intenta con el tercer XPath
            precio_normal_element = driver.find_element("xpath", '/html/body/div[2]/main/div[3]/div/div[1]/div[4]/div[1]/span[2]') #Cambiar
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

print(results)
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
							range='amigales!K2',#CAMBIAR
							valueInputOption='USER_ENTERED',
							body={'values':values}).execute()


#Valores que se pasan a Sheets
values = [[item['SKU'], item['Precio'], item['Precio_oferta']] for item in results]
result = sheet.values().update(spreadsheetId=SPREADSHEET_ID,
							range='amigales!A2:C',#CAMBIAR
							valueInputOption='USER_ENTERED',
							body={'values':values}).execute()
print(f"Datos insertados correctamente")

df = pd.DataFrame(results)
print(df)
print(df.head)

competitor = "Amigales"  # Cambiar 
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
values = [[row['SKU'], competitor, row['Precio'], row['Precio_oferta'], now_str] for _, row in df.iterrows()]

# Insertar los resultados en la nueva hoja después de la última fila
update_range = f'petvet!A{last_row}:E{last_row + len(values) - 1}' #Cambiar
result = sheet.values().update(
    spreadsheetId=NEW_SPREADSHEET_ID,
    range=update_range,
    valueInputOption='USER_ENTERED',
    body={'values': values}
).execute()

print(f"Datos insertados correctamente en la nueva hoja de Google Sheets en el rango {update_range}")