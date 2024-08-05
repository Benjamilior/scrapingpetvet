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
    "petdotu1": "https://www.centralvet.cl/farmacia-veterinaria/21003-apoquel-16-mg-zoetis-20-comprimidos-venta-con-receta.html",
    "petdotu2": "https://www.centralvet.cl/farmacia-veterinaria/21001-apoquel-36mg-zoetis-venta-con-receta.html",
    "petdotu3": "https://www.centralvet.cl/farmacia-veterinaria/21002-apoquel-54mg-zoetis-venta-con-receta.html",
    "petdotu176": "https://www.centralvet.cl/acana/20661-acana-wild-atlantic-grain-free-para-gatos-45kg-064992685041.html",
    "petdotu6": "https://www.centralvet.cl/inicio/22462-acana-classic-prairie-poultry-para-perros-9kg.html#/1111111133-peso-113_kg",
    "petdotu45": "https://www.centralvet.cl/alimentos-de-prescripcion-veterinaria/4932-royal-canin-hipoalergenico-hypoallergenic-para-perro-2-kg.html",
    "petdotu172": "https://www.centralvet.cl/para-perros/23421-nexgard-spectra-antiparasitario-perros-entre-36-a-75-kg-3-dosis.html",
    "petdotu189": "https://www.centralvet.cl/para-perros/21817-nexgard-spectra-antiparasitario-perros-entre-36-a-75-kg-1-dosis.html",
    "petdotu68": "https://www.centralvet.cl/para-perros/21816-nexgard-spectra-antiparasitario-perros-entre-76-a-15-kg-1-dosis.html",
    "petdotu70": "https://www.centralvet.cl/para-perros/21818-nexgard-spectra-antiparasitario-perros-entre-151-a-30-kg-1-dosis.html",
    "petdotu69": "https://www.centralvet.cl/para-perros/25992-nexgard-spectra-antiparasitario-perros-entre-151-a-30-kg-1-dosis.html",
    "petdotu138": "https://www.centralvet.cl/para-perros/23192-nexgard-spectra-antiparasitario-perros-entre-301-a-60-kg-3-dosis.html",
    "petdotu147": "https://www.centralvet.cl/para-perros/21819-nexgard-spectra-antiparasitario-perros-entre-301-a-60-kg-1-dosis.html",
    "petdotu31": "https://www.centralvet.cl/higiene-para-gatos/23214-bravecto-plus-gatos-28-a-625-kg-pipeta-antiparasitarios-internos-externos.html",
    "petdotu148": "https://www.centralvet.cl/higiene-para-gatos/23214-bravecto-plus-gatos-28-a-625-kg-pipeta-antiparasitarios-internos-externos.html",
    "petdotu32": "https://www.centralvet.cl/farmacia-para-perros/7777-bravecto-masticable-contra-pulgasgarrapatas-2-a-45kg.html",
    "petdotu30": "https://www.centralvet.cl/farmacia-para-perros/7784-bravecto-masticable-contra-pulgasgarrapatas-45-a-10kg.html",
    "petdotu29": "https://www.centralvet.cl/farmacia-para-perros/7779-bravecto-masticable-contra-pulgasgarrapatas-10-a-20kg.html",
    "petdotu28": "https://www.centralvet.cl/farmacia-para-perros/7781-bravecto-masticable-contra-pulgasgarrapatas-20-a-40kg.html",
    "petdotu181": "https://www.centralvet.cl/inicio/7786-bravecto-para-perros-40-a-56kg-antiparasitario-contra-pulgasgarrapatas.html",
    "petdotu84": "https://www.centralvet.cl/arena-sanitaria/21339-arena-sanitaria-america-litter-ultra-odor-seal-15-kg.html",
    "petdotu72": "https://www.centralvet.cl/arena-sanitaria/23596-arena-sanitaria-america-litter-ultra-odor-seal-15-kg-aroma-lavanda.html",
    "petdotu52": "https://www.centralvet.cl/productos-para-perros/20784-brit-care-perro-adulto-small-breed-cordero-y-arroz-75kg.html",
    "petdotu53": "https://www.centralvet.cl/inicio/21072-21305-brit-care-perro-adulto-medium-breed-cordero-y-arroz.html#/1111111130-peso-12_kg",
    "petdotu51": "https://www.centralvet.cl/perros-senior/23799-brit-care-perro-senior-cordero-y-arroz-12kg.html",
    "petdotu55": "https://www.centralvet.cl/alimentos/23807-23082-brit-care-gato-esterilizado-urinary-health-pollo-fresco-.html#/1111111129-peso-7_kg",
    "petdotu106": "https://www.centralvet.cl/inicio/20786-brit-care-perro-cachorro-puppy-lamb-cordero-hypoallergenic-12-kg.html",
    "petdotu110": "https://www.centralvet.cl/alimentos/23808-23084-brit-care-gato-grain-free-sterilized-weight-control-pato-y-pavo-fresco-control-de-peso.html#/1111111129-peso-7_kg",
    "petdotu113": "https://www.centralvet.cl/perros-cachorros/21106-brit-care-perro-junior-large-breed-lamb-cordero-hypoallergenic-12kg.html",
    "petdotu139": "https://www.centralvet.cl/inicio/21912-25170-brit-care-perro-grain-free-adulto-sensitive-venison.html#/1111111130-peso-12_kg",
    "petdotu122": "https://www.centralvet.cl/inicio/20783-brit-care-perro-adulto-small-breed-lamb-cordero-hypoallergenic-3kg.html",
    "petdotu27": "https://www.centralvet.cl/farmacia-para-perros/6297-rimadyl-100-mg-carprofeno-14-tabletas-anti-inflamatorio-zoetis.html",
    "petdotu26": "https://www.centralvet.cl/farmacia-para-perros/9452-rimadyl-100-mg-carprofeno-60-tabletas-anti-inflamatorio-zoetis.html",
    "petdotu5": "https://www.centralvet.cl/higiene-para-gatos/23522-revolution-plus-para-gatos-entre-125-y-25-kg-antiparasitario-zoetis.html",
    "petdotu4": "https://www.centralvet.cl/higiene-para-gatos/23523-revolution-plus-para-gatos-entre-25-y-5-kg-antiparasitario-zoetis.html",
    "petdotu119": "https://www.centralvet.cl/higiene-para-gatos/26174-revolution-plus-para-gatos-entre-5-y-10-kg-antiparasitario-zoetis.html",
    "petdotu99": "https://www.centralvet.cl/alimentos-de-prescripcion-veterinaria/22768-21711-hills-prescription-diet-rd-para-perros-reduccion-del-peso-a-pedido.html#/1111111259-peso-79_kg",
    "petdotu22": "https://www.centralvet.cl/para-perros/21812-simparica-antiparasitario-perros-entre-10-a-20-kg-1-dosis-zoetis.html",
    "petdotu24": "https://www.centralvet.cl/para-perros/22003-simparica-antiparasitario-perros-entre-5-a-10kg-3-dosis-zoetis.html",
    "petdotu25": "https://www.centralvet.cl/para-perros/21810-simparica-antiparasitario-perros-entre-5-a-10-kg-1-dosis-zoetis.html",
    "petdotu203": "https://www.centralvet.cl/para-perros/21811-simparica-antiparasitario-perros-entre-26-a-5-kg-1-dosis-zoetis.html",
    "petdotu169": "https://www.centralvet.cl/para-perros/22004-simparica-antiparasitario-perros-entre-26-a-5kg-3-dosis-zoetis-oferta.html",
    "petdotu88": "https://www.centralvet.cl/alimentos/24262-hills-science-diet-adulto-small-paws-para-adultos-toy-2kg.html",
    "petdotu61": "https://www.centralvet.cl/farmacia-para-perros/6204-mixantip-plus-pomo-15g-tratamientos-dermatologicos.html",
    "petdotu60": "https://www.centralvet.cl/farmacia-para-perros/6206-mixantip-plus-pote-50-g-tratamientos-dermatologicos.html",
    "petdotu85": "https://www.centralvet.cl/alimentos-de-prescripcion-veterinaria/9053-21713-hills-metabolic-para-perros-a-pedido.html#/1111111259-peso-79_kg",
    "petdotu97": "https://www.centralvet.cl/farmacia-para-perros/21239-adaptil-collar-para-perros-raza-mediana-grande.html",
    "petdotu73": "https://www.centralvet.cl/farmacia-para-perros/21223-silimarina-vitanimal-caja-30-comprimidos.html",
    "petdotu74": "https://www.centralvet.cl/farmacia-para-perros/9810-silimarina-vitanimal-frasco-90-comprimidos.html",
    "petdotu82": "https://www.centralvet.cl/farmacia-para-perros/5976-artri-tabs-60-comps-regenerador-articular-en-perros-y-gatos.html",
    "petdotu93": "https://www.centralvet.cl/farmacia-para-perros/15783-adaptil-difusor-con-kit-de-iniciacion.html",
    "petdotu42": "https://www.centralvet.cl/accesorios-y-bienestar/16558-feliway-classic-difusor-electrico-48-ml.html",
    "petdotu43": "https://www.centralvet.cl/bienestar/18607-felifriend-feliway-friends-difusor-48ml.html",
    "petdotu40": "https://www.centralvet.cl/bienestar/6892-feliway-classic-spray-para-problemas-de-comportamiento-en-gatos-60-ml.html",
    "petdotu39": "https://www.centralvet.cl/repuestos/6890-feliway-classic-repuesto-para-difusor-48-ml.html",
    "petdotu66": "https://www.centralvet.cl/farmacia-para-gatos/6335-laveta-taurina-suplemento-vitaminico-para-gatos.html",
    "petdotu65": "https://www.centralvet.cl/farmacia-para-perros/6175-laveta-carnitina-suplemento-vitaminico-para-perros.html",
    "petdotu49": "https://www.centralvet.cl/alimentos/6764-bil-jac-select-small-breed-perros-adultos-27kg.html",
    "petdotu83": "https://www.centralvet.cl/farmacia-para-perros/6025-condrovet-condroprotector-para-perros-30-comprimidos.html",
    "petdotu98": "https://www.centralvet.cl/farmacia-para-perros/5959-allercalm-shampoo-medicado-virbac-frasco-250-ml.html",
    "petdotu41": "https://www.centralvet.cl/bienestar/18610-felifriend-feliway-friends-repuesto-para-difusor-48ml.html",
    "petdotu34": "https://www.centralvet.cl/farmacia-para-gatos/6328-calming-spot-on-para-gatos-3-pipetas-100-natural-beaphar.html",
    "petdotu35": "https://www.centralvet.cl/farmacia-para-gatos/21230-calming-home-spray-ambiental-para-gatos-y-perros-125-ml-beaphar.html",
    "petdotu94": "https://www.centralvet.cl/farmacia-para-perros/21498-ohm-biomodulador-de-ansiedad-21-comprimidos-holliday.html",
    "petdotu81": "https://www.centralvet.cl/farmacia-veterinaria/22564-calmer-30-ml-spray-ayuda-a-tranquilizar-baja-la-ansiedad-aromvet-aromaterapia.html",
    "petdotu89": "https://www.centralvet.cl/farmacia-para-perros/10671-sucravet-sucralfato-10-100-ml-perros-y-gatos.html",
    "petdotu36": "https://www.centralvet.cl/farmacia-para-gatos/21232-calming-treats-para-gatos-35g-beaphar.html",
    "petdotu38": "https://www.centralvet.cl/farmacia-para-gatos/22615-calming-tablets-para-gatos-y-perros-20-tabletas-beaphar.html",
    "petdotu37": "https://www.centralvet.cl/farmacia-para-gatos/21229-calming-collar-para-gatos-100-natural-beaphar.html",
    "petdotu79": "https://www.centralvet.cl/farmacia-para-perros/9523-synulox-10-comprimidos-venta-con-receta-zoetis.html",
    "petdotu92": "https://www.centralvet.cl/farmacia-para-perros/7974-ursovet-jarabe-de-60-ml.html",
    "petdotu71": "https://www.centralvet.cl/farmacia-para-perros/21271-florafix-pet-probiotico-para-mascotas-15g.html",
    "petdotu75": "https://www.centralvet.cl/farmacia-para-perros/6217-naxpet-suspension-oral-20-ml.html",
    "petdotu87": "https://www.centralvet.cl/farmacia-para-perros/6158-itraskin-jarabe-120-ml-antifungico-para-perros-y-gatos.html",
    "petdotu91": "https://www.centralvet.cl/farmacia-para-perros/8072-dermisolona-30-ml-jarabe-suspension-oral.html",
    "petdotu90": "https://www.centralvet.cl/farmacia-para-perros/6252-pacifor-tranquilizante-solucion-oral-10-ml-receta.html",
    "petdotu95": "https://www.centralvet.cl/farmacia-para-perros/6044-dermisolona-prednisolona-20-mg-10-comprimidos.html",
    "petdotu100": "https://www.centralvet.cl/farmacia-para-gatos/6184-limpiador-oidos-phisio-antiolor-virbac-frasco-100-ml.html",
    "petdotu160": "https://www.centralvet.cl/alimentos/17786-acana-free-run-poultry-grain-free-para-perros-59-kg-064992501136.html",
    "petdotu121": "https://www.centralvet.cl/productos-para-perros/20869-acana-pork-squash-para-perros-102-kg.html",
    "petdotu161": "https://www.centralvet.cl/alimentos/22893-21818-leonardo-senior-alimento-para-gatos-mayores-de-10-anos.html",
    "petdotu146": "https://www.centralvet.cl/alimentos/20817-20431-hpm-virbac-gato-adulto-esterilizado-neutered.html#/1111111129-peso-7_kg",
    "petdotu118": "https://www.centralvet.cl/alimentos-de-prescripcion-veterinaria/23082-22169-hpm-virbac-perro-allergy-intolerancia-alimentaria.html#/1111111130-peso-12_kg",
    "petdotu107": "https://www.centralvet.cl/farmacia-para-perros/24865-holliday-pimocard-5-pimobendan-5-mg-x-20-comp-p-perros-7798042367740.html",
    "petdotu108": "https://www.centralvet.cl/medicina-holistica/23876-traumeel-100-comps-heel-vet-a-pedido.html",
    "petdotu142": "https://www.centralvet.cl/higiene-para-gatos/7633-advantage-antipulgas-para-gatos-hasta-4-kg-04-ml-elanco.html",
    "petdotu135": "https://www.centralvet.cl/higiene-para-gatos/13263-advantage-antipulgas-para-gatos-desde-4-hasta-8-kg-elanco.html",
    "petdotu185": "https://www.centralvet.cl/farmacia-para-perros/9892-drontal-plus-antiparasitario-interno-para-perros-sobre-35-kilos-1-comprimido-elanco.html",
    "petdotu188": "https://www.centralvet.cl/farmacia-para-gatos/26286-drontal-gatos-antiparasitario-interno-1-comprimido-elanco.html",
    "petdotu145": "https://www.centralvet.cl/farmacia-para-perros/23812-neptra-solucion-otica-2-blister-con-1-tubo-de-1ml.html",
    "petdotu149": "https://www.centralvet.cl/inicio/21209-advocate-04-ml-para-gatos-pequenos-y-hurones-hasta-4-kg-de-peso-antiparasitario-interno-y-externo-elanco.html",
    "petdotu157": "https://www.centralvet.cl/farmacia-para-perros/6236-oftavet-solucion-oftalmica-5-ml-dragpharma.html",
    "petdotu158": "https://www.centralvet.cl/farmacia-para-perros/24410-hemolivet-para-perros-y-gatos-30-comprimidos-vitanimal.html",
    "petdotu154": "https://www.centralvet.cl/farmacia-para-perros/25270-canigest-combi-pasta-32-ml-probiotico-para-mascotas.html",
    "petdotu178": "https://www.centralvet.cl/farmacia-para-perros/24059-canigest-combi-pasta-16-ml-probiotico-para-mascotas.html",
    "petdotu165": "https://www.centralvet.cl/gatos-adultos/14724-20824-nutrience-original-gatos-adultos-polloarroz-integral.html#/1111111116-peso-25_kg",
    "petdotu167": "https://www.centralvet.cl/farmacia-para-perros/6022-clindabone-clindamicina-165-mg-caja-20-comprimidos.html",
   "petdotu171": "https://www.centralvet.cl/alimentos/21804-20888-bravery-chicken-perro-adulto-mediumlarge-breed.html#/1111111130-peso-12_kg",
    "petdotu173": "https://www.centralvet.cl/alimentos-de-prescripcion-veterinaria-gatos/20639-pro-plan-gato-urinary-optitract-75-kg.html",
    "petdotu174": "https://www.centralvet.cl/laboratorio-virbac/21629-nutribound-perros-150-ml-virbac.html",
    "petdotu175": "https://www.centralvet.cl/gatos-adultos/18445-20827-nutrience-original-gatos-adultos-indoorhairball.html#/1111111121-peso-5_kg",
    "petdotu179": "https://www.centralvet.cl/farmacia-para-perros/6287-regepipel-plus-shampoo-medicado-150ml-drag-pharma.html",
    "petdotu180": "https://www.centralvet.cl/alimentos/20655-pro-plan-perro-puppy-cachorro-de-razas-medianas-15-kg-.html",
    "petdotu182": "https://www.centralvet.cl/farmacia-para-perros/6136-hematon-b12-jarabe-100-ml.html",
    "petdotu186": "https://www.centralvet.cl/farmacia-para-perros/6131-glicopan-pet-suplemento-aminoacido-vitaminico-125-ml-vetnil.html",
    "petdotu187": "https://www.centralvet.cl/alimentos-de-prescripcion-veterinaria-gatos/16660-pro-plan-gato-urinary-optitract-3-kg.html",
    "petdotu193": "https://www.centralvet.cl/farmacia-para-perros/6078-doguivit-senior-multivitaminico-perro-30-comprimidos.html",
    "petdotu195": "https://www.centralvet.cl/para-perros/21145-paz-pet-60-ml-dragpharma.html",
    "petdotu198": "https://www.centralvet.cl/farmacia-para-perros/22253-naxpet-comprimidos-10mg.html",
    "petdotu200": "https://www.centralvet.cl/inicio/23239-vetgastril-50-ml-pharmadiet.html",
    "petdotu201": "https://www.centralvet.cl/farmacia-para-perros/21526-senilpet-cerebral5-frasco-60-comprimidos-oral.html",
    "petdotu202": "https://www.centralvet.cl/farmacia-para-perros/6270-petever-forte-shampoo-medicado-frasco-150ml-drag-pharma.html",
    "petdotu205": "https://www.centralvet.cl/farmacia-para-perros/16560-adaptil-repuesto-difusor.html",
    "petdotu206": "https://www.centralvet.cl/farmacia-para-perros/22513-papainpet-30-comprimidos-papaina-perros-y-gatos.html",
    "petdotu207": "https://www.centralvet.cl/farmacia-para-perros/22135-silimadrag-suspension-oral-120-ml.html",
    "petdotu208": "https://www.centralvet.cl/farmacia-para-perros/6141-hemolitan-pet-suplemento-mineral-vitaminico-60-ml-vetnil.html",
    "petdotu210": "https://www.centralvet.cl/suplementos-alimenticios/5943-aceite-omega-3-6-superpet-125-ml-para-gatos-sabor-cangrejo.html",
    "petdotu46": "https://www.centralvet.cl/perros-cachorros/5456-20686-royal-canin-perro-mini-puppy-3kg.html#/1111111128-peso-3_kg",
    "petdotu47": "https://www.centralvet.cl/alimentos/5451-21425-royal-canin-mini-adulto.html#/1111111116-peso-25_kg",
    "petdotu184": "https://www.centralvet.cl/alimentos/17096-pro-plan-perro-adulto-optilife-small-breed-3-kg.html",
    "petdotu204":"https://www.centralvet.cl/26477-nexgard-combo-antiparasitario-interno-y-externo-para-gatitos-entre-08-a-25-kg-boehringer-ingelheim.html",
    "petdotu168":"https://www.centralvet.cl/26476-nexgard-combo-antiparasitario-interno-y-externo-para-gatos-de-25-75-kg-boehringer-ingelheim.html"
}
sku2={ "petdotu36": "https://www.centralvet.cl/inicio/22462-acana-classic-prairie-poultry-para-perros-9kg.html#/1111111133-peso-113_kg"}
results = []

for sku_key, url in sku.items():
    driver.get(url)
    precio_oferta = "No disponible"
    precio_normal = "No disponible"
    stock = "Con Stock"
    time.sleep(1)
    
    try:
        # Intenta obtener el precio de oferta
        precio_oferta_element = driver.find_element("xpath", '/html/body/main/section/div[2]/div/section/div[2]/div[1]/div[2]/div[1]/div/div[2]/div/span[1]') #Cambiar
        precio_oferta = precio_oferta_element.text  # Guarda el precio de oferta
        stock_element= driver.find_element(By.CSS_SELECTOR,"#product-availability")
        stock = stock_element.text
    except NoSuchElementException:
        pass  # Si no se encuentra el precio de oferta, se continuará con el siguiente bloque de código

    try:
        # Intenta obtener el precio normal
        precio_normal_element = driver.find_element("xpath", '/html/body/main/section/div[2]/div/section/div[2]/div[1]/div[2]/div[1]/div/div[2]/div/span[2]') #Cambiar
        precio_normal = precio_normal_element.text  # Guarda el precio normal
        stock_element= driver.find_element(By.CSS_SELECTOR,"#product-availability")
        stock = stock_element.text
    except NoSuchElementException:
        pass  # Si no se encuentra el precio normal, se continuará con el siguiente bloque de código

    if precio_oferta == "No disponible" and precio_normal == "No disponible":
        try:
            # Si no se puede encontrar ni el precio de oferta ni el precio normal, intenta con el tercer XPath
            precio_normal_element = driver.find_element_by_class_name("product-price") #Cambiar
            precio_normal = precio_normal_element.text  # Guarda el precio normal
            stock_element= driver.find_element(By.CSS_SELECTOR,"#product-availability")
            stock = stock_element.text
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
							range='centralvet!K2',#CAMBIAR
							valueInputOption='USER_ENTERED',
							body={'values':values}).execute()


#Valores que se pasan a Sheets
values = [[item['SKU'], item['Precio'], item['Precio_oferta']] for item in results]
result = sheet.values().update(spreadsheetId=SPREADSHEET_ID,
							range='centralvet!A2:C',#CAMBIAR
							valueInputOption='USER_ENTERED',
							body={'values':values}).execute()
print(f"Datos insertados correctamente")
#Valores que se pasan a Sheets
values = [[item['Stock']] for item in results]
result = sheet.values().update(spreadsheetId=SPREADSHEET_ID,
							range='centralvet!M2:N',#CAMBIAR
							valueInputOption='USER_ENTERED',
							body={'values':values}).execute()
print(f"Datos insertados correctamente")

df = pd.DataFrame(results)
print(df)
print(df.head)
        

competitor = "Central Vet"  # Cambiar 
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
