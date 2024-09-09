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
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
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

sku = {
    "petdotu1": "https://bestforpets.cl/tienda/farmacia-para-perros/5388-11515-apoquel.html",
    "petdotu2": "https://bestforpets.cl/tienda/farmacia-para-perros/5388-11513-apoquel.html",
    "petdotu3": "https://bestforpets.cl/tienda/farmacia-para-perros/5388-11514-apoquel.html",
    "petdotu197": "https://bestforpets.cl/tienda/alimento-acana-para-gatos/4948-10597-acana-indoor-entree-cat.html",
    "petdotu194": "https://bestforpets.cl/tienda/alimento-acana-para-perros/3739-5740-acana-classic-wild-coast.html",
    "petdotu176": "https://bestforpets.cl/tienda/alimento-acana-para-gatos/2898-8943-acana-wild-atlantic-cat.html",
    "petdotu12": "https://bestforpets.cl/tienda/alimento-acana-para-perros/2780-3516-acana-free-run-poultry.html",
    "petdotu8": "https://bestforpets.cl/tienda/alimento-acana-para-perros/3411-4955-acana-puppy-junior.html",
    "petdotu9": "https://bestforpets.cl/tienda/alimento-acana-para-gatos/4949-10599-acana-bountiful-catch-cat.html",
    "petdotu14": "https://bestforpets.cl/tienda/alimento-acana-para-perros/2784-13228-acana-duck-pear.html",
    "petdotu11": "https://bestforpets.cl/tienda/alimento-acana-para-perros/2781-3519-acana-freshwater-fish.html",
    "petdotu13": "https://bestforpets.cl/tienda/alimento-acana-para-perros/3412-4958-acana-light-fit.html",
    "petdotu10": "https://bestforpets.cl/tienda/alimento-acana-para-gatos/4947-10593-acana-first-feast-kitten.html",
    "petdotu45": "https://bestforpets.cl/tienda/royalcanin/251145royalcaninhypoallergeniccanino.html",
    "petdotu172": "https://bestforpets.cl/tienda/antiparasitarios-para-perros/3915-6381-nexgard-spectra-antiparasitario-masticable-de-36-75-kg.html",
    "petdotu189": "https://bestforpets.cl/tienda/antiparasitarios-para-perros/3915-6382-nexgard-spectra-antiparasitario-masticable-de-36-75-kg.html",
    "petdotu68": "https://bestforpets.cl/tienda/antiparasitarios-para-perros/3916-6384-nexgard-spectra-antiparasitario-masticable-de-76-15-kg.html",
    "petdotu67": "https://bestforpets.cl/tienda/antiparasitarios-para-perros/3916-6383-nexgard-spectra-antiparasitario-masticable-de-76-15-kg.html",
    "petdotu70": "https://bestforpets.cl/tienda/antiparasitarios-para-perros/3917-6386-nexgard-spectra-antiparasitario-masticable-de-151-30-kg.html",
    "petdotu69": "https://bestforpets.cl/tienda/antiparasitarios-para-perros/3917-6385-nexgard-spectra-antiparasitario-masticable-de-151-30-kg.html",
    "petdotu138": "https://bestforpets.cl/tienda/antiparasitarios-para-perros/3918-6387-nexgard-spectra-antiparasitario-masticable-de-301-60-kg.html",
    "petdotu147": "https://bestforpets.cl/tienda/antiparasitarios-para-perros/3918-6388-nexgard-spectra-antiparasitario-masticable-de-301-60-kg.html",
    "petdotu32": "https://bestforpets.cl/tienda/antiparasitarios-para-perros/3807-5970-bravecto-antiparasitario-masticable.html",
    "petdotu30": "https://bestforpets.cl/tienda/antiparasitarios-para-perros/3807-5971-bravecto-antiparasitario-masticable.html",
    "petdotu29": "https://bestforpets.cl/tienda/antiparasitarios-para-perros/3807-5972-bravecto-antiparasitario-masticable.html",
    "petdotu28": "https://bestforpets.cl/tienda/antiparasitarios-para-perros/3807-5973-bravecto-antiparasitario-masticable.html",
    "petdotu181": "https://bestforpets.cl/tienda/antiparasitarios-para-perros/3807-5974-bravecto-antiparasitario-masticable.html",
    "petdotu84": "https://bestforpets.cl/tienda/arena-para-gatos/2902-3857-america-litter-ultra-odor-seal.html",
    "petdotu72": "https://bestforpets.cl/tienda/arena-para-gatos/4339-9543-america-litter-ultra-odor-seal-aroma-lavanda.html",
    "petdotu58": "https://bestforpets.cl/tienda/alimento-brit-care-para-perros/2343-2540-brit-care-puppy-salmon-grain-free.html",
    "petdotu52": "https://bestforpets.cl/tienda/alimento-brit-care-para-perros/2836-3718-brit-care-adult-small-breed-lamb-rice.html",
    "petdotu53": "https://bestforpets.cl/tienda/alimento-brit-care-para-perros/2837-3720-brit-care-adult-medium-breed-lamb-hypoallergenic.html",
    "petdotu51": "https://bestforpets.cl/tienda/alimento-brit-care-para-perros/2839-3724-brit-care-senior-lamb-hypoallergenic.html",
    "petdotu55": "https://bestforpets.cl/tienda/alimento-brit-care-para-gatos/4694-9812-brit-care-cat-sterilized-urinary.html",
    "petdotu106": "https://bestforpets.cl/tienda/alimento-brit-care-para-perros/2834-3714-brit-care-puppy-lamb-hypoallergenic.html",
    "petdotu110": "https://bestforpets.cl/tienda/alimento-brit-care-para-gatos/4692-9808-brit-care-cat-sterilized-weight-control.html",
    "petdotu116": "https://bestforpets.cl/tienda/alimento-brit-care-para-perros/2344-2543-brit-care-junior-large-breed-salmon-grain-free.html",
    "petdotu123": "https://bestforpets.cl/tienda/alimento-brit-care-para-perros/2344-2543-brit-care-junior-large-breed-salmon-grain-free.html",
    "petdotu113": "https://bestforpets.cl/tienda/alimento-brit-care-para-perros/2835-3716-brit-care-junior-large-breed-lamb-hypoallergenic.html",
    "petdotu127": "https://bestforpets.cl/tienda/alimento-brit-care-para-gatos/4688-9800-brit-care-kitten-healthy-growth-development.html",
    "petdotu130": "https://bestforpets.cl/tienda/alimento-brit-care-para-gatos/4689-9802-brit-care-cat-haircare-healthy-shiny-coat.html",
    "petdotu133": "https://bestforpets.cl/tienda/alimento-brit-care-para-gatos/4689-9802-brit-care-cat-haircare-healthy-shiny-coat.html",
    "petdotu134": "https://bestforpets.cl/tienda/alimento-brit-care-para-gatos/4691-9806-brit-care-cat-senior-weight-control.html",
    "petdotu136": "https://bestforpets.cl/tienda/alimento-brit-care-para-perros/2343-2539-brit-care-puppy-salmon-grain-free.html",
    "petdotu139": "https://bestforpets.cl/tienda/alimento-brit-care-para-perros/3842-6080-brit-care-sensitive-venison-grain-free.html",
    "petdotu140": "https://bestforpets.cl/tienda/alimento-brit-care-para-perros/2350-2558-brit-care-weight-loss-rabbit-hypoallergenic.html",
    "petdotu155": "https://bestforpets.cl/tienda/alimento-brit-care-para-gatos/4694-9813-brit-care-cat-sterilized-urinary.html",
    "petdotu122": "https://bestforpets.cl/tienda/alimento-brit-care-para-gatos/4694-9813-brit-care-cat-sterilized-urinary.html",
    "petdotu27": "https://bestforpets.cl/tienda/farmacia-para-perros/5391--rimadyl-masticable-25mg-14-tabletas.html",
    "petdotu26": "https://bestforpets.cl/tienda/farmacia-para-perros/5390--rimadyl-masticable-100mg-60-tabletas.html",
    "petdotu5": "https://bestforpets.cl/tienda/antiparasitarios-para-gatos/4563--revolution-plus-025-ml.html",
    "petdotu4": "https://bestforpets.cl/tienda/antiparasitarios-para-gatos/4564--revolution-plus-05-ml.html",
    "petdotu183": "https://bestforpets.cl/tienda/alimento-hills-para-perros/141-72-hill%C2%B4s-science-diet-adult-7-small-bites.html",
    "petdotu203": "https://bestforpets.cl/tienda/antiparasitarios-para-perros/3662-5521-simparica-10-mg-25-a-5-kg.html",
    "petdotu169": "https://bestforpets.cl/tienda/antiparasitarios-para-perros/3662-5522-simparica-10-mg-25-a-5-kg.html",
    "petdotu97": "https://bestforpets.cl/tienda/educacion-y-adiestramiento-perros/2478-2832-adaptil-collar.html",
    "petdotu96": "https://bestforpets.cl/tienda/educacion-y-adiestramiento-perros/2478-2831-adaptil-collar.html",
    "petdotu63": "https://bestforpets.cl/tienda/alimento-oven-baked-para-perros/3207-4520-oven-baked-tradition-adult-all-breeds-fish.html",
    "petdotu62": "https://bestforpets.cl/tienda/alimento-oven-baked-para-perros/3205-4517-oven-baked-tradition-adult-all-breeds-chicken.html",
    "petdotu42": "https://bestforpets.cl/tienda/antiestres-y-educacion-para-gatos/2474--feliway-difusor.html",
    "petdotu43": "https://bestforpets.cl/tienda/antiestres-y-educacion-para-gatos/2853--feliway-friends-difusor.html",
    "petdotu40": "https://bestforpets.cl/tienda/antiestres-y-educacion-para-gatos/738--feliway-spray.html",
    "petdotu39": "https://bestforpets.cl/tienda/antiestres-y-educacion-para-gatos/2474--feliway-difusor.html",
    "petdotu66": "https://bestforpets.cl/tienda/suplementos-y-vitaminas-para-gatos/572--beaphar-laveta-taurina.html",
    "petdotu65": "https://bestforpets.cl/tienda/suplementos-y-vitaminas-para-perros/702--beaphar-laveta-carnitina.html",
    "petdotu41": "https://bestforpets.cl/tienda/antiestres-y-educacion-para-gatos/2854--feliway-friends-repuesto-difusor.html",
    "petdotu34": "https://bestforpets.cl/tienda/antiestres-y-educacion-para-gatos/1974--beaphar-calming-spot-on-for-cats.html",
    "petdotu35": "https://bestforpets.cl/tienda/educacion-y-adiestramiento-perros/3349--beaphar-calming-home-spray.html",
    "petdotu36": "https://bestforpets.cl/tienda/antiestres-y-educacion-para-gatos/3350--beaphar-calming-cat-treats.html",
    "petdotu38": "https://bestforpets.cl/tienda/educacion-y-adiestramiento-perros/3351--beaphar-calming-tablets.html",
    "petdotu37": "https://bestforpets.cl/tienda/antiestres-y-educacion-para-gatos/3347--beaphar-calming-collar-for-cats.html",
    "petdotu79": "https://bestforpets.cl/tienda/farmacia-para-perros/5389--synulox.html",
    "petdotu92": "https://bestforpets.cl/tienda/farmacia/1793--ursovet-suspensi%C3%B3n-oral.html",
    "petdotu75": "https://bestforpets.cl/tienda/farmacia-para-perros/5400--naxpet%C2%AE-soluci%C3%B3n-oral-20ml.html",
    "petdotu109": "https://bestforpets.cl/tienda/alimento-josera-para-perros/5326-13716-josera-festival.html",
    "petdotu120": "https://bestforpets.cl/tienda/alimento-josera-para-perros/5331-13541-josera-ente-kartoffel.html",
    "petdotu117": "https://bestforpets.cl/tienda/alimento-josera-para-perros/5293-11304-josidog-regular.html",
    "petdotu156": "https://bestforpets.cl/tienda/alimento-josera-para-perros/5334-11367-josera-light-vital.html",
    "petdotu141": "https://bestforpets.cl/tienda/Alimentos-Josera-para-gatos/5290-11361-josera-naturelle.html",
    "petdotu144": "https://bestforpets.cl/tienda/alimento-josera-para-perros/5327-13717-josera-balance.html",
    "petdotu209": "https://bestforpets.cl/tienda/alimento-josera-para-perros/5329-13718-josera-miniwell.html",
    "petdotu160": "https://bestforpets.cl/tienda/alimento-acana-para-perros/2780-3515-acana-free-run-poultry.html",
    "petdotu121": "https://bestforpets.cl/tienda/alimento-acana-para-perros/3164-13227-acana-pork-squash.html",
    "petdotu151": "https://bestforpets.cl/tienda/alimento-leonardo-para-gatos/4071-6735-leonardo-senior.html",
    "petdotu152": "https://bestforpets.cl/tienda/alimento-leonardo-para-gatos/4070-6734-leonardo-adult-light.html",
    "petdotu161": "https://bestforpets.cl/tienda/alimento-leonardo-para-gatos/4071-6736-leonardo-senior.html",
    "petdotu164": "https://bestforpets.cl/tienda/alimento-leonardo-para-gatos/4069-6732-leonardo-adult-pato.html",
    "petdotu131": "https://bestforpets.cl/tienda/alimento-orijen-para-perros/3408-13419-orijen-puppy.html",
    "petdotu153": "https://bestforpets.cl/tienda/alimento-orijen-para-gatos/2832-3806-orijen-original-cat.html",
    "petdotu114": "https://bestforpets.cl/tienda/alimento-orijen-para-perros/5074-10852-orijen-small-breed.html",
    "petdotu132": "https://bestforpets.cl/tienda/alimento-belcando-para-perros/4049-6698-belcando-finest-grain-free-senior.html",
    "petdotu170": "https://bestforpets.cl/tienda/alimento-belcando-para-perros/4043-6685-belcando-finest-light.html",
    "petdotu146": "https://bestforpets.cl/tienda/virbac-veterinary-hpm-gatos/4294-7648-virbac-hpm-adult-neutered-cat.html",
    "petdotu125": "https://bestforpets.cl/tienda/arena-para-gatos/5754-12739-america-litter-clean-paws.html",
    "petdotu105": "https://bestforpets.cl/tienda/alimento-excellent-para-perros/4444-9253-excellent-adult-skin-care-salm%C3%B3n.html",
    "petdotu142": "https://bestforpets.cl/tienda/antiparasitarios-para-gatos/708--advantage-hasta-4-kg.html",
    "petdotu135": "https://bestforpets.cl/tienda/antiparasitarios-para-gatos/5772--advantage-de-4-a-8-kg.html",
    "petdotu188": "https://bestforpets.cl/tienda/antiparasitarios-para-gatos/4497--drontal-gatos.html",
    "petdotu149": "https://bestforpets.cl/tienda/antiparasitarios-para-gatos/4324--advocate-pipeta-04-ml.html",
    "petdotu115": "https://bestforpets.cl/tienda/antiparasitarios-para-gatos/4325--advocate-pipeta-08-ml.html",
    "petdotu157": "https://bestforpets.cl/tienda/farmacia-para-perros/5403--oftavet%C2%AE-soluci%C3%B3n-oft%C3%A1lmica.html",
    "petdotu159": "https://bestforpets.cl/tienda/farmacia/1596--cerenia-24-mg-.html",
    "petdotu165": "https://bestforpets.cl/tienda/alimento-nutrience-para-gatos/1862-1064-nutrience-original-adult-felino.html",
    "petdotu168": "https://bestforpets.cl/tienda/antiparasitarios-para-gatos/3909--broadline-pipeta-gato-09ml-25-75kg.html",
    "petdotu171": "https://bestforpets.cl/tienda/alimento-bravery-para-perros/3314-4734-bravery-chicken-adult-largemedium-breeds.html",
    "petdotu173": "https://bestforpets.cl/tienda/alimento-pro-plan-para-gatos/162-1206-pro-plan-cat-urinary-optitract.html",
    "petdotu175": "https://bestforpets.cl/tienda/alimento-nutrience-para-gatos/2817-4272-nutrience-original-adult-indoor-hairball.html",
    "petdotu180": "https://bestforpets.cl/tienda/alimento-pro-plan-para-perros/177-13937-pro-plan-puppy-optistart-medium-breed-canino.html",
    "petdotu187": "https://bestforpets.cl/tienda/alimento-pro-plan-para-gatos/162-78-pro-plan-cat-urinary-optitract.html",
    "petdotu190": "https://bestforpets.cl/tienda/alimento-excellent-para-perros/1666-2212-excellent-puppy-chickenrice.html",
    "petdotu191": "https://bestforpets.cl/tienda/alimento-excellent-para-perros/1667-2214-excellent-adult-dog-chickenrice.html",
    "petdotu192": "https://bestforpets.cl/tienda/alimento-pro-plan-para-gatos/161-2984-pro-plan-cat-sterilized-optirenal.html",
    "petdotu198": "https://bestforpets.cl/tienda/farmacia-para-perros/5401--naxpet%C2%AE-comprimidos-10-mg.html",
    "petdotu202": "https://bestforpets.cl/tienda/cremas-y-shampoos-para-perros/660--petever-forte-shampoo.html",
    "petdotu205": "https://bestforpets.cl/tienda/educacion-y-adiestramiento-perros/2477--adaptil-repuesto-difusor.html",
    "petdotu206": "https://bestforpets.cl/tienda/farmacia-para-perros/5405--papainpet%C2%AE-comprimidos.html",
    "petdotu46": "https://bestforpets.cl/tienda/royal-canin/214-7179-royal-canin-mini-puppy.html",
    "petdotu47": "https://bestforpets.cl/tienda/royal-canin/215-891-royal-canin-mini-adult-canino.html"
}
sku2 = { "petdotu1": "https://bestforpets.cl/tienda/alimento-acana-para-perros/2780-3516-acana-free-run-poultry.html"}
    

results = []

for sku_key, url in sku.items():
    driver.get(url)
    precio_oferta = "No disponible"
    precio_normal = "No disponible"
    stock="Con Stock"
    try:
        # Intenta obtener el precio de oferta
        precio_oferta_element = driver.find_element_by_xpath("/html/body/main/header/section/div/div[1]/div[1]/section/div[1]/div[2]/div[2]/div[1]/div[1]/span[1]") #Cambiar
        precio_oferta = precio_oferta_element.text  # Guarda el precio de oferta
        stock_element= driver.find_element(By.XPATH,"/html/body/main/header/section/div/div[1]/div[1]/section/div[1]/div[2]/div[2]/div[2]")
        stock= stock_element.text
    except NoSuchElementException:
        pass  # Si no se encuentra el precio de oferta, se continuará con el siguiente bloque de código

    try:
        # Intenta obtener el precio normal
        precio_normal_element = driver.find_element_by_class_name("product-discount") #Cambiar
        precio_normal = precio_normal_element.text  # Guarda el precio normal
        stock_element= driver.find_element(By.XPATH,"/html/body/main/header/section/div/div[1]/div[1]/section/div[1]/div[2]/div[2]/div[2]")
        stock= stock_element.text
    except NoSuchElementException:
        pass  # Si no se encuentra el precio normal, se continuará con el siguiente bloque de código

    if precio_oferta == "No disponible" and precio_normal == "No disponible":
        try:
            # Si no se puede encontrar ni el precio de oferta ni el precio normal, intenta con el tercer XPath
            precio_normal_element = driver.find_element_by_class_name("current-price") #Cambiar
            precio_normal = precio_normal_element.text  # Guarda el precio normal
            stock_element= driver.find_element(By.XPATH,"/html/body/main/header/section/div/div[1]/div[1]/section/div[1]/div[2]/div[2]/div[2]")
            stock= stock_element.text
        except NoSuchElementException as e:
            print(f"No se pudo encontrar el precio en la URL {url} - {e}")

    data = {
        "SKU": sku_key,
        "Precio": precio_normal,
        "Precio_oferta": precio_oferta,
        "Stock":stock
    }
    results.append(data)
    print(data)
    time.sleep(3)
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
							range='bestforpets!I2',#CAMBIAR
							valueInputOption='USER_ENTERED',
							body={'values':values}).execute()


#Valores que se pasan a Sheets
values = [[item['SKU'], item['Precio_oferta'], item['Precio']] for item in results]
result = sheet.values().update(spreadsheetId=SPREADSHEET_ID,
							range='bestforpets!A2:C',#CAMBIAR
							valueInputOption='USER_ENTERED',
							body={'values':values}).execute()
print(f"Datos insertados correctamente")

#Valores que se pasan a Sheets
values = [[item['Stock']] for item in results]
result = sheet.values().update(spreadsheetId=SPREADSHEET_ID,
							range='bestforpets!M2:N',#CAMBIAR
							valueInputOption='USER_ENTERED',
							body={'values':values}).execute()
print(f"Datos insertados correctamente")




competitor = "Best For Pets"  # Cambiar 
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
values = [[row['SKU'], competitor, row['Precio'], row['Precio_oferta'], row["Stock"]] for _, row in df.iterrows()]

# Insertar los resultados en la nueva hoja después de la última fila
update_range = f'apipets!A{last_row}:E{last_row + len(values) - 1}' #Cambiar
result = sheet.values().update(
    spreadsheetId=NEW_SPREADSHEET_ID,
    range=update_range,
    valueInputOption='USER_ENTERED',
    body={'values': values}
).execute()
