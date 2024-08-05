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
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException

import json
import datetime

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


sku2= {"petdotu1": "https://braloy.cl/revolution/7260-revolution-plus-gato-125-a-25-kg.html"} #CAMBIAR
sku= {
    "petdotu44": "https://braloy.cl/royal-canin/987-royal-canin-mother-babycat-15-kg.html",
    "petdotu45": "https://braloy.cl/royal-canin/305-royal-canin-hipoalergenico-perros-medianos-y-grandes-2-kg.html",
    "petdotu172": "https://braloy.cl/bayer/1721-nexgard-spectra-3-comprimidos-36-a-75-kg.html",
    "petdotu189": "https://braloy.cl/bayer/1718-nexgard-spectra-1-comprimido-36-a-75-kg.html",
    "petdotu68": "https://braloy.cl/bayer/1445-nexgard-spectra-1-comprimido-76-a-15-kg.html",
    "petdotu67": "https://braloy.cl/bayer/1722-nexgard-spectra-3-comprimidos-76-a-15-kg.html",
    "petdotu70": "https://braloy.cl/bayer/1446-nexgard-spectra-1-comprimido-15-a-30-kg.html",
    "petdotu69": "https://braloy.cl/bayer/1719-nexgard-spectra-3-comprimidos-15-a-30-kg.html",
    "petdotu138": "https://braloy.cl/bayer/1723-nexgard-spectra-3-comprimidos-30-a-60-kg.html",
    "petdotu147": "https://braloy.cl/bayer/1447-nexgard-spectra-1-comprimido-30-a-60-kg.html",
    "petdotu33": "https://braloy.cl/bravecto/1846-bravecto-plus-gato-12-a-28-kg.html",
    "petdotu31": "https://braloy.cl/bravecto/1845-bravecto-plus-gato-28-a-625-kg.html",
    "petdotu148": "https://braloy.cl/bravecto/1845-bravecto-plus-gato-28-a-625-kg.html",
    "petdotu32": "https://braloy.cl/bravecto/727-bravecto-2-a-45-kg.html",
    "petdotu30": "https://braloy.cl/bravecto/619-bravecto-45-a-10-kg.html",
    "petdotu29": "https://braloy.cl/bravecto/316-bravecto-10-a-20-kg.html",
    "petdotu28": "https://braloy.cl/bravecto/1035-bravecto-20-a-40-kg.html",
    "petdotu181": "https://braloy.cl/bravecto/850-bravecto-40-a-56-kg.html",
    "petdotu84": "https://braloy.cl/america-litter/1332-arena-america-litter-ultra-odor-seal-15-kg.html",
    "petdotu72": "https://braloy.cl/america-litter/2150-arena-america-litter-ultra-odor-seal-lavanda-15-kg.html",
    "petdotu27": "https://braloy.cl/zoetis/1452-rimadyl-100-mg-14-comprimidos.html",
    "petdotu26": "https://braloy.cl/zoetis/603-rimadyl-100-mg-60-comprimidos.html",
    "petdotu5": "https://braloy.cl/revolution/7260-revolution-plus-gato-125-a-25-kg.html",
    "petdotu4": "https://braloy.cl/revolution/7259-revolution-plus-gato-25-a-5-kg.html",
    "petdotu119": "https://braloy.cl/revolution/7259-revolution-plus-gato-25-a-5-kg.html",
    "petdotu48": "https://braloy.cl/bil-jac/626-bil-jac-adulto-136-kg.html",
    "petdotu99": "https://braloy.cl/hills/1558-hills-r-d-perro-reduccion-de-peso-798-kg.html",
    "petdotu183": "https://braloy.cl/hills/1505-hills-adulto-7-small-68-kg.html",
    "petdotu22": "https://braloy.cl/mascotas/7418-simparica-40-mg-10-a-20-kg-1-comprimido.html",
    "petdotu23": "https://braloy.cl/mascotas/7424-simparica-40-mg-10-a-20-kg-3-comprimidos.html",
    "petdotu24": "https://braloy.cl/mascotas/7423-simparica-20-mg-5-a-10-kg-3-comprimidos.html",
    "petdotu25": "https://braloy.cl/mascotas/7417-simparica-20-mg-5-a-10-kg-1-comprimido.html",
    "petdotu21": "https://braloy.cl/mascotas/7426-simparica-80-mg-20-a-40-kg-3-comprimidos.html",
    "petdotu20": "https://braloy.cl/mascotas/7426-simparica-80-mg-20-a-40-kg-3-comprimidos.html",
    "petdotu203": "https://braloy.cl/mascotas/7416-simparica-10-mg-25-a-5-kg-1-comprimido.html",
    "petdotu169": "https://braloy.cl/mascotas/7421-simparica-10-mg-25-a-5-kg-3-comprimidos.html",
    "petdotu163": "https://braloy.cl/mascotas/7434-simparica-trio-20-a-40-kg-3-comprimidos.html",
    "petdotu88": "https://braloy.cl/hills/1977-hills-adulto-small-paws-204-kg.html",
    "petdotu50": "https://braloy.cl/bil-jac/464-bil-jac-puppy-136-kg.html",
    "petdotu85": "https://braloy.cl/hills/1561-hills-metabolic-perro-control-de-peso-798-kg.html",
    "petdotu97": "https://braloy.cl/adaptil/1462-adaptil-collar-mediano-y-grande.html",
    "petdotu96": "https://braloy.cl/adaptil/1461-adaptil-collar-pequeno.html",
    "petdotu63": "https://braloy.cl/oven-baked/3224-oven-baked-tradition-adulto-all-breeds-fish-perro-1134-kg.html",
    "petdotu62": "https://braloy.cl/oven-baked/2128-oven-baked-tradition-adulto-all-breeds-chicken-perro-1134-kg.html",
    "petdotu64": "https://braloy.cl/oven-baked/3234-oven-baked-tradition-senior-all-breeds-chicken-perro-1134-kg.html",
    "petdotu78": "https://braloy.cl/inicio/7960-arena-traper-natural-4-kg.html",
    "petdotu18": "https://braloy.cl/fit-formula/645-fit-formula-cachorros-10-kg.html",
    "petdotu15": "https://braloy.cl/fit-formula/386-fit-formula-gato-10-kg.html",
    "petdotu93": "https://braloy.cl/adaptil/1459-adaptil-difusor-repuesto-48-ml.html",
    "petdotu42": "https://braloy.cl/feliway/1468-feliway-friends-difusor-repuesto-48-ml.html",
    "petdotu43": "https://braloy.cl/feliway/1468-feliway-friends-difusor-repuesto-48-ml.html",
    "petdotu40": "https://braloy.cl/feliway/1463-feliway-classic-spray-60-ml.html",
    "petdotu39": "https://braloy.cl/feliway/1465-feliway-classic-repuesto-48-ml.html",
    "petdotu49": "https://braloy.cl/bil-jac/334-bil-jac-adulto-small-27-kg.html",
    "petdotu77": "https://braloy.cl/brouwer/696-oxtrin-30-comprimidos.html",
    "petdotu41": "https://braloy.cl/feliway/1469-feliway-friends-repuesto-48-ml.html",
    "petdotu86": "https://braloy.cl/inicio/7624-wanpy-jerky-slices-lamb-100-grs.html",
    "petdotu17": "https://braloy.cl/fit-formula/413-fit-formula-adulto-20-kg.html",
    "petdotu16": "https://braloy.cl/fit-formula/541-fit-formula-senior-20-kg.html",
    "petdotu19": "https://braloy.cl/fit-formula/429-fit-formula-adulto-raza-pequena-10-kg.html",
    "petdotu126": "https://braloy.cl/fit-formula/884-fit-formula-senior-raza-pequena-10-kg.html",
    "petdotu109": "https://braloy.cl/josera/8140-josera-festival-125-kg.html",
    "petdotu120": "https://braloy.cl/josera/8047-josera-ente-kartoffel-125-kg.html",
    "petdotu117": "https://braloy.cl/josera/1107-josera-josidog-regular-18-kg.html",
    "petdotu124": "https://braloy.cl/josera/1106-josera-naturecat-10-kg.html",
    "petdotu156": "https://braloy.cl/josera/1655-josera-light-vital-15-kg.html",
    "petdotu141": "https://braloy.cl/josera/1658-josera-naturelle-10-kg.html",
    "petdotu144": "https://braloy.cl/josera/8139-josera-balance-125-kg.html",
    "petdotu209": "https://braloy.cl/josera/8144-josera-miniwell-10-kg.html",
    "petdotu151": "https://braloy.cl/inicio/2390-leonardo-senior-2-kg.html",
    "petdotu152": "https://braloy.cl/inicio/2385-leonardo-adulto-light-75-kg.html",
    "petdotu161": "https://braloy.cl/inicio/2391-leonardo-senior-75-kg.html",
    "petdotu164": "https://braloy.cl/inicio/2383-leonardo-adulto-duck-75-kg.html",
    "petdotu132": "https://braloy.cl/inicio/2407-belcando-finest-grain-free-senior-125-kg.html",
    "petdotu170": "https://braloy.cl/inicio/2398-belcando-finest-light-125-kg.html",
    "petdotu125": "https://braloy.cl/america-litter/7329-arena-america-litter-clean-paws-15-kg.html",
    "petdotu105": "https://braloy.cl/inicio/8272-excellent-adulto-skin-care-15-kg.html",
    "petdotu142": "https://braloy.cl/bayer/1432-advantage-gato-hasta-4-kg.html",
    "petdotu135": "https://braloy.cl/bayer/1433-advantage-gato-4-a-8-kg.html",
    "petdotu143": "https://braloy.cl/bayer/1456-drontal-plus-perro-2-comprimidos-10-kg.html",
    "petdotu185": "https://braloy.cl/bayer/1457-drontal-plus-perro-1-comprimido-35-kg.html",
    "petdotu188": "https://braloy.cl/bayer/1454-drontal-gatos-1-comprimido.html",
    "petdotu150": "https://braloy.cl/inicio/7875-osteodrag-ha-30-comprimidos.html",
    "petdotu177": "https://braloy.cl/bayer/3042-advocate-perro-10-a-25-kg.html",
    "petdotu196": "https://braloy.cl/bayer/3043-advocate-perro-25-a-40-kg.html",
    "petdotu199": "https://braloy.cl/bayer/3041-advocate-perro-4-a-10-kg.html",
    "petdotu149": "https://braloy.cl/mascotas/3044-advocate-gatos-hasta-4-kg.html",
    "petdotu115": "https://braloy.cl/mascotas/3045-advocate-gatos-4-a-8-kg.html",
    "petdotu165": "https://braloy.cl/nutrience/846-nutrience-original-gato-adulto-5-kg.html",
    "petdotu171": "https://braloy.cl/mascotas/1623-bravery-adulto-medium-y-large-pollo-12-kg.html",
    "petdotu173": "https://braloy.cl/inicio/8247-pro-plan-gato-urinary-75-kg.html",
    "petdotu175": "https://braloy.cl/nutrience/851-nutrience-original-gato-indoor-hairball-5-kg.html",
    "petdotu180": "https://braloy.cl/inicio/8218-pro-plan-puppy-razas-medianas-15-kg.html",
    "petdotu187": "https://braloy.cl/inicio/8246-pro-plan-gato-urinary-3-kg.html",
    "petdotu190": "https://braloy.cl/inicio/8270-excellent-puppy-razas-medianas-y-grandes-15-kg.html",
    "petdotu192": "https://braloy.cl/inicio/8245-pro-plan-gato-sterilized-75-kg.html",
    "petdotu193": "https://braloy.cl/inicio/7909-doguivit-senior-30-comprimidos.html",
    "petdotu195": "https://braloy.cl/inicio/7877-paz-pet-60-ml.html",
    "petdotu201": "https://braloy.cl/inicio/7881-senilpet-cerebral-5.html",
    "petdotu205": "https://braloy.cl/adaptil/1460-adaptil-repuesto-48-ml.html",
    "petdotu206": "https://braloy.cl/inicio/7876-papainpet-30-comprimidos.html",
    "petdotu210": "https://braloy.cl/drag-pharma/1704-superpet-omega-3-y-6-gato-125-ml.html",
    "petdotu80": "https://braloy.cl/odour-buster/345-arena-odour-buster-original-14-kg.html",
    "petdotu46": "https://braloy.cl/royal-canin/723-royal-canin-mini-puppy-3-kg.html",
    "petdotu47": "https://braloy.cl/royal-canin/375-royal-canin-mini-adulto-25-kg.html",
    "petdotu184": "https://braloy.cl/inicio/8222-pro-plan-adulto-razas-pequenas-3-kg.html",
    "petdotu13":"https://braloy.cl/fit-formula/1661-fit-formula-light-20-kg.html"
}

results = []

for sku_key, url in sku.items():
    driver.get(url)
    precio_oferta = "No disponible"
    precio_normal = "No disponible"
    stock   = "Con Stock"
    
    time.sleep(3)
    
    try:
        # Intenta obtener el precio de oferta
        precio_oferta_element = driver.find_element("xpath", '/html/body/main/section/div/div/section/div[2]/div[1]/div[2]/div[2]/div[2]/form/div[2]/div/div[2]/div/span[1]/span') #Cambiar
        precio_oferta = precio_oferta_element.text  # Guarda el precio de oferta
        stock_element= driver.find_element(By.CSS_SELECTOR,"#product-availability")
        stock = stock_element.text
    except NoSuchElementException:
        pass  # Si no se encuentra el precio de oferta, se continuará con el siguiente bloque de código

    try:
        # Intenta obtener el precio normal
        precio_oferta_element = driver.find_element("xpath", '/html/body/main/section/div/div/section/div[2]/div[1]/div[2]/div[2]/div[2]/form/div[2]/div/div[2]/div/span[1]/span') #Cambiar
        precio_oferta = precio_oferta_element.text  # Guarda el precio de oferta
        stock_element= driver.find_element(By.CSS_SELECTOR,"#product-availability")
        stock = stock_element.text
    except NoSuchElementException:
        pass  # Si no se encuentra el precio normal, se continuará con el siguiente bloque de código

    if precio_oferta == "No disponible" and precio_normal == "No disponible":
        try:
            # Si no se puede encontrar ni el precio de oferta ni el precio normal, intenta con el tercer XPath
            precio_oferta_element = driver.find_element("xpath", '/html/body/main/section/div/div/section/div[2]/div[1]/div[2]/div[2]/div[2]/form/div[2]/div/div[2]/div/span[1]/span') #Cambiar
            precio_oferta = precio_oferta_element.text  # Guarda el precio de oferta
            stock_element= driver.find_element(By.CSS_SELECTOR,"#product-availability")
            stock = stock_element.text
           
        except NoSuchElementException as e:
            print(f"No se pudo encontrar el precio en la URL {url} - {e}")
            
    # Limpiar los textos de precios
    precio_normal = precio_normal.replace("Precio Lista:", "").strip()
    precio_oferta = precio_oferta.replace("Precio Oferta:", "").strip()

    data = {
        "SKU": sku_key,
        "Precio": precio_normal,
        "Precio_oferta": precio_oferta,
        "Stock" :stock
    }
    results.append(data)
    print(data)
   
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
values = [[item['SKU'], item['Precio'],item['Precio_oferta']] for item in results]
result = sheet.values().update(spreadsheetId=SPREADSHEET_ID,
							range='braloy!A2:C',#CAMBIAR
							valueInputOption='USER_ENTERED',
							body={'values':values}).execute()
print(f"Datos insertados correctamente")

#Valores que se pasan a Sheets
values = [[item['Stock']] for item in results]
result = sheet.values().update(spreadsheetId=SPREADSHEET_ID,
							range='braloy!M2:N',#CAMBIAR
							valueInputOption='USER_ENTERED',
							body={'values':values}).execute()
print(f"Datos insertados correctamente")
df = pd.DataFrame(results)
print(df)
print(df.head)

competitor = "Braloy"  # Cambiar 
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
values = [[row['SKU'], "No Disponible",competitor, row['Precio'], now_str] for _, row in df.iterrows()]

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
