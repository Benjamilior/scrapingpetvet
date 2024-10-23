
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
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
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
    "petdotu194": "https://www.tusmascotas.cl/product/acana-classic-wild-coast-2kg/",
    "petdotu7": "https://www.tusmascotas.cl/product/acana-classic-wild-coast/",
    "petdotu160": "https://www.tusmascotas.cl/product/acana-heritage-free-run-poultry-pollo-pavo-y-huevo-59-kg/",
    "petdotu197": "https://www.tusmascotas.cl/product/indoor-entree-cat-acana/",
    "petdotu121": "https://www.tusmascotas.cl/product/acana-pork-and-squash/",
    "petdotu176": "https://www.tusmascotas.cl/product/acana-regionals-wild-atlantic-pescado-45-kg/",
    "petdotu6": "https://www.tusmascotas.cl/product/acana-classic-praire-poultry/",
    "petdotu97": "https://www.tusmascotas.cl/product/adaptil-collar-m-l/",
    "petdotu96": "https://www.tusmascotas.cl/product/adaptil-collar-s-m/",
    "petdotu93": "https://www.tusmascotas.cl/product/adaptil-difusor-mas-repuesto/",
    "petdotu205": "https://www.tusmascotas.cl/product/adaptil-repuesto/",
    "petdotu135": "https://www.tusmascotas.cl/product/pipeta-advantage-para-gatos-4-kg-a-8-kg/",
    "petdotu142": "https://www.tusmascotas.cl/product/pipeta-advantage-para-gatos-hasta-4-kg/",
    "petdotu149": "https://www.tusmascotas.cl/product/advocate-felino-hasta-4kg/",
    "petdotu115": "https://www.tusmascotas.cl/product/advocate-felino-4-a-8/",
    "petdotu177": "https://www.tusmascotas.cl/product/advocate-perro-10-25kg/",
    "petdotu196": "https://www.tusmascotas.cl/product/advocate-perro-25-40kg/",
    "petdotu98": "https://www.tusmascotas.cl/product/allercalm-250-ml/",
    "petdotu125": "https://www.tusmascotas.cl/product/america-litter-odor-seal-clean-pawz-15kg/",
    "petdotu84": "https://www.tusmascotas.cl/product/america-litter-ultra-scooping-odor-seal-15-kg/",
    "petdotu72": "https://www.tusmascotas.cl/product/america-litter-lavanda-15kg/",
    "petdotu1": "https://www.tusmascotas.cl/product/apoquel-16mg-oclacitinib/",
    "petdotu2": "https://www.tusmascotas.cl/product/apoquel-3-6mg-oclacitinib-20-comprimidos/",
    "petdotu3": "https://www.tusmascotas.cl/product/apoquel-54mg-oclacitinib-receta-requerida/",
    "petdotu82": "https://www.tusmascotas.cl/product/artri-tabs-60-comprimidos/",
    "petdotu132": "https://www.tusmascotas.cl/product/belcando-finest-gf-senior-12-5kg/",
    "petdotu49": "https://www.tusmascotas.cl/product/bil-jac-small-breed-adult-2-7kg/",
    "petdotu9": "https://www.tusmascotas.cl/product/acana-bountiful-cath-cat-45-kg/",
    "petdotu181": "https://www.tusmascotas.cl/product/bravecto-antiparasitario-externo-para-perros-40-kg-a-56-kg/",
    "petdotu28": "https://www.tusmascotas.cl/product/bravecto-antiparasitario-externo-para-perros-20-kg-a-40-kg/",
    "petdotu32": "https://www.tusmascotas.cl/product/bravecto-antiparasitario-externo-para-perros-2-kg-a-45-kg/",
    "petdotu30": "https://www.tusmascotas.cl/product/bravecto-antiparasitario-externo-para-perros-45-kg-a-10-kg/",
    "petdotu29": "https://www.tusmascotas.cl/product/bravecto-antiparasitario-externo-para-perros-10-kg-a-20-kg/",
    "petdotu171": "https://www.tusmascotas.cl/product/bravery-pollo-adulto-razas-medianas-y-grandes-12kg/",
    "petdotu53": "https://www.tusmascotas.cl/product/brit-medium-breed-lambrice/",
    "petdotu52": "https://www.tusmascotas.cl/product/brit-adult-small-breed/",
    "petdotu130": "https://www.tusmascotas.cl/product/brit-care-cat-grain-free-haircare-sabor-salmonchicken-7kg-c-100905/",
    "petdotu134": "https://www.tusmascotas.cl/product/brit-care-cat-senior-2/",
    "petdotu155": "https://www.tusmascotas.cl/product/brit-care-cat-sterilized-urinary-sabor-a-chicken-2kg/",
    "petdotu55": "https://www.tusmascotas.cl/product/brit-care-cat-grain-free-sterilized-urinary-sabor-a-chicken-7kg-c-100903909/",
    "petdotu110": "https://www.tusmascotas.cl/product/brit-care-cat-grain-free-sterelized-weight-control-duck-turkey-07-kg-c-100902/",
    "petdotu116": "https://www.tusmascotas.cl/product/brit-adulto-salmon-3/",
    "petdotu57": "https://www.tusmascotas.cl/product/brit-adulto-salmon-3/",
    "petdotu133": "https://www.tusmascotas.cl/product/brit-adulto-salmon/",
    "petdotu58": "https://www.tusmascotas.cl/product/brit-puppy-salmon/",
    "petdotu136": "https://www.tusmascotas.cl/product/brit-puppy-salmon-2/",
    "petdotu59": "https://www.tusmascotas.cl/product/brit-perro-senior-light-salmon-y-papa-12-kg/",
    "petdotu139": "https://www.tusmascotas.cl/product/brit-sensitive-venison-potato-ciervo-12kg/",
    "petdotu106": "https://www.tusmascotas.cl/product/brit-perro-puppy-cordero-y-arroz-12kg/",
    "petdotu113": "https://www.tusmascotas.cl/product/brit-junior-cordero-y-arroz/",
    "petdotu123": "https://www.tusmascotas.cl/product/brit-perro-junior-salmon-y-papa-12-kg/",
    "petdotu51": "https://www.tusmascotas.cl/product/brit-perro-senior-lamb-y-rice-12kgs/",
    "petdotu56": "https://www.tusmascotas.cl/product/brit-perro-weight-loss-conejo-y-arroz-12-kg/",
    "petdotu140": "https://www.tusmascotas.cl/product/brit-perro-weight-loss-conejo-y-arroz-3-kg/",
    "petdotu204": "https://www.tusmascotas.cl/product/nexgard-combo-cat-s-0-3ml-0-8-2-5kg-2/",
    "petdotu168": "https://www.tusmascotas.cl/product/nexgard-combo-cat-l-0-9ml-2-5-7-5kg/",
    "petdotu81": "https://www.tusmascotas.cl/product/calmer-para-perros-gatos/",
    "petdotu178": "https://www.tusmascotas.cl/product/canigest-combi-16ml/",
    "petdotu167": "https://www.tusmascotas.cl/product/clindabone-clindamicina-165mg-20-comp/#:~:text=Clindabone%20Clindamicina%20165mg%2020%20comp%20es%20indicada%20para%20el%20tratamiento,perfringens%20y%20muchas%20especies%20de",
    "petdotu95": "https://www.tusmascotas.cl/product/dermisolona-10-comp-20-mg/",
    "petdotu91": "https://www.tusmascotas.cl/product/dermisolona-suspension-oral-30ml/",
    "petdotu193": "https://www.tusmascotas.cl/product/multivitaminico-doguivit-senior-30-comp/",
    "petdotu188": "https://www.tusmascotas.cl/product/drontal-antiparasitario-interno-para-gatos-2-comprimidos/",
    "petdotu143": "https://www.tusmascotas.cl/product/drontal-antiparasitario-interno-para-perros-de-hasta-10-kg/",
    "petdotu185": "https://www.tusmascotas.cl/product/drontal-antiparasitario-interno-para-perros-de-35-kg/",
    "petdotu14": "https://www.tusmascotas.cl/product/acana-duck-and-pear-2/",
    "petdotu42": "https://www.tusmascotas.cl/product/feliway-difusor-mas-repuesto/",
    "petdotu43": "https://www.tusmascotas.cl/product/feliway-friends-difusor-mas-repuesto/",
    "petdotu41": "https://www.tusmascotas.cl/product/feliway-friends-repuesto/",
    "petdotu39": "https://www.tusmascotas.cl/product/feliway-repuesto/",
    "petdotu40": "https://www.tusmascotas.cl/product/feliway-spray/",
    "petdotu22": "https://www.tusmascotas.cl/product/simparica-antiparasitario-externo-1-comprimido-101-kg-a-20-kg/",
    "petdotu10": "https://www.tusmascotas.cl/product/first-feast-cat-acana/",
    "petdotu71": "https://www.tusmascotas.cl/product/flora-fix-pet-15g/",
    "petdotu12": "https://www.tusmascotas.cl/product/acana-heritage-free-run-poultry-pollo-pavo-y-huevo-113-kg/",
    "petdotu11": "https://www.tusmascotas.cl/product/acana-heritage-freshwater-fish-trucha-arcoiris-bagre-azul-y-perca-dorada-113-kg/",
    "petdotu186": "https://www.tusmascotas.cl/product/glicopan-pet-125-ml/",
    "petdotu208": "https://www.tusmascotas.cl/product/hemolitan-pet-60ml/",
    "petdotu158": "https://www.tusmascotas.cl/product/hemolivet-30-capsulas/",
    "petdotu87": "https://www.tusmascotas.cl/product/itraskin-suspension-oral-120-ml-receta-requerida/",
    "petdotu144": "https://www.tusmascotas.cl/product/josera-balance-125kg-perro/",
    "petdotu120": "https://www.tusmascotas.cl/product/josera-ente-kartoffel-adult-senior-125kg/",
    "petdotu109": "https://www.tusmascotas.cl/product/josera-festival-adult-125kg/",
    "petdotu124": "https://www.tusmascotas.cl/product/josera-nature-cat-adult-10kg/",
    "petdotu141": "https://www.tusmascotas.cl/product/josera-naturelle-adult-sterilized-10kg/",
    "petdotu117": "https://www.tusmascotas.cl/product/josidog-regular-josera-adult-18kg/",
    # "petdotu156": "https://www.tusmascotas.cl/product/josera-light-y-vital-adult-15kg/",
    "petdotu65": "https://www.tusmascotas.cl/product/laveta-carnitine-50ml/",
    "petdotu66": "https://www.tusmascotas.cl/product/laveta-taurina-50ml/",
    "petdotu164": "https://www.tusmascotas.cl/product/leonardo-adulto-duck-7-5kg/",
    "petdotu152": "https://www.tusmascotas.cl/product/leonardo-gato-adulto-light/",
    "petdotu151": "https://www.tusmascotas.cl/product/leonardo-adult-senior-1-8-kg/",
    "petdotu161": "https://www.tusmascotas.cl/product/adult-senior-75-kg-leonardo/",
    "petdotu162": "https://www.tusmascotas.cl/product/meloxivet-meloxicam-1-solucion-oral-60-ml/",
    "petdotu60": "https://www.tusmascotas.cl/product/mixantip-plus-50gr/",
    "petdotu75": "https://www.tusmascotas.cl/product/jarabe-naxpet-ketoprofeno-20ml/",
    "petdotu198": "https://www.tusmascotas.cl/product/naxpet-ketoprofeno-10mg-receta-requerida/",
    "petdotu70": "https://www.tusmascotas.cl/product/nexgard-spectra-151-30kg-1-comprimidos/",
    "petdotu69": "https://www.tusmascotas.cl/product/nexgard-spectra-151-30kg-3-comprimido/",
    "petdotu189": "https://www.tusmascotas.cl/product/nexgard-spectra-36-75kg-1-comprimido/",
    "petdotu172": "https://www.tusmascotas.cl/product/nexgard-spectra-36-75kg-3-comprimidos/",
    "petdotu147": "https://www.tusmascotas.cl/product/nexgard-spectra-301-60kg-1-comprimido/",
    "petdotu138": "https://www.tusmascotas.cl/product/nexgard-spectra-301-60kg-3-comprimidos/",
    "petdotu68": "https://www.tusmascotas.cl/product/nexgard-spectra-76-15kg-1-comprimido/",
    "petdotu67": "https://www.tusmascotas.cl/product/nexgard-spectra-76-15kg-3-comprimidos/",
    "petdotu165": "https://www.tusmascotas.cl/product/nutrience-original-cat-adulto-5kg/",
    "petdotu175": "https://www.tusmascotas.cl/product/nutrience-original-cat-indoor-5kg/",
    "petdotu157": "https://www.tusmascotas.cl/product/oftavet-solucion-oftalmica-5ml/",
    "petdotu94": "https://www.tusmascotas.cl/product/ohm-pastillas-calmantes/",
    "petdotu153": "https://www.tusmascotas.cl/product/orijen-cat-and-kitten-545-kg/",
    "petdotu114": "https://www.tusmascotas.cl/product/orijen-small-breed-perro-45-kg/",
    "petdotu131": "https://www.tusmascotas.cl/product/orijen-puppy-106-kg/",
    "petdotu77": "https://www.tusmascotas.cl/product/oxtrin-30-comprimidos/",
    "petdotu206": "https://www.tusmascotas.cl/product/papainpet-suplemento-30-comprimidos/",
    "petdotu195": "https://www.tusmascotas.cl/product/paz-pet-60ml/",
    "petdotu202": "https://www.tusmascotas.cl/product/shampoo-antiseptico-150ml-petever-forte/",
    "petdotu100": "https://www.tusmascotas.cl/product/virbac-phisio-anti-olor-orejas-100-ml/",
    "petdotu192": "https://www.tusmascotas.cl/product/pro-plan-sterilized-cat-75-kg/",
    "petdotu173": "https://www.tusmascotas.cl/product/proplan-urinary-cat-7-5kg/",
    "petdotu184": "https://www.tusmascotas.cl/product/pro-plan-perro-adulto-razas-pequenas-3-kg/",
    "petdotu8": "https://www.tusmascotas.cl/product/acana-heritage-puppy-junior-1135kg/",
    "petdotu179": "https://www.tusmascotas.cl/product/regepipel-plus-150ml/",
    "petdotu5": "https://www.tusmascotas.cl/product/revolution-plus-0-25ml/",
    "petdotu4": "https://www.tusmascotas.cl/product/revolution-plus-0-50ml/",
    "petdotu27": "https://www.tusmascotas.cl/product/rimadyl-carprofeno-100mg/",
    "petdotu207": "https://www.tusmascotas.cl/product/silimadrag-suspencion-120-ml/",
    "petdotu73": "https://www.tusmascotas.cl/product/silimarina-vitanimal-30-comprimidos/",
    "petdotu74": "https://www.tusmascotas.cl/product/silimarina-90-comprimidos/",
    "petdotu203": "https://www.tusmascotas.cl/product/simparica-trio-2-5-a-5-kg-1-comprimido/",
    "petdotu169": "https://www.tusmascotas.cl/product/simparica-antiparasitario-externo-3-comprimidos-5-kg-a-10-kg/",
    "petdotu25": "https://www.tusmascotas.cl/product/simparica-antiparasitario-externo-1-comprimido-51-kg-a-10-kg/",
    "petdotu24": "https://www.tusmascotas.cl/product/simparica-antiparasitario-externo-3-comprimidos-5-kg-a-10-kg/",
    "petdotu23": "https://www.tusmascotas.cl/product/simparica-antiparasitario-externo-3-comprimidos-10-kg-a-20-kg/",
    "petdotu21": "https://www.tusmascotas.cl/product/simparica-1-comprimidos/",
    "petdotu20": "https://www.tusmascotas.cl/product/simparica-antiparasitario-externo-3-comprimidos-20-kg-a-40-kg/",
    "petdotu163": "https://www.tusmascotas.cl/product/simparica-trio-20-a-40-kg-3-comprimidos/",
    "petdotu89": "https://www.tusmascotas.cl/product/sucravet-sucralfato-100ml/",
    "petdotu210": "https://www.tusmascotas.cl/product/superpet-omega-36-gato-125ml/",
    "petdotu79": "https://www.tusmascotas.cl/product/synulox-antibiotico-10-comprimidos-receta-requerida/",
    "petdotu108": "https://www.tusmascotas.cl/product/heel-traumeel-perros-y-gatos-100-tab/",
    "petdotu92": "https://www.tusmascotas.cl/product/ursovet-suspension-oral-60ml/",
    "petdotu166": "https://www.tusmascotas.cl/product/virbac-hpm-felino-hypoallergy-3kg/",
    "petdotu146": "https://www.tusmascotas.cl/product/virbac-hpm-felino-adult-neutered-7kg/",
    "petdotu118": "https://www.tusmascotas.cl/product/virbac-hpm-canino-allergy-12kg/",
    "petdotu137": "https://www.tusmascotas.cl/product/virbac-hpm-adult-weight-loss-control-12kg/",
    "petdotu128": "https://www.tusmascotas.cl/product/virbac-hpm-adult-weight-loss-diabetes-12kg/",
    "petdotu50": "https://www.tusmascotas.cl/product/bil-jac-puppy-dog-food-13-6kg/",
    "petdotu48": "https://www.tusmascotas.cl/product/bil-jac-select-dog-food-13-6kg/",
    "petdotu33": "https://www.tusmascotas.cl/product/bravecto-antiparasitario-externo-para-gatos-12-kg-a-28-kg/",
    "petdotu31": "https://www.tusmascotas.cl/product/bravecto-gatos-250mg-28-625kg/",
    "petdotu54": "https://www.tusmascotas.cl/product/brit-perro-puppy-cordero-y-arroz-12kg/",
    "petdotu34": "https://www.tusmascotas.cl/product/pipeta-calming-spot-on-gato/",
    "petdotu35": "https://www.tusmascotas.cl/product/calming-home-spray-125-ml/",
    "petdotu38": "https://www.tusmascotas.cl/product/calming-tabletas-de-beaphar-20-und-dog-cat/",
    "petdotu36": "https://www.tusmascotas.cl/product/calming-cat-treats-35gr/",
    "petdotu88": "https://www.tusmascotas.cl/product/hills-small-paws-adulto/",
    "petdotu45": "https://www.tusmascotas.cl/product/royal-canin-anallergenic-perro/",
    "petdotu47": "https://www.tusmascotas.cl/product/royal-canin-mini-adulto/",
    "petdotu46": "https://www.tusmascotas.cl/product/royal-canin-mini-puppy-3-kg/",
    "petdotu61": "https://www.tusmascotas.cl/product/mixantip-plus-15-g/",
    "petdotu44": "https://www.tusmascotas.cl/product/mother-and-babycat-3/",
    "petdotu80": "https://www.tusmascotas.cl/product/odour-buster-original-14kg-arena-santiaria-para-gatos/",
    "petdotu62": "https://www.tusmascotas.cl/product/oven-baked-tradition-adult-2/",
    "petdotu63": "https://www.tusmascotas.cl/product/oven-baked-tradition/",
    "petdotu90": "https://www.tusmascotas.cl/product/pacifor-gotas-10ml/",
    "petdotu86": "https://www.tusmascotas.cl/product/wanpy-lamb-jerky/",
    "petdotu222": "https://www.tusmascotas.cl/product/acana-heritage-light-fit-formula-11-35kg/",
    "petdotu600": "https://www.tusmascotas.cl/product/leonardo-adulto-grain-free-3"
}
sku2 = {  "petdotu50": "https://www.tusmascotas.cl/product/bil-jac-puppy-dog-food-13-6kg/",
    "petdotu33": "https://www.tusmascotas.cl/product/bravecto-antiparasitario-externo-para-gatos-12-kg-a-28-kg/",
    "petdotu31": "https://www.tusmascotas.cl/product/bravecto-gatos-250mg-28-625kg/",
    "petdotu54": "https://www.tusmascotas.cl/product/brit-perro-puppy-cordero-y-arroz-12kg/",
    "petdotu204":"https://www.tusmascotas.cl/product/nexgard-combo-cat-s-0-3ml-0-8-2-5kg-2/",
    "petdotu168":"https://www.tusmascotas.cl/product/nexgard-combo-cat-l-0-9ml-2-5-7-5kg/",
    "petdotu600":"https://www.tusmascotas.cl/product/leonardo-adulto-grain-free-3/"}
results = []

for sku_key, url in sku.items():
    driver.get(url)
    precio_oferta = "No disponible"
    precio_normal = "No disponible"
    stock = "Con Stock"
    
    try:
        # Intenta obtener el precio de oferta con un timeout de 5 segundos
        precio_oferta_element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div/div/div/div[2]/div[1]/div[2]/div/div/div[2]/div/p[1]/ins/span'))
        )
        precio_oferta = precio_oferta_element.text  # Guarda el precio de oferta
        stock_element = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div/div/div[2]/div[1]/div[2]/div/div/div[2]/div/p[2]')
        stock = stock_element.text
    except (TimeoutException, NoSuchElementException):
        pass  # Si no se encuentra el precio de oferta, o si hay un timeout, pasa al siguiente bloque
    
    try:
        # Intenta obtener el precio normal con un timeout de 5 segundos
        precio_normal_element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div/div/div/div[2]/div[1]/div[2]/div/div/div[2]/div/p[1]/del/span[2]'))
        )
        precio_normal = precio_normal_element.text  # Guarda el precio normal
        stock_element = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div/div/div[2]/div[1]/div[2]/div/div/div[2]/div/p[2]')
        stock = stock_element.text
    except (TimeoutException, NoSuchElementException):
        pass  # Si no se encuentra el precio normal, o si hay un timeout, pasa al siguiente bloque
    
    if precio_oferta == "No disponible" and precio_normal == "No disponible":
        try:
            # Intenta el tercer XPath con un timeout de 5 segundos
            precio_normal_element = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div/div/div/div[2]/div[1]/div[2]/div/div/div[2]/div/p[1]/span[2]'))
            )
            precio_normal = precio_normal_element.text  # Guarda el precio normal
            stock_element = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div/div/div[2]/div[1]/div[2]/div/div/div[2]/div/p[2]')
            stock = stock_element.text
        except (TimeoutException, NoSuchElementException) as e:
            print(f"No se pudo encontrar el precio en la URL {url} - {e}")

    data = {
        "SKU": sku_key,
        "Precio": precio_normal,
        "Precio_oferta": precio_oferta,
        "Stock": stock
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
							range='tusmascotas!k2',#CAMBIAR
							valueInputOption='USER_ENTERED',
							body={'values':values}).execute()


#Valores que se pasan a Sheets
values = [[item['SKU'], item['Precio'],item['Precio_oferta']] for item in results]
result = sheet.values().update(spreadsheetId=SPREADSHEET_ID,
							range='tusmascotas!A2:E',#CAMBIAR
							valueInputOption='USER_ENTERED',
							body={'values':values}).execute()
print(f"Datos insertados correctamente")

#Valores que se pasan a Sheets
values = [[item['Stock']] for item in results]
result = sheet.values().update(spreadsheetId=SPREADSHEET_ID,
							range='tusmascotas!M2:N',#CAMBIAR
							valueInputOption='USER_ENTERED',
							body={'values':values}).execute()
print(f"Datos insertados correctamente")


df = pd.DataFrame(results)
print(df)
print(df.head)


competitor = "Tus Mascotas"  # Cambiar 
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
values = [[row['SKU'],competitor,row["Precio_oferta"], row['Precio'], now_str] for _, row in df.iterrows()]

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
SPREADSHEET_ID_API = '1S8jzZl4UehXDJxWuHfTSLftBnq3CKUXhgRGrJIShyhE'  
# Obtener la última fila con datos en la nueva hoja
result = sheet.values().get(spreadsheetId=SPREADSHEET_ID_API, range='apipets!A:A').execute() #Cambiar donde llega la info
values = result.get('values', [])
last_row = len(values) + 1  # Obtener el índice de la última fila vacía

# Convertir resultados a la lista de valores
values = [[row['SKU'], competitor, row['Precio_oferta'], row['Precio'], row["Stock"]] for _, row in df.iterrows()]

# Insertar los resultados en la nueva hoja después de la última fila
update_range = f'apipets!A{last_row}:E{last_row + len(values) - 1}' #Cambiar
result = sheet.values().update(
    spreadsheetId=SPREADSHEET_ID_API,
    range=update_range,
    valueInputOption='USER_ENTERED',
    body={'values': values}
).execute()
