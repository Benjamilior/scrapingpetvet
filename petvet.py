import requests
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
import requests

#Google Sheets
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
KEY = 'key.json'
SPREADSHEET_ID = '1PrHE2FBeBhQnVYeCLQclLqj_tiIOq7z3JuMAG-2aAXg'
creds = None
creds = service_account.Credentials.from_service_account_file(KEY, scopes=SCOPES)
service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()


#Ejecutador del Codigo

start_time = time.time()  # Tiempo de inicio de la ejecución

urls = {
    "43683672457377": "https://petvet.cl/products/acana-indoor-entree-gato.js",
    "41689309708449": "https://petvet.cl/products/wild-coast-perro.js",
    "41689274712225": "https://petvet.cl/products/wild-atlantic-gato.js",
    "42708471840929": "https://petvet.cl/products/nexgard-spectra-3-6-7-5-kg.js",
    "42708471808161": "https://petvet.cl/products/nexgard-spectra-3-6-7-5-kg.js",
    "42738555453601": "https://petvet.cl/products/bravecto-perros-40-56-kg-1-400-mg-1.js",
    "41857347190945": "https://petvet.cl/products/canine-adult-7-small-bites.js",
    "41633900232865": "https://petvet.cl/products/simparica-2-6-5-kg-10-mg.js",
    "43577664241825": "https://petvet.cl/products/simparica-2-6-5-kg-10-mg-3comp.js",
    "43584104792225": "https://petvet.cl/products/simparica-trio-20-40-kg-3-comprimidos.js",
    "44329056895137": "https://petvet.cl/products/josera-miniwell-10kg.js",
    "43094808625313": "https://petvet.cl/products/leonardo-adulto-senior.js",
    "43094794338465": "https://petvet.cl/products/leonardo-adulto-pato.js",
    "43191176495265": "https://petvet.cl/products/belcando-finest-light.js",
    "43090610749601": "https://petvet.cl/products/drontal-plus-razas-grandes.js",
    "42361890668705": "https://petvet.cl/products/drontal-cats-x2.js",
    "42738689900705": "https://petvet.cl/products/advocate-perros-10-25-kg-2-5-ml.js",
    "43724309790881": "https://petvet.cl/products/advocate-perros-25-a-40-kg-4-0ml.js",
    "42738689704097": "https://petvet.cl/products/advocate-perros-4-10-kg-1-ml.js",
    "42463428378785": "https://petvet.cl/products/canigest-combi-16ml.js",
    "41896974680225": "https://petvet.cl/products/meloxivet.js",
    "43893233680545": "https://petvet.cl/products/nutrience-original-gato-adulto.js",
    "43785612230817": "https://petvet.cl/products/virbac-hpm-allergy-cat-3-kg.js",
    "42392893620385": "https://petvet.cl/products/clindabone-165-mg-x-20-comp.js",
    "43899298611361": "https://petvet.cl/products/bravery-perro-cachorro-pollo-razas-mediana-y-grandes.js",
    "43596331090081": "https://petvet.cl/products/pro-plan-gato-urinario.js",
    "42463321850017": "https://petvet.cl/products/nutribound-perro-150-ml.js",
    "43893240627361": "https://petvet.cl/products/nutrience-original-gato-adulto-indoor.js",
    "40152480219297": "https://petvet.cl/products/regepipel-plus.js",
    "43854457536673": "https://petvet.cl/products/pro-plan-puppy-razas-medianas-15kg.js",
    "43707310964897": "https://petvet.cl/products/hematon-b12-elixir-perros-y-gatos-100ml.js",
    "42361910132897": "https://petvet.cl/products/glicopan.js",
    "43596331057313": "https://petvet.cl/products/pro-plan-gato-urinario.js",
    "44181000421537": "https://petvet.cl/products/purina-excellent-cachorro-15kg.js",
    "43156268744865": "https://petvet.cl/products/purina-excellent-perro-adulto-pollo-arroz.js",
    "43596219056289": "https://petvet.cl/products/pro-plan-gato-adulto-esterilizado.js",
    "42310076858529": "https://petvet.cl/products/doguivit-senior-30-comprimidos.js",
    "40152479039649": "https://petvet.cl/products/paz-pet-suspension-oral.js",
    "40152448958625": "https://petvet.cl/products/naxpet-gato-perro.js",
    "44279760748705": "https://petvet.cl/products/vetgastril-50-ml.js",
    "42463409701025": "https://petvet.cl/products/senilpet-cerebral-5-x-60-comp.js",
    "40152459051169": "https://petvet.cl/products/petever-shampoo.js",
    "42271737249953": "https://petvet.cl/products/adaptil-repuesto-48-ml.js",
    "40152478777505": "https://petvet.cl/products/papainpet.js",
    "40152485757089": "https://petvet.cl/products/silimadrag-suspension.js",
    "42361911541921": "https://petvet.cl/products/hemolitan-perros-y-gatos.js",
    "40152488312993": "https://petvet.cl/products/superpet-omega-gato.js",
    "43596385386657": "https://petvet.cl/products/pro-plan-sensitive-skin-razas-pequenas.js",
    "41857592361121": "https://petvet.cl/products/apoquel-16mg-20-comp.js",
    "41857592754337": "https://petvet.cl/products/apoquel-3-6-mg-20-comp.js",
    "41857597014177": "https://petvet.cl/products/apoquel-5-4-mg-20-comp.js",
    "42033421123745": "https://petvet.cl/products/free-run-poultry-perro.js",
    "43111864369313": "https://petvet.cl/products/acana-puppy-junior-perro.js",
    "41689298796705": "https://petvet.cl/products/prairie-poultry-perro.js",
    "41857724350625": "https://petvet.cl/products/bountiful-catch-gato.js",
    "41689377341601": "https://petvet.cl/products/duck-pear-perro.js",
    "43111863189665": "https://petvet.cl/products/acana-freshwater-fish-11-35-kg.js",
    "42423305797793": "https://petvet.cl/products/acana-light-fit-2-kg-1.js",
    "42033421156513": "https://petvet.cl/products/wild-coast-perro.js",
    "42423280697505": "https://petvet.cl/products/first-feast-gato.js",
    "40152493490337": "https://petvet.cl/products/mother-and-babycat.js",
    "40152491622561": "https://petvet.cl/products/canino-hypoallergenic.js",
    "42708472463521": "https://petvet.cl/products/nexgard-spectra-7-6-15-kg.js",
    "42708472496289": "https://petvet.cl/products/nexgard-spectra-7-6-15-kg.js",
    "42708470136993": "https://petvet.cl/products/nexgard-spectra-15-1-30-kg.js",
    "42708470169761": "https://petvet.cl/products/nexgard-spectra-15-1-30-kg.js",
    "42730103177377": "https://petvet.cl/products/nexgard-spectra-30-1-60-kg.js",
    "42730103144609": "https://petvet.cl/products/nexgard-spectra-30-1-60-kg.js",
    "43771918090401": "https://petvet.cl/products/bravecto-plus-pipeta-gato-1-2-2-8-kg.js",
    "43771996864673": "https://petvet.cl/products/bravecto-plus-pipeta-gato-2-8-6-25-kg.js",
    "42738538872993": "https://petvet.cl/products/bravecto-perros-2-4-5-kg-112-5-mg.js",
    "42738539692193": "https://petvet.cl/products/bravecto-perros-4-5-10-kg-250-mg.js",
    "42738543263905": "https://petvet.cl/products/bravecto-perros-10-20-kg-500-mg.js",
    "42738545557665": "https://petvet.cl/products/bravecto-perros-20-40-kg-1-000-mg.js",
    "42324007878817": "https://petvet.cl/products/americalitter-ultra-odor-seal.js",
    "44388326178977": "https://petvet.cl/products/america-litter-ultra-odor-seal-lavanda-15kg.js",
    "42271448629409": "https://petvet.cl/products/brit-care-gf-puppy-salmon.js",
    "42271606767777": "https://petvet.cl/products/brit-care-adult-small-breed-l-r.js",
    "42271434178721": "https://petvet.cl/products/brit-care-adult-medium-breed-l-r.js",
    "42271541362849": "https://petvet.cl/products/brit-care-puppy-l-r.js",
    "42271560237217": "https://petvet.cl/products/brit-care-weight-loss-rabbit.js",
    "42271478841505": "https://petvet.cl/products/brit-care-gf-senior-light-salmon.js",
    "42271548801185": "https://petvet.cl/products/brit-care-senior-lamb.js",
    "42271444598945": "https://petvet.cl/products/brit-care-gf-adult-salmon.js",
    "42423170367649": "https://petvet.cl/products/brit-care-cat-gf-sterilized-urinary.js",
    "43019722981537": "https://petvet.cl/products/brit-care-cat-gf-sterilized-weight-control-7-5-kg.js",
    "44042326245537": "https://petvet.cl/products/brit-care-junior-large-breed-salmon.js",
    "43091932020897": "https://petvet.cl/products/brit-care-junior-large-breed-lamb.js",
    "43019722096801": "https://petvet.cl/products/brit-care-cat-gf-kitten-healthy-growth-development.js",
    "43019722326177": "https://petvet.cl/products/brit-care-cat-gf-haircare-healthy-shiny-coat.js",
    "42271444631713": "https://petvet.cl/products/brit-care-gf-adult-salmon.js",
    "43083183095969": "https://petvet.cl/products/brit-care-cat-senior-weight-control.js",
    "42271448662177": "https://petvet.cl/products/brit-care-gf-puppy-salmon.js",
    "43487989072033": "https://petvet.cl/products/brit-care-adult-sensitive-venado.js",
    "42271560269985": "https://petvet.cl/products/brit-care-weight-loss-rabbit.js",
    "42423170334881": "https://petvet.cl/products/brit-care-cat-gf-sterilized-urinary.js",
    "42271606800545": "https://petvet.cl/products/brit-care-adult-small-breed-l-r.js",
    "40087240835233": "https://petvet.cl/products/rimadyl.js",
    "40159957549217": "https://petvet.cl/products/rimadyl.js",
    "40087277830305": "https://petvet.cl/products/revolution-plus-gatos-1-25-2-5kg-0-25ml.js",
    "42738646745249": "https://petvet.cl/products/revolution-plus-gatos-2-5-5-kg-0-5-ml.js",
    "43830181560481": "https://petvet.cl/products/revolution-plus-gatos-5-10-kg-1-ml.js",
    "42785343013025": "https://petvet.cl/products/bil-jac-selected-adult-dog-food.js",
    "41981042000033": "https://petvet.cl/products/hills-prescription-diet-canine-c-d-7-98-kg.js",
    "41633978810529": "https://petvet.cl/products/antigarrapatas-10-1-20-kg-40-mg.js",
    "43577667354785": "https://petvet.cl/products/simparica-10-20-kg-40-mg-3-comprimidos.js",
    "43577665388705": "https://petvet.cl/products/simparica-5-1-10-kg-20-mg-3-comprimidos.js",
    "41633916944545": "https://petvet.cl/products/simparica-5-1-10-kg-20-mg.js",
    "43577669910689": "https://petvet.cl/products/simparica-20-1-40-kg-80-mg-3-comprimidos.js",
    "40152468979873": "https://petvet.cl/products/hills-canine-adult-toy-breed.js",
    "41634051162273":"https://petvet.cl/products/simparica-20-1-40-kg-80-mg.js",
    "40087248470177": "https://petvet.cl/products/mixantip-plus.js",
    "40087248437409": "https://petvet.cl/products/mixantip-plus.js",
    "42785360314529": "https://petvet.cl/products/bil-jac-puppy-food.js",
    "41857368359073": "https://petvet.cl/products/canine-adult-metabolic-7-98-kg.js",
    "42392861278369": "https://petvet.cl/products/adaptil-collar-perro.js",
    "42392861245601": "https://petvet.cl/products/adaptil-collar-perro.js",
    "43037801152673": "https://petvet.cl/products/oven-baked-adulto-pescado-11-34-kg.js",
    "43037801087137": "https://petvet.cl/products/oven-baked-adulto-pollo-11-34-kg.js",
    "43037801218209": "https://petvet.cl/products/oven-baked-senior-11-34-kg.js",
    "40087214227617": "https://petvet.cl/products/arena-traper.js",
    "42361913311393": "https://petvet.cl/products/silimarina-vitanimal-120mg.js",
    "42361913344161": "https://petvet.cl/products/silimarina-vitanimal-120mg.js",
    "40159961317537": "https://petvet.cl/products/fit-cachorro.js",
    "40159961383073": "https://petvet.cl/products/fit-formula-gato.js",
    "40152463147169": "https://petvet.cl/products/artritabs.js",
    "40152464588961": "https://petvet.cl/products/adaptil.js",
    "40087277043873": "https://petvet.cl/products/feliway-classic.js",
    "40087277338785": "https://petvet.cl/products/feliway-friends.js",
    "40087277600929": "https://petvet.cl/products/feliway-spray.js",
    "41715631194273": "https://petvet.cl/products/feliway-classic-repuesto-48-ml.js",
    "40152475599009": "https://petvet.cl/products/laveta-taurina-gatos-50-ml.js",
    "40152475238561": "https://petvet.cl/products/laveta-carnitina-perros-50ml.js",
    "42785365131425": "https://petvet.cl/products/bil-jac-small-breed-adult-2-7-kg.js",
    "40152471437473": "https://petvet.cl/products/condrovet-30-comp.js",
    "42008137629857": "https://petvet.cl/products/oxtrin-condroprotector-30-comp.js",
    "42463441125537": "https://petvet.cl/products/allercalm-250-ml.js",
    "41715635650721": "https://petvet.cl/products/feliway-friends-repuesto.js",
    "40152476713121": "https://petvet.cl/products/calming-spot-on-gatos.js",
    "40087281172641": "https://petvet.cl/products/calming-spray.js",
    "41556602650785": "https://petvet.cl/products/wanpy2.js",
    "41896962752673": "https://petvet.cl/products/ohm-modulador-de-ansiedad-perros-y-gatos.js",
    "40152452071585": "https://petvet.cl/products/calmer.js",
    "42471476134049": "https://petvet.cl/products/sucravet-10-100-ml.js",
    "40087280287905": "https://petvet.cl/products/calming-treats-gato.js",
    "40087281074337": "https://petvet.cl/products/calming-tableta.js",
    "40087282319521": "https://petvet.cl/products/calming-colllar-gato.js",
    "40476213674145": "https://petvet.cl/products/synulox250mg.js",
    "42874800144545": "https://petvet.cl/products/ursovet-60-ml.js",
    "41654177792161": "https://petvet.cl/products/florafix-pet.js",
    "40152477597857": "https://petvet.cl/products/naxpet-0-4-suspension-oral.js",
    "41896955117729": "https://petvet.cl/products/fit-formula-adulto-20-kg.js",
    "41896954822817": "https://petvet.cl/products/fit-formula-senior-20-kg.js",
    "40159961252001": "https://petvet.cl/products/fit-adulto-razas-pequenas.js",
    "40152495685793": "https://petvet.cl/products/fit-formula-senior-razas-pequenas.js",
    "41065522004129": "https://petvet.cl/products/pederol-aerosol.js",
    "42392930091169": "https://petvet.cl/products/itraskin-suspension-120-ml.js",
    "42361854394529": "https://petvet.cl/products/dermisolona-suspension.js",
    "42271785713825": "https://petvet.cl/products/pacifor-gotas-10-ml.js",
    "42361853804705": "https://petvet.cl/products/dermisolona-comp-x-10.js",
    "42713335824545": "https://petvet.cl/products/phisio-anti-olor-limpiador-auricular-virbac-100ml.js",
    "43925724266657": "https://petvet.cl/products/josera-festival-12-5kg.js",
    "43888893034657": "https://petvet.cl/products/josera-ente-kartoffel-12-5kg.js",
    "43888873275553": "https://petvet.cl/products/josera-josidog-regular-18kg.js",
    "43888931307681": "https://petvet.cl/products/josera-gato-naturecat.js",
    "43888860692641": "https://petvet.cl/products/josera-light-vital-15kg.js",
    "43888923771041": "https://petvet.cl/products/josera-gato-naturelle-2kg.js",
    "44042727424161": "https://petvet.cl/products/josera-balance-12-5kg.js",
    "41689363579041": "https://petvet.cl/products/free-run-poultry-perro.js",
    "44537640386721": "https://petvet.cl/products/acana-pork-squash-perro-10kg.js",
    "43094808592545": "https://petvet.cl/products/leonardo-adulto-senior.js",
    "43094807543969": "https://petvet.cl/products/leonardo-adulto-light.js",
    "44044562399393": "https://petvet.cl/products/orijen-pupy-perro-cachorro.js",
    "43238489948321": "https://petvet.cl/products/orijen-original-gato.js",
    "43513906102433": "https://petvet.cl/products/orijen-perro-razas-pequenas.js",
    "43191190782113": "https://petvet.cl/products/belcando-finest-grain-free-senior.js",
    "43749564645537": "https://petvet.cl/products/virbac-hpm-adult-neutered-cat.js",
    "43750029230241": "https://petvet.cl/products/virbac-hpm-dog-allergy.js",
    "43942971113633": "https://petvet.cl/products/virbac-hpm-dog-weight-loss-diabetes.js",
    "44397883162785": "https://petvet.cl/products/virbac-hpm-dog-weight-loss-control-12-kgs.js",
    "43384186437793": "https://petvet.cl/products/america-litter-clean-pawz.js",
    "43156259471521": "https://petvet.cl/products/purina-excellent-perro-adulto-skin-care-salmon.js",
    "43356432924833": "https://petvet.cl/products/pimocard-5-20-comprimidos.js",
    "42361852821665": "https://petvet.cl/products/traumeel-modulador-de-inflamacion-y-dolor.js",
    "42361852854433": "https://petvet.cl/products/traumeel-modulador-de-inflamacion-y-dolor.js",
    "43852825165985": "https://petvet.cl/products/galliprant-100-mg-30-comprimidos.js",
    "40087273341089": "https://petvet.cl/products/advantage-gatos.js",
    "42738744393889": "https://petvet.cl/products/advantage-gatos-4-8-kg-0-8-ml.js",
    "40159957221537": "https://petvet.cl/products/drontal-plus.js",
    "44054704259233": "https://petvet.cl/products/neptra-solucion-otica.js",
    "44279072227489": "https://petvet.cl/products/osteodrag-ha-30-comprimidos.js",
    "41646114996385": "https://petvet.cl/products/antiparasitario-advocate-gatos.js",
    "42738659557537": "https://petvet.cl/products/advocate-gatos-4-8-kg-0-8-ml.js",
    "41857461190817": "https://petvet.cl/products/oftavet-5-ml.js",
    "43830826074273": "https://petvet.cl/products/hemolivet-30-comprimidos.js",
    "42366871928993": "https://petvet.cl/products/cerenia-24-mg-x-4-comp.js",
    "43591189987489": "https://petvet.cl/products/canigest-combi-32ml.js",
    "44309699166369":"https://petvet.cl/products/fit-formula-light-20-kg.js",
    "44430172684449":"https://petvet.cl/products/nexgard-combo-gato-1-pipeta-0-8-2-5-kg.js",
    "44427832033441":"https://petvet.cl/products/nexgard-combo-gato-1-pipeta-2-5-7-5-kg.js"
    
}

urls2={  "44427832033441":"https://petvet.cl/products/nexgard-combo-gato-1-pipeta-2-5-7-5-kg.js"}
# Headers para las solicitudes
headers = {
    "cookie": "secure_customer_sig=; _tracking_consent=%257B%2522con%2522%253A%257B%2522CMP%2522%253A%2522%2522%252C%2522a%2522%253A%2522%2522%252C%2522p%2522%253A%2522%2522%252C%2522s%2522%253A%2522%2522%257D%257D%252C%2522v%2522%253A%25222.1%2522%252C%2522region%2522%253A%2522CLRM%2522%252C%2522reg%2522%253A%2522%2522%257D; _shopify_y=6e06c95b-88fa-4ce0-b0ea-a8fba8fdf7ac; _shopify_s=a1dae16c-7a4c-468b-a001-ce827f8c08a9",
    "User-Agent": "insomnia/8.6.0"
}

# Lista para almacenar los datos extraídos
price_data = []

# Función para realizar la consulta y extraer los datos 
def fetch_data(product_id, product_url):
    response = requests.get(product_url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if "variants" in data:
            for variant in data["variants"]:
                if variant["id"] == product_id:
                    price = variant["price"]
                    compare_at_price = variant.get("compare_at_price", "N/A")
                    available = variant.get("available", "Unknown")  # Extrae la disponibilidad
                    price_data.append({
                        "SKU": product_id,
                        "Price": price,
                        "Compare_at_Price": compare_at_price if compare_at_price is not None else "",
                        "Available": available
                    })
                    print(product_id, price, compare_at_price, available)
                    return
    else:
        print(f"Failed to retrieve data for ID {product_id}. Status code: {response.status_code}")

# Iterar sobre el diccionario y realizar la consulta para cada enlace
for product_id, product_url in urls.items():
    fetch_data(int(product_id), product_url)

# Crear un DataFrame con los datos extraídos
df = pd.DataFrame(price_data)
print(df)
print(df.head())

# Fecha de Extracción
now = datetime.datetime.now()
now_str = now.strftime('%Y-%m-%d %H:%M:%S')
data = {"": now_str}
json_data = json.dumps(data)

# Actualizar fecha de extracción en Google Sheets
values = [[json_data]]
result = sheet.values().update(
    spreadsheetId=SPREADSHEET_ID,
    range='petvet!G2',  # CAMBIAR
    valueInputOption='USER_ENTERED',
    body={'values': values}
).execute()

# Valores que se pasan a Sheets
values = [[item['SKU'], item['Price'],item['Compare_at_Price']] for item in price_data]
result = sheet.values().update(
    spreadsheetId=SPREADSHEET_ID,
    range='petvet!A2:D1000',  # CAMBIAR
    valueInputOption='USER_ENTERED',
    body={'values': values}
).execute()
print(f"Datos insertados correctamente")

values = [[item['Available']] for item in price_data]
result = sheet.values().update(
    spreadsheetId=SPREADSHEET_ID,
    range='petvet!M2:N1000',  # CAMBIAR
    valueInputOption='USER_ENTERED',
    body={'values': values}
).execute()
print(f"Datos insertados correctamente")





# Enviar datos a Google Sheets BBDD
competitor = "Petvet"  # Cambiar
NEW_SPREADSHEET_ID = '1lLfl_jSGUEtitfsezo_zz53Bn2zAzID73VtxIi4dKRo'  # ID de la nueva hoja de cálculo

# Obtener la última fila con datos en la nueva hoja
result = sheet.values().get(spreadsheetId=NEW_SPREADSHEET_ID, range='petvet!A:A').execute()  # Cambiar donde llega la info
values = result.get('values', [])
last_row = len(values) + 1  # Obtener el índice de la última fila vacía

# Convertir resultados a la lista de valores
values = [[row['SKU'], competitor, "No Disponible", row['Price'], now_str] for _, row in df.iterrows()]

# Insertar los resultados en la nueva hoja después de la última fila
print(values)
update_range = f'petvet!A{last_row}:E{last_row + len(values) - 1}'  # Cambiar
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
values = [[now_str, competitor,row['SKU'], row['Available']] for _, row in df.iterrows()]

# Insertar los resultados en la nueva hoja después de la última fila
print(values)
update_range = f'Stock!A{last_row}:E{last_row + len(values) - 1}'  # Cambiar
result = sheet.values().update(
    spreadsheetId=NEW_SPREADSHEET_ID,
    range=update_range,
    valueInputOption='USER_ENTERED',
    body={'values': values}
).execute()

