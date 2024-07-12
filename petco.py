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


# #URLs

sku = {
    "petdotu6": "https://www.petco.cl/petco-chile/es_CL/PRODUCTOS/Perro/Alimento/Alimento-Natural/Acana-Alimento-Natural-Seco-para-Perro-Acana-Classic-Prairie-Poultry%2C-11-35-kg/p/601190",
    "petdotu194": "https://www.petco.cl/petco-chile/es_CL/PRODUCTOS/Perro/Alimento/Alimento-Natural/Acana-Alimento-Natural-Seco-para-Perro-Acana-Classic-Wild-Coast%2C-11-35-kg/p/601221",
    "petdotu7": "https://www.petco.cl/petco-chile/es_CL/PRODUCTOS/Perro/Alimento/Alimento-Natural/Acana-Alimento-Natural-Seco-para-Perro-Acana-Classic-Wild-Coast%2C-11-35-kg/p/601191",
    "petdotu197": "https://www.petco.cl/petco-chile/es_CL/PRODUCTOS/Gato/Alimento/Acana-Alimento-Natural-Seco-para-Gato-Indoor-Entr%C3%A9e%2C-4-5-kg/p/601241",
    "petdotu176": "https://www.petco.cl/petco-chile/es_CL/PRODUCTOS/Gato/Alimento/Acana-Alimento-Natural-Seco-para-Gato-Wild-Atlantic%2C-4-5-kg/p/601253",
    "petdotu97": "https://www.petco.cl/petco-chile/es_CL/PRODUCTOS/Perro/Salud-y-Bienestar/Estr%C3%A9s-y-Ansiedad/Ceva-Adaptil-Calm-Collar-con-Efecto-Calmante-para-Perro%2C-Mediano-Grande/p/122231",
    "petdotu96": "https://www.petco.cl/petco-chile/es_CL/PRODUCTOS/Perro/Salud-y-Bienestar/Estr%C3%A9s-y-Ansiedad/Ceva-Adaptil-Calm-Collar-con-Efecto-Calmante-para-Perro%2C-Chico-Mediano/p/122230",
    "petdotu93": "https://www.petco.cl/petco-chile/es_CL/PRODUCTOS/Perro/Salud-y-Bienestar/Estr%C3%A9s-y-Ansiedad/Ceva-Adaptil-Calm-Set-Difusor-y-Repuesto-con-Efecto-Calmante-para-Perro%2C-48-ml/p/122240",
    "petdotu205": "https://www.petco.cl/petco-chile/es_CL/PRODUCTOS/Perro/Salud-y-Bienestar/Estr%C3%A9s-y-Ansiedad/Ceva-Adaptil-Calm-Repuesto-con-Efecto-Calmante-para-Difusor-para-Perro%2C-48-ml/p/122242",
    "petdotu149": "https://www.petco.cl/petco-chile/es_CL/PRODUCTOS/Gato/Advotate-Pipeta-Antiparasitarias-para-Par%C3%A1sitos-Externos-e-Internos-para-Gato%2C-4-a-8-kg/p/601469",
    "petdotu115": "https://www.petco.cl/petco-chile/es_CL/PRODUCTOS/Gato/Advotate-Pipeta-Antiparasitarias-para-Par%C3%A1sitos-Externos-e-Internos-para-Gato%2C-4-a-8-kg/p/601131",
    "petdotu199": "https://www.petco.cl/petco-chile/es_CL/MARCAS/Advotate/Advotate-Pipeta-Antiparasitaria-para-Par%C3%A1sitos-Externos-e-Internos-para-Perro%2C-10-15-kg/p/602001",
    "petdotu177": "https://www.petco.cl/petco-chile/es_CL/MARCAS/Advotate/Advotate-Pipeta-Antiparasitaria-para-Par%C3%A1sitos-Externos-e-Internos-para-Perro%2C-10-15-kg/p/601610",
    "petdotu196": "https://www.petco.cl/petco-chile/es_CL/MARCAS/Advotate/Advotate-Pipeta-Antiparasitaria-para-Par%C3%A1sitos-Externos-e-Internos-para-Perro%2C-10-15-kg/p/601430",
    "petdotu132": "https://www.petco.cl/petco-chile/es_CL/PRODUCTOS/Perro/Alimento/Alimento-Perros-Senior/Belcando-Alimento-Natural-Seco-para-Senior-Finest-Libre-de-Granos-Perro%2C-12-5-kg/p/600397",
    "petdotu170": "https://www.petco.cl/petco-chile/es_CL/PRODUCTOS/Perro/Belcando-Alimento-Natural-Seco-para-Adulto-Finest-Light-Perro%2C-12-5-kg/p/600403",
    "petdotu9": "https://www.petco.cl/petco-chile/es_CL/PRODUCTOS/Gato/Alimento/Acana-Alimento-Natural-Seco-para-Gato-Bountiful-Catch%2C-4-5-kg/p/601251",
    "petdotu181": "https://www.petco.cl/petco-chile/es_CL/PRODUCTOS/Bienestar-para-tu-Mascota-Perro/Bravecto-Tableta-Masticable-Antiparasitaria-Externa-para-Perro%2C-40---56-kg/p/139980",
    "petdotu28": "https://www.petco.cl/petco-chile/es_CL/PRODUCTOS/Bienestar-para-tu-Mascota-Perro/Bravecto-Tableta-Masticable-Antiparasitaria-Externa-para-Perro%2C-20---40-kg/p/139979",
    "petdotu32": "https://www.petco.cl/petco-chile/es_CL/PRODUCTOS/Bienestar-para-tu-Mascota-Perro/Bravecto-Tableta-Masticable-Antiparasitaria-Externa-para-Perro%2C-2---4-5-kg/p/139976",
    "petdotu30": "https://www.petco.cl/petco-chile/es_CL/PRODUCTOS/Bienestar-para-tu-Mascota-Perro/Bravecto-Tableta-Masticable-Antiparasitaria-Externa-para-Perro%2C-4-5---10-kg/p/139977",
    "petdotu29": "https://www.petco.cl/petco-chile/es_CL/App/Antiparasitarios/Bravecto-Tableta-Masticable-Antiparasitaria-Externa-para-Perro%2C-10---20-kg/p/139978",
    "petdotu171": "https://www.petco.cl/petco-chile/es_CL/PRODUCTOS/Perro/Bravery-Alimento-Seco-Natural-Libre-de-Granos-para-Perro-Adulto-Raza-Mediana-Grande-Receta-Pollo%2C-12-kg/p/601132",
    "petdotu83": "https://www.petco.cl/petco-chile/es_CL/MARCAS/Drag-Pharma/Drag-Pharma-Condrovet-Suplemento-Nutricional-Articular-para-Perros%2C-30-Comprimidos/p/600579",
    "petdotu188": "https://www.petco.cl/petco-chile/es_CL/PRODUCTOS/Gato/Salud-y-Bienestar/Drontal-Comprimidos-Antiparasitarios-Internos-de-Amplio-Espectro-para-Gato%2C-2-Tabletas/p/602010",
    "petdotu143": "https://www.petco.cl/petco-chile/es_CL/PRODUCTOS/Perro/Salud-y-Bienestar/Desparasitantes/Drontal-Plus-Saborizado-Comprimidos-Antiparasitarios-Internos-para-Perro%2C-35-kg/p/602011",
    "petdotu185": "https://www.petco.cl/petco-chile/es_CL/PRODUCTOS/Perro/Salud-y-Bienestar/Desparasitantes/Drontal-Plus-Saborizado-Comprimidos-Antiparasitarios-Internos-para-Perro%2C-35-kg/p/602012",
    "petdotu42": "https://www.petco.cl/petco-chile/es_CL/MARCAS/Ceva/Feliway-Classic-Set-Difusor-y-Repuesto-con-Efecto-Tranquilizante-para-Gato%2C-48-ml/p/122244",
    "petdotu43": "https://www.petco.cl/petco-chile/es_CL/PRODUCTOS/Gato/Ceva-Feliway-Friends-Set-Difusor-y-Repuesto-con-Efecto-de-Apaciguamiento-para-Gato%2C-48-ml/p/126895",
    "petdotu41": "https://www.petco.cl/petco-chile/es_CL/PRODUCTOS/Gato/Salud-y-Bienestar/Estr%C3%A9s-y-Ansiedad/Feliway-Friends-Repuesto-con-Efecto-de-Apaciguamiento-para-Gato%2C-48-ml/p/126896",
    "petdotu39": "https://www.petco.cl/petco-chile/es_CL/MARCAS/Ceva/Feliway-Classic-Repuesto-para-Difusor-con-Efecto-Tranquilizante-ante-para-Gatos%2C-48-ml/p/122245",
    "petdotu40": "https://www.petco.cl/petco-chile/es_CL/MARCAS/Ceva/Feliway-Classic-Spray-con-Efecto-Tranquilizante-para-Gato%2C-60-ml/p/122246",
    "petdotu10": "https://www.petco.cl/petco-chile/es_CL/PRODUCTOS/Gato/Alimento/Acana-Alimento-Natural-Seco-para-Gato-First-Feast-Kitten%2C-1-8-kg/p/601240",
    "petdotu12": "https://www.petco.cl/petco-chile/es_CL/PRODUCTOS/Perro/Alimento/Alimento-Natural/Acana-Alimento-Natural-Seco-para-Perro-Free-Run-Poultry%2C-11-35-kg/p/601192",
    "petdotu11": "https://www.petco.cl/petco-chile/es_CL/PRODUCTOS/Perro/Alimento/Alimento-Natural/Acana-Alimento-Natural-Seco-para-Perro-Freshwater-Fish%2C-11-35-kg/p/601193",
    "petdotu183": "https://www.petco.cl/petco-chile/es_CL/PRODUCTOS/Perro/Alimento/Alimento-Perros-Senior/Hill%27s-Science-Diet-Small-Bites-Alimento-Seco-para-Perro-Senior-Raza-Peque%C3%B1a-Receta-Pollo-y-Cebada%2C-2-kg/p/105261",
    "petdotu164": "https://www.petco.cl/petco-chile/es_CL/MARCAS/Leonardo/Leonardo-Alimento-Natural-Seco-para-Adulto-Duck-Gato%2C-7-5-kg/p/600459",
    "petdotu152": "https://www.petco.cl/petco-chile/es_CL/MARCAS/Leonardo/Leonardo-Alimento-Natural-Seco-para-Adulto-Light-Gato%2C-7-5-kg/p/600460",
    "petdotu151": "https://www.petco.cl/petco-chile/es_CL/MARCAS/Leonardo/Leonardo-Alimento-Natural-Seco-para-Senior-Gato%2C-7-5-kg/p/600455",
    "petdotu161": "https://www.petco.cl/petco-chile/es_CL/MARCAS/Leonardo/Leonardo-Alimento-Natural-Seco-para-Senior-Gato%2C-7-5-kg/p/600461",
    "petdotu189": "https://www.petco.cl/petco-chile/es_CL/MARCAS/Nexgard-Spectra/NexGard-Spectra-Masticable-Desparasitante-Externo-e-Interno-para-Perro%2C-Chico/p/138415",
    "petdotu147": "https://www.petco.cl/petco-chile/es_CL/MARCAS/Nexgard-Spectra/NexGard-Spectra-Masticable-Desparasitante-Externo-e-Interno-para-Perro%2C-X-Grande/p/138418",
    "petdotu153": "https://www.petco.cl/petco-chile/es_CL/PRODUCTOS/Gato/Orijen-Alimento-Natural-Seco-para-Gato-Original-Cat%2C-5-4-kg/p/601237",
    "petdotu114": "https://www.petco.cl/petco-chile/es_CL/PRODUCTOS/Perro/Alimento/Alimento-Perros-Talla-Peque%C3%B1a/Orijen-Alimento-Natural-Seco-para-Perro-Small-Breed%2C-4-5-kg/p/601236",
    "petdotu131": "https://www.petco.cl/petco-chile/es_CL/PRODUCTOS/Perro/Alimento/Alimento-para-Cachorro/Orijen-Alimento-Natural-Seco-para-Perro-Cachorro%2C-11-35-kg/p/601204",
    "petdotu192": "https://www.petco.cl/petco-chile/es_CL/PRODUCTOS/Gato/Pro-Plan-Alimento-Seco-para-Gato-Esterilizado-de-Todas-las-Razas%2C-1-kg/p/600047",
    "petdotu187": "https://www.petco.cl/petco-chile/es_CL/PRODUCTOS/Gato/Pro-Plan-Urinary-Alimento-Seco-para-Gato-Adulto-de-Todas-las-Razas%2C-1-kg/p/600049",
    "petdotu173": "https://www.petco.cl/petco-chile/es_CL/PRODUCTOS/Gato/Pro-Plan-Urinary-Alimento-Seco-para-Gato-Adulto-de-Todas-las-Razas%2C-1-kg/p/600049",
    "petdotu180": "https://www.petco.cl/petco-chile/es_CL/PRODUCTOS/Perro/Alimento/Alimento-Perros-Talla-Grande/Pro-Plan-Alimento-Seco-para-Cachorro-de-Razas-Medianas%2C-1-kg/p/600001",
    "petdotu8": "https://www.petco.cl/petco-chile/es_CL/PRODUCTOS/Perro/Alimento/Alimento-para-Cachorro/Acana-Alimento-Natural-Seco-para-Perro-Cachorro-%26-Junior%2C-11-35-kg/p/601194",
    "petdotu5": "https://www.petco.cl/petco-chile/es_CL/PRODUCTOS/Gato/Salud-y-Bienestar/Revolution-Plus-15-mg-2-5-mg-Pipeta-Antiparasitaria-Externa-e-Interna-para-Gato%2C-1-25--2-5-kg/p/601041",
    "petdotu4": "https://www.petco.cl/petco-chile/es_CL/PRODUCTOS/Gato/Salud-y-Bienestar/Revolution-Plus-30-mg-5-mg-Pipeta-Antiparasitaria-Externa-e-Interna-para-Gato%2C-2-5---5-kg/p/601042",
    "petdotu25": "https://www.petco.cl/petco-chile/es_CL/App/Zoetis/Zoetis-Simparica-Masticable-Desparasitante-Externo-para-Perro%2C-5-10-kg/p/139961",
    "petdotu22": "https://www.petco.cl/petco-chile/es_CL/App/Zoetis/Zoetis-Simparica-Masticable-Desparasitante-Externo-para-Perro%2C-10-20-kg/p/139962",
    "petdotu23": "https://www.petco.cl/petco-chile/es_CL/App/Zoetis/Zoetis-Simparica-Masticable-Desparasitante-Externo-para-Perro-10-20-kg%2C-3-Tabletas/p/139958",
    "petdotu21": "https://www.petco.cl/petco-chile/es_CL/App/Zoetis/Zoetis-Simparica-Masticable-Desparasitante-Externo-para-Perro%2C-20-40-kg/p/139963",
    "petdotu20": "https://www.petco.cl/petco-chile/es_CL/App/Zoetis/Zoetis-Simparica-Masticable-Desparasitante-Externo-para-Perro-20-40-kg%2C-3-Tabletas/p/139959",
    "petdotu210": "https://www.petco.cl/petco-chile/es_CL/PRODUCTOS/Gato/Drag-Pharma-Superpet-Omega-Gato-Suplemento-Nutricional-de-%C3%81cidos-Grasos-para-Gato%2C-125-ml/p/600583",
    "petdotu33": "https://www.petco.cl/petco-chile/es_CL/PRODUCTOS/Bienestar-para-tu-Mascota-Perro/Bravecto-Spot-On-Pipeta-Antiparasitaria-Externa-para-Gato%2C-1-2--2-8-kg/p/138380",
    "petdotu88": "https://www.petco.cl/petco-chile/es_CL/App/Alimento/Hill%27s-Science-Diet/Hill%27s-Science-Diet-Small-Paws-Alimento-Seco-para-Perro-Adulto-Raza-Peque%C3%B1a-Receta-Pollo-y-Arroz%2C-2-04-kg/p/105231",
    "petdotu45": "https://www.petco.cl/petco-chile/es_CL/PRODUCTOS/Perro/Royal-Canin-Alimento-Seco-para-Perro-Medicado-Anallergenic-Canine%2C-8-kg/p/600744",
    "petdotu99": "https://www.petco.cl/petco-chile/es_CL/PRODUCTOS/Perro/Alimento/Alimento-Medicado-/Hill%27s%C2%A0Prescription-Diet-r-d%2C-Alimento-Seco-Reducci%C3%B3n-de-Peso-para-Perro-Adulto%2C-8-kg/p/105325",
    "petdotu44": "https://www.petco.cl/petco-chile/es_CL/PRODUCTOS/Gato/Royal-Canin-Mother-Baby-Cat-Alimento-Seco-para-Gato-en-Gestaci%C3%B3n-Lactancia-Destete-Receta-Pollo%2C-1-5-kg/p/600692",
    "petdotu62": "https://www.petco.cl/petco-chile/es_CL/PRODUCTOS/Perro/Oven-Baked-Tradition-Adulto-All-Breeds-Pollo-Perro%2C-11-34-kg/p/600816",
    "petdotu63": "https://www.petco.cl/petco-chile/es_CL/MARCAS/Oven-Baked-Tradition/Oven-Baked-Tradition-Adulto-All-Breeds-Pescado-Perro%2C-11-34-kg/p/600817",
    "petdotu64": "https://www.petco.cl/petco-chile/es_CL/PRODUCTOS/Perro/Alimento/Alimento-Perros-Senior/Oven-Baked-Tradition-Senior-Pollo-Perro%2C-5-67-kg/p/600821"
}
sku2 = {"petdotu97": "https://www.petco.cl/petco-chile/es_CL/PRODUCTOS/Perro/Salud-y-Bienestar/Estr%C3%A9s-y-Ansiedad/Ceva-Adaptil-Calm-Collar-con-Efecto-Calmante-para-Perro%2C-Mediano-Grande/p/122231"}
results = []

for sku_key, url in sku.items():
    driver.get(url)
    precio_oferta = "No disponible"
    precio_normal = "No disponible"
    time.sleep(1)
    try:
        # Intenta obtener el precio de oferta
        precio_oferta_element = driver.find_element("xpath", '/html/body/main/div[3]/div[2]/div[1]/div[5]/div/div/div[1]/div[2]/div[2]/div[1]/div/div/span[3]') #Cambiar
        precio_oferta = precio_oferta_element.text  # Guarda el precio de oferta
    except NoSuchElementException:
        pass  # Si no se encuentra el precio de oferta, se continuará con el siguiente bloque de código

    if precio_oferta == "No disponible" and precio_normal == "No disponible":
        try:
            # Si no se puede encontrar ni el precio de oferta ni el precio normal, intenta con el tercer XPath
            precio_normal_element = driver.find_element("xpath", '/html/body/main/div[3]/div[2]/div[1]/div[5]/div/div/div[1]/div[2]/div[2]/div[1]/div/div') #Cambiar
            precio_normal = precio_normal_element.text  # Guarda el precio normal
        except NoSuchElementException as e:
            pass
        
    if precio_oferta == "No disponible" and precio_normal == "No disponible":
        try:
            # Si no se puede encontrar ni el precio de oferta ni el precio normal, intenta con el tercer XPath
            precio_normal_element = driver.find_element("xpath", '/html/body/main/div[3]/div[2]/div[1]/div[5]/div/div/div[1]/div[2]/div[2]/div[1]/div/div') #Cambiar
            precio_normal = precio_normal_element.text  # Guarda el precio normal
        except NoSuchElementException as e:
            pass
    if precio_oferta == "No disponible" and precio_normal == "No disponible":
        try:
            # Intenta obtener el precio normal
            precio_normal_element = driver.find_element("xpath", '/html/body/main/div[3]/div[2]/div[1]/div[5]/div/div/div[1]/div[2]/div[2]/div[2]/div/div[2]/span[2]') #Cambiar
            precio_normal = precio_normal_element.text  # Guarda el precio normal
        except NoSuchElementException:
            pass  # Si no se encuentra el precio normal, se continuará con el siguiente bloque de código
        
    if precio_oferta == "No disponible" and precio_normal == "No disponible":
        try:
            # Si no se puede encontrar ni el precio de oferta ni el precio normal, intenta con el tercer XPath
            precio_normal_element = driver.find_element_by_class_name('discountedPrice') #Cambiar
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
    time.sleep(1.5)
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
							range='petco!K2',#CAMBIAR
							valueInputOption='USER_ENTERED',
							body={'values':values}).execute()


#Valores que se pasan a Sheets
values = [[item['SKU'], item['Precio'], item['Precio_oferta']] for item in results]
result = sheet.values().update(spreadsheetId=SPREADSHEET_ID,
							range='petco!A2:E',#CAMBIAR
							valueInputOption='USER_ENTERED',
							body={'values':values}).execute()
print(f"Datos insertados correctamente")

df = pd.DataFrame(results)
print(df)
print(df.head)
        

competitor = "Petco"  # Cambiar 
# Enviar datos a Google Sheets BBDD
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