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

direccionestipo2 = ["/html/body/main/section/div[2]/div/section/div[2]/div[1]/div[2]/div[2]/div[2]/form/div[1]/div/ul/li[1]/input",
               "/html/body/main/section/div[2]/div/section/div[2]/div[1]/div[2]/div[2]/div[2]/form/div[1]/div/ul/li[2]/input",
               "/html/body/main/section/div[2]/div/section/div[2]/div[1]/div[2]/div[2]/div[2]/form/div[1]/div/ul/li[3]/input"]
direccionestipo3 = ["/html/body/main/section/div[2]/div/section/div[2]/div[1]/div[2]/div[2]/div[2]/form/div[1]/div/ul/li[1]/input",
               "/html/body/main/section/div[2]/div/section/div[2]/div[1]/div[2]/div[2]/div[2]/form/div[1]/div/ul/li[2]/input"]
# #URLs

urls = ["https://www.centralvet.cl/farmacia-veterinaria/21003-apoquel-16-mg-zoetis-20-comprimidos-venta-con-receta.html"]

tipo1 = [
    "https://www.centralvet.cl/farmacia-veterinaria/21003-apoquel-16-mg-zoetis-20-comprimidos-venta-con-receta.html",
    "https://www.centralvet.cl/farmacia-veterinaria/21001-apoquel-36mg-zoetis-venta-con-receta.html",
    "https://www.centralvet.cl/farmacia-veterinaria/21002-apoquel-54mg-zoetis-venta-con-receta.html",
    "https://www.centralvet.cl/para-perros/22003-simparica-antiparasitario-perros-entre-5-a-10kg-3-dosis-zoetis.html",
    "https://www.centralvet.cl/para-perros/21810-simparica-antiparasitario-perros-entre-5-a-10-kg-1-dosis-zoetis.html",
    "https://www.centralvet.cl/farmacia-para-perros/6297-rimadyl-100-mg-carprofeno-14-tabletas-anti-inflamatorio-zoetis.html",
    "https://www.centralvet.cl/farmacia-para-perros/7784-bravecto-masticable-contra-pulgasgarrapatas-45-a-10kg.html",
    "https://www.centralvet.cl/farmacia-para-perros/7777-bravecto-masticable-contra-pulgasgarrapatas-2-a-45kg.html",
    "https://www.centralvet.cl/farmacia-para-gatos/21230-calming-home-spray-ambiental-para-gatos-y-perros-125-ml-beaphar.html",
    "https://www.centralvet.cl/farmacia-para-gatos/21232-calming-treats-para-gatos-35g-beaphar.html",
    "https://www.centralvet.cl/farmacia-para-gatos/21229-calming-collar-para-gatos-100-natural-beaphar.html",
    "https://www.centralvet.cl/farmacia-para-gatos/22615-calming-tablets-para-gatos-y-perros-20-tabletas-beaphar.html",
    "https://www.centralvet.cl/repuestos/6890-feliway-classic-repuesto-para-difusor-48-ml.html",
    "https://www.centralvet.cl/bienestar/18610-felifriend-feliway-friends-repuesto-para-difusor-48ml.html",
    "https://www.centralvet.cl/accesorios-y-bienestar/16558-feliway-classic-difusor-electrico-48-ml.html",
    "https://www.centralvet.cl/alimentos-de-prescripcion-veterinaria/4932-royal-canin-hipoalergenico-hypoallergenic-para-perro-2-kg.html",
    "https://www.centralvet.cl/alimentos/5451-21425-royal-canin-mini-adulto.html#/1111111116-peso-25_kg",
    "https://www.centralvet.cl/alimentos/6764-bil-jac-select-small-breed-perros-adultos-27kg.html",
    "https://www.centralvet.cl/perros-senior/23799-brit-care-perro-senior-cordero-y-arroz-12kg.html",
    "https://www.centralvet.cl/productos-para-perros/20784-brit-care-perro-adulto-small-breed-cordero-y-arroz-75kg.html",
    "https://www.centralvet.cl/farmacia-para-perros/6204-mixantip-plus-pomo-15g-tratamientos-dermatologicos.html",
    "https://www.centralvet.cl/farmacia-para-gatos/6335-laveta-taurina-suplemento-vitaminico-para-gatos.html",
    "https://www.centralvet.cl/farmacia-para-perros/21271-florafix-pet-probiotico-para-mascotas-15g.html",
    "https://www.centralvet.cl/farmacia-para-perros/21223-silimarina-vitanimal-caja-30-comprimidos.html",
    "https://www.centralvet.cl/farmacia-para-perros/9810-silimarina-vitanimal-frasco-90-comprimidos.html",
    "https://www.centralvet.cl/farmacia-para-perros/9523-synulox-10-comprimidos-venta-con-receta-zoetis.html",
    "https://www.centralvet.cl/farmacia-veterinaria/22564-calmer-30-ml-spray-ayuda-a-tranquilizar-baja-la-ansiedad-aromvet-aromaterapia.html",
    "https://www.centralvet.cl/farmacia-para-perros/6025-condrovet-condroprotector-para-perros-30-comprimidos.html",
    "https://www.centralvet.cl/farmacia-para-perros/6158-itraskin-jarabe-120-ml-antifungico-para-perros-y-gatos.html",
    "https://www.centralvet.cl/alimentos/24262-hills-science-diet-adulto-small-paws-para-adultos-toy-2kg.html",
    "https://www.centralvet.cl/farmacia-para-perros/10671-sucravet-sucralfato-10-100-ml-perros-y-gatos.html",
    "https://www.centralvet.cl/farmacia-para-perros/6252-pacifor-tranquilizante-solucion-oral-10-ml-receta.html",
    "https://www.centralvet.cl/farmacia-para-perros/8072-dermisolona-30-ml-jarabe-suspension-oral.html",
    "https://www.centralvet.cl/farmacia-para-perros/15783-adaptil-difusor-con-kit-de-iniciacion.html",
    "https://www.centralvet.cl/farmacia-para-perros/21498-ohm-biomodulador-de-ansiedad-21-comprimidos-holliday.html",
    "https://www.centralvet.cl/farmacia-para-perros/6044-dermisolona-prednisolona-20-mg-10-comprimidos.html",
    "https://www.centralvet.cl/farmacia-para-perros/21239-adaptil-collar-para-perros-raza-mediana-grande.html",
    "https://www.centralvet.cl/farmacia-para-perros/5959-allercalm-shampoo-medicado-virbac-frasco-250-ml.html",
    "https://www.centralvet.cl/farmacia-para-gatos/6184-limpiador-oidos-phisio-antiolor-virbac-frasco-100-ml.html1"
]
tipo2 = ["https://www.centralvet.cl/inicio/22462-21454-acana-classic-prairie-poultry-para-perros.html#/1111111133-peso-113_kg",
"https://www.centralvet.cl/alimentos-de-prescripcion-veterinaria/22768-21711-hills-prescription-diet-rd-para-perros-reduccion-del-peso-a-pedido.html#/1111111259-peso-79_kg"]
tipo3 = ["https://www.centralvet.cl/inicio/21072-21305-brit-care-perro-adulto-medium-breed-cordero-y-arroz.html#/1111111130-peso-12_kg",
"https://www.centralvet.cl/alimentos/23807-23083-brit-care-gato-esterilizado-urinary-health-pollo-fresco-.html#/1111111131-peso-2_kg"]

sku = {
    "petdotu1": "https://www.centralvet.cl/farmaciaveterinaria/21003apoquel16mgzoetis20comprimidosventaconreceta.html",
    "petdotu2": "https://www.centralvet.cl/farmacia-veterinaria/21001-apoquel-36mg-zoetis-venta-con-receta.html",
    "petdotu3": "https://www.centralvet.cl/farmacia-veterinaria/21002-apoquel-54mg-zoetis-venta-con-receta.html",
    "petdotu4": "https://www.centralvet.cl/higiene-para-gatos/23523-revolution-plus-para-gatos-entre-25-y-5-kg-antiparasitario-zoetis.html",
    "petdotu5": "https://www.centralvet.cl/higiene-para-gatos/23522-revolution-plus-para-gatos-entre-125-y-25-kg-antiparasitario-zoetis.html",
    "petdotu6": "https://www.centralvet.cl/inicio/22462-21454-acana-classic-prairie-poultry-para-perros.html#/1111111133-peso-113_kg",
    "petdotu14": "https://www.centralvet.cl/inicio/24478-23756-acana-duck-pear-singles-formula-perro.html#/1111111133-peso-113_kg",
    "petdotu22": "https://www.centralvet.cl/para-perros/21812-simparica-antiparasitario-perros-entre-10-a-20-kg-1-dosis-zoetis.html",
    "petdotu24": "https://www.centralvet.cl/para-perros/22003-simparica-antiparasitario-perros-entre-5-a-10kg-3-dosis-zoetis.html",
    "petdotu25": "https://www.centralvet.cl/para-perros/21810-simparica-antiparasitario-perros-entre-5-a-10-kg-1-dosis-zoetis.html",
    "petdotu26": "https://www.centralvet.cl/farmacia-para-perros/9452-rimadyl-100-mg-carprofeno-60-tabletas-anti-inflamatorio-zoetis.html",
    "petdotu27": "https://www.centralvet.cl/farmacia-para-perros/6297-rimadyl-100-mg-carprofeno-14-tabletas-anti-inflamatorio-zoetis.html",
    "petdotu28": "https://www.centralvet.cl/farmacia-para-perros/7781-bravecto-masticable-contra-pulgasgarrapatas-20-a-40kg.html",
    "petdotu30": "https://www.centralvet.cl/farmacia-para-perros/7784-bravecto-masticable-contra-pulgasgarrapatas-45-a-10kg.html",
    "petdotu32": "https://www.centralvet.cl/farmacia-para-perros/7777-bravecto-masticable-contra-pulgasgarrapatas-2-a-45kg.html",
    "petdotu35": "https://www.centralvet.cl/farmacia-para-gatos/21230-calming-home-spray-ambiental-para-gatos-y-perros-125-ml-beaphar.html",
    "petdotu36": "https://www.centralvet.cl/farmacia-para-gatos/21232-calming-treats-para-gatos-35g-beaphar.html",
    "petdotu37": "https://www.centralvet.cl/farmacia-para-gatos/21229-calming-collar-para-gatos-100-natural-beaphar.html",
    "petdotu38": "https://www.centralvet.cl/farmacia-para-gatos/22615-calming-tablets-para-gatos-y-perros-20-tabletas-beaphar.html",
    "petdotu39": "https://www.centralvet.cl/repuestos/6890-feliway-classic-repuesto-para-difusor-48-ml.html",
    "petdotu40": "https://www.centralvet.cl/bienestar/6892-feliway-classic-spray-para-problemas-de-comportamiento-en-gatos-60-ml.html",
    "petdotu41": "https://www.centralvet.cl/bienestar/18610-felifriend-feliway-friends-repuesto-para-difusor-48ml.html",
    "petdotu42": "https://www.centralvet.cl/accesorios-y-bienestar/16558-feliway-classic-difusor-electrico-48-ml.html",
    "petdotu45": "https://www.centralvet.cl/alimentos-de-prescripcion-veterinaria/4932-royal-canin-hipoalergenico-hypoallergenic-para-perro-2-kg.html",
    "petdotu47": "https://www.centralvet.cl/alimentos/5451-21425-royal-canin-mini-adulto.html#/1111111116-peso-25_kg",
    "petdotu49": "https://www.centralvet.cl/alimentos/6764-bil-jac-select-small-breed-perros-adultos-27kg.html",
    "petdotu51": "https://www.centralvet.cl/perros-senior/23799-brit-care-perro-senior-cordero-y-arroz-12kg.html",
    "petdotu52": "https://www.centralvet.cl/productos-para-perros/20784-brit-care-perro-adulto-small-breed-cordero-y-arroz-75kg.html",
    "petdotu53": "https://www.centralvet.cl/inicio/21072-21305-brit-care-perro-adulto-medium-breed-cordero-y-arroz.html#/1111111130-peso-12_kg",
    "petdotu55": "https://www.centralvet.cl/alimentos/23807-23083-brit-care-gato-esterilizado-urinary-health-pollo-fresco-.html#/1111111131-peso-2_kg",
    "petdotu61": "https://www.centralvet.cl/farmacia-para-perros/6204-mixantip-plus-pomo-15g-tratamientos-dermatologicos.html",
    "petdotu65": "https://www.centralvet.cl/farmacia-para-perros/6175-laveta-carnitina-suplemento-vitaminico-para-perros.html",
    "petdotu66": "https://www.centralvet.cl/farmacia-para-gatos/6335-laveta-taurina-suplemento-vitaminico-para-gatos.html",
    "petdotu71": "https://www.centralvet.cl/farmacia-para-perros/21271-florafix-pet-probiotico-para-mascotas-15g.html",
    "petdotu73": "https://www.centralvet.cl/farmacia-para-perros/21223-silimarina-vitanimal-caja-30-comprimidos.html",
    "petdotu74": "https://www.centralvet.cl/farmacia-para-perros/9810-silimarina-vitanimal-frasco-90-comprimidos.html",
    "petdotu79": "https://www.centralvet.cl/farmacia-para-perros/9523-synulox-10-comprimidos-venta-con-receta-zoetis.html",
    "petdotu81": "https://www.centralvet.cl/farmacia-veterinaria/22564-calmer-30-ml-spray-ayuda-a-tranquilizar-baja-la-ansiedad-aromvet-aromaterapia.html",
    "petdotu83": "https://www.centralvet.cl/farmacia-para-perros/6025-condrovet-condroprotector-para-perros-30-comprimidos.html",
    "petdotu84": "https://www.centralvet.cl/arena-sanitaria/21338-arena-sanitaria-americalitter-7kg-ultra-odor-seal.html",
    "petdotu87": "https://www.centralvet.cl/farmacia-para-perros/6158-itraskin-jarabe-120-ml-antifungico-para-perros-y-gatos.html",
    "petdotu88": "https://www.centralvet.cl/alimentos/24262-hills-science-diet-adulto-small-paws-para-adultos-toy-2kg.html",
    "petdotu89": "https://www.centralvet.cl/farmacia-para-perros/10671-sucravet-sucralfato-10-100-ml-perros-y-gatos.html",
    "petdotu90": "https://www.centralvet.cl/farmacia-para-perros/6252-pacifor-tranquilizante-solucion-oral-10-ml-receta.html",
    "petdotu91": "https://www.centralvet.cl/farmacia-para-perros/8072-dermisolona-30-ml-jarabe-suspension-oral.html",
    "petdotu93": "https://www.centralvet.cl/farmacia-para-perros/15783-adaptil-difusor-con-kit-de-iniciacion.html",
    "petdotu94": "https://www.centralvet.cl/farmacia-para-perros/21498-ohm-biomodulador-de-ansiedad-21-comprimidos-holliday.html",
    "petdotu95": "https://www.centralvet.cl/farmacia-para-perros/6044-dermisolona-prednisolona-20-mg-10-comprimidos.html",
    "petdotu97": "https://www.centralvet.cl/farmacia-para-perros/21239-adaptil-collar-para-perros-raza-mediana-grande.html",
    "petdotu98": "https://www.centralvet.cl/farmacia-para-perros/5959-allercalm-shampoo-medicado-virbac-frasco-250-ml.html",
    "petdotu99": "https://www.centralvet.cl/alimentos-de-prescripcion-veterinaria/22768-21711-hills-prescription-diet-rd-para-perros-reduccion-del-peso-a-pedido.html#/1111111259-peso-79_kg",
    "petdotu100": "https://www.centralvet.cl/farmacia-para-gatos/6184-limpiador-oidos-phisio-antiolor-virbac-frasco-100-ml.html1"
}
sku1 = {"petdotu1": "https://www.centralvet.cl/farmacia-veterinaria/21003-apoquel-16-mg-zoetis-20-comprimidos-venta-con-receta.html"}

results = []

# driver.get("https://www.amigales.cl/condrovet-30-comprimidos.html")

for sku_key, url in sku.items():
    driver.get(url)
    try:
        nombresku = driver.find_element("xpath", '/html/body/main/section/div[2]/div/section/div[2]/div[1]/div[2]/div[1]/h1/span') #Cambiar 
        precio = driver.find_element("xpath", '/html/body/main/section/div[2]/div/section/div[2]/div[1]/div[2]/div[1]/div/div[2]/div/span[1]/span')#Cambiar
        data = {
            "SKU":sku_key,
            "Nombre SKU": nombresku.text,
            "Precio": precio.text,
              # Si deseas almacenar la URL junto con los datos
        }
        results.append(data)
    except Exception as e:
        print(f"Error en la URL {url} - {e}")

driver.quit()

# #Apretar los 3 botones y sacar la info de cada uno en una URL
# for i in direccionestipo2:
#     for a in tipo2:
#         driver.get(a)  # Cambia la URL para cada botón

#         # Apretar el botón correspondiente
#         boton = driver.find_element(By.XPATH, i)  # Puedes usar "url" para ubicar el botón si es único en cada página
#         boton.click()
#         time.sleep(1)

#         # Seleccionar todos los Xpath Extradiables
#         nombresku = driver.find_element(By.XPATH, '/html/body/main/section/div[2]/div/section/div[2]/div[1]/div[2]/div[1]/h1/span')
#         price = driver.find_element_by_class_name('product-price')
#         tipoalimento = driver.find_element(By.XPATH, i)

#         resultado_dict = {
#             'nombre': nombresku.text,
#             'tipo_alimento': tipoalimento.text,
#             'precio': price.text
#         }
#         results.append(resultado_dict)

# #Apretar 2 botones y sacar la info de cada uno en una URL  
# for i in direccionestipo3:
#     for a in tipo3:
#         driver.get(a)  # Cambia la URL para cada botón

#         # Apretar el botón correspondiente
#         boton = driver.find_element(By.XPATH, i)  # Puedes usar "url" para ubicar el botón si es único en cada página
#         boton.click()
#         time.sleep(1)

#         # Seleccionar todos los Xpath Extradiables
#         nombresku = driver.find_element(By.XPATH, '/html/body/main/section/div[2]/div/section/div[2]/div[1]/div[2]/div[1]/h1/span')
#         price = driver.find_element_by_class_name('product-price')
#         tipoalimento = driver.find_element(By.XPATH, i)

#         resultado_dict = {
#             'nombre': nombresku.text,
#             'tipo_alimento': tipoalimento.text,
#             'precio': price.text
#         }
#         results.append(resultado_dict)
        

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
							range='centralvet!F2',#CAMBIAR
							valueInputOption='USER_ENTERED',
							body={'values':values}).execute()


#Valores que se pasan a Sheets
values = [[item['SKU'], item['Nombre SKU'], item['Precio']] for item in results]
result = sheet.values().update(spreadsheetId=SPREADSHEET_ID,
							range='centralvet!A2:C83',#CAMBIAR
							valueInputOption='USER_ENTERED',
							body={'values':values}).execute()
print(f"Datos insertados correctamente")
        