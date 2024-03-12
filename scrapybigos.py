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

direccionestipo2 = ["/html/body/main/section/div[2]/div/section/div[2]/div[1]/div[2]/div[2]/div[2]/form/div[1]/div/ul/li[1]/input",
               "/html/body/main/section/div[2]/div/section/div[2]/div[1]/div[2]/div[2]/div[2]/form/div[1]/div/ul/li[2]/input",
               "/html/body/main/section/div[2]/div/section/div[2]/div[1]/div[2]/div[2]/div[2]/form/div[1]/div/ul/li[3]/input"]
direccionestipo3 = ["/html/body/main/section/div[2]/div/section/div[2]/div[1]/div[2]/div[2]/div[2]/form/div[1]/div/ul/li[1]/input",
               "/html/body/main/section/div[2]/div/section/div[2]/div[1]/div[2]/div[2]/div[2]/form/div[1]/div/ul/li[2]/input"]



# #URLs
sku = {
    "petdotu1": "https://www.bigos.cl/farmacia-mascotas/7921-apoquel-16-mgs-20-tabletas-5414736044217.html",
    "petdotu2": "https://www.bigos.cl/farmacia-mascotas/7920-apoquel-36-mgs-20-tabletas-5414736044194.html",
    "petdotu3": "https://www.bigos.cl/farmacia-mascotas/7341-apoquel-54-mgs-20-tabletas-5414736044200.html",
    "petdotu4": "https://www.bigos.cl/antiparasitarios-para-gatos/7993-revolution-plus-gatos-25-a-5-kgs-antiparasitario-5414736042992.html",
    "petdotu5": "https://www.bigos.cl/antiparasitarios-para-gatos/7994-revolution-plus-gatos-hasta-25-kg-antiparasitario-5414736042985.html",
    "petdotu8": "https://www.bigos.cl/alimentos-para-perros/4500-31-acana-puppy-and-junior-para-cachorros.html#/506-tamano-113_kg_saco",
    "petdotu9": "https://www.bigos.cl/alimentos-para-gatos/6845-acana-bountiful-catch-para-gatos.html",
    "petdotu10": "https://www.bigos.cl/alimentos-para-gatos/6843-398-acana-first-feast-kitten-para-gatitos.html#/501-tamano-18_kg_bolsa",
    "petdotu11": "https://www.bigos.cl/alimentos-para-perros/4498-40-acana-freshwater-fish-para-perros.html#/506-tamano-113_kg_saco",
    "petdotu12": "https://www.bigos.cl/alimentos-para-perros/4496-46-acana-free-run-poultry-para-perros.html#/506-tamano-113_kg_saco",
    "petdotu13": "https://www.bigos.cl/alimentos-para-perros/4502-34-acana-light-and-fit-para-perros.html#/506-tamano-113_kg_saco",
    "petdotu20": "https://www.bigos.cl/antiparasitarios-para-perros/6785-simparica-antiparasitario-20-a-40-kgs-3-comp-7804650311096.html",
    "petdotu21": "https://www.bigos.cl/antiparasitarios-para-perros/6788-simparica-antiparasitario-20-a-40-kgs-1-comp-7804650311164.html",
    "petdotu22": "https://www.bigos.cl/antiparasitarios-para-perros/6787-simparica-antiparasitario-10-a-20-kgs-1-comp-7804650311157.html",
    "petdotu23": "https://www.bigos.cl/antiparasitarios-para-perros/6784-simparica-antiparasitario-10-a-20-kgs-3-comp-7804650311089.html",
    "petdotu24": "https://www.bigos.cl/antiparasitarios-para-perros/6769-simparica-antiparasitario-5-a-10-kgs-3-comp-7804650311072.html",
    "petdotu25": "https://www.bigos.cl/antiparasitarios-para-perros/6768-simparica-antiparasitario-5-a-10-kgs-1-comp-7804650311140.html",
    "petdotu27": "https://www.bigos.cl/farmacia-mascotas/8274-rimadyl-100-mg-14-tabletas-7804650310891.html",
    "petdotu28": "https://www.bigos.cl/antiparasitarios-para-perros/7316-bravecto-antiparasitario-perros-20-a-40-kgs-8713184148957.html",
    "petdotu29": "https://www.bigos.cl/antiparasitarios-para-perros/7317-bravecto-antiparasitario-perros-10-a-20-kgs-8713184148964.html",
    "petdotu30": "https://www.bigos.cl/antiparasitarios-para-perros/7318-bravecto-antiparasitario-perros-45-a-10-kgs-8713184148971.html",
    "petdotu31": "https://www.bigos.cl/antiparasitarios-para-gatos/5539-bravecto-gatos-spot-on-desde-28-kgs-8713184194640.html",
    "petdotu37": "https://www.bigos.cl/calmantes-para-gatos/4842-beaphar-calming-collar-gato-8711231175840.html",
    "petdotu38": "https://www.bigos.cl/calmantes-para-gatos/5200-beaphar-calming-tabletas-gato-perro-8711231175772.html",
    "petdotu39": "https://www.bigos.cl/calmantes-para-gatos/4168-feliway-friends-repuesto-48-ml-3411112251230.html",
    "petdotu40": "https://www.bigos.cl/calmantes-para-gatos/3263-feliway-clasico-en-spray-60-ml-3411112133789.html",
    "petdotu42": "https://www.bigos.cl/calmantes-para-gatos/feliway-clasico-difusor-carga-48-ml",
    "petdotu43": "https://www.bigos.cl/calmantes-para-gatos/3775-feliway-friends-difusor-carga-3411112251186.html",
    "petdotu82": "https://www.bigos.cl/vitaminas-para-perros/9057-artri-tabs-suplemento-articulaciones-para-perros-60-tab-714193699711.html",
    "petdotu83": "https://www.bigos.cl/vitaminas-para-perros/7106-dragpharma-condrovet-30-comp-7800006005619.html",
    "petdotu86": "https://www.bigos.cl/snacks-para-perros/5045-wanpy-lamb-jerky-strips-100-grs-6927749840046.html",
    "petdotu93": "https://www.bigos.cl/calmantes-y-relajantes-para-perros/8039-adaptil-difusor-repuesto-48-ml-relajante-perro-3411112169252.html",
    "petdotu96": "https://www.bigos.cl/calmantes-y-relajantes-para-perros/4166-adaptil-collar-pequeno-mediano-3411112116652.html",
    "petdotu97": "https://www.bigos.cl/calmantes-y-relajantes-para-perros/4167-adaptil-collar-mediano-grande-3411112116676.html"
}

sku2 = {"petdotu97": "https://www.bigos.cl/calmantes-y-relajantes-para-perros/4167-adaptil-collar-mediano-grande-3411112116676.html"}
results = []

#Tipo 1
for sku_key, url in sku.items():
    driver.get(url)
    try:
        nombresku = driver.find_element("xpath", '/html/body/div[3]/div[1]/div[1]/div/main/div/section[1]/div[1]/div/div[1]/div[2]/div/div[1]/div/h1') # Cambiar 
        precio = driver.find_element("xpath", '/html/body/div[3]/div[1]/div[1]/div/main/div/section[1]/div[1]/div/div[1]/div[2]/div/div[2]/div[3]/div[1]/div[2]/div/span[5]') # Cambiar
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
							range='bigos!F2',#CAMBIAR
							valueInputOption='USER_ENTERED',
							body={'values':values}).execute()


#Valores que se pasan a Sheets
values = [[item['SKU'], item['Nombre SKU'], item['Precio']] for item in results]
result = sheet.values().update(spreadsheetId=SPREADSHEET_ID,
							range='bigos!A2:C83',#CAMBIAR
							valueInputOption='USER_ENTERED',
							body={'values':values}).execute()
print(f"Datos insertados correctamente")