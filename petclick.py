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

sku= {
    "petdotu1": "https://www.petclick.cl/medicamentos/453-apoquel-16mg-comprimidos-5414736044217.html",
    "petdotu2": "https://www.petclick.cl/medicamentos/452-apoquel-36mg-comprimidos-5414736044194.html",
    "petdotu3": "https://www.petclick.cl/medicamentos/466-apoquel-54mg-comprimidos-5414736044200.html",
    "petdotu197": "https://www.petclick.cl/alimentos-grain-free/699-593-acana-indoor-entree-cat.html",
    "petdotu176": "https://www.petclick.cl/alimentos-grain-free/706-acana-wild-atlantic-cat-45kg.html",
    "petdotu12": "https://www.petclick.cl/alimentos-grain-free/671-acana-free-run-poultry-1135kg.html",
    "petdotu8": "https://www.petclick.cl/alimentos-grain-free/675-acana-puppy-114kg.html",
    "petdotu9": "https://www.petclick.cl/alimentos-grain-free/702-acana-bountiful-catch-45kg.html",
    "petdotu14": "https://www.petclick.cl/alimentos-grain-free/685-acana-singles-duck-pear-1135kg.html",
    "petdotu11": "https://www.petclick.cl/alimentos-grain-free/672-537-acana-freshwater-fish-recipe.html#/117-tamano-114kg",
    "petdotu13": "https://www.petclick.cl/alimentos-grain-free/677-acana-light-fit-114kg.html",
    "petdotu10": "https://www.petclick.cl/alimentos-grain-free/698-acana-first-feast-cat.html",
    "petdotu45": "https://www.petclick.cl/alimentos-medicados/109-52-royal-canin-hypoallergenic-7896181213543.html#/13-tamano-2kg",
    "petdotu172": "https://www.petclick.cl/antiparasitarios/476-674-nexgard-spectra-36-a-75kg.html#/120-envase-3_comprimidos",
    "petdotu189": "https://www.petclick.cl/antiparasitarios/476-673-nexgard-spectra-36-a-75kg.html",
    "petdotu68": "https://www.petclick.cl/antiparasitarios/85-669-nexgard-spectra-76-a-15kg.html#/119-envase-1_comprimido",
    "petdotu67": "https://www.petclick.cl/antiparasitarios/85-670-nexgard-spectra-76-a-15kg.html#/120-envase-3_comprimidos",
    "petdotu70": "https://www.petclick.cl/antiparasitarios/86-671-nexgard-spectra-15-a-30kg.html#/119-envase-1_comprimido",
    "petdotu138": "https://www.petclick.cl/antiparasitarios/87-701-nexgard-spectra-30-a-60kg.html#/120-envase-3_comprimidos",
    "petdotu147": "https://www.petclick.cl/antiparasitarios/87-700-nexgard-spectra-30-a-60kg.html#/119-envase-1_comprimido",
    "petdotu33": "https://www.petclick.cl/antiparasitarios/600-bravecto-gatos-pipeta-12-a-28kg-8713184197689.html",
    "petdotu31": "https://www.petclick.cl/antiparasitarios/601-bravecto-gatos-pipeta-28-a-625kg-8713184194640.html",
    "petdotu32": "https://www.petclick.cl/antiparasitarios/66-bravecto-2-45kg-8713184148988.html",
    "petdotu30": "https://www.petclick.cl/antiparasitarios/67-bravecto-45-10kg-8713184148971.html",
    "petdotu29": "https://www.petclick.cl/antiparasitarios/68-bravecto-10-20kg-8713184148964.html",
    "petdotu28": "https://www.petclick.cl/antiparasitarios/69-bravecto-20-40kg-8713184148957.html",
    "petdotu181": "https://www.petclick.cl/antiparasitarios/70-bravecto-40-56kg-8713184148940.html",
    "petdotu84": "https://www.petclick.cl/arenas-sanitarias-para-gatos/1055-america-litter-ultra-odor-seal-15kg-6956131001321.html",
    "petdotu58": "https://www.petclick.cl/alimento-para-perros-cachorros/427-brit-care-grain-free-puppy-salmon-12kg-8595602510047.html",
    "petdotu52": "https://www.petclick.cl/alimento-para-perros/419-brit-care-adult-small-breed-cordero-75kg-8595602509881.html",
    "petdotu53": "https://www.petclick.cl/alimento-para-perros/420-brit-care-adult-medium-cordero-12kg-8595602509928.html",
    "petdotu54": "https://www.petclick.cl/alimento-para-perros-cachorros/416-brit-care-puppy-cordero-y-arroz-12kg-8595602509799.html",
    "petdotu56": "https://www.petclick.cl/alimento-para-perros/425-brit-care-weight-loss-conejo-y-arroz-12kg-8595602510313.html",
    "petdotu59": "https://www.petclick.cl/alimentos-grain-free/432-brit-care-senior-light-salmon-12kg-8595602510269.html",
    "petdotu51": "https://www.petclick.cl/alimento-para-perros/423-brit-care-senior-cordero-y-arroz-12kg-8595602510009.html",
    "petdotu57": "https://www.petclick.cl/alimentos-grain-free/430-brit-care-grain-free-adult-salmon-12kg-8595602510139.html",
    "petdotu55": "https://www.petclick.cl/alimento-para-gatos/787-brit-care-cat-sterilized-urinary-7kg.html",
    "petdotu106": "https://www.petclick.cl/alimento-para-perros-cachorros/416-brit-care-puppy-cordero-12kg-8595602509799.html",
    "petdotu110": "https://www.petclick.cl/alimento-para-gatos/785-brit-cat-sterilized-weight-control-7kg.html",
    "petdotu116": "https://www.petclick.cl/alimentos-grain-free/430-brit-care-grain-free-adult-salmon-12kg-8595602510139.html",
    "petdotu123": "https://www.petclick.cl/alimento-para-perros-cachorros/428-brit-care-junior-large-breed-salmon-12kg-8595602510092.html",
    "petdotu113": "https://www.petclick.cl/alimento-para-perros-cachorros/417-brit-care-junior-large-cordero-12kg-8595602509836.html",
    "petdotu127": "https://www.petclick.cl/alimento-para-gatos/433-641-brit-care-cat-kitten.html#/13-tamano-2kg",
    "petdotu130": "https://www.petclick.cl/alimento-para-gatos/782-brit-care-cat-haircare-7kg-8595602540877.html",
    "petdotu133": "https://www.petclick.cl/alimento-para-perros-cachorros/415-374-brit-care-puppy-cordero-8595602509805.html#/1-tamano-3kg",
    "petdotu134": "https://www.petclick.cl/alimento-para-gatos/784-brit-care-cat-senior-7kg-8595602540938.html",
    "petdotu136": "https://www.petclick.cl/alimento-para-perros-cachorros/426-390-brit-care-grain-free-puppy-salmon-8595602510061.html#/1-tamano-3kg",
    "petdotu139": "https://www.petclick.cl/alimento-para-perros-adultos/780-brit-care-sensitive-ciervo-12kg-8595602559138.html",
    "petdotu140": "https://www.petclick.cl/alimento-para-perros/424-386-brit-care-weight-loss-conejo-y-arroz-8595602510337.html#/1-tamano-3kg",
    "petdotu155": "https://www.petclick.cl/alimento-para-gatos/464-665-brit-care-cat-sterilized-urinary.html#/13-tamano-2kg",
    "petdotu122": "https://www.petclick.cl/alimento-para-perros/418-379-brit-care-adult-small-breed-cordero-8595602509898.html#/1-tamano-3kg",
    "petdotu27": "https://www.petclick.cl/medicamentos/296-rimadyl-100mg-14-comprimidos-7804650310891.html",
    "petdotu26": "https://www.petclick.cl/medicamentos/413-rimadyl-100mg-60-comprimidos-7804650310884.html",
    "petdotu5": "https://www.petclick.cl/antiparasitarios/608-revolution-plus-gatos-125-a-25kg-5414736042985.html",
    "petdotu4": "https://www.petclick.cl/antiparasitarios/609-revolution-plus-gatos-25-a-5kg-5414736042992.html",
    "petdotu99": "https://www.petclick.cl/alimentos-medicados/397-hills-rd-weight-reduction-798kg.html",
    "petdotu183": "https://www.petclick.cl/alimento-para-perros/376-hills-adult-7-small-bites-68kg.html",
    "petdotu88": "https://www.petclick.cl/alimento-para-perros/366-hills-adult-small-paws-204kg.html",
    "petdotu61": "https://www.petclick.cl/medicamentos/342-mixantip-plus-crema-15g.html",
    "petdotu60": "https://www.petclick.cl/medicamentos/483-mixantip-plus-crema-50g.html",
    "petdotu85": "https://www.petclick.cl/alimentos-medicados/401-hills-metabolic-canine-798kg.html",
    "petdotu97": "https://www.petclick.cl/entrenamiento-y-comportamiento/236-adaptil-collar-perros-medianos-y-grandes-m-l-3411112116676.html",
    "petdotu96": "https://www.petclick.cl/entrenamiento-y-comportamiento/235-adaptil-collar-perros-pequenos-s-m-3411112116652.html",
    "petdotu73": "https://www.petclick.cl/medicamentos/499-silimarina-vitanimal-30-comprimidos-0761887135476.html",
    "petdotu74": "https://www.petclick.cl/medicamentos/529-silimarina-vitanimal-90-comprimidos-761778204082.html",
    "petdotu18": "https://www.petclick.cl/alimento-para-perros/79-fit-formula-cachorro-10kg-7804658500027.html",
    "petdotu15": "https://www.petclick.cl/alimento-para-gatos/213-fit-formula-gato-10kg.html",
    "petdotu82": "https://www.petclick.cl/medicamentos/646-artri-tabs-complex-60-comprimidos.html",
    "petdotu93": "https://www.petclick.cl/entrenamiento-y-comportamiento/652-adaptil-calm-home-difusor-repuesto-48ml-3411112169252.html",
    "petdotu42": "https://www.petclick.cl/entrenamiento-y-comportamiento/472-feliway-classic-difusor-repuesto-48ml-3411112169498.html",
    "petdotu40": "https://www.petclick.cl/entrenamiento-y-comportamiento/474-feliway-classic-spray-60ml-3411112133789.html",
    "petdotu39": "https://www.petclick.cl/entrenamiento-y-comportamiento/473-feliway-classic-repuesto-48ml-3411112169603.html",
    "petdotu66": "https://www.petclick.cl/medicamentos/339-laveta-taurina-50ml-para-gatos-8711231114306.html",
    "petdotu65": "https://www.petclick.cl/medicamentos/338-laveta-carnitina-50ml-para-perros-8711231114283.html",
    "petdotu83": "https://www.petclick.cl/medicamentos/411-condrovet-comprimidos-7800006005619.html",
    "petdotu77": "https://www.petclick.cl/medicamentos/346-oxtrin-30-comprimidos-7797600000600.html",
    "petdotu98": "https://www.petclick.cl/shampoos-medicados/247-allercalm-shampoo-con-avena-250ml-7502010422627.html",
    "petdotu41": "https://www.petclick.cl/entrenamiento-y-comportamiento/905-feliway-friends-repuesto-48ml-3411112251230.html",
    "petdotu35": "https://www.petclick.cl/entrenamiento-y-comportamiento/521-calming-home-spray-125ml-8711231110896.html",
    "petdotu94": "https://www.petclick.cl/medicamentos/560-ohm-comprimidos-modulador-de-ansiedad-7798042366804.html",
    "petdotu89": "https://www.petclick.cl/medicamentos/354-sucravet-jarabe-100ml-7804605270874.html",
    "petdotu36": "https://www.petclick.cl/entrenamiento-y-comportamiento/539-calming-cat-treats-35g-8711231175789.html",
    "petdotu37": "https://www.petclick.cl/entrenamiento-y-comportamiento/471-calming-collar-para-gatos-8711231175840.html",
    "petdotu79": "https://www.petclick.cl/medicamentos/355-synulox-250mg-comprimidos-7804650310952.html",
    "petdotu92": "https://www.petclick.cl/medicamentos/358-ursovet-jarabe-60ml-7800006007033.html",
    "petdotu71": "https://www.petclick.cl/medicamentos/638-florafix-pet-pasta-15g.html",
    "petdotu75": "https://www.petclick.cl/medicamentos/294-naxpet-20ml-suspension-oral-7800006006814.html",
    "petdotu17": "https://www.petclick.cl/alimento-para-perros/78-fit-formula-adulto-20kg-7804658500034.html",
    "petdotu16": "https://www.petclick.cl/alimento-para-perros/649-fit-formula-senior-20kg.html",
    "petdotu19": "https://www.petclick.cl/alimento-para-perros/648-fit-formula-raza-pequena-10kg.html",
    "petdotu126": "https://www.petclick.cl/alimento-para-perros/651-fit-formula-senior-raza-pequena-10kg.html",
    "petdotu87": "https://www.petclick.cl/medicamentos/336-itraskin-120ml-suspension-oral-7800006007132.html",
    "petdotu91": "https://www.petclick.cl/medicamentos/320-dermisolona-jarabe-30ml-7800006009891.html",
    "petdotu90": "https://www.petclick.cl/medicamentos/298-pacifor-gotas-10ml-7800006000294.html",
    "petdotu95": "https://www.petclick.cl/medicamentos/319-dermisolona-20mg-comprimidos-7800006005268.html",
    "petdotu100": "https://www.petclick.cl/medicamentos/341-phisio-antiolor-100ml-limpiador-auricular-7502010422641.html",
    "petdotu131": "https://www.petclick.cl/alimentos-grain-free/695-orijen-puppy-107kg.html",
    "petdotu153": "https://www.petclick.cl/alimentos-grain-free/710-orijen-cat-kitten-545kg.html",
    "petdotu114": "https://www.petclick.cl/alimentos-grain-free/697-orijen-small-breed-45kg.html",
    "petdotu125": "https://www.petclick.cl/arenas-sanitarias-para-gatos/1057-america-litter-clean-paws-15kg-6956131000508.html",
    "petdotu108": "https://www.petclick.cl/medicamentos/907-traumeel-veterinario-100-comprimidos-7800093000832.html",
    "petdotu129": "https://www.petclick.cl/medicamentos/1070-galliprant-100mg-comprimidos-5420036980261.html",
    "petdotu142": "https://www.petclick.cl/antiparasitarios/132-advantage-gatos-hasta-4kg-7702123000907.html",
    "petdotu135": "https://www.petclick.cl/antiparasitarios/133-advantage-gatos-entre-4-8kg-4007221042914.html",
    "petdotu143": "https://www.petclick.cl/antiparasitarios-internos/442-drontal-plus-10kg-2-comprimidos-7805750400895.html",
    "petdotu185": "https://www.petclick.cl/antiparasitarios-internos/443-drontal-plus-35kg-7891106003704.html",
    "petdotu188": "https://www.petclick.cl/antiparasitarios-internos/444-drontal-cats-gatos-2-comprimidos.html",
    "petdotu145": "https://www.petclick.cl/medicamentos/1071-neptra-solucion-otica-4007221052333.html",
    "petdotu150": "https://www.petclick.cl/medicamentos/955-osteodrag-ha-30-comprimidos-7800006011269.html",
    "petdotu177": "https://www.petclick.cl/antiparasitarios/598-advocate-perros-10-a-25kg-4007221052661.html",
    "petdotu196": "https://www.petclick.cl/antiparasitarios/599-advocate-perros-25-a-40kg-4007221052647.html",
    "petdotu199": "https://www.petclick.cl/antiparasitarios/597-advocate-perros-4-a-10kg-4007221052654.html",
    "petdotu149": "https://www.petclick.cl/antiparasitarios/527-advocate-gatos-hasta-4kg-4007221048329.html",
    "petdotu115": "https://www.petclick.cl/antiparasitarios/528-advocate-gatos-4-a-8kg-4007221048336.html",
    "petdotu157": "https://www.petclick.cl/medicamentos/297-oftavet-5ml-7800006008238.html",
    "petdotu158": "https://www.petclick.cl/medicamentos/909-hemolivet-vitanimal-30-comprimidos.html",
    "petdotu159": "https://www.petclick.cl/farmacia/603-cerenia-24mg-comprimidos.html",
    "petdotu178": "https://www.petclick.cl/medicamentos/647-canigest-combi-16ml.html",
    "petdotu162": "https://www.petclick.cl/medicamentos/517-meloxivet-60ml-7800006010330.html#:~:text=Meloxivet%20es%20un%20antiinflamatorio%20no,a%20la%20osteoartritis%20en%20perros.",
    "petdotu167": "https://www.petclick.cl/medicamentos/313-clindabone-165mg-comprimidos-7800006006364.html",
    "petdotu173": "https://www.petclick.cl/alimento-para-gatos/81-proplan-urinary-cat-75kg-7613039947739.html",
    "petdotu174": "https://www.petclick.cl/medicamentos/910-nutribound-perros-150ml-7502010426861.html",
    "petdotu179": "https://www.petclick.cl/shampoos-medicados/242-regepipel-plus-shampoo-150ml.html#:~:text=Regepipel%20Plus%20es%20un%20shampoo,canis%20en%20perros%20y%20gatos.",
    "petdotu180": "https://www.petclick.cl/alimento-para-perros/21-proplan-puppy-razas-medianas-15kg-7613287028549.html",
    "petdotu182": "https://www.petclick.cl/medicamentos/333-hematon-b12-elixir-100ml-7730407023830.html",
    "petdotu186": "https://www.petclick.cl/medicamentos/455-465-glicopan-pet-30ml-7898053580340.html#/111-envase-125ml",
    "petdotu187": "https://www.petclick.cl/alimento-para-gatos/131-85-proplan-urinary-cat-7613039947111.html",
    "petdotu192": "https://www.petclick.cl/alimento-para-gatos/7-678-proplan-sterilized-cat-7613039947784.html#/3-tamano-75kg",
    "petdotu195": "https://www.petclick.cl/medicamentos/347-paz-pet-60ml-suspension-oral-7800006005589.html",
    "petdotu198": "https://www.petclick.cl/medicamentos/292-naxpet-10mg-comprimidos-7800006002410.html",
    "petdotu201": "https://www.petclick.cl/medicamentos/498-senilpet-cerebral-5-7800006009983.html",
    "petdotu202": "https://www.petclick.cl/shampoos-medicados/245-petever-forte-shampoo-150ml-7800006001291.html",
    "petdotu205": "https://www.petclick.cl/entrenamiento-y-comportamiento/653-adaptil-calm-repuesto-48ml-3411112169344.html",
    "petdotu206": "https://www.petclick.cl/medicamentos/645-papainpet-comprimidos-7800006010170.html",
    "petdotu207": "https://www.petclick.cl/medicamentos/530-silimadrag-suspension-oral-120ml-7800006010217.html",
    "petdotu208": "https://www.petclick.cl/medicamentos/456-463-hemolitan-pet-30ml-7898053580234.html#/110-envase-60ml",
    "petdotu46": "https://www.petclick.cl/alimento-para-perros/38-18-royal-canin-puppy-mini-7896181218937.html#/15-tamano-25kg",
    "petdotu47": "https://www.petclick.cl/alimento-para-perros/34-849-royal-canin-mini-adulto-3182550402170.html#/15-tamano-25kg",
    "petdotu184": "https://www.petclick.cl/alimento-para-perros/11-78-proplan-adult-razas-pequenas-7613287029195.html#/1-tamano-3kg",
    "petdotu13":"https://www.petclick.cl/alimento-para-perros/650-fit-formula-light-20kg.html"
}

sku2= {"petdotu1233": "https://www.petclick.cl/medicamentos/358-ursovet-jarabe-60ml-7800006007033.html"}
results = []

for sku_key, url in sku.items():
    driver.get(url)
    precio_oferta = "No disponible"
    precio_normal = "No disponible"
    stock= "Con Stock"
    try:
        # Intenta obtener el precio de oferta
        precio_oferta_element = driver.find_element("xpath", '/html/body/main/section/div/div/div/section/div[1]/div[2]/div[1]/div[1]/div') #Cambiar
        precio_oferta = precio_oferta_element.text  # Guarda el precio de oferta
        stock_element= driver.find_element(By.XPATH,"/html/body/main/section/div/div/div/section/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]")
        stock=stock_element.text
    except NoSuchElementException:
        pass  # Si no se encuentra el precio de oferta, se continuará con el siguiente bloque de código

    try:
        # Intenta obtener el precio normal
        precio_normal_element = driver.find_element("xpath", '/html/body/main/section/div/div/div/section/div[1]/div[2]/div[1]/div[1]/div') #Cambiar
        precio_normal = precio_normal_element.text  # Guarda el precio normal
        stock_element= driver.find_element(By.XPATH,"/html/body/main/section/div/div/div/section/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]")
        stock=stock_element.text
        
    except NoSuchElementException:
        pass  # Si no se encuentra el precio normal, se continuará con el siguiente bloque de código

    if precio_oferta == "No disponible" and precio_normal == "No disponible":
        try:
            # Si no se puede encontrar ni el precio de oferta ni el precio normal, intenta con el tercer XPath
            precio_normal_element = driver.find_element("xpath", '/html/body/div[2]/main/div[3]/div/div[1]/div[4]/div[1]/span[2]') #Cambiar
            precio_normal = precio_normal_element.text  # Guarda el precio normal
            stock_element= driver.find_element(By.XPATH,"/html/body/main/section/div/div/div/section/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]")
            stock=stock_element.text
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
							range='petclick!J2',#CAMBIAR
							valueInputOption='USER_ENTERED',
							body={'values':values}).execute()


#Valores que se pasan a Sheets
values = [[item['SKU'], item['Precio'],item['Precio_oferta'],item['Stock']] for item in results]
result = sheet.values().update(spreadsheetId=SPREADSHEET_ID,
							range='petclick!A2:E1000',#CAMBIAR
							valueInputOption='USER_ENTERED',
							body={'values':values}).execute()
print(f"Datos insertados correctamente")


#Valores que se pasan a Sheets a Stock
values = [[item['Stock']] for item in results]
result = sheet.values().update(spreadsheetId=SPREADSHEET_ID,
							range='petclick!M2:N',#CAMBIAR
							valueInputOption='USER_ENTERED',
							body={'values':values}).execute()
print(f"Datos insertados correctamente")

df = pd.DataFrame(results)
print(df)
print(df.head)


competitor = "Petclick"  # Cambiar 
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
values = [[row['SKU'], "No disponible",competitor, row['Precio'], now_str] for _, row in df.iterrows()]

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
values = [[row['SKU'], competitor, row['Precio'], "No disponible", row["Stock"]] for _, row in df.iterrows()]

# Insertar los resultados en la nueva hoja después de la última fila
update_range = f'apipets!A{last_row}:E{last_row + len(values) - 1}' #Cambiar
result = sheet.values().update(
    spreadsheetId=NEW_SPREADSHEET_ID,
    range=update_range,
    valueInputOption='USER_ENTERED',
    body={'values': values}
).execute()
