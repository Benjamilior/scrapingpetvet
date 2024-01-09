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

#Google Sheets
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
KEY = '../key.json'
SPREADSHEET_ID = '1PrHE2FBeBhQnVYeCLQclLqj_tiIOq7z3JuMAG-2aAXg'
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




#URLs

urls = ["https://www.petclick.cl/medicamentos/452-apoquel-36mg-comprimidos-5414736044194.html"]

urls2 = [
    "https://www.petclick.cl/medicamentos/453-apoquel-16mg-comprimidos-5414736044217.html",
    "https://www.petclick.cl/medicamentos/452-apoquel-36mg-comprimidos-5414736044194.html",
    "https://www.petclick.cl/medicamentos/466-apoquel-54mg-comprimidos-5414736044200.html",
    "https://www.petclick.cl/antiparasitarios/609-revolution-plus-gatos-25-a-5kg-5414736042992.html",
    "https://www.petclick.cl/antiparasitarios/608-revolution-plus-gatos-125-a-25kg-5414736042985.html",
    "https://www.petclick.cl/alimentos-grain-free/675-acana-puppy-114kg.html",
    "https://www.petclick.cl/alimentos-grain-free/702-acana-bountiful-catch-45kg.html",
    "https://www.petclick.cl/alimentos-grain-free/698-acana-first-feast-cat.html",
    "https://www.petclick.cl/alimentos-grain-free/672-537-acana-freshwater-fish-recipe.html#/117-tamano-114kg",
    "https://www.petclick.cl/alimentos-grain-free/671-acana-free-run-poultry-1135kg.html",
    "https://www.petclick.cl/alimentos-grain-free/677-acana-light-fit-114kg.html",
    "https://www.petclick.cl/alimentos-grain-free/685-acana-singles-duck-pear-1135kg.html",
    "https://www.petclick.cl/alimento-para-gatos/213-fit-formula-gato-10kg.html",
    "https://www.petclick.cl/alimento-para-perros/649-fit-formula-senior-20kg.html",
    "https://www.petclick.cl/alimento-para-perros/78-fit-formula-adulto-20kg-7804658500034.html",
    "https://www.petclick.cl/alimento-para-perros/79-fit-formula-cachorro-10kg-7804658500027.html",
    "https://www.petclick.cl/alimento-para-perros/648-fit-formula-raza-pequena-10kg.html",
    "https://www.petclick.cl/medicamentos/413-rimadyl-100mg-60-comprimidos-7804650310884.html",
    "https://www.petclick.cl/medicamentos/296-rimadyl-100mg-14-comprimidos-7804650310891.html",
    "https://www.petclick.cl/antiparasitarios/69-bravecto-20-40kg-8713184148957.html",
    "https://www.petclick.cl/antiparasitarios/68-bravecto-10-20kg-8713184148964.html",
    "https://www.petclick.cl/antiparasitarios/67-bravecto-45-10kg-8713184148971.html",
    "https://www.petclick.cl/antiparasitarios/601-bravecto-gatos-pipeta-28-a-625kg-8713184194640.html",
    "https://www.petclick.cl/antiparasitarios/66-bravecto-2-45kg-8713184148988.html",
    "https://www.petclick.cl/antiparasitarios/600-bravecto-gatos-pipeta-12-a-28kg-8713184197689.html",
    "https://www.petclick.cl/entrenamiento-y-comportamiento/521-calming-home-spray-125ml-8711231110896.html",
    "https://www.petclick.cl/entrenamiento-y-comportamiento/539-calming-cat-treats-35g-8711231175789.html",
    "https://www.petclick.cl/entrenamiento-y-comportamiento/471-calming-collar-para-gatos-8711231175840.html",
    "https://www.petclick.cl/entrenamiento-y-comportamiento/473-feliway-classic-repuesto-48ml-3411112169603.html",
    "https://www.petclick.cl/entrenamiento-y-comportamiento/474-feliway-classic-spray-60ml-3411112133789.html",
    "https://www.petclick.cl/entrenamiento-y-comportamiento/905-feliway-friends-repuesto-48ml-3411112251230.html",
    "https://www.petclick.cl/entrenamiento-y-comportamiento/472-feliway-classic-difusor-repuesto-48ml-3411112169498.html",
    "https://www.petclick.cl/alimentos-medicados/109-52-royal-canin-hypoallergenic-7896181213543.html#/13-tamano-2kg",
    "https://www.petclick.cl/alimento-para-perros/423-brit-care-senior-cordero-y-arroz-12kg-8595602510009.html",
    "https://www.petclick.cl/alimento-para-perros/419-brit-care-adult-small-breed-cordero-75kg-8595602509881.html",
    "https://www.petclick.cl/alimento-para-perros/420-brit-care-adult-medium-cordero-12kg-8595602509928.html",
    "https://www.petclick.cl/alimento-para-perros-cachorros/416-brit-care-puppy-cordero-y-arroz-12kg-8595602509799.html",
    "https://www.petclick.cl/alimento-para-gatos/787-brit-care-cat-sterilized-urinary-7kg.html",
    "https://www.petclick.cl/alimento-para-perros/425-brit-care-weight-loss-conejo-y-arroz-12kg-8595602510313.html",
    "https://www.petclick.cl/alimentos-grain-free/430-brit-care-grain-free-adult-salmon-12kg-8595602510139.html",
    "https://www.petclick.cl/alimento-para-perros-cachorros/427-brit-care-grain-free-puppy-salmon-12kg-8595602510047.html",
    "https://www.petclick.cl/alimentos-grain-free/432-brit-care-senior-light-salmon-12kg-8595602510269.html",
    "https://www.petclick.cl/medicamentos/342-mixantip-plus-crema-15g.html",
    "https://www.petclick.cl/medicamentos/338-laveta-carnitina-50ml-para-perros-8711231114283.html",
    "https://www.petclick.cl/medicamentos/339-laveta-taurina-50ml-para-gatos-8711231114306.html",
    "https://www.petclick.cl/medicamentos/638-florafix-pet-pasta-15g.html",
    "https://www.petclick.cl/medicamentos/499-silimarina-vitanimal-30-comprimidos-0761887135476.html",
    "https://www.petclick.cl/medicamentos/529-silimarina-vitanimal-90-comprimidos-761778204082.html",
    "https://www.petclick.cl/medicamentos/294-naxpet-20ml-suspension-oral-7800006006814.html",
    "https://www.petclick.cl/medicamentos/346-oxtrin-30-comprimidos-7797600000600.html",
    "https://www.petclick.cl/medicamentos/355-synulox-250mg-comprimidos-7804650310952.html",
    "https://www.petclick.cl/medicamentos/646-artri-tabs-complex-60-comprimidos.html",
    "https://www.petclick.cl/medicamentos/411-condrovet-comprimidos-7800006005619.html",
    "https://www.petclick.cl/medicamentos/336-itraskin-120ml-suspension-oral-7800006007132.html",
    "https://www.petclick.cl/medicamentos/354-sucravet-jarabe-100ml-7804605270874.html",
    "https://www.petclick.cl/medicamentos/298-pacifor-gotas-10ml-7800006000294.html",
    "https://www.petclick.cl/medicamentos/320-dermisolona-jarabe-30ml-7800006009891.html",
    "https://www.petclick.cl/medicamentos/358-ursovet-jarabe-60ml-7800006007033.html",
    "https://www.petclick.cl/entrenamiento-y-comportamiento/652-adaptil-calm-home-difusor-repuesto-48ml-3411112169252.html",
    "https://www.petclick.cl/medicamentos/560-ohm-comprimidos-modulador-de-ansiedad-7798042366804.html",
    "https://www.petclick.cl/medicamentos/319-dermisolona-20mg-comprimidos-7800006005268.html",
    "https://www.petclick.cl/entrenamiento-y-comportamiento/235-adaptil-collar-perros-pequenos-s-m-3411112116652.html",
    "https://www.petclick.cl/entrenamiento-y-comportamiento/236-adaptil-collar-perros-medianos-y-grandes-m-l-3411112116676.html",
    "https://www.petclick.cl/shampoos-medicados/247-allercalm-shampoo-con-avena-250ml-7502010422627.html",
    "https://www.petclick.cl/alimentos-medicados/397-hills-rd-weight-reduction-798kg.html",
    "https://www.petclick.cl/medicamentos/341-phisio-antiolor-100ml-limpiador-auricular-7502010422641.html",
    "https://www.petclick.cl/antiparasitarios/85-670-nexgard-spectra-76-a-15kg.html#/120-envase-3_comprimidos",
    "https://www.petclick.cl/antiparasitarios/85-669-nexgard-spectra-76-a-15kg.html#/119-envase-1_comprimido",
    "https://www.petclick.cl/antiparasitarios/86-671-nexgard-spectra-15-a-30kg.html#/119-envase-1_comprimido"
]
sku1= {"petdotu1": "https://www.petclick.cl/medicamentos/453-apoquel-16mg-comprimidos-5414736044217.html"}
sku= {
    "petdotu1": "https://www.petclick.cl/medicamentos/453-apoquel-16mg-comprimidos-5414736044217.html",
    "petdotu2": "https://www.petclick.cl/medicamentos/452-apoquel-36mg-comprimidos-5414736044194.html",
    "petdotu3": "https://www.petclick.cl/medicamentos/466-apoquel-54mg-comprimidos-5414736044200.html",
    "petdotu4": "https://www.petclick.cl/antiparasitarios/609-revolution-plus-gatos-25-a-5kg-5414736042992.html",
    "petdotu5": "https://www.petclick.cl/antiparasitarios/608-revolution-plus-gatos-125-a-25kg-5414736042985.html",
    "petdotu8": "https://www.petclick.cl/alimentos-grain-free/675-acana-puppy-114kg.html",
    "petdotu9": "https://www.petclick.cl/alimentos-grain-free/702-acana-bountiful-catch-45kg.html",
    "petdotu10": "https://www.petclick.cl/alimentos-grain-free/698-acana-first-feast-cat.html",
    "petdotu11": "https://www.petclick.cl/alimentos-grain-free/672-537-acana-freshwater-fish-recipe.html#/117-tamano-114kg",
    "petdotu12": "https://www.petclick.cl/alimentos-grain-free/671-acana-free-run-poultry-1135kg.html",
    "petdotu13": "https://www.petclick.cl/alimentos-grain-free/677-acana-light-fit-114kg.html",
    "petdotu14": "https://www.petclick.cl/alimentos-grain-free/685-acana-singles-duck-pear-1135kg.html",
    "petdotu15": "https://www.petclick.cl/alimento-para-gatos/213-fit-formula-gato-10kg.html",
    "petdotu16": "https://www.petclick.cl/alimento-para-perros/649-fit-formula-senior-20kg.html",
    "petdotu17": "https://www.petclick.cl/alimento-para-perros/78-fit-formula-adulto-20kg-7804658500034.html",
    "petdotu18": "https://www.petclick.cl/alimento-para-perros/79-fit-formula-cachorro-10kg-7804658500027.html",
    "petdotu19": "https://www.petclick.cl/alimento-para-perros/648-fit-formula-raza-pequena-10kg.html",
    "petdotu26": "https://www.petclick.cl/medicamentos/413-rimadyl-100mg-60-comprimidos-7804650310884.html",
    "petdotu27": "https://www.petclick.cl/medicamentos/296-rimadyl-100mg-14-comprimidos-7804650310891.html",
    "petdotu28": "https://www.petclick.cl/antiparasitarios/69-bravecto-20-40kg-8713184148957.html",
    "petdotu29": "https://www.petclick.cl/antiparasitarios/68-bravecto-10-20kg-8713184148964.html",
    "petdotu30": "https://www.petclick.cl/antiparasitarios/67-bravecto-45-10kg-8713184148971.html",
    "petdotu31": "https://www.petclick.cl/antiparasitarios/601-bravecto-gatos-pipeta-28-a-625kg-8713184194640.html",
    "petdotu32": "https://www.petclick.cl/antiparasitarios/66-bravecto-2-45kg-8713184148988.html",
    "petdotu33": "https://www.petclick.cl/antiparasitarios/600-bravecto-gatos-pipeta-12-a-28kg-8713184197689.html",
    "petdotu35": "https://www.petclick.cl/entrenamiento-y-comportamiento/521-calming-home-spray-125ml-8711231110896.html",
    "petdotu36": "https://www.petclick.cl/entrenamiento-y-comportamiento/539-calming-cat-treats-35g-8711231175789.html",
    "petdotu37": "https://www.petclick.cl/entrenamiento-y-comportamiento/471-calming-collar-para-gatos-8711231175840.html",
    "petdotu39": "https://www.petclick.cl/entrenamiento-y-comportamiento/473-feliway-classic-repuesto-48ml-3411112169603.html",
    "petdotu40": "https://www.petclick.cl/entrenamiento-y-comportamiento/474-feliway-classic-spray-60ml-3411112133789.html",
    "petdotu41": "https://www.petclick.cl/entrenamiento-y-comportamiento/905-feliway-friends-repuesto-48ml-3411112251230.html",
    "petdotu42": "https://www.petclick.cl/entrenamiento-y-comportamiento/472-feliway-classic-difusor-repuesto-48ml-3411112169498.html",
    "petdotu45": "https://www.petclick.cl/alimentos-medicados/109-52-royal-canin-hypoallergenic-7896181213543.html#/13-tamano-2kg",
    "petdotu51": "https://www.petclick.cl/alimento-para-perros/423-brit-care-senior-cordero-y-arroz-12kg-8595602510009.html",
    "petdotu52": "https://www.petclick.cl/alimento-para-perros/419-brit-care-adult-small-breed-cordero-75kg-8595602509881.html",
    "petdotu53": "https://www.petclick.cl/alimento-para-perros/420-brit-care-adult-medium-cordero-12kg-8595602509928.html",
    "petdotu54": "https://www.petclick.cl/alimento-para-perros-cachorros/416-brit-care-puppy-cordero-y-arroz-12kg-8595602509799.html",
    "petdotu55": "https://www.petclick.cl/alimento-para-gatos/787-brit-care-cat-sterilized-urinary-7kg.html",
    "petdotu56": "https://www.petclick.cl/alimento-para-perros/425-brit-care-weight-loss-conejo-y-arroz-12kg-8595602510313.html",
    "petdotu57": "https://www.petclick.cl/alimentos-grain-free/430-brit-care-grain-free-adult-salmon-12kg-8595602510139.html",
    "petdotu58": "https://www.petclick.cl/alimento-para-perros-cachorros/427-brit-care-grain-free-puppy-salmon-12kg-8595602510047.html",
    "petdotu59": "https://www.petclick.cl/alimentos-grain-free/432-brit-care-senior-light-salmon-12kg-8595602510269.html",
    "petdotu61": "https://www.petclick.cl/medicamentos/342-mixantip-plus-crema-15g.html",
    "petdotu65": "https://www.petclick.cl/medicamentos/338-laveta-carnitina-50ml-para-perros-8711231114283.html",
    "petdotu66": "https://www.petclick.cl/medicamentos/339-laveta-taurina-50ml-para-gatos-8711231114306.html",
    "petdotu71": "https://www.petclick.cl/medicamentos/638-florafix-pet-pasta-15g.html",
    "petdotu73": "https://www.petclick.cl/medicamentos/499-silimarina-vitanimal-30-comprimidos-0761887135476.html",
    "petdotu74": "https://www.petclick.cl/medicamentos/529-silimarina-vitanimal-90-comprimidos-761778204082.html",
    "petdotu75": "https://www.petclick.cl/medicamentos/294-naxpet-20ml-suspension-oral-7800006006814.html",
    "petdotu77": "https://www.petclick.cl/medicamentos/346-oxtrin-30-comprimidos-7797600000600.html",
    "petdotu79": "https://www.petclick.cl/medicamentos/355-synulox-250mg-comprimidos-7804650310952.html",
    "petdotu82": "https://www.petclick.cl/medicamentos/646-artri-tabs-complex-60-comprimidos.html",
    "petdotu83": "https://www.petclick.cl/medicamentos/411-condrovet-comprimidos-7800006005619.html",
    "petdotu87": "https://www.petclick.cl/medicamentos/336-itraskin-120ml-suspension-oral-7800006007132.html",
    "petdotu89": "https://www.petclick.cl/medicamentos/354-sucravet-jarabe-100ml-7804605270874.html",
    "petdotu90": "https://www.petclick.cl/medicamentos/298-pacifor-gotas-10ml-7800006000294.html",
    "petdotu91": "https://www.petclick.cl/medicamentos/320-dermisolona-jarabe-30ml-7800006009891.html",
    "petdotu92": "https://www.petclick.cl/medicamentos/358-ursovet-jarabe-60ml-7800006007033.html",
    "petdotu93": "https://www.petclick.cl/entrenamiento-y-comportamiento/652-adaptil-calm-home-difusor-repuesto-48ml-3411112169252.html",
    "petdotu94": "https://www.petclick.cl/medicamentos/560-ohm-comprimidos-modulador-de-ansiedad-7798042366804.html",
    "petdotu95": "https://www.petclick.cl/medicamentos/319-dermisolona-20mg-comprimidos-7800006005268.html",
    "petdotu96": "https://www.petclick.cl/entrenamiento-y-comportamiento/235-adaptil-collar-perros-pequenos-s-m-3411112116652.html",
    "petdotu97": "https://www.petclick.cl/entrenamiento-y-comportamiento/236-adaptil-collar-perros-medianos-y-grandes-m-l-3411112116676.html",
    "petdotu98": "https://www.petclick.cl/shampoos-medicados/247-allercalm-shampoo-con-avena-250ml-7502010422627.html",
    "petdotu99": "https://www.petclick.cl/alimentos-medicados/397-hills-rd-weight-reduction-798kg.html",
    "petdotu100": "https://www.petclick.cl/medicamentos/341-phisio-antiolor-100ml-limpiador-auricular-7502010422641.html",
    "petdotu67": "https://www.petclick.cl/antiparasitarios/85-670-nexgard-spectra-76-a-15kg.html#/120-envase-3_comprimidos",
    "petdotu68": "https://www.petclick.cl/antiparasitarios/85-669-nexgard-spectra-76-a-15kg.html#/119-envase-1_comprimido",
    "petdotu70": "https://www.petclick.cl/antiparasitarios/86-671-nexgard-spectra-15-a-30kg.html#/119-envase-1_comprimido",
}

results = []

for sku_key, url in sku.items():
    driver.get(url)
    try:
        nombresku = driver.find_element("xpath", '/html/body/main/section/div/div/div/section/div[1]/div[2]/h1') # Cambiar 
        precio = driver.find_element("xpath", '/html/body/main/section/div/div/div/section/div[1]/div[2]/div[1]/div[1]/div/span') # Cambiar
        data = {
            "SKU":sku_key,
            "Nombre SKU": nombresku.text,
            "Precio": precio.text,
              # Si deseas almacenar la URL junto con los datos
        }
        results.append(data)
        
        print(data)
    except Exception as e:
        print(f"Error en la URL {url} - {e}")

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
							range='petclick!F2',#CAMBIAR
							valueInputOption='USER_ENTERED',
							body={'values':values}).execute()


#Valores que se pasan a Sheets
values = [[item['SKU'], item['Nombre SKU'], item['Precio']] for item in results]
result = sheet.values().update(spreadsheetId=SPREADSHEET_ID,
							range='petclick!A2:C83',#CAMBIAR
							valueInputOption='USER_ENTERED',
							body={'values':values}).execute()
print(f"Datos insertados correctamente")

