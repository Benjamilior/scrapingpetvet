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

#Google Sheets
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
KEY = '../key.json'
SPREADSHEET_ID = '1PrHE2FBeBhQnVYeCLQclLqj_tiIOq7z3JuMAG-2aAXg'
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


sku= {"petdotu1": "https://braloy.cl/revolution/7260-revolution-plus-gato-125-a-25-kg.html"} #CAMBIAR
sku= {"petdotu4": "https://braloy.cl/revolution/7259-revolution-plus-gato-25-a-5-kg.html", "petdotu5": "https://braloy.cl/revolution/7260-revolution-plus-gato-125-a-25-kg.html", "petdotu15": "https://braloy.cl/fit-formula/386-fit-formula-gato-10-kg.html", "petdotu16": "https://braloy.cl/fit-formula/541-fit-formula-senior-20-kg.html", "petdotu17": "https://braloy.cl/fit-formula/413-fit-formula-adulto-20-kg.html", "petdotu18": "https://braloy.cl/fit-formula/645-fit-formula-cachorros-10-kg.html", "petdotu19": "https://braloy.cl/fit-formula/429-fit-formula-adulto-raza-pequena-10-kg.html", "petdotu20": "https://braloy.cl/mascotas/7426-simparica-80-mg-20-a-40-kg-3-comprimidos.html", "petdotu21": "https://braloy.cl/mascotas/7426-simparica-80-mg-20-a-40-kg-3-comprimidos.html", "petdotu22": "https://braloy.cl/mascotas/7418-simparica-40-mg-10-a-20-kg-1-comprimido.html", "petdotu23": "https://braloy.cl/mascotas/7424-simparica-40-mg-10-a-20-kg-3-comprimidos.html", "petdotu24": "https://braloy.cl/mascotas/7423-simparica-20-mg-5-a-10-kg-3-comprimidos.html", "petdotu25": "https://braloy.cl/mascotas/7417-simparica-20-mg-5-a-10-kg-1-comprimido.html", "petdotu26": "https://braloy.cl/zoetis/603-rimadyl-100-mg-60-comprimidos.html", "petdotu27": "https://braloy.cl/zoetis/1452-rimadyl-100-mg-14-comprimidos.html", "petdotu28": "https://braloy.cl/bravecto/1035-bravecto-20-a-40-kg.html", "petdotu29": "https://braloy.cl/bravecto/316-bravecto-10-a-20-kg.html", "petdotu30": "https://braloy.cl/bravecto/619-bravecto-45-a-10-kg.html", "petdotu31": "https://braloy.cl/bravecto/1845-bravecto-gato-28-a-625-kg.html", "petdotu32": "https://braloy.cl/bravecto/727-bravecto-2-a-45-kg.html", "petdotu33": "https://braloy.cl/bravecto/1846-bravecto-gato-12-a-28-kg.html", "petdotu39": "https://braloy.cl/feliway/1465-feliway-classic-repuesto-48-ml.html", "petdotu40": "https://braloy.cl/feliway/1463-feliway-classic-spray-60-ml.html", "petdotu41": "https://braloy.cl/feliway/1469-feliway-friends-repuesto-48-ml.html", "petdotu42": "https://braloy.cl/feliway/1468-feliway-friends-difusor-repuesto-48-ml.html", "petdotu43": "https://braloy.cl/feliway/1468-feliway-friends-difusor-repuesto-48-ml.html", "petdotu44": "https://braloy.cl/royal-canin/987-royal-canin-mother-babycat-15-kg.html", "petdotu45": "https://braloy.cl/royal-canin/305-royal-canin-hipoalergenico-perros-medianos-y-grandes-2-kg.html", "petdotu46": "https://braloy.cl/royal-canin/723-royal-canin-mini-puppy-3-kg.html", "petdotu47": "https://braloy.cl/royal-canin/375-royal-canin-mini-adulto-25-kg.html", "petdotu48": "https://braloy.cl/bil-jac/626-bil-jac-adulto-136-kg.html", "petdotu49": "https://braloy.cl/bil-jac/334-bil-jac-adulto-small-27-kg.html", "petdotu50": "https://braloy.cl/bil-jac/464-bil-jac-puppy-136-kg.html", "petdotu51": "https://braloy.cl/brit-care/722-brit-care-senior-cordero-12-kg.html", "petdotu52": "https://braloy.cl/brit-care/750-brit-care-adulto-small-cordero-75-kg.html", "petdotu53": "https://braloy.cl/brit-care/531-brit-care-adulto-medium-cordero-12-kg.html", "petdotu54": "https://braloy.cl/brit-care/670-brit-care-puppy-cordero-12-kg.html", "petdotu55": "https://braloy.cl/brit-care/587-brit-care-sterilized-urinary-grain-free-7-kg.html", "petdotu56": "https://braloy.cl/brit-care/684-brit-care-weight-loss-12-kg.html", "petdotu57": "https://braloy.cl/brit-care/675-brit-care-adulto-salmon-12-kg.html", "petdotu58": "https://braloy.cl/brit-care/510-brit-care-junior-large-cordero-12-kg.html", "petdotu59": "https://braloy.cl/brit-care/732-brit-care-senior-light-salmon-12-kg.html", "petdotu62": "https://braloy.cl/oven-baked/2128-oven-baked-tradition-adulto-all-breeds-chicken-perro-1134-kg.html", "petdotu63": "https://braloy.cl/oven-baked/3224-oven-baked-tradition-adulto-all-breeds-fish-perro-1134-kg.html", "petdotu64": "https://braloy.cl/oven-baked/3234-oven-baked-tradition-senior-all-breeds-chicken-perro-1134-kg.html", "petdotu67": "https://braloy.cl/bayer/1722-nexgard-spectra-3-comprimidos-76-a-15-kg.html", "petdotu68": "https://braloy.cl/bayer/1445-nexgard-spectra-1-comprimido-76-a-15-kg.html", "petdotu69": "https://braloy.cl/bayer/1719-nexgard-spectra-3-comprimidos-15-a-30-kg.html", "petdotu70": "https://braloy.cl/bayer/1446-nexgard-spectra-1-comprimido-15-a-30-kg.html", "petdotu72": "https://braloy.cl/america-litter/2150-arena-america-litter-ultra-odor-seal-lavanda-15-kg.html", "petdotu77": "https://braloy.cl/brouwer/696-oxtrin-30-comprimidos.html", "petdotu80": "https://braloy.cl/odour-buster/345-arena-odour-buster-original-14-kg.html", "petdotu84": "https://braloy.cl/america-litter/1332-arena-america-litter-ultra-odor-seal-15-kg.html", "petdotu85": "https://braloy.cl/hills/1561-hills-metabolic-perro-control-de-peso-798-kg.html", "petdotu86": "https://braloy.cl/inicio/7624-wanpy-jerky-slices-lamb-100-grs.html", "petdotu88": "https://braloy.cl/hills/1977-hills-adulto-small-paws-204-kg.html", "petdotu93": "https://braloy.cl/adaptil/1459-adaptil-difusor-repuesto-48-ml.html", "petdotu96": "https://braloy.cl/adaptil/1461-adaptil-collar-pequeno.html", "petdotu97": "https://braloy.cl/adaptil/1462-adaptil-collar-mediano-y-grande.html", "petdotu99": "https://braloy.cl/hills/1558-hills-r-d-perro-reduccion-de-peso-798-kg.html"}

results = []

for sku_key, url in sku.items():
    driver.get(url)
    try:
        # nombresku = driver.find_element("xpath", '/html/body/main/section/div/div/div/section/div[1]/div[2]/h1') # Cambiar 
        precio = driver.find_element("xpath", '/html/body/main/section/div/div/section/div[2]/div[1]/div[2]/div[2]/div[2]/form/div[2]/div/div[2]/div/span[1]/span') # Cambiar
        data = {
            "SKU":sku_key,
            "Precio": precio.text,
              # Si deseas almacenar la URL junto con los datos
        }
        results.append(data)
        
        print(data)
    except Exception as e:
        print(f"Error en la URL {url} - {e}")

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
							range='braloy!F2',#CAMBIAR
							valueInputOption='USER_ENTERED',
							body={'values':values}).execute()


#Valores que se pasan a Sheets
values = [[item['SKU'], item['Precio']] for item in results]
result = sheet.values().update(spreadsheetId=SPREADSHEET_ID,
							range='braloy!A2:C83',#CAMBIAR
							valueInputOption='USER_ENTERED',
							body={'values':values}).execute()
print(f"Datos insertados correctamente")

