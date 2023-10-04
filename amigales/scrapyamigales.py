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
KEY = '../key.json'
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
tipo13 = [ "https://www.amigales.cl/acana-first-feas-gatitos.html",
    "https://www.amigales.cl/fit-formula-gato-adulto-10kg.html",
    "https://www.amigales.cl/fit-formula-perro-senior.html",
    "https://www.amigales.cl/fit-formula-perro-adulto-20kg.html",
    "https://www.amigales.cl/fit-formula-cachorro-10kg.html",
    "https://www.amigales.cl/beaphar-calmingspot-gatos.html",
    "https://www.amigales.cl/snacks-calmantes-gatos.html"]
tipo13 = ["https://laikamascotas.cl/producto/matisse-alimento-para-gato-castrado-salmon?sku=7898939952704"]
tipo1 = [
    "https://www.amigales.cl/acana-first-feas-gatitos.html",
    "https://www.amigales.cl/fit-formula-gato-adulto-10kg.html",
    "https://www.amigales.cl/fit-formula-perro-senior.html",
    "https://www.amigales.cl/fit-formula-perro-adulto-20kg.html",
    "https://www.amigales.cl/fit-formula-cachorro-10kg.html",
    "https://www.amigales.cl/beaphar-calmingspot-gatos.html",
    "https://www.amigales.cl/snacks-calmantes-gatos.html",
    "https://www.amigales.cl/collar-calmante-gatos.html",
    "https://www.amigales.cl/tabletas-calmantes-beaphar.html",
    "https://www.amigales.cl/feliway-classic-repuesto.html",
    "https://www.amigales.cl/feliway-classic-spray.html",
    "https://www.amigales.cl/feliway-friends-repuesto.html",
    "https://www.amigales.cl/feliway-classic-difusor-repuesto.html",
    "https://www.amigales.cl/feliway-friends-difusor-repuesto.html",
    "https://www.amigales.cl/brit-care-cordero-perros-raza-mediana.html",
    "https://www.amigales.cl/brit-care-conejo-hipoalergenico-perros-sobrepeso.html",
    "https://www.amigales.cl/oven-baked-pollo-perros-11-34-kg.html",
    "https://www.amigales.cl/oven-baked-pescado-perros-11-34-kg.html",
    "https://www.amigales.cl/oven-baked-pollo-perros-senior-11-34-kg.html",
    "https://www.amigales.cl/beaphar-laveta-carnitina.html",
    "https://www.amigales.cl/beaphar-laveta-taurina.html",
    "https://www.amigales.cl/florafix-15g.html",
    "https://www.amigales.cl/naxpet-solucion-oral.html",
    "https://www.amigales.cl/oxtrin.html",
    "https://www.amigales.cl/synulox-250mg.html",
    "https://www.amigales.cl/calmer-calma.html",
    "https://www.amigales.cl/artri-tabs-60-tabletas.html",
    "https://www.amigales.cl/condrovet-30-comprimidos.html",
    "https://www.amigales.cl/wanpy-jerky-cordero.html",
    "https://www.amigales.cl/itraskin-suspension-oral.html",
    "https://www.amigales.cl/sucravet.html",
    "https://www.amigales.cl/dermisolona-30-ml-solucion-oral.html",
    "https://www.amigales.cl/ursovet-drag-pharma.html",
    "https://www.amigales.cl/adaptil-difusor-repuesto.html",
    "https://www.amigales.cl/ohm-comprimidos-calmantes-perros-gatos.html",
    "https://www.amigales.cl/dermisolona-20mg-10-comprimidos.html",
    "https://www.amigales.cl/virbac-allercalm-shampoo.html",
    "https://www.amigales.cl/phisio-anti-olor-auricular.html"
]
tipo2 = ["https://www.centralvet.cl/inicio/22462-21454-acana-classic-prairie-poultry-para-perros.html#/1111111133-peso-113_kg",
"https://www.centralvet.cl/alimentos-de-prescripcion-veterinaria/22768-21711-hills-prescription-diet-rd-para-perros-reduccion-del-peso-a-pedido.html#/1111111259-peso-79_kg"]
tipo3 = ["https://www.centralvet.cl/inicio/21072-21305-brit-care-perro-adulto-medium-breed-cordero-y-arroz.html#/1111111130-peso-12_kg",
"https://www.centralvet.cl/alimentos/23807-23083-brit-care-gato-esterilizado-urinary-health-pollo-fresco-.html#/1111111131-peso-2_kg"]

sku = {
    "petdotu5": "https://www.amigales.cl/revolution-plus-antiparasitario-gatos.html",
    "petdotu6": "https://www.amigales.cl/acana-prairie-poultry-perros.html",
    "petdotu7": "https://www.amigales.cl/acana-wild-coast-perros.html",
    "petdotu8": "https://www.amigales.cl/acana-heritage-puppy-junior-cachorro.html",
    "petdotu10": "https://www.amigales.cl/acana-first-feas-gatitos.html",
    "petdotu11": "https://www.amigales.cl/acana-heritage-freshwater-fish-perros.html",
    "petdotu15": "https://www.amigales.cl/fit-formula-gato-adulto-10kg.html",
    "petdotu16": "https://www.amigales.cl/fit-formula-perro-senior.html",
    "petdotu17": "https://www.amigales.cl/fit-formula-perro-adulto-20kg.html",
    "petdotu18": "https://www.amigales.cl/fit-formula-cachorro-10kg.html",
    "petdotu33": "https://www.amigales.cl/antiparasitario-pipeta-bravecto-gatos.html",
    "petdotu34": "https://www.amigales.cl/beaphar-calmingspot-gatos.html",
    "petdotu36": "https://www.amigales.cl/snacks-calmantes-gatos.html",
    "petdotu37": "https://www.amigales.cl/collar-calmante-gatos.html",
    "petdotu38": "https://www.amigales.cl/tabletas-calmantes-beaphar.html",
    "petdotu39": "https://www.amigales.cl/feliway-classic-repuesto.html",
    "petdotu40": "https://www.amigales.cl/feliway-classic-spray.html",
    "petdotu41": "https://www.amigales.cl/feliway-friends-repuesto.html",
    "petdotu42": "https://www.amigales.cl/feliway-classic-difusor-repuesto.html",
    "petdotu43": "https://www.amigales.cl/feliway-friends-difusor-repuesto.html",
    "petdotu44": "https://www.amigales.cl/royal-canin-mother-baby-cat-1-5kg.html",
    "petdotu47": "https://www.amigales.cl/royal-canin-mini-perro-adulto.html",
    "petdotu48": "https://www.amigales.cl/biljac-adultselect-perros.html",
    "petdotu50": "https://www.amigales.cl/alimento-bil-jac-puppy-select-cachorros.html",
    "petdotu51": "https://www.amigales.cl/brit-care-cordero-arroz-senior.html",
    "petdotu52": "https://www.amigales.cl/brit-care-cordero-arroz-perro-raza-pequena.html",
    "petdotu53": "https://www.amigales.cl/brit-care-cordero-perros-raza-mediana.html",
    "petdotu54": "https://www.amigales.cl/brit-care-cordero-hipoalergenico-cachorros.html",
    "petdotu56": "https://www.amigales.cl/brit-care-conejo-hipoalergenico-perros-sobrepeso.html",
    "petdotu58": "https://www.amigales.cl/brit-cachorros-salmon-papas.html",
    "petdotu59": "https://www.amigales.cl/brit-care-salmon-light-grain-free-perros-senior.html",
    "petdotu61": "https://www.amigales.cl/catalog/product/view/id/5199/s/mixantip-plus-crema/category/2/",
    "petdotu62": "https://www.amigales.cl/oven-baked-pollo-perros-11-34-kg.html",
    "petdotu63": "https://www.amigales.cl/oven-baked-pescado-perros-11-34-kg.html",
    "petdotu64": "https://www.amigales.cl/oven-baked-pollo-perros-senior-11-34-kg.html",
    "petdotu65": "https://www.amigales.cl/beaphar-laveta-carnitina.html",
    "petdotu66": "https://www.amigales.cl/beaphar-laveta-taurina.html",
    "petdotu71": "https://www.amigales.cl/florafix-15g.html",
    "petdotu73": "https://www.amigales.cl/silimavet-silimarina-vitanimal.html",
    "petdotu75": "https://www.amigales.cl/naxpet-solucion-oral.html",
    "petdotu77": "https://www.amigales.cl/oxtrin.html",
    "petdotu79": "https://www.amigales.cl/synulox-250mg.html",
    "petdotu81": "https://www.amigales.cl/calmer-calma.html",
    "petdotu82": "https://www.amigales.cl/artri-tabs-60-tabletas.html",
    "petdotu83": "https://www.amigales.cl/condrovet-30-comprimidos.html",
    "petdotu84": "https://www.amigales.cl/arena-sanitaria-america-litter-ultra-odor-seal.html",
    "petdotu85": "https://www.amigales.cl/hills-metabolic-perros.html",
    "petdotu86": "https://www.amigales.cl/wanpy-jerky-cordero.html",
    "petdotu87": "https://www.amigales.cl/itraskin-suspension-oral.html",
    "petdotu88": "https://www.amigales.cl/hills-small-paws-cachorros.html",
    "petdotu89": "https://www.amigales.cl/sucravet.html",
    "petdotu91": "https://www.amigales.cl/dermisolona-30-ml-solucion-oral.html",
    "petdotu92": "https://www.amigales.cl/ursovet-drag-pharma.html",
    "petdotu93": "https://www.amigales.cl/adaptil-difusor-repuesto.html",
    "petdotu94": "https://www.amigales.cl/ohm-comprimidos-calmantes-perros-gatos.html",
    "petdotu95": "https://www.amigales.cl/dermisolona-20mg-10-comprimidos.html",
    "petdotu98": "https://www.amigales.cl/virbac-allercalm-shampoo.html",
    "petdotu99": "https://www.amigales.cl/hills-rd-perros.html",
    "petdotu100": "https://www.amigales.cl/phisio-anti-olor-auricular.html",
    "petdotu96": "https://www.amigales.cl/collar-adaptil.html"
}
sku2 = {"petdotu5": "https://www.amigales.cl/revolution-plus-antiparasitario-gatos.html"}
results = []

#Tipo 1
for sku_key, url in sku.items():
    driver.get(url)
    try:
        nombresku = driver.find_element("xpath", '/html/body/div[2]/main/div[3]/div/div[1]/div[1]/h1/span') # Cambiar 
        precio = driver.find_element("xpath", '/html/body/div[2]/main/div[3]/div/div[1]/div[4]/div[1]/span/span/span[2]/span') # Cambiar
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

#Tipo 2
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

#Tipo 3
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
							range='amigales!F2',#CAMBIAR
							valueInputOption='USER_ENTERED',
							body={'values':values}).execute()


#Valores que se pasan a Sheets
values = [[item['SKU'], item['Nombre SKU'], item['Precio']] for item in results]
result = sheet.values().update(spreadsheetId=SPREADSHEET_ID,
							range='amigales!A2:C83',#CAMBIAR
							valueInputOption='USER_ENTERED',
							body={'values':values}).execute()
print(f"Datos insertados correctamente")