
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
    "petdotu4": "https://www.clubdeperrosygatos.cl/shop/saludybienestar/controlparasitario/pipetarevolutiongatosplus255kg/",
    "petdotu5": "https://www.clubdeperrosygatos.cl/shop/saludybienestar/controlparasitario/pipetarevolutiongatosplus12525kg/",
    "petdotu9": "https://www.clubdeperrosygatos.cl/shop/alimento/alimentoparagatos/acanaparagatos/comecanacanabountifulcatchcat45kg/",
    "petdotu10": "https://www.clubdeperrosygatos.cl/shop/alimento/alimentoparagatos/acanaparagatos/comecanacanafirstfeastcat18kg/",
    "petdotu16": "https://www.clubdeperrosygatos.cl/shop/alimento/alimentoparaperros/fitformulaparaperros/fitformulaalimentoperrosenior20kg/",
    "petdotu17": "https://www.clubdeperrosygatos.cl/shop/alimento/alimentoparaperros/fitformulaparaperros/fitformulaalimentoperroadulto20kg/",
    "petdotu18": "https://www.clubdeperrosygatos.cl/shop/alimento/alimentoparaperros/fitformulaparaperros/fitformulaalimentoperrocachorro10kg/",
    "petdotu26": "https://www.clubdeperrosygatos.cl/shop/saludybienestar/farmaciaperrosygatos/farmaciaconreceta/rimadylantiinflamatorio60comprimidos/",
    "petdotu27": "https://www.clubdeperrosygatos.cl/shop/saludybienestar/farmaciaperrosygatos/farmaciaconreceta/rimadylantiinflamatorio14comprimidos/",
    "petdotu34": "https://www.clubdeperrosygatos.cl/shop/salud-y-bienestar/farmacia-perros-y-gatos/calming-spot-on-gatos/",
    "petdotu36": "https://www.clubdeperrosygatos.cl/shop/alimento/snacksperrosygatos/snacksparagatos/masticablesgato/beapharcalmingcattreats/",
    "petdotu37": "https://www.clubdeperrosygatos.cl/shop/saludybienestar/antiestresyrelajacion/calmingcollargato/",
    "petdotu38": "https://www.clubdeperrosygatos.cl/shop/saludybienestar/farmaciaperrosygatos/calmingtablets20comp/",
    "petdotu39": "https://www.clubdeperrosygatos.cl/shop/salud-y-bienestar/entrenamiento-salud-y-bienestar/feliway-difusor-repuesto-feromonas-48-ml-2/",
    "petdotu40": "https://www.clubdeperrosygatos.cl/shop/saludybienestar/antiestresyrelajacion/feliwayspray60ml/",
    "petdotu41": "https://www.clubdeperrosygatos.cl/shop/saludybienestar/farmaciaperrosygatos/feliwayfriendsdifusorrepuestoferomonas48ml/",
    "petdotu42": "https://www.clubdeperrosygatos.cl/shop/saludybienestar/entrenamientosaludybienestar/feliwaydifusorrepuestoferomonas48ml/",
    "petdotu43": "https://www.clubdeperrosygatos.cl/shop/saludybienestar/farmaciaperrosygatos/feliwayfriendsdifusorrepuestoferomonas48ml2/",
    "petdotu44": "https://www.clubdeperrosygatos.cl/shop/alimento/alimentoparagatos/royalcaninparagatos/royalcaninmotherbabycat15kg/",
    "petdotu46": "https://www.clubdeperrosygatos.cl/shop/alimento/alimento-para-perros/royal-canin/royal-canin-mini-junior-1-kg/",
    "petdotu47": "https://www.clubdeperrosygatos.cl/shop/alimento/alimento-para-perros/royal-canin/royal-canin-mini-adult-8-3kg/",
    "petdotu65": "https://www.clubdeperrosygatos.cl/shop/saludybienestar/farmaciaperrosygatos/lavetacarnitina50ml/",
    "petdotu66": "https://www.clubdeperrosygatos.cl/shop/saludybienestar/farmaciaperrosygatos/lavetataurina50ml/",
    "petdotu71": "https://www.clubdeperrosygatos.cl/shop/saludybienestar/farmaciaperrosygatos/florafixpet/",
    "petdotu72": "https://www.clubdeperrosygatos.cl/shop/salud-y-bienestar/arenas-sanitarias/arena-america-litter-lavanda-15-kg/",
    "petdotu77": "https://www.clubdeperrosygatos.cl/shop/saludybienestar/farmaciaperrosygatos/oxtrin30comprimidos/",
    "petdotu79": "https://www.clubdeperrosygatos.cl/shop/saludybienestar/farmaciaperrosygatos/farmaciaconreceta/synulox200mgamox50mgacclv10comp/",
    "petdotu81": "https://www.clubdeperrosygatos.cl/shop/saludybienestar/farmaciaperrosygatos/vetaromcalmerefectoansioliticonatural/",
    "petdotu82": "https://www.clubdeperrosygatos.cl/shop/saludybienestar/farmaciaperrosygatos/artritabsparaarticulaciones60comprimidos/",
    "petdotu83": "https://www.clubdeperrosygatos.cl/shop/saludybienestar/farmaciaperrosygatos/condrovetde30comprimidos/",
    "petdotu84": "https://www.clubdeperrosygatos.cl/shop/regalos/catlovers/americalitterultraodorseal/",
    "petdotu85": "https://www.clubdeperrosygatos.cl/shop/alimento/alimentoparaperros/hills/hillsrdreduccionpesocanino798kg/",
    "petdotu86": "https://www.clubdeperrosygatos.cl/shop/alimento/snacksperrosygatos/snacksparaperros/masticablesperro/wanpybeefjerky/",
    "petdotu87": "https://www.clubdeperrosygatos.cl/shop/salud-y-bienestar/farmacia-perros-y-gatos/farmacia-con-receta/itraskin-2-susp-oral-120-ml/",
    "petdotu89": "https://www.clubdeperrosygatos.cl/shop/saludybienestar/farmaciaperrosygatos/farmaciaconreceta/sucravetantiacido100ml/",
    "petdotu91": "https://www.clubdeperrosygatos.cl/shop/salud-y-bienestar/farmacia-perros-y-gatos/farmacia-con-receta/dermisolona-susp-oral-0-4-x-30ml/",
    "petdotu92": "https://www.clubdeperrosygatos.cl/shop/saludybienestar/farmaciaperrosygatos/farmaciaconreceta/ursovetsusporal60ml/",
    "petdotu93": "https://www.clubdeperrosygatos.cl/shop/saludybienestar/farmaciaperrosygatos/adaptilreductorestresdifusorrepuesto48ml/",
    "petdotu94": "https://www.clubdeperrosygatos.cl/shop/saludybienestar/antiestresyrelajacion/hollidayohmmoduladordeansiedad/",
    "petdotu95": "https://www.clubdeperrosygatos.cl/shop/saludybienestar/farmaciaperrosygatos/farmaciaconreceta/dermisolona20mg10comprimidos/",
    "petdotu96": "https://www.clubdeperrosygatos.cl/shop/saludybienestar/farmaciaperrosygatos/adaptilcollarperrosreductorestressm/",
    "petdotu97": "https://www.clubdeperrosygatos.cl/shop/saludybienestar/farmaciaperrosygatos/adaptilcollarperrosreductorestresml/",
    "petdotu98": "https://www.clubdeperrosygatos.cl/shop/saludybienestar/higieneybelleza/virbacshampomedicado250mlallercalmavena/",
    "petdotu99": "https://www.clubdeperrosygatos.cl/shop/alimento/alimento-para-perros/hills/hills-r-d-canino-3-8-kg/",
    "petdotu100": "https://www.clubdeperrosygatos.cl/shop/saludybienestar/farmaciaperrosygatos/virbacphisioantiolorparaorejas100ml/"
}

results = []

for sku_key, url in sku.items():
    driver.get(url)
    precio_oferta = "No disponible"
    precio_normal = "No disponible"
    try:
        # Intenta obtener el precio de oferta
        precio_oferta_element = driver.find_element("xpath", '/html/body/div[3]/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div/div[2]/div/p/del/span') #Cambiar
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

