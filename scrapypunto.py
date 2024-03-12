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

tipo1 = [
    "https://puntomascotas.cl/cicatrizantes/37170-apoquel-16-mg-x-20-comprimidos-5414736044217.html",
    "https://puntomascotas.cl/cicatrizantes/37171-apoquel-36-mg-x-20-comprimidos-5414736044194.html",
    "https://puntomascotas.cl/cicatrizantes/37172-apoquel-54-mg-x-20-comprimidos-5414736044200.html",
    "https://puntomascotas.cl/farmacia-veterinaria/38466-revolution-6-gatos-hasta-75-kg-7804650310136.html",
    "https://puntomascotas.cl/farmacia-veterinaria/38467-revolution-plus-25-a-5-kg-7804650310136.html",
    "https://puntomascotas.cl/acana/35557-acana-heritage-freshwater-fish-21kg-64992502256.html",
    "https://puntomascotas.cl/acana/35555-acana-heritage-free-run-poultry-21-kg-64992501259.html",
    "https://puntomascotas.cl/simparica/38343-simparica-13-a-25-kg-3-comprimidos.html",
    "https://puntomascotas.cl/simparica/38344-simparica-13-a-25-kg-3-comprimidos.html",
    "https://puntomascotas.cl/simparica/38342-simparica-13-a-25-kg-3-comprimidos.html",
    "https://puntomascotas.cl/simparica/38341-simparica-13-a-25-kg-3-comprimidos.html",
    "https://puntomascotas.cl/simparica/38339-simparica-13-a-25-kg-3-comprimidos.html",
    "https://puntomascotas.cl/simparica/38340-simparica-13-a-25-kg-3-comprimidos.html",
    "https://puntomascotas.cl/farmacia-veterinaria/30520-rimadyl-100-mg-60-comprimidos-7804650310884.html",
    "https://puntomascotas.cl/farmacia-veterinaria/32656-rimadyl-100-mg-14-comprimidos-7804650310891.html",
    "https://puntomascotas.cl/farmacia-veterinaria/34139-bravecto-2-a-45-kg-8713184148957.html",
    "https://puntomascotas.cl/farmacia-veterinaria/34141-bravecto-2-a-45-kg-8713184148964.html",
    "https://puntomascotas.cl/farmacia-veterinaria/34140-bravecto-2-a-45-kg-8713184148971.html",
    "https://puntomascotas.cl/farmacia-veterinaria/38964-bravecto-gato-62-a-125-kg-8713184197696.html",
    "https://puntomascotas.cl/farmacia-veterinaria/34136-bravecto-2-a-45-kg-8713184148988.html",
    "https://puntomascotas.cl/farmacia-veterinaria/38415-bravecto-gato-12-a-28-kg-8713184197689.html",
    "https://puntomascotas.cl/calmante-y-control-ansiedad/35481-spray-calming-felino-beaphar-8711231110896.html",
    "https://puntomascotas.cl/golosinas-para-gatos/37002-golosinas-calmantes-felinas-beaphar-8711231110889.html",
    "https://puntomascotas.cl/calmante-y-control-ansiedad/35483-collar-calming-gatos-beaphar-8711231110902.html",
    "https://puntomascotas.cl/calmante-y-control-ansiedad/35480--tabletas-calamantes-gatos-y-perros-8711231171101.html",
    "https://puntomascotas.cl/farmacia-veterinaria/34964-feliway-difusor-repuesto-48-ml-3411112169603.html",
    "https://puntomascotas.cl/farmacia-veterinaria/30767-feliway-spray-3411112133789.html",
    "https://puntomascotas.cl/farmacia-veterinaria/35604-feliway-difusor-repuesto-48-ml-3411112251230.html",
    "https://puntomascotas.cl/farmacia-veterinaria/35602-feliway-friends-kit-inicial-3411112251186.html",
    "https://puntomascotas.cl/farmacia-veterinaria/30773-dermisolona-7800006005268.html",
    "https://puntomascotas.cl/farmacia-veterinaria/34960-adaptil-collar-large-3411112116652.html",
    "https://puntomascotas.cl/farmacia-veterinaria/34959-adaptil-collar-large-3411112116676.html",
    "https://puntomascotas.cl/farmacia-veterinaria/34200-shampoo-allercalm-7502010422627.html",
    "https://puntomascotas.cl/perros-necesidades-especificas"

]

    
tipo2 = []
tipo3 = []

sku = {
    "petdotu1": "https://puntomascotas.cl/cicatrizantes/37170-apoquel-16-mg-x-20-comprimidos-5414736044217.html",
    "petdotu2": "https://puntomascotas.cl/cicatrizantes/37171-apoquel-36-mg-x-20-comprimidos-5414736044194.html",
    "petdotu3": "https://puntomascotas.cl/cicatrizantes/37172-apoquel-54-mg-x-20-comprimidos-5414736044200.html",
    "petdotu4": "https://puntomascotas.cl/farmacia-veterinaria/38466-revolution-6-gatos-hasta-75-kg-7804650310136.html",
    "petdotu5": "https://puntomascotas.cl/farmacia-veterinaria/38467-revolution-plus-25-a-5-kg-7804650310136.html",
    "petdotu11": "https://puntomascotas.cl/acana/35557-acana-heritage-freshwater-fish-21kg-64992502256.html",
    "petdotu12": "https://puntomascotas.cl/acana/35555-acana-heritage-free-run-poultry-21-kg-64992501259.html",
    "petdotu20": "https://puntomascotas.cl/simparica/38343-simparica-13-a-25-kg-3-comprimidos.html",
    "petdotu21": "https://puntomascotas.cl/simparica/38344-simparica-13-a-25-kg-3-comprimidos.html",
    "petdotu22": "https://puntomascotas.cl/simparica/38342-simparica-13-a-25-kg-3-comprimidos.html",
    "petdotu23": "https://puntomascotas.cl/simparica/38341-simparica-13-a-25-kg-3-comprimidos.html",
    "petdotu24": "https://puntomascotas.cl/simparica/38339-simparica-13-a-25-kg-3-comprimidos.html",
    "petdotu25": "https://puntomascotas.cl/simparica/38340-simparica-13-a-25-kg-3-comprimidos.html",
    "petdotu26": "https://puntomascotas.cl/farmacia-veterinaria/30520-rimadyl-100-mg-60-comprimidos-7804650310884.html",
    "petdotu27": "https://puntomascotas.cl/farmacia-veterinaria/32656-rimadyl-100-mg-14-comprimidos-7804650310891.html",
    "petdotu28": "https://puntomascotas.cl/farmacia-veterinaria/34139-bravecto-2-a-45-kg-8713184148957.html",
    "petdotu29": "https://puntomascotas.cl/farmacia-veterinaria/34141-bravecto-2-a-45-kg-8713184148964.html",
    "petdotu30": "https://puntomascotas.cl/farmacia-veterinaria/34140-bravecto-2-a-45-kg-8713184148971.html",
    "petdotu31": "https://puntomascotas.cl/farmacia-veterinaria/38964-bravecto-gato-62-a-125-kg-8713184197696.html",
    "petdotu32": "https://puntomascotas.cl/farmacia-veterinaria/34136-bravecto-2-a-45-kg-8713184148988.html",
    "petdotu33": "https://puntomascotas.cl/farmacia-veterinaria/38415-bravecto-gato-12-a-28-kg-8713184197689.html",
    "petdotu35": "https://puntomascotas.cl/calmante-y-control-ansiedad/35481-spray-calming-felino-beaphar-8711231110896.html",
    "petdotu36": "https://puntomascotas.cl/golosinas-para-gatos/37002-golosinas-calmantes-felinas-beaphar-8711231110889.html",
    "petdotu37": "https://puntomascotas.cl/calmante-y-control-ansiedad/35483-collar-calming-gatos-beaphar-8711231110902.html",
    "petdotu38": "https://puntomascotas.cl/calmante-y-control-ansiedad/35480--tabletas-calamantes-gatos-y-perros-8711231171101.html",
    "petdotu39": "https://puntomascotas.cl/farmacia-veterinaria/34964-feliway-difusor-repuesto-48-ml-3411112169603.html",
    "petdotu40": "https://puntomascotas.cl/farmacia-veterinaria/30767-feliway-spray-3411112133789.html",
    "petdotu41": "https://puntomascotas.cl/farmacia-veterinaria/35604-feliway-difusor-repuesto-48-ml-3411112251230.html",
    "petdotu42": "https://puntomascotas.cl/farmacia-veterinaria/34963-feliway-difusor-repuesto-48-ml-3411112169498.html",
    "petdotu43": "https://puntomascotas.cl/farmacia-veterinaria/35602-feliway-friends-kit-inicial-3411112251186.html",
    "petdotu44": "https://puntomascotas.cl/cats/35445-royal-canin-growth-mother-babycat-15kg-7896181215875.html",
    "petdotu45": "https://puntomascotas.cl/dogs/30118-royal-canin-vet-diet-canino-hypoallergenic-canine-2kg-7896181213543.html",
    "petdotu47": "https://puntomascotas.cl/perros-adulto/35340-royal-canin-mini-adulto-3kg-7896181297857.html",
    "petdotu51": "https://puntomascotas.cl/brit-care/35723-brit-care-senior-cordero-y-arroz-1-kg-8595602510009.html",
    "petdotu52": "https://puntomascotas.cl/brit-care/35714-brit-care-adult-small-cordero-y-arroz-1-kg-8595602509881.html",
    "petdotu53": "https://puntomascotas.cl/brit-care/35717-brit-care-adult-medium-cordero-y-arroz-8595602509928.html",
    "petdotu54": "https://puntomascotas.cl/brit-care/35708-brit-care-puppy-large-cordero-y-arroz-8595602509799.html",
    "petdotu55": "https://puntomascotas.cl/cats/38991-brit-care-sterilized-urinary-7-kg-8595602540723.html",
    "petdotu56": "https://puntomascotas.cl/brit-care/35378-brit-care-weight-loss-conejo-y-arroz-12kg-8595602510313.html",
    "petdotu57": "https://puntomascotas.cl/brit-care/35376-brit-care-libre-de-grano-adult-salmon-12kg-8595602510139.html",
    "petdotu58": "https://puntomascotas.cl/brit-care/35372-brit-care-puppy-salmon-papas-8595602510047.html",
    "petdotu59": "https://puntomascotas.cl/brit-care/35380-brit-care-libre-de-granos-senior-y-light-salmon-12-kg-8595602510269.html",
    "petdotu60": "https://puntomascotas.cl/farmacia-veterinaria/33556-mixantip-plus-crema-50gr-7800006008221.html",
    "petdotu61": "https://puntomascotas.cl/farmacia-veterinaria/30441-mixantip-plus-crema-15gr-7800006003455.html",
    "petdotu62": "https://puntomascotas.cl/oven-baked/37104-oven-baked-adult-pollo-todas-las-razas-1134kg-669066001651.html",
    "petdotu63": "https://puntomascotas.cl/oven-baked/37115-oven-baked-perro-adulto-todas-las-razas-pescado-1134kg-669066001781.html",
    "petdotu65": "https://puntomascotas.cl/farmacia-veterinaria/30771-laveta-carnitina-perros-8711231114283.html",
    "petdotu66": "https://puntomascotas.cl/farmacia-veterinaria/30770-laveta-taurina-gatos-8711231114306.html",
    "petdotu67": "https://puntomascotas.cl/nexgard-spectra/37705-nexgard-spectra-301-a-60-kg-7809599501973.html",
    "petdotu68": "https://puntomascotas.cl/nexgard-spectra/37496-nexgard-spectra-301-a-60-kg-7809599501928.html",
    "petdotu69": "https://puntomascotas.cl/nexgard-spectra/37701-nexgard-spectra-301-a-60-kg-7809599501980.html",
    "petdotu70": "https://puntomascotas.cl/nexgard-spectra/37494-nexgard-spectra-301-a-60-kg-7809599501935.html",
    "petdotu71": "https://puntomascotas.cl/farmacia-veterinaria/35477-mira-canis-3547735477.html",
    "petdotu72": "https://puntomascotas.cl/arenas-y-banos-sanitarios/36238-arena-cat-performance-9-kg-6956131001321.html",
    "petdotu73": "https://puntomascotas.cl/farmacia-veterinaria/37025-silimavet-silimarina-30-comprimidos-761887135476.html",
    "petdotu74": "https://puntomascotas.cl/farmacia-veterinaria/35652-slimavet-90-comprimidos-761778204082.html",
    "petdotu75": "https://puntomascotas.cl/farmacia-veterinaria/30437-naxpet-jarabe-7800006006814.html",
    "petdotu76": "https://puntomascotas.cl/farmacia-veterinaria/34417-pederol-250ml-8436529621938.html",
    "petdotu77": "https://puntomascotas.cl/farmacia-veterinaria/30749-oxtrin-comprimidos-7797600000600.html",
    "petdotu79": "https://puntomascotas.cl/farmacia-veterinaria/30600-synulox-250--7804650310952.html",
    "petdotu80": "https://puntomascotas.cl/arenas-y-banos-sanitarios/36402-arena-odour-buster-original-14-kg-895792000273.html",
    "petdotu81": "https://puntomascotas.cl/calmante-y-control-ansiedad/38995-calmer-spray-calamante-30ml-7804613901845.html",
    "petdotu82": "https://puntomascotas.cl/inicio/35487-artritabs-complex-60-comp-714193699711.html",
    "petdotu83": "https://puntomascotas.cl/farmacia-veterinaria/30465-condrovet-comprimidos-7800006005619.html",
    "petdotu84": "https://puntomascotas.cl/arenas-y-banos-sanitarios/40179-arena-america-litter-odor-seal-lavanda-15-kg-6956131001864.html",
    "petdotu85": "https://puntomascotas.cl/dogs/32876-hills-canine-prescription-diet-metabolic-27-kg-52742195209.html",
    "petdotu86": "https://puntomascotas.cl/wanpy/37019-wanpy-lamb-100-grs-6927749840046.html",
    "petdotu88": "https://puntomascotas.cl/dogs/33177-hills-adulto-small-toy-204kg-52742909608.html",
    "petdotu89": "https://puntomascotas.cl/gastro-enterico/36346-sucravet-100ml-7804605270874.html",
    "petdotu90": "https://puntomascotas.cl/farmacia-veterinaria/30444-pacifor-gotas-10ml-7800006000294.html",
    "petdotu91": "https://puntomascotas.cl/farmacia-veterinaria/34167-dermisolona-jarabe-04-30-ml-7800006009891.html",
    "petdotu92": "https://puntomascotas.cl/farmacia-veterinaria/30442-ursovet-60ml-7800006007033.html",
    "petdotu93": "https://puntomascotas.cl/farmacia-veterinaria/34961-adaptil-difusor-y-repuesto-de-48-ml-3411112169252.html",
    "petdotu94": "https://puntomascotas.cl/calmante-y-control-ansiedad/37444-ohm-modulador-de-ansiedad-7798042366804.html",
    "petdotu95": "https://puntomascotas.cl/farmacia-veterinaria/30773-dermisolona-7800006005268.html",
    "petdotu96": "https://puntomascotas.cl/farmacia-veterinaria/34960-adaptil-collar-large-3411112116652.html",
    "petdotu97": "https://puntomascotas.cl/farmacia-veterinaria/34959-adaptil-collar-large-3411112116676.html",
    "petdotu98": "https://puntomascotas.cl/farmacia-veterinaria/34200-shampoo-allercalm-7502010422627.html",
    "petdotu99": "https://puntomascotas.cl/perros-necesidades-especificas/32018-hills-canine-prescription-diet-r-d-798kg-52742862507.html",
    "petdotu100": "https://puntomascotas.cl/farmacia-veterinaria/35518-phisio-anti-olor-limpiador-auricular-100-ml-7502010422641.html"
}
sku1 = {"petdotu1": "https://puntomascotas.cl/cicatrizantes/37170-apoquel-16-mg-x-20-comprimidos-5414736044217.html"}
results = []

#Tipo 1
for sku_key, url in sku.items():
    driver.get(url)
    try:
        nombresku = driver.find_element("xpath", '/html/body/main/section/div/div/div/div/div/section/div[1]/div[1]/div[2]/section/h1') #CAMBIAR
        precio = driver.find_element("xpath", '/html/body/main/section/div/div/div/div/div/section/div[1]/div[1]/div[2]/section/div[1]/div/div[5]/div/form/div[2]/div[1]/span[1]/span[1]')#CAMBIAR

        data = {
            "SKU":sku_key,
            "Nombre SKU": nombresku.text,
            "Precio": precio.text,
              # Si deseas almacenar la URL junto con los datos
        }
        results.append(data)
    except Exception as e:
        print(f"Error en la URL {url} - {e}")
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
        
#Tipo 4

#Tipo 5

#Tipo 6


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
							range='puntomascotas!F2',#CAMBIAR
							valueInputOption='USER_ENTERED',
							body={'values':values}).execute()


#Valores que se pasan a Sheets
values = [[item['SKU'], item['Nombre SKU'], item['Precio']] for item in results]
result = sheet.values().update(spreadsheetId=SPREADSHEET_ID,
							range='puntomascotas!A2:C83',#CAMBIAR
							valueInputOption='USER_ENTERED',
							body={'values':values}).execute()
print(f"Datos insertados correctamente")        