
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
SPREADSHEET_ID = '1d_pPMYKjdHfxyP8qfblwDhrqlkyr_kK-rr2ps7kkmuQ' #Cambiar
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
    "petdotu194": "https://petcity.cl/tienda/acana-classic-wild-coast-2-kgs",
    "petdotu160": "https://petcity.cl/tienda/acana-free-run-poultry-perro-5-9-kgs",
    "petdotu135": "https://petcity.cl/tienda/advantage-gato-pipeta-4-8-kgs",
    "petdotu142": "https://petcity.cl/tienda/advantage-gato-pipeta-0-4-kgs",
    "petdotu115": "https://petcity.cl/tienda/advocate-cat-pipeta-0-8-ml-4-8-kg",
    "petdotu98": "https://petcity.cl/tienda/shampoo-med-allercalm-250ml",
    "petdotu125": "https://petcity.cl/tienda/arena-america-litter-clean-paws-odor-seal-15kg",
    "petdotu84": "https://petcity.cl/tienda/arena-america-litter-15-kgs",
    "petdotu72": "https://petcity.cl/tienda/arena-america-litter-odor-seal-lavanda-15kg",
    "petdotu132": "https://petcity.cl/tienda/belcando-finest-gf-senior/?attribute_pa_formato=12-5-kgs",
    "petdotu49": "https://petcity.cl/tienda/bil-jac-select-small-2-7-kgs",
    "petdotu181": "https://petcity.cl/tienda/bravecto-40-56-kg",
    "petdotu28": "https://petcity.cl/tienda/bravecto-20-40kg",
    "petdotu32": "https://petcity.cl/tienda/bravecto-2-4-5kg",
    "petdotu30": "https://petcity.cl/tienda/bravecto-4-5-10kg/",
    "petdotu29": "https://petcity.cl/tienda/bravecto-10-20kg",
    "petdotu148": "https://petcity.cl/tienda/bravecto-gato-2-8-a-6-25-kgs-250-mg/",
    "petdotu171": "https://petcity.cl/tienda/bravery-chicken-puppy-large-medium-breeds-12-kg/",
    "petdotu53": "https://petcity.cl/tienda/brit-care-adulto-medium-breed-lamb-rice-12-kgs/",
    "petdotu122": "https://petcity.cl/tienda/brit-care-adult-small-breed-lamb-rice-3-kgs/",
    "petdotu52": "https://petcity.cl/tienda/brit-care-adult-small-breed-lamb-rice-7-kgs/",
    "petdotu130": "https://petcity.cl/tienda/brit-care-cat-gf-haircare-helthy-shiny-coat-7-kgs",
    "petdotu127": "https://petcity.cl/tienda/brit-care-cat-gf-kitten-healthy-growth-development-2-kgs/",
    "petdotu134": "https://petcity.cl/tienda/brit-care-cat-gf-senior-weight-control-7-kgs/",
    "petdotu155": "https://petcity.cl/tienda/brit-care-cat-gf-sterilized-urinary-2-kgs/",
    "petdotu55": "https://petcity.cl/tienda/brit-care-cat-gf-sterilized-urinary-7-kgs",
    "petdotu110": "https://petcity.cl/tienda/brit-care-cat-gf-sterilized-weight-control-7-kgs/",
    "petdotu116": "https://petcity.cl/tienda/brit-care-gf-adult-large-breed-salmon-12-kgs/",
    "petdotu57": "https://petcity.cl/tienda/brit-care-gf-adult-salmon-12-kgs/",
    "petdotu133": "https://petcity.cl/tienda/brit-care-gf-adult-salmon-3-kgs/",
    "petdotu58": "https://petcity.cl/tienda/brit-care-gf-puppy-salmon-12-kgs/",
    "petdotu136": "https://petcity.cl/tienda/brit-care-gf-puppy-salmon-3-kgs/",
    "petdotu59": "https://petcity.cl/tienda/brit-care-gf-senior-light-salmon-12-kgs/",
    "petdotu139": "https://petcity.cl/tienda/brit-care-sensitive-venison-potato-12-kgs/",
    "petdotu106": "https://petcity.cl/tienda/brit-care-puppy-lamb-rice-12-kgs/",
    "petdotu113": "https://petcity.cl/tienda/brit-care-junior-large-lamb-rice-12-kgs/",
    "petdotu123": "https://petcity.cl/tienda/brit-care-gf-junior-large-breed-salmon-potato-12-kgs/",
    "petdotu51": "https://petcity.cl/tienda/brit-care-senior-lam-rice-12-kgs/",
    "petdotu56": "https://petcity.cl/tienda/brit-care-gf-weight-loss-rabbit-rice-12-kgs/",
    "petdotu140": "https://petcity.cl/tienda/brit-care-gf-weight-loss-rabbit-rice-3-kgs/",
    "petdotu37": "https://petcity.cl/tienda/calming-collar-gato/",
    "petdotu178": "https://petcity.cl/tienda/canigest-combi-16-ml/",
    "petdotu167": "https://petcity.cl/tienda/clindabone-165mg/",
    "petdotu83": "https://petcity.cl/tienda/condrovet-30-comprimidos/",
    "petdotu193": "https://petcity.cl/tienda/doguivit-senior-30-tabletas/",
    "petdotu143": "https://petcity.cl/tienda/drontal-dog-clinico-10-kgs-2-comp",
    "petdotu185": "https://petcity.cl/tienda/drontal-dog-clinico-35kg-1comp",
    "petdotu190": "https://petcity.cl/tienda/excellent-puppy-15-kgs/",
    "petdotu191": "https://petcity.cl/tienda/excellent-adulto-15-kgs/",
    "petdotu105": "https://petcity.cl/tienda/excellent-adulto-sensitive-15-kgs/",
    "petdotu19": "https://petcity.cl/tienda/fit-formula-perro-raza-pequena-10-kgs/",
    "petdotu18": "https://petcity.cl/tienda/fit-formula-cachorro-10-kgs",
    "petdotu17": "https://petcity.cl/tienda/fit-formula-adulto-20-kgs",
    "petdotu15": "https://petcity.cl/tienda/fit-formula-gato-adulto-10-kgs/",
    "petdotu126": "https://petcity.cl/tienda/fit-formula-senior-raza-pequena-10-kgs/",
    "petdotu16": "https://petcity.cl/tienda/fit-formula-senior-20-kgs/",
    "petdotu71": "https://petcity.cl/tienda/florafix-pet-oral-x-15grs/",
    "petdotu12": "https://petcity.cl/tienda/acana-free-run-poultry-perro-11-3-kgs/",
    "petdotu11": "https://petcity.cl/tienda/acana-freshwater-fish-perro-11-3-kgs/",
    "petdotu183": "https://petcity.cl/tienda/hills-canino-mature-sb-6-8-kgs/",
    "petdotu87": "https://petcity.cl/tienda/itraskin-120ml-susp-oral/",
    "petdotu65": "https://petcity.cl/tienda/laveta-carnitina-50ml/",
    "petdotu66": "https://petcity.cl/tienda/laveta-taurine-50ml/",
    "petdotu164": "https://petcity.cl/tienda/leonardo-adult-duck/?attribute_pa_formato=7-5-kgs",
    "petdotu152": "https://petcity.cl/tienda/leonardo-adult-light/?attribute_pa_formato=7-5-kgs",
    "petdotu151": "https://petcity.cl/tienda/leonardo-adult-senior/?attribute_pa_formato=2-kgs",
    "petdotu161": "https://petcity.cl/tienda/leonardo-adult-senior/?attribute_pa_formato=7-5-kgs",
    "petdotu13": "https://petcity.cl/tienda/fit-formula-adulto-light-20-kgs/",
    "petdotu162": "https://petcity.cl/tienda/meloxivet-60ml/",
    "petdotu70": "https://petcity.cl/tienda/nexgard-antiparasitario-15-1-30-kgs-3-comprimido/",
    "petdotu189": "https://petcity.cl/tienda/nexgard-spectra/?attribute_peso=3.6+-+7.5+Kg",
    "petdotu147": "https://petcity.cl/tienda/nexgard-spectra/?attribute_peso=30+-+60+Kg",
    "petdotu68": "https://petcity.cl/tienda/nexgard-spectra/?attribute_peso=7+-+15+Kg",
    "petdotu8": "https://petcity.cl/tienda/acana-puppy-junior-perro-11-3-kgs/",
    "petdotu179": "https://petcity.cl/tienda/shampoo-med-regepipel-plus-150-ml/",
    "petdotu5": "https://petcity.cl/tienda/revolution-plus-cat-1-25-2-5-kgs-0-25-ml/",
    "petdotu4": "https://petcity.cl/tienda/revolution-plus-cat-0-5-ml-2-5-5-kgs/",
    "petdotu27": "https://petcity.cl/tienda/rimadyl-14-comprimidos/?attribute_miligramos=100+Mg",
    "petdotu207": "https://petcity.cl/tienda/silimadrag-jarabe-120ml/",
    "petdotu203": "https://petcity.cl/tienda/simparica-10-mg-2-6-5-kg-1-comprimido/",
    "petdotu169": "https://petcity.cl/tienda/simparica-10-mg-2-6-5-kg-3-comprimidos/",
    "petdotu24": "https://petcity.cl/tienda/simparica-20-mg-5-1-10-k-x-3-comp/",
    "petdotu22": "https://petcity.cl/tienda/simparica-40mg-10-1-20k-x1-comp/",
    "petdotu23": "https://petcity.cl/tienda/simparica-40-mg-10-20-kg-x3-comp/",
    "petdotu21": "https://petcity.cl/tienda/simparica-80-mg-20-40-kg-1-comprimido",
    "petdotu89": "https://petcity.cl/tienda/sucravet-100-ml/",
    "petdotu210": "https://petcity.cl/tienda/superpet-omega-gatos-125-ml"
}
sku2 = {    "petdotu194": "https://petcity.cl/tienda/acana-classic-wild-coast-2-kgs"}
results = []

for sku_key, url in sku.items():
    driver.get(url)
    precio_oferta = "No disponible"
    precio_normal = "No disponible"
    stock= "Con Stock"
    try:
        # Intenta obtener el precio de oferta
        precio_oferta_element = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div/div/div[2]/div[1]/div[2]/div/div/div[2]/div/p[1]') #Cambiar
        precio_oferta = precio_oferta_element.text  # Guarda el precio de oferta
        stock_element= driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/div/div/div[2]/div[1]/div[2]/div/div/div[2]/div/p[2]")
        stock = stock_element.text
    except NoSuchElementException:
        pass  # Si no se encuentra el precio de oferta, se continuará con el siguiente bloque de código

    try:
        # Intenta obtener el precio normal
        precio_normal_element = driver.find_element("xpath", '/html/body/div[1]/div[1]/div/div/div/div[2]/div[1]/div[2]/div/div/div[2]/div/form/div/div[1]/div[2]/span/ins/span') #Cambiar
        precio_normal = precio_normal_element.text  # Guarda el precio normal
        stock_element= driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/div/div/div[2]/div[1]/div[2]/div/div/div[2]/div/p[2]")
        stock = stock_element.text
    except NoSuchElementException:
        pass  # Si no se encuentra el precio normal, se continuará con el siguiente bloque de código

    if precio_oferta == "No disponible" and precio_normal == "No disponible":
        try:
            # Si no se puede encontrar ni el precio de oferta ni el precio normal, intenta con el tercer XPath
            precio_normal_element = driver.find_element("xpath", '/html/body/div[1]/div[1]/div/div/div/div[2]/div[1]/div[2]/div/div/div[2]/div/p[1]') #Cambiar
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
							range='petcity!k2',#CAMBIAR
							valueInputOption='USER_ENTERED',
							body={'values':values}).execute()


#Valores que se pasan a Sheets
values = [[item['SKU'], item['Precio'],item['Precio_oferta']] for item in results]
result = sheet.values().update(spreadsheetId=SPREADSHEET_ID,
							range='petcity!A2:E',#CAMBIAR
							valueInputOption='USER_ENTERED',
							body={'values':values}).execute()
print(f"Datos insertados correctamente")

#Valores que se pasan a Sheets
values = [[item['Stock']] for item in results]
result = sheet.values().update(spreadsheetId=SPREADSHEET_ID,
							range='petcity!M2:N',#CAMBIAR
							valueInputOption='USER_ENTERED',
							body={'values':values}).execute()
print(f"Datos insertados correctamente")


df = pd.DataFrame(results)
print(df)
print(df.head)

# #Para Precio BBDD ----------------------------------------------------------------------------------------------------------------    
# competitor = "petcity"  # Cambiar 
# # Enviar datos a otro Google Sheets
# SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
# KEY = 'key.json'
# NEW_SPREADSHEET_ID = '1lLfl_jSGUEtitfsezo_zz53Bn2zAzID73VtxIi4dKRo'  # ID de la nueva hoja de cálculo

# creds = service_account.Credentials.from_service_account_file(KEY, scopes=SCOPES)
# service = build('sheets', 'v4', credentials=creds)
# sheet = service.spreadsheets()

# # Obtener la última fila con datos en la nueva hoja
# result = sheet.values().get(spreadsheetId=NEW_SPREADSHEET_ID, range='petvet!A:A').execute() #Cambiar donde llega la info
# values = result.get('values', [])
# last_row = len(values) + 1  # Obtener el índice de la última fila vacía

# # Convertir resultados a la lista de valores
# values = [[row['SKU'], "No disponible",competitor, row['Precio'], now_str] for _, row in df.iterrows()]

# # Insertar los resultados en la nueva hoja después de la última fila
# update_range = f'petvet!A{last_row}:E{last_row + len(values) - 1}' #Cambiar
# result = sheet.values().update(
#     spreadsheetId=NEW_SPREADSHEET_ID,
#     range=update_range,
#     valueInputOption='USER_ENTERED',
#     body={'values': values}
# ).execute()

# #Para Stock BBDD ----------------------------------------------------------------------------------------------------------------    
# print(f"Datos insertados correctamente en la nueva hoja de Google Sheets en el rango {update_range}")
# # Obtener la última fila con datos en la nueva hoja
# result = sheet.values().get(spreadsheetId=NEW_SPREADSHEET_ID, range='Stock!A:A').execute()  # Cambiar donde llega la info
# values = result.get('values', [])
# last_row = len(values) + 1  # Obtener el índice de la última fila vacía
# # Convertir resultados a la lista de valores
# values = [[now_str, competitor,row['SKU'], row['Stock']] for _, row in df.iterrows()]

# # Insertar los resultados en la nueva hoja después de la última fila
# print(values)
# update_range = f'Stock!A{last_row}:E{last_row + len(values) - 1}'  # Cambiar
# result = sheet.values().update(
#     spreadsheetId=NEW_SPREADSHEET_ID,
#     range=update_range,
#     valueInputOption='USER_ENTERED',
#     body={'values': values}
# ).execute()
