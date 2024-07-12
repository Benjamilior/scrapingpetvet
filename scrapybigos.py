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



#Ejecutador del Codigo

# PATH = "C:\\Program Files (x86)\\chromedriver.exe"
PATH = "/usr/local/bin/chromedriver"
# Configurar las opciones de Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")  # Ver el Navegador
chrome_options.add_argument("--window-size=1920x1080")

start_time = time.time()  # Tiempo de inicio de la ejecución

driver = webdriver.Chrome(options=chrome_options)

# #URLs
sku = {
    "petdotu1": "https://www.bigos.cl/farmacia-mascotas/7921-apoquel-16-mgs-20-tabletas-5414736044217.html",
    "petdotu2": "https://www.bigos.cl/farmacia-mascotas/7920-apoquel-36-mgs-20-tabletas-5414736044194.html",
    "petdotu3": "https://www.bigos.cl/farmacia-mascotas/7341-apoquel-54-mgs-20-tabletas-5414736044200.html",
    "petdotu197": "https://www.bigos.cl/alimentos-para-gatos/acana-indoor-entree-para-gatos",
    "petdotu194": "https://www.bigos.cl/alimentos-para-perros/acana-wild-coast-para-perros#/504-tamano-2_kg_bolsa",
    "petdotu176": "https://www.bigos.cl/alimentos-para-gatos/acana-wild-atlantic-para-gatos",
    "petdotu12": "https://www.bigos.cl/alimentos-para-perros/4496-46-acana-free-run-poultry-para-perros.html#/506-tamano-113_kg_saco",
    "petdotu8": "https://www.bigos.cl/alimentos-para-perros/4500-31-acana-puppy-and-junior-para-cachorros.html#/506-tamano-113_kg_saco",
    "petdotu6": "https://www.bigos.cl/alimentos-para-perros/acana-prairie-poultry-para-perros#/537-tamano-97_kg_saco",
    "petdotu9": "https://www.bigos.cl/alimentos-para-gatos/6845-acana-bountiful-catch-para-gatos.html",
    "petdotu14": "https://www.bigos.cl/alimentos-para-perros/acana-duck-and-pear-para-perros#/525-tamano-102_kg_saco",
    "petdotu11": "https://www.bigos.cl/alimentos-para-perros/4498-40-acana-freshwater-fish-para-perros.html#/506-tamano-113_kg_saco",
    "petdotu13": "https://www.bigos.cl/alimentos-para-perros/4502-34-acana-light-and-fit-para-perros.html#/506-tamano-113_kg_saco",
    "petdotu7": "https://www.bigos.cl/alimentos-para-perros/acana-wild-coast-para-perros#/537-tamano-97_kg_saco",
    "petdotu10": "https://www.bigos.cl/alimentos-para-gatos/6843-398-acana-first-feast-kitten-para-gatitos.html#/501-tamano-18_kg_bolsa",
    "petdotu44": "https://www.bigos.cl/alimentos-para-gatos/royal-canin-kitten-para-gatitos#/521-tamano-15_kg_bolsa",
    "petdotu32": "https://www.bigos.cl/antiparasitarios-para-perros/bravecto-antiparasitario-perros-2-a-45-kgs",
    "petdotu30": "https://www.bigos.cl/antiparasitarios-para-perros/7318-bravecto-antiparasitario-perros-45-a-10-kgs-8713184148971.html",
    "petdotu29": "https://www.bigos.cl/antiparasitarios-para-perros/7317-bravecto-antiparasitario-perros-10-a-20-kgs-8713184148964.html",
    "petdotu28": "https://www.bigos.cl/antiparasitarios-para-perros/7316-bravecto-antiparasitario-perros-20-a-40-kgs-8713184148957.html",
    "petdotu181": "https://www.bigos.cl/antiparasitarios-para-perros/bravecto-antiparasitario-perros-40-a-56-kg",
    "petdotu27": "https://www.bigos.cl/farmacia-mascotas/8274-rimadyl-100-mg-14-tabletas-7804650310891.html",
    "petdotu5": "https://www.bigos.cl/antiparasitarios-para-gatos/7994-revolution-plus-gatos-hasta-25-kg-antiparasitario-5414736042985.html",
    "petdotu4": "https://www.bigos.cl/antiparasitarios-para-gatos/7993-revolution-plus-gatos-25-a-5-kgs-antiparasitario-5414736042992.html",
    "petdotu22": "https://www.bigos.cl/antiparasitarios-para-perros/6787-simparica-antiparasitario-10-a-20-kgs-1-comp-7804650311157.html",
    "petdotu23": "https://www.bigos.cl/antiparasitarios-para-perros/6784-simparica-antiparasitario-10-a-20-kgs-3-comp-7804650311089.html",
    "petdotu24": "https://www.bigos.cl/antiparasitarios-para-perros/6769-simparica-antiparasitario-5-a-10-kgs-3-comp-7804650311072.html",
    "petdotu25": "https://www.bigos.cl/antiparasitarios-para-perros/6768-simparica-antiparasitario-5-a-10-kgs-1-comp-7804650311140.html",
    "petdotu21": "https://www.bigos.cl/antiparasitarios-para-perros/6788-simparica-antiparasitario-20-a-40-kgs-1-comp-7804650311164.html",
    "petdotu20": "https://www.bigos.cl/antiparasitarios-para-perros/6785-simparica-antiparasitario-20-a-40-kgs-3-comp-7804650311096.html",
    "petdotu203": "https://www.bigos.cl/antiparasitarios-para-perros/simparica-antiparasitario-2-a-5-kgs-1-comp",
    "petdotu169": "https://www.bigos.cl/antiparasitarios-para-perros/simparica-antiparasitario-2-a-5-kgs-3-comprimidos",
    "petdotu163": "https://www.bigos.cl/antiparasitarios-para-perros/simparica-antiparasitario-20-a-40-kgs-3-comp",
    "petdotu61": "https://www.bigos.cl/cuidado-de-piel-para-perros/dragpharma-mixantip-plus-crema-15-grs",
    "petdotu97": "https://www.bigos.cl/calmantes-y-relajantes-para-perros/4167-adaptil-collar-mediano-grande-3411112116676.html",
    "petdotu96": "https://www.bigos.cl/calmantes-y-relajantes-para-perros/4166-adaptil-collar-pequeno-mediano-3411112116652.html",
    "petdotu82": "https://www.bigos.cl/vitaminas-para-perros/9057-artri-tabs-suplemento-articulaciones-para-perros-60-tab-714193699711.html",
    "petdotu93": "https://www.bigos.cl/calmantes-y-relajantes-para-perros/8039-adaptil-difusor-repuesto-48-ml-relajante-perro-3411112169252.html",
    "petdotu42": "https://www.bigos.cl/calmantes-para-gatos/feliway-clasico-difusor-carga-48-ml",
    "petdotu43": "https://www.bigos.cl/calmantes-para-gatos/3775-feliway-friends-difusor-carga-3411112251186.html",
    "petdotu40": "https://www.bigos.cl/calmantes-para-gatos/3263-feliway-clasico-en-spray-60-ml-3411112133789.html",
    "petdotu39": "https://www.bigos.cl/calmantes-para-gatos/4168-feliway-friends-repuesto-48-ml-3411112251230.html",
    "petdotu65": "https://www.bigos.cl/vitaminas-para-perros/beaphar-vitaminas-laveta-carnitina-50-ml",
    "petdotu83": "https://www.bigos.cl/vitaminas-para-perros/7106-dragpharma-condrovet-30-comp-7800006005619.html",
    "petdotu98": "https://www.bigos.cl/shampoo-para-perros/virbac-shampoo-allercalm-250-ml",
    "petdotu41": "https://www.bigos.cl/calmantes-para-gatos/4168-feliway-friends-repuesto-48-ml-3411112251230.html",
    "petdotu34": "https://www.bigos.cl/calmantes-para-gatos/beaphar-calming-pipeta-para-gatos",
    "petdotu86": "https://www.bigos.cl/snacks-para-perros/5045-wanpy-lamb-jerky-strips-100-grs-6927749840046.html",
    "petdotu38": "https://www.bigos.cl/calmantes-para-gatos/5200-beaphar-calming-tabletas-gato-perro-8711231175772.html",
    "petdotu37": "https://www.bigos.cl/calmantes-para-gatos/4842-beaphar-calming-collar-gato-8711231175840.html",
    "petdotu160": "https://www.bigos.cl/alimentos-para-perros/acana-free-run-poultry-para-perros#/505-tamano-59_kg_saco",
    "petdotu121": "https://www.bigos.cl/alimentos-para-perros/acana-pork-and-squash-para-perros#/525-tamano-102_kg_saco",
    "petdotu151": "https://www.bigos.cl/alimentos-para-gatos/leonardo-senior-para-gatos#/504-tamano-2_kg_bolsa",
    "petdotu152": "https://www.bigos.cl/alimentos-para-gatos/leonardo-light-para-gatos-adultos#/519-tamano-75_kg_saco",
    "petdotu161": "https://www.bigos.cl/alimentos-para-gatos/leonardo-senior-para-gatos",
    "petdotu164": "https://www.bigos.cl/alimentos-para-gatos/leonardo-pato-para-gatos-adultos#/519-tamano-75_kg_saco",
    "petdotu131": "https://www.bigos.cl/alimentos-para-perros/orijen-puppy-para-cachorros#/536-tamano-106_kg_saco",
    "petdotu114": "https://www.bigos.cl/alimentos-para-perros/orijen-small-breed-para-perro-raza-pequena#/502-tamano-45_kg_saco",
    "petdotu132": "https://www.bigos.cl/alimentos-para-perros/belcando-finest-gf-senior-para-perros?q=Marca-Bravery",
    "petdotu170": "https://www.bigos.cl/alimentos-para-perros/belcando-finest-light-para-perros#/522-tamano-125_kg_saco",
    "petdotu142": "https://www.bigos.cl/antiparasitarios-para-gatos/elanco-advantage-gato-hasta-4-kg",
    "petdotu135": "https://www.bigos.cl/antiparasitarios-para-gatos/elanco-advantage-gato-4-a-8-kg",
    "petdotu143": "https://www.bigos.cl/antiparasitarios-para-perros/bayer-drontal-plus-saborizado-antiparasitario",
    "petdotu185": "https://www.bigos.cl/antiparasitarios-para-perros/bayer-drontal-plus-35-antiparasitario",
    "petdotu188": "https://www.bigos.cl/antiparasitarios-para-gatos/bayer-drontal-gatos-2-comp",
    "petdotu177": "https://www.bigos.cl/antiparasitarios-para-perros/bayer-advocate-perro-10-a-25-kgs",
    "petdotu196": "https://www.bigos.cl/antiparasitarios-para-perros/bayer-advocate-perro-25-a-40-kgs",
    "petdotu199": "https://www.bigos.cl/antiparasitarios-para-perros/bayer-advocate-perro-4-a-10-kgs",
    "petdotu149": "https://www.bigos.cl/antiparasitarios-para-gatos/elanco-antiparasitario-advocate-gatos-hasta-4-kgs",
    "petdotu115": "https://www.bigos.cl/antiparasitarios-para-gatos/elanco-antiparasitario-advocate-gatos-4-a-8-kgs",
    "petdotu165": "https://www.bigos.cl/alimentos-para-gatos/nutrience-original-para-gatos#/500-tamano-5_kg_bolsa",
    "petdotu173": "https://www.bigos.cl/alimentos-para-gatos/proplan-urinary-optitract-para-gatos-adultos#/519-tamano-75_kg_saco",
    "petdotu174": "https://www.bigos.cl/vitaminas-para-perros/virbac-nutribound-perro-150-ml",
    "petdotu175": "https://www.bigos.cl/alimentos-para-gatos/nutrience-original-indoor-para-gatos#/500-tamano-5_kg_bolsa",
    "petdotu180": "https://www.bigos.cl/alimentos-para-perros/proplan-puppy-para-cachorro-raza-mediana#/520-tamano-15_kg_saco",
    "petdotu186": "https://www.bigos.cl/vitaminas-para-perros/vetnil-glicopan-125-ml",
    "petdotu187": "https://www.bigos.cl/alimentos-para-gatos/proplan-urinary-optitract-para-gatos-adultos",
    "petdotu192": "https://www.bigos.cl/alimentos-para-gatos/proplan-sterilized-optirenal-para-gatos-adultos",
    "petdotu193": "https://www.bigos.cl/vitaminas-para-perros/dragpharma-doguivit-perro-senior-30-comp",
    "petdotu201": "https://www.bigos.cl/vitaminas-para-perros/dragpharma-senilpet-60-comp",
    "petdotu205": "https://www.bigos.cl/calmantes-y-relajantes-para-perros/adaptil-repuesto-48-ml-relajante-perro",
    "petdotu206": "https://www.bigos.cl/vitaminas-para-perros/dragpharma-papainpet-30-comp",
    "petdotu207": "https://www.bigos.cl/vitaminas-para-perros/dragpharma-silimadrag-120-ml",
    "petdotu208": "https://www.bigos.cl/vitaminas-para-perros/vetnil-hemolitan-60-ml",
    "petdotu210": "https://www.bigos.cl/vitaminas-para-gatos/dragpharma-superpet-gato-125-ml",
    "petdotu184": "https://www.bigos.cl/alimentos-para-perros/proplan-adulto-para-perro-raza-pequena"
}

sku2 = {"petdotu97": "https://www.bigos.cl/alimentos-para-perros/acana-free-run-poultry-para-perros#/506-tamano-113_kg_saco"}
results = []

for sku_key, url in sku.items():
    driver.get(url)
    precio_oferta = "No disponible"
    precio_normal = "No disponible"
    
    time.sleep(3)
    
    try:
        # Intenta obtener el precio de oferta
        precio_oferta_element = driver.find_element("xpath", '/html/body/div[3]/div[1]/div[1]/div/main/div/section[1]/div[1]/div/div[1]/div[2]/div/div[2]/div[3]/div[1]/div[2]/div/span[5]') #Cambiar
        precio_oferta = precio_oferta_element.text  # Guarda el precio de oferta
    except NoSuchElementException:
        pass  # Si no se encuentra el precio de oferta, se continuará con el siguiente bloque de código

    try:
        # Intenta obtener el precio normal
        precio_normal_element = driver.find_element("xpath", '/html/body/div[3]/div[1]/div[1]/div/main/div/section[1]/div[1]/div/div[1]/div[2]/div/div[2]/div[3]/div[1]/div[1]/div/span[3]') #Cambiar
        precio_normal = precio_normal_element.text  # Guarda el precio normal
    except NoSuchElementException:
        pass  # Si no se encuentra el precio normal, se continuará con el siguiente bloque de código

    if precio_oferta == "No disponible" and precio_normal == "No disponible":
        try:
            # Si no se puede encontrar ni el precio de oferta ni el precio normal, intenta con el tercer XPath
            precio_normal_element = driver.find_element("xpath", '/html/body/div[3]/div[1]/div[1]/div/main/div/section[1]/div[1]/div/div[1]/div[2]/div/div[2]/div[3]/div[1]/div[2]/div/span[5]') #Cambiar
            precio_normal = precio_normal_element.text  # Guarda el precio normal
        except NoSuchElementException as e:
            print(f"No se pudo encontrar el precio en la URL {url} - {e}")
            
    # Limpiar los textos de precios
    precio_normal = precio_normal.replace("Precio Lista:", "").strip()
    precio_oferta = precio_oferta.replace("Precio Oferta:", "").strip()

    data = {
        "SKU": sku_key,
        "Precio": precio_normal,
        "Precio_oferta": precio_oferta
    }
    results.append(data)
    print(data)
   
driver.quit()

print(results)

df = pd.DataFrame(results)
print(df)
print(df.head)

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
							range='bigos!K2',#CAMBIAR
							valueInputOption='USER_ENTERED',
							body={'values':values}).execute()


#Valores que se pasan a Sheets
values = [[item['SKU'], item['Precio'],item['Precio_oferta']] for item in results]
result = sheet.values().update(spreadsheetId=SPREADSHEET_ID,
							range='bigos!A2:D',#CAMBIAR
							valueInputOption='USER_ENTERED',
							body={'values':values}).execute()
print(f"Datos insertados correctamente")



competitor = "Bigos"  # Cambiar 
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