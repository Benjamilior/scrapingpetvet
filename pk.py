
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
    "petdotu194": "https://pyk.cl/catalogo/producto/9727/classic-wild-coast-2-kg",
    "petdotu7": "https://pyk.cl/catalogo/producto/10841/classic-wild-coast-11-35-kg",
    "petdotu160": "https://pyk.cl/catalogo/producto/3509/heritage-free-run-poultry-dog-5-9-kg",
    "petdotu197": "https://pyk.cl/catalogo/producto/8468/indoor-entree-cat-1-8-kg",
    "petdotu121": "https://pyk.cl/catalogo/producto/3522/singles-pork-squash-dog-11-35-kg",
    "petdotu176": "https://pyk.cl/catalogo/producto/5963/regionals-wild-atlantic-cat-4-5-kg",
    "petdotu6": "https://pyk.cl/catalogo/producto/8460/classic-prairie-poultry-11-35-kg",
    "petdotu97": "https://pyk.cl/catalogo/producto/1407/adaptil-collar-m-l",
    "petdotu96": "https://pyk.cl/catalogo/producto/1415/adaptil-collar-s-m",
    "petdotu93": "https://pyk.cl/catalogo/producto/1077/adaptil-difusor-repuesto",
    "petdotu205": "https://pyk.cl/catalogo/producto/2116/adaptil-repuesto-difusor",
    "petdotu135": "https://pyk.cl/catalogo/producto/2617/advantage-desde-4-a-8-kg",
    "petdotu142": "https://pyk.cl/catalogo/producto/2672/advantage-hasta-4-kg",
    "petdotu149": "https://pyk.cl/catalogo/producto/4096/advocate-hasta-4-kg",
    "petdotu115": "https://pyk.cl/catalogo/producto/4097/advocate-4-a-8-kg",
    "petdotu98": "https://pyk.cl/catalogo/producto/1898/allercalm-shampoo-250-ml",
    "petdotu125": "https://pyk.cl/catalogo/producto/10656/clean-paws-15-kg",
    "petdotu84": "https://pyk.cl/catalogo/producto/3406/arena-america-litter-15-kg",
    "petdotu72": "https://pyk.cl/catalogo/producto/10657/ultra-odor-seal-lavanda-15-kg",
    "petdotu1": "https://pyk.cl/catalogo/producto/3726/apoquel-16-mg-20-comprimidos",
    "petdotu2": "https://pyk.cl/catalogo/producto/3724/apoquel-3-6-mg-20-comprimidos",
    "petdotu3": "https://pyk.cl/catalogo/producto/3725/apoquel-5-4-mg-20-comprimidos",
    "petdotu132": "https://pyk.cl/catalogo/producto/5667/finest-gf-senior-12-5-kg",
    "petdotu170": "https://pyk.cl/catalogo/producto/5623/finest-light-12-5-kg",
    "petdotu49": "https://pyk.cl/catalogo/producto/332/adult-small-breed-2-72-kg",
    "petdotu181": "https://pyk.cl/catalogo/producto/1812/bravecto-40-a-56-kg",
    "petdotu28": "https://pyk.cl/catalogo/producto/1720/bravecto-20-a-40-kg",
    "petdotu32": "https://pyk.cl/catalogo/producto/1722/bravecto-2-a-4-5-kg",
    "petdotu30": "https://pyk.cl/catalogo/producto/1727/bravecto-4-5-a-10-kg",
    "petdotu29": "https://pyk.cl/catalogo/producto/1721/bravecto-10-a-20-kg",
    "petdotu171": "https://pyk.cl/catalogo/producto/5802/chicken-puppy-large-medium-breeds-12-kg",
    "petdotu53": "https://pyk.cl/catalogo/producto/3483/adult-medium-breed-lamb-rice-12-kg",
    "petdotu122": "https://pyk.cl/catalogo/producto/3560/adult-small-breed-lamb-rice-3-kg",
    "petdotu52": "https://pyk.cl/catalogo/producto/3482/adult-small-breed-lamb-rice-7-5-kg",
    "petdotu130": "https://pyk.cl/catalogo/producto/3547/grain-free-haircare-healthy-shiny-coat-7-kg",
    "petdotu127": "https://pyk.cl/catalogo/producto/3544/kitten-2-kg",
    "petdotu134": "https://pyk.cl/catalogo/producto/3557/grain-free-senior-weight-control-7-kg",
    "petdotu155": "https://pyk.cl/catalogo/producto/3554/sterilised-urinary-2-kg",
    "petdotu55": "https://pyk.cl/catalogo/producto/3553/sterilised-urinary-7-kg",
    "petdotu116": "https://pyk.cl/catalogo/producto/3492/grain-free-adult-large-breed-salmon-12-kg",
    "petdotu57": "https://pyk.cl/catalogo/producto/3490/grain-free-adult-salmon-12-kg",
    "petdotu133": "https://pyk.cl/catalogo/producto/3491/grain-free-adult-salmon-3-kg",
    "petdotu58": "https://pyk.cl/catalogo/producto/3486/grain-free-puppy-salmon-12-kg",
    "petdotu136": "https://pyk.cl/catalogo/producto/3487/grain-free-puppy-salmon-3-kg",
    "petdotu59": "https://pyk.cl/catalogo/producto/3493/grain-free-senior-light-salmon-12-kg",
    "petdotu139": "https://pyk.cl/catalogo/producto/9589/sensitive-venison-and-potato-12-kg",
    "petdotu106": "https://pyk.cl/catalogo/producto/3479/puppy-lamb-rice-12-kg",
    "petdotu113": "https://pyk.cl/catalogo/producto/3481/junior-large-breed-lamb-rice-12-kg",
    "petdotu123": "https://pyk.cl/catalogo/producto/3488/grain-free-junior-large-breed-salmon-12-kg",
    "petdotu51": "https://pyk.cl/catalogo/producto/3485/senior-lamb-rice-12-kg",
    "petdotu56": "https://pyk.cl/catalogo/producto/3495/weight-loss-rabbit-12-kg",
    "petdotu140": "https://pyk.cl/catalogo/producto/3496/weight-loss-rabbit-3-kg",
    "petdotu81": "https://pyk.cl/catalogo/producto/6640/calmer-30-ml",
    "petdotu37": "https://pyk.cl/catalogo/producto/5807/calming-collar-gato",
    "petdotu178": "https://pyk.cl/catalogo/producto/10015/canigest-combi-x-16-ml",
    "petdotu154": "https://pyk.cl/catalogo/producto/10847/canigest-combi-x-32-ml",
    "petdotu159": "https://pyk.cl/catalogo/producto/5928/cerenia-24-mg",
    "petdotu167": "https://pyk.cl/catalogo/producto/9119/clindabone-165-mg",
    "petdotu83": "https://pyk.cl/catalogo/producto/3692/condrovet-30-comprimidos",
    "petdotu95": "https://pyk.cl/catalogo/producto/8895/dermisolona-20-mg",
    "petdotu91": "https://pyk.cl/catalogo/producto/8899/dermisolona-0-4-30-ml",
    "petdotu193": "https://pyk.cl/catalogo/producto/3688/doguivit-senior-30-comprimidos",
    "petdotu188": "https://pyk.cl/catalogo/producto/1843/drontal-gatos",
    "petdotu143": "https://pyk.cl/catalogo/producto/1802/drontal-plus-saborizado-hasta-10-kg",
    "petdotu185": "https://pyk.cl/catalogo/producto/1842/drontal-plus-saborizado-sobre-35-kg",
    "petdotu191": "https://pyk.cl/catalogo/producto/5867/adulto-raza-mediana-y-grande-15-kg",
    "petdotu42": "https://pyk.cl/catalogo/producto/1079/feliway-classic-difusor-48-ml-repuesto",
    "petdotu43": "https://pyk.cl/catalogo/producto/7897/friends-difusor-repuesto-48-ml",
    "petdotu40": "https://pyk.cl/catalogo/producto/2932/feliway-classic-60-ml",
    "petdotu10": "https://pyk.cl/catalogo/producto/8465/first-feast-cat-1-8-kg",
    "petdotu71": "https://pyk.cl/catalogo/producto/3717/florafix-pasta-probiotico-15-gr",
    "petdotu12": "https://pyk.cl/catalogo/producto/3510/heritage-free-run-poultry-dog-11-35-kg",
    "petdotu11": "https://pyk.cl/catalogo/producto/3513/heritage-freshwater-fish-dog-11-35-kg",
    "petdotu186": "https://pyk.cl/catalogo/producto/3716/glicopan-pet-125-ml",
    "petdotu208": "https://pyk.cl/catalogo/producto/3715/hemolitan-gotas-60-ml",
    "petdotu158": "https://pyk.cl/catalogo/producto/10531/hemolivet-30-comprimidos",
    "petdotu87": "https://pyk.cl/catalogo/producto/8897/itraskin-2-120-ml-supension-oral",
    "petdotu144": "https://pyk.cl/catalogo/producto/11041/balance-12-5-kg",
    "petdotu120": "https://pyk.cl/catalogo/producto/11192/alimento-perro-ente-kartoffel-12-5-kg",
    "petdotu109": "https://pyk.cl/catalogo/producto/11152/festival-12-5-kg",
    "petdotu124": "https://pyk.cl/catalogo/producto/8622/alimento-gato-naturecat-10-kg",
    "petdotu141": "https://pyk.cl/catalogo/producto/8624/alimento-gato-naturelle-10-kg",
    "petdotu117": "https://pyk.cl/catalogo/producto/6363/alimento-perro-regular-18-kg",
    "petdotu209": "https://pyk.cl/catalogo/producto/11153/miniwell-10-kg",
    "petdotu65": "https://pyk.cl/catalogo/producto/1904/laveta-carnitina",
    "petdotu66": "https://pyk.cl/catalogo/producto/1905/laveta-taurina",
    "petdotu164": "https://pyk.cl/catalogo/producto/5652/adult-duck-7-5-kg",
    "petdotu152": "https://pyk.cl/catalogo/producto/5656/adult-light-7-5-kg",
    "petdotu151": "https://pyk.cl/catalogo/producto/5657/adult-senior-2-kg",
    "petdotu161": "https://pyk.cl/catalogo/producto/5658/adult-senior-7-5-kg",
    "petdotu162": "https://pyk.cl/catalogo/producto/5207/meloxivet-solucion-oral-60-ml",
    "petdotu60": "https://pyk.cl/catalogo/producto/3697/mixantip-plus-crema-50-gr",
    "petdotu75": "https://pyk.cl/catalogo/producto/8896/naxpet-0-4-20-ml",
    "petdotu198": "https://pyk.cl/catalogo/producto/9112/naxpet-10-mg",
    "petdotu69": "https://pyk.cl/catalogo/producto/8928/nexgard-spectra-x-3-tableta-masticables-15-1-a-30-kg",
    "petdotu172": "https://pyk.cl/catalogo/producto/8927/nexgard-spectra-x-3-tabletas-masticables-3-6-a-7-5-kg",
    "petdotu147": "https://pyk.cl/catalogo/producto/10950/spectra-x-1-tableta-masticable-30-1-a-60-kg",
    "petdotu138": "https://pyk.cl/catalogo/producto/8929/nexgard-spectra-x-3-tabletas-30-1-a-60-kg",
    "petdotu165": "https://pyk.cl/catalogo/producto/2816/original-cat-adult-5-kg",
    "petdotu175": "https://pyk.cl/catalogo/producto/10974/original-adult-indoor-5-kg",
    "petdotu157": "https://pyk.cl/catalogo/producto/8898/oftavet-5-ml",
    "petdotu153": "https://pyk.cl/catalogo/producto/3505/original-cat-5-45-kg",
    "petdotu114": "https://pyk.cl/catalogo/producto/8463/small-breed-dog-4-5-kg",
    "petdotu131": "https://pyk.cl/catalogo/producto/9242/heritage-puppy-11-4-kg",
    "petdotu206": "https://pyk.cl/catalogo/producto/3609/papainpet",
    "petdotu202": "https://pyk.cl/catalogo/producto/3682/petever-forte-shampoo-150-ml",
    "petdotu100": "https://pyk.cl/catalogo/producto/3672/phisio-anti-olor-limpiador-100-ml",
    "petdotu192": "https://pyk.cl/catalogo/producto/7304/sterilized-cat-7-5-kg",
    "petdotu187": "https://pyk.cl/catalogo/producto/7303/alimento-gato-urinary-3-kg",
    "petdotu173": "https://pyk.cl/catalogo/producto/7345/alimento-gato-urinary-7-5-kg",
    "petdotu184": "https://pyk.cl/catalogo/producto/7376/sensitive-skin-razas-pequenas-3-kg",
    "petdotu180": "https://pyk.cl/catalogo/producto/385/cachorros-complete-15-kg",
    "petdotu179": "https://pyk.cl/catalogo/producto/3691/regepipel-plus-shampoo-150-ml",
    "petdotu5": "https://pyk.cl/catalogo/producto/7422/revolution-plus-0-25-gatos-de-1-25-a-2-5-kg",
    "petdotu4": "https://pyk.cl/catalogo/producto/7423/revolution-plus-0-5-gatos-de-2-5-a-5-kg",
    "petdotu27": "https://pyk.cl/catalogo/producto/9140/rimadyl-100-mg",
    "petdotu201": "https://pyk.cl/catalogo/producto/3698/senilpet-cerebral-5-razas-pequenas",
    "petdotu207": "https://pyk.cl/catalogo/producto/3907/silimadrag-suspension-oral-120-ml",
    "petdotu73": "https://pyk.cl/catalogo/producto/3670/silimarina-120-mg",
    "petdotu74": "https://pyk.cl/catalogo/producto/2554/silimarina-90-comprimidos",
    "petdotu203": "https://pyk.cl/catalogo/producto/4455/simparica-10-mg-1-tableta-2-5-a-5-kg",
    "petdotu25": "https://pyk.cl/catalogo/producto/4683/simparica-20-mg-1-tableta-5-a-10-kg",
    "petdotu22": "https://pyk.cl/catalogo/producto/4456/simparica-40-mg-1-tableta-10-a-20-kg",
    "petdotu23": "https://pyk.cl/catalogo/producto/5796/simparica-40-mg-3-tableta-10-a-20-kg",
    "petdotu21": "https://pyk.cl/catalogo/producto/4457/simparica-80-mg-1-tableta-20-a-40-kg",
    "petdotu20": "https://pyk.cl/catalogo/producto/8732/simparica-80-mg-3-comprimidos",
    "petdotu89": "https://pyk.cl/catalogo/producto/7688/sucravet-10-suspension-oral-100-ml",
    "petdotu210": "https://pyk.cl/catalogo/producto/3689/superpet-gato-125-ml",
    "petdotu79": "https://pyk.cl/catalogo/producto/8903/synulox-comprimidos",
    "petdotu108": "https://pyk.cl/catalogo/producto/6610/traumeel-100-comprimidos",
    "petdotu92": "https://pyk.cl/catalogo/producto/9123/ursovet-60-ml"
}
sku2 = {"petdotu194": "https://pyk.cl/catalogo/producto/9727/classic-wild-coast-2-kg",}
results = []

for sku_key, url in sku.items():
    driver.get(url)
    precio_oferta = "No disponible"
    precio_normal = "No disponible"
    stock= "Con Stock"
    try:
        # Intenta obtener el precio de oferta                  
        precio_oferta_element = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[3]/div[1]/div/div[2]/div[3]/div[2]/span[1]') #Cambiar
        precio_oferta = precio_oferta_element.text  # Guarda el precio de oferta
        stock_element= driver.find_element(By.XPATH,"/html/body/div[6]/div/div[3]/div[1]/div/div[2]/div[4]/div/div/p")
        stock = stock_element.text
    except NoSuchElementException:
        pass  # Si no se encuentra el precio de oferta, se continuará con el siguiente bloque de código

    try:
        # Intenta obtener el precio normal
        precio_normal_element = driver.find_element("xpath", '/html/body/div[6]/div/div[3]/div[1]/div/div[2]/div[3]/div[1]/span[1]') #Cambiar
        precio_normal = precio_normal_element.text  # Guarda el precio normal
        stock_element= driver.find_element(By.XPATH,"/html/body/div[6]/div/div[3]/div[1]/div/div[2]/div[4]/div/div/p")
        stock = stock_element.text
    except NoSuchElementException:
        pass  # Si no se encuentra el precio normal, se continuará con el siguiente bloque de código

    if precio_oferta == "No disponible" and precio_normal == "No disponible":
        try:
            # Si no se puede encontrar ni el precio de oferta ni el precio normal, intenta con el tercer XPath
            precio_normal_element = driver.find_element("xpath", '/html/body/div[6]/div/div[3]/div[1]/div/div[2]/div[3]/div[1]') #Cambiar
            precio_normal = precio_normal_element.text  # Guarda el precio normal
            stock_element= driver.find_element(By.XPATH,"/html/body/div[6]/div/div[3]/div[1]/div/div[2]/div[4]/div/div/p")
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
							range='p&k!k2',#CAMBIAR
							valueInputOption='USER_ENTERED',
							body={'values':values}).execute()


#Valores que se pasan a Sheets
values = [[item['SKU'], item['Precio'],item['Precio_oferta']] for item in results]
result = sheet.values().update(spreadsheetId=SPREADSHEET_ID,
							range='p&k!A2:E',#CAMBIAR
							valueInputOption='USER_ENTERED',
							body={'values':values}).execute()
print(f"Datos insertados correctamente")

#Valores que se pasan a Sheets
values = [[item['Stock']] for item in results]
result = sheet.values().update(spreadsheetId=SPREADSHEET_ID,
							range='p&k!M2:N',#CAMBIAR
							valueInputOption='USER_ENTERED',
							body={'values':values}).execute()
print(f"Datos insertados correctamente")


df = pd.DataFrame(results)
print(df)
print(df.head)

#Para Precio BBDD ---------------------------------------------------------------------------------------------------------------- 
competitor = "p&k"  # Cambiar 
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
values = [[row['SKU'], competitor, row['Precio'], row["Precio_oferta"], now_str] for _, row in df.iterrows()]

# Insertar los resultados en la nueva hoja después de la última fila
update_range = f'petvet!A{last_row}:E{last_row + len(values) - 1}' #Cambiar
result = sheet.values().update(
    spreadsheetId=NEW_SPREADSHEET_ID,
    range=update_range,
    valueInputOption='USER_ENTERED',
    body={'values': values}
).execute()

print(f"Datos insertados correctamente en la nueva hoja de Google Sheets en el rango {update_range}")

#Para Stock BBDD ----------------------------------------------------------------------------------------------------------------        
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
SPREADSHEET_ID_API = '1S8jzZl4UehXDJxWuHfTSLftBnq3CKUXhgRGrJIShyhE'  
# Obtener la última fila con datos en la nueva hoja
result = sheet.values().get(spreadsheetId=SPREADSHEET_ID_API, range='apipets!A:A').execute() #Cambiar donde llega la info
values = result.get('values', [])
last_row = len(values) + 1  # Obtener el índice de la última fila vacía

# Convertir resultados a la lista de valores
values = [[row['SKU'], competitor, row['Precio'], row['Precio_oferta'], row["Stock"]] for _, row in df.iterrows()]

# Insertar los resultados en la nueva hoja después de la última fila
update_range = f'apipets!A{last_row}:E{last_row + len(values) - 1}' #Cambiar
result = sheet.values().update(
    spreadsheetId=SPREADSHEET_ID_API,
    range=update_range,
    valueInputOption='USER_ENTERED',
    body={'values': values}
).execute()
