#Codigo para sacar el precio de producto donde la pagina no tiene boton 
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementClickInterceptedException

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException


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

sku2 = {
    "petdotu197": {
        "url": "https://www.amigales.cl/acana-entree-gatos-indoor.html",
        "button_xpath": "//*[@id=\"option-label-acana_catfood_size-1308-item-3593\"]"
        
    },
    "petdotu194": {
        "url": "https://www.amigales.cl/acana-wild-coast-perros.html",
        "button_xpath": "//*[@id=\"option-label-acana_wildcoast_perros-906-item-2334\"]"
    },
    "petdotu176": {
        "url": "https://www.amigales.cl/acana-wild-atlantic-gatos.html",
        "button_xpath": "//*[@id=\"option-label-acana_wildatlan_gatos_cantidad-676-item-1656\"]"
    },
    "petdotu12": {
        "url": "https://www.amigales.cl/acana-heritage-free-run-poultry-perros.html",
        "button_xpath": "//*[@id=\"option-label-acana_freerun_perros_cantidad-642-item-1555\"]"
    },
    "petdotu8": {
        "url": "https://www.amigales.cl/acana-heritage-puppy-junior-cachorro.html",
        "button_xpath": "//*[@id=\"option-label-acana_puppyjunior_cantidad-645-item-1564\"]"
    },
    "petdotu6": {
        "url": "https://www.amigales.cl/acana-prairie-poultry-perros.html",
        "button_xpath": "//*[@id=\"option-label-acana_prairiepoultry_perro-905-item-2333\"]"
    },
    "petdotu9": {
        "url": "https://www.amigales.cl/acana-bountiful-catch-gatos.html",
        "button_xpath": "//*[@id=\"option-label-acana_catfood_size-1308-item-3594\"]"
    },
    "petdotu14": {
        "url": "https://www.amigales.cl/acana-singles-duck-pear-perros.html",
        "button_xpath": "//*[@id=\"option-label-acana_duckpear_perros_cantidad-644-item-1561\"]"
    },
    "petdotu11": {
        "url": "https://www.amigales.cl/acana-heritage-freshwater-fish-perros.html",
        "button_xpath": "//*[@id=\"option-label-acana_fresh_perros_cantidad-643-item-1558\"]"
    },
    "petdotu10": {
        "url": "https://www.amigales.cl/acana-first-feas-gatitos.html",
        "button_xpath": "-"
    },
    "petdotu160": {
        "url": "https://www.amigales.cl/acana-heritage-free-run-poultry-perros.html",
        "button_xpath": "//*[@id=\"option-label-acana_freerun_perros_cantidad-642-item-1554\"]"
    },
    "petdotu121": {
        "url": "https://www.amigales.cl/acana-singles-pork-squash-perros.html",
        "button_xpath": "//*[@id=\"option-label-acana_porksquash_perros-903-item-2327\"]"
    },
    "petdotu205": {
        "url": "https://www.amigales.cl/adaptil-repuesto.html",
        "button_xpath": "-"
    },
    "petdotu97": {
        "url": "https://www.amigales.cl/collar-adaptil.html",
        "button_xpath": "-"
    },
    "petdotu96": {
        "url": "https://www.amigales.cl/collar-adaptil.html",
        "button_xpath": "//*[@id=\"option-label-collar_adaptil_tamano-325-item-570\"]"
    },
    "petdotu93": {
        "url": "https://www.amigales.cl/adaptil-difusor-repuesto.html",
        "button_xpath": "-"
    },
    "petdotu142": {
        "url": "https://www.amigales.cl/advantage-pipeta-antipulgas-para-gatos-hasta-4-kilos.html",
        "button_xpath": "-"
    },
    "petdotu135": {
        "url": "https://www.amigales.cl/advantage-pipeta-antipulgas-para-gatos-desde-4-a-8-kilos.html",
        "button_xpath": "-"
    },
    "petdotu84": {
        "url": "https://www.amigales.cl/arena-sanitaria-america-litter-ultra-odor-seal.html",
        "button_xpath": "//*[@id=\"option-label-arena_americalitter_cantidad-518-item-1119\"]"
    },
    "petdotu72": {
        "url": "https://www.amigales.cl/arena-sanitaria-american-litter-lavanda.html",
        "button_xpath": "//*[@id=\"option-label-americalitter_lavanda_size-1171-item-3112\"]"
    },
    "petdotu125": {
        "url": "https://www.amigales.cl/arena-sanitaria-america-litter.html",
        "button_xpath": "//*[@id=\"option-label-arena_americalitter_cantidad-518-item-1119\"]"
    },
    "petdotu1": {
        "url": "https://www.amigales.cl/apoquel-zoetis-20-comprimidos.html",
        "button_xpath": "//*[@id=\"option-label-apoquel_zoetis_contenido-785-item-1985\"]"
    },
    "petdotu2": {
        "url": "https://www.amigales.cl/apoquel-zoetis-20-comprimidos.html",
        "button_xpath": "//*[@id=\"option-label-apoquel_zoetis_contenido-785-item-1983\"]"
    },
    "petdotu3": {
        "url": "https://www.amigales.cl/apoquel-zoetis-20-comprimidos.html",
        "button_xpath": "//*[@id=\"option-label-apoquel_zoetis_contenido-785-item-1984\"]"
    },
    "petdotu82": {
        "url": "https://www.amigales.cl/artri-tabs-60-tabletas.html",
        "button_xpath": "-"
    },
    "petdotu66": {
        "url": "https://www.amigales.cl/beaphar-laveta-taurina.html",
        "button_xpath": "-"
    },
    "petdotu65": {
        "url": "https://www.amigales.cl/beaphar-laveta-carnitina.html",
        "button_xpath": "-"
    },
    "petdotu34": {
        "url": "https://www.amigales.cl/beaphar-calmingspot-gatos.html",
        "button_xpath": "-"
    },
    "petdotu36": {
        "url": "https://www.amigales.cl/snacks-calmantes-gatos.html",
        "button_xpath": "-"
    },
    "petdotu38": {
        "url": "https://www.amigales.cl/tabletas-calmantes-beaphar.html",
        "button_xpath": "-"
    },
    "petdotu37": {
        "url": "https://www.amigales.cl/collar-calmante-gatos.html",
        "button_xpath": "-"
    },
    "petdotu170": {
        "url": "https://www.amigales.cl/belcando-finest-light.html",
        "button_xpath": "//*[@id=\"option-label-belcando_finestlight_peso-1018-item-2644\"]"
    },
    "petdotu132": {
        "url": "https://www.amigales.cl/belcando-finest-gf-senior.html",
        "button_xpath": "//*[@id=\"option-label-belcando_finestgfsenior_peso-1024-item-2663\"]"
    },
    "petdotu48": {
        "url": "https://www.amigales.cl/biljac-adultselect-perros.html",
        "button_xpath": "//*[@id=\"option-label-biljac_adultselect_peso-869-item-2234\"]"
    },
    "petdotu50": {
        "url": "https://www.amigales.cl/alimento-bil-jac-puppy-select-cachorros.html",
        "button_xpath": "//*[@id=\"option-label-biljac_puppy_peso-306-item-2216\"]"
    },
    "petdotu49": {
        "url": "https://www.amigales.cl/bil-jac-small-breed-para-perros.html",
        "button_xpath": "-"
    },
    "petdotu33": {
        "url": "https://www.amigales.cl/antiparasitario-pipeta-bravecto-gatos.html",
        "button_xpath": "//*[@id=\"option-label-bravecto_gatos-1029-item-2673\"]"
    },
    "petdotu31": {
        "url": "https://www.amigales.cl/antiparasitario-pipeta-bravecto-gatos.html",
        "button_xpath": "//*[@id=\"option-label-bravecto_gatos-1029-item-2674\"]"
    },
    "petdotu148": {
        "url": "https://www.amigales.cl/antiparasitario-pipeta-bravecto-gatos.html",
        "button_xpath": "//*[@id=\"option-label-bravecto_gatos-1029-item-2875\"]"
    },
    "petdotu32": {
        "url": "https://www.amigales.cl/bravecto-perros.html",
        "button_xpath": "//*[@id=\"option-label-bravecto_pesos-321-item-553\"]"
    },
    "petdotu30": {
        "url": "https://www.amigales.cl/bravecto-perros.html",
        "button_xpath": "//*[@id=\"option-label-bravecto_pesos-321-item-554\"]"
    },
    "petdotu29": {
        "url": "https://www.amigales.cl/bravecto-perros.html",
        "button_xpath": "//*[@id=\"option-label-bravecto_pesos-321-item-555\"]"
    },
    "petdotu28": {
        "url": "https://www.amigales.cl/bravecto-perros.html",
        "button_xpath": "//*[@id=\"option-label-bravecto_pesos-321-item-556\"]"
    },
    "petdotu181": {
        "url": "https://www.amigales.cl/bravecto-perros.html",
        "button_xpath": "//*[@id=\"option-label-bravecto_pesos-321-item-557\"]"
    },
    "petdotu171": {
        "url": "https://www.amigales.cl/bravery-pollo-razas-grandes-medianas.html",
        "button_xpath": "//*[@id=\"option-label-bravery_pollo_largemedium-836-item-2153\"]"
    },
    "petdotu58": {
        "url": "https://www.amigales.cl/brit-cachorros-salmon-papas.html",
        "button_xpath": "//*[@id=\"option-label-brit_salmon_cachorros-711-item-1745\"]"
    },
    "petdotu52": {
        "url": "https://www.amigales.cl/brit-care-cordero-arroz-perro-raza-pequena.html",
        "button_xpath": "//*[@id=\"option-label-brit_cordero_pequena-721-item-1762\"]"
    },
    "petdotu53": {
        "url": "https://www.amigales.cl/brit-care-cordero-perros-raza-mediana.html",
        "button_xpath": "//*[@id=\"option-label-brit_cordero_mediana-725-item-1777\"]"
    },
    "petdotu54": {
        "url": "https://www.amigales.cl/brit-care-cordero-hipoalergenico-cachorros.html",
        "button_xpath": "//*[@id=\"option-label-brit_cordero_cachorro-866-item-2225\"]"
    },
    "petdotu56": {
        "url": "https://www.amigales.cl/brit-care-conejo-hipoalergenico-perros-sobrepeso.html",
        "button_xpath": "//*[@id=\"option-label-brit_conejo_perdidapeso-728-item-1788\"]"
    },
    "petdotu59": {
        "url": "https://www.amigales.cl/brit-care-salmon-light-grain-free-perros-senior.html",
        "button_xpath": "//*[@id=\"option-label-brit_salmon_light_senior-714-item-1750\"]"
    },
    "petdotu51": {
        "url": "https://www.amigales.cl/brit-care-cordero-arroz-senior.html",
        "button_xpath": "//*[@id=\"option-label-brit_cordero_senior-726-item-1779\"]"
    },
    "petdotu57": {
        "url": "https://www.amigales.cl/brit-para-perros-adultos-salmon-raza-pequena-mediana-12-kilos.html",
        "button_xpath": "-"
    },
    "petdotu106": {
        "url": "https://www.amigales.cl/brit-care-cordero-hipoalergenico-cachorros.html",
        "button_xpath": "//*[@id=\"option-label-brit_cordero_cachorro-866-item-2225\"]"
    },
    "petdotu110": {
        "url": "https://www.amigales.cl/brit-care-esterilizado-control-peso-gatos.html",
        "button_xpath": "//*[@id=\"option-label-britcat_daisy_peso-876-item-2255\"]"
    },
    "petdotu123": {
        "url": "https://www.amigales.cl/brit-care-salmon-junior-grain-free-perros-raza-grande.html",
        "button_xpath": "//*[@id=\"option-label-brit_salmon_cachorros-711-item-1745\"]"
    },
    "petdotu127": {
        "url": "https://www.amigales.cl/brit-care-kitten-gatitos.html",
        "button_xpath": "//*[@id=\"option-label-britcat_crazy_pesos-879-item-2263\"]"
    },
    "petdotu130": {
        "url": "https://www.amigales.cl/brit-care-pelaje-haircare-healthy-shiny-coat-gatos.html",
        "button_xpath": "//*[@id=\"option-label-britcat_sunny_peso-883-item-2276\"]"
    },
    "petdotu133": {
        "url": "https://www.amigales.cl/brit-perros-adultos-salmon-pequena-mediana.html",
        "button_xpath": "//*[@id=\"option-label-brit_adulto_salmon_peq_med-708-item-1736\"]"
    },
    "petdotu134": {
        "url": "https://www.amigales.cl/brit-care-kitten-gatitos.html",
        "button_xpath": "//*[@id=\"option-label-britcat_crazy_pesos-879-item-2264\"]"
    },
    "petdotu136": {
        "url": "https://www.amigales.cl/brit-cachorros-salmon-grain-free-cachorros.html",
        "button_xpath": "//*[@id=\"option-label-brit_salmon_cachorros-711-item-1744\"]"
    },
    "petdotu139": {
        "url": "https://www.amigales.cl/brit-care-sensitive-venado-perros.html",
        "button_xpath": "//*[@id=\"option-label-brit_sensitive_peso-1048-item-2723\"]"
    },
    "petdotu155": {
        "url": "https://www.amigales.cl/brit-care-esterilizado-salud-urinaria-gatos.html",
        "button_xpath": "//*[@id=\"option-label-britcat_missy_peso-877-item-2257\"]"
    },
    "petdotu81": {
        "url": "https://www.amigales.cl/calmer-calma.html",
        "button_xpath": "-"
    },
    "petdotu159": {
        "url": "https://www.amigales.cl/cerenia-comprimidos.html",
        "button_xpath": "//*[@id=\"option-label-zoetis_cerenia_mg-1098-item-2887\"]"
    },
    "petdotu77": {
        "url": "https://www.amigales.cl/oxtrin.html",
        "button_xpath": "-"
    },
    "petdotu89": {
        "url": "https://www.amigales.cl/sucravet.html",
        "button_xpath": "-"
    },
    "petdotu71": {
        "url": "https://www.amigales.cl/florafix-15g.html",
        "button_xpath": "-"
    },
    "petdotu167": {
        "url": "https://www.amigales.cl/clindabone-165-clindamicina.html",
        "button_xpath": "-"
    },
    "petdotu83": {
        "url": "https://www.amigales.cl/condrovet-30-comprimidos.html",
        "button_xpath": "-"
    },
    "petdotu91": {
        "url": "https://www.amigales.cl/dermisolona-30-ml-solucion-oral.html",
        "button_xpath": "-"
    },
    "petdotu95": {
        "url": "https://www.amigales.cl/dermisolona-20mg-10-comprimidos.html",
        "button_xpath": "-"
    },
    "petdotu182": {
        "url": "https://www.amigales.cl/hematon-b12-elixir.html",
        "button_xpath": "-"
    },
    "petdotu193": {
        "url": "https://www.amigales.cl/doguivit-senior.html",
        "button_xpath": "-"
    },
    "petdotu61": {
        "url": "https://www.amigales.cl/catalog/product/view/id/5199/s/mixantip-plus-crema/category/2/",
        "button_xpath": "//*[@id=\"option-label-dragpharma_mixantip_gr-1121-item-2943\"]"
    },
    "petdotu60": {
        "url": "https://www.amigales.cl/catalog/product/view/id/5199/s/mixantip-plus-crema/category/2/",
        "button_xpath": "//*[@id=\"option-label-dragpharma_mixantip_gr-1121-item-2944\"]"
    },
    "petdotu185": {
        "url": "https://www.amigales.cl/antiparasitario-comprimido-drontal-plus-perros.html",
        "button_xpath": "//*[@id=\"option-label-drontal_plus_perro_peso-196-item-219\"]"
    },
    "petdotu143": {
        "url": "https://www.amigales.cl/antiparasitario-comprimido-drontal-plus-perros.html",
        "button_xpath": "//*[@id=\"option-label-drontal_plus_perro_peso-196-item-218\"]"
    },
    "petdotu188": {
        "url": "https://www.amigales.cl/antiparasitario-drontal-gatos.html",
        "button_xpath": "//*[@id=\"option-label-drontal_cats_cantidad-815-item-2079\"]"
    },
    "petdotu145": {
        "url": "https://www.amigales.cl/neptra-solucion-otica.html",
        "button_xpath": "-"
    },
    "petdotu190": {
        "url": "https://www.amigales.cl/purina-excellent-cachorros-razas-medianas-grandes.html",
        "button_xpath": "-"
    },
    "petdotu191": {
        "url": "https://www.amigales.cl/purina-excellent-perro-adulto-raza-grande-15kg.html",
        "button_xpath": "-"
    },
    "petdotu105": {
        "url": "https://www.amigales.cl/purina-excellent-perro-adulto-smn-skin-care.html",
        "button_xpath": "-"
    },
    "petdotu42": {
        "url": "https://www.amigales.cl/feliway-classic-difusor-repuesto.html",
        "button_xpath": "-"
    },
    "petdotu43": {
        "url": "https://www.amigales.cl/feliway-friends-difusor-repuesto.html",
        "button_xpath": "-"
    },
    "petdotu40": {
        "url": "https://www.amigales.cl/feliway-classic-spray.html",
        "button_xpath": "-"
    },
    "petdotu39": {
        "url": "https://www.amigales.cl/feliway-classic-repuesto.html",
        "button_xpath": "-"
    },
    "petdotu41": {
        "url": "https://www.amigales.cl/feliway-friends-repuesto.html",
        "button_xpath": "-"
    },
    "petdotu18": {
        "url": "https://www.amigales.cl/fit-formula-cachorro.html",
        "button_xpath": "//*[@id=\"option-label-fit_formula_dog-1788-item-5174\"]"
    },
    "petdotu15": {
        "url": "https://www.amigales.cl/fit-formula-gato-adulto.html",
        "button_xpath": "//*[@id=\"option-label-fit_formula_cat-1789-item-5176\"]"
    },
    "petdotu17": {
        "url": "https://www.amigales.cl/fit-formula-perro-adulto-20kg.html",
        "button_xpath": "-"
    },
    "petdotu16": {
        "url": "https://www.amigales.cl/fit-formula-perro-senior.html",
        "button_xpath": "-"
    },
    "petdotu19": {
        "url": "https://www.amigales.cl/fit-formula-perro-adulto-raza-pequena-10kg.html",
        "button_xpath": "-"
    },
    "petdotu126": {
        "url": "https://www.amigales.cl/fit-formula-perro-senior-raza-pequena-10kg.html",
        "button_xpath": "-"
    },
    "petdotu99": {
        "url": "https://www.amigales.cl/hills-rd-perros.html",
        "button_xpath": "//*[@id=\"option-label-hills_rd_perros-931-item-2400\"]"
    },
    "petdotu88": {
        "url": "https://www.amigales.cl/hills-small-paws-cachorros.html",
        "button_xpath": "//*[@id=\"option-label-hills_smallpupy_size-1265-item-3447\"]"
    },
    "petdotu85": {
        "url": "https://www.amigales.cl/hills-metabolic-perros.html",
        "button_xpath": "//*[@id=\"option-label-hills_metabolic_perro_peso-1057-item-2759\"]"
    },
    "petdotu94": {
        "url": "https://www.amigales.cl/ohm-comprimidos-calmantes-perros-gatos.html",
        "button_xpath": "-"
    },
    "petdotu87": {
        "url": "https://www.amigales.cl/itraskin-suspension-oral.html",
        "button_xpath": "-"
    },
    "petdotu109": {
        "url": "https://www.amigales.cl/josera-festival-perros-medianos-grandes.html",
        "button_xpath": "Revisar"
    },
    "petdotu120": {
        "url": "https://www.amigales.cl/josera-ente-kartoffel-perros-todas-razas.html",
        "button_xpath": "Revisar"
    },
    "petdotu117": {
        "url": "https://www.amigales.cl/josera-josidog-regular-perros-adultos.html",
        "button_xpath": "-"
    },
    "petdotu124": {
        "url": "https://www.amigales.cl/josera-naturecat-gatos-junior.html",
        "button_xpath": "Revisar"
    },
    "petdotu156": {
        "url": "https://www.amigales.cl/josera-light-vital-perros-todas-razas.html",
        "button_xpath": "Revisar"
    },
    "petdotu141": {
        "url": "https://www.amigales.cl/josera-naturelle-gatos-sobrepeso-esterilizado.html",
        "button_xpath": "//*[@id=\"option-label-josera_gatos_kilos-1359-item-3787\"]"
    },
    "petdotu144": {
        "url": "https://www.amigales.cl/josera-balance-perros-senior-razas-medianas-grandes.html",
        "button_xpath": "-"
    },
    "petdotu161": {
        "url": "https://www.amigales.cl/leonardo-senior-gato.html",
        "button_xpath": "//*[@id=\"option-label-leonardo_senior_peso-995-item-2571\"]"
    },
    "petdotu164": {
        "url": "https://www.amigales.cl/leonardo-pato-gato.html",
        "button_xpath": "//*[@id=\"option-label-leonardo_pato_peso-993-item-2565\"]"
    },
    "petdotu151": {
        "url": "https://www.amigales.cl/leonardo-senior-gato.html",
        "button_xpath": "//*[@id=\"option-label-leonardo_senior_peso-995-item-2570\"]"
    },
    "petdotu152": {
        "url": "https://www.amigales.cl/leonardo-light-gatos.html",
        "button_xpath": "//*[@id=\"option-label-leonardo_light_gatos-994-item-2569\"]"
    },
    "petdotu162": {
        "url": "https://www.amigales.cl/meloxivet-solucion-oral.html",
        "button_xpath": "-"
    },
    "petdotu198": {
        "url": "https://www.amigales.cl/naxpet-10mg.html",
        "button_xpath": "-"
    },
    "petdotu75": {
        "url": "https://www.amigales.cl/naxpet-solucion-oral.html",
        "button_xpath": "-"
    },
    "petdotu172": {
        "url": "https://www.amigales.cl/nexgard-spectra-antiparasitario-3-tabletas.html",
        "button_xpath": "//*[@id=\"option-label-nexgard_spectra_1_peso-1052-item-2747\"]"
    },
    "petdotu189": {
        "url": "https://www.amigales.cl/nexgard-spectra-antiparasitario-1-tableta.html",
        "button_xpath": "//*[@id=\"option-label-nexgard_spectra_1_peso-1052-item-2747\"]"
    },
    "petdotu68": {
        "url": "https://www.amigales.cl/nexgard-spectra-antiparasitario-1-tableta.html",
        "button_xpath": "//*[@id=\"option-label-nexgard_spectra_1_peso-1052-item-2748\"]"
    },
    "petdotu67": {
        "url": "https://www.amigales.cl/nexgard-spectra-antiparasitario-3-tabletas.html",
        "button_xpath": "//*[@id=\"option-label-nexgard_spectra_1_peso-1052-item-2748\"]"
    },
    "petdotu70": {
        "url": "https://www.amigales.cl/nexgard-spectra-antiparasitario-1-tableta.html",
        "button_xpath": "//*[@id=\"option-label-nexgard_spectra_1_peso-1052-item-2749\"]"
    },
    "petdotu69": {
        "url": "https://www.amigales.cl/nexgard-spectra-antiparasitario-3-tabletas.html",
        "button_xpath": "//*[@id=\"option-label-nexgard_spectra_1_peso-1052-item-2749\"]"
    },
    "petdotu138": {
        "url": "https://www.amigales.cl/nexgard-spectra-antiparasitario-3-tabletas.html",
        "button_xpath": "//*[@id=\"option-label-nexgard_spectra_1_peso-1052-item-2750\"]"
    },
    "petdotu147": {
        "url": "https://www.amigales.cl/nexgard-spectra-antiparasitario-1-tableta.html",
        "button_xpath": "//*[@id=\"option-label-nexgard_spectra_1_peso-1052-item-2750\"]"
    },
    "petdotu174": {
        "url": "https://www.amigales.cl/nutribound-perros-virbac.html",
        "button_xpath": "-"
    },
    "petdotu165": {
        "url": "https://www.amigales.cl/nutrience-original-gatos-adultos.html",
        "button_xpath": "//*[@id=\"option-label-nutrience_catoriginal_adult-1247-item-3379\"]"
    },
    "petdotu175": {
        "url": "https://www.amigales.cl/nutrience-original-gatos-indoor.html",
        "button_xpath": "//*[@id=\"option-label-nutrience_catoriginal_adult-1247-item-3379\"]"
    },
    "petdotu80": {
        "url": "https://www.amigales.cl/arena-sanitaria-odour-buster-original.html",
        "button_xpath": "//*[@id=\"option-label-odourbuster_original_cantidad-656-item-1598\"]"
    },
    "petdotu157": {
        "url": "https://www.amigales.cl/oftavet-solucion-oftalmologica.html",
        "button_xpath": "-"
    },
    "petdotu131": {
        "url": "https://www.amigales.cl/orijen-puppy.html",
        "button_xpath": "//*[@id=\"option-label-orijen_puppy_cantidad-677-item-1659\"]"
    },
    "petdotu153": {
        "url": "https://www.amigales.cl/orijen-original-cat-gatos.html",
        "button_xpath": "//*[@id=\"option-label-orijen_catkitten_cantidad-647-item-1569\"]"
    },
    "petdotu63": {
        "url": "https://www.amigales.cl/oven-baked-pescado-perros-11-34-kg.html",
        "button_xpath": "-"
    },
    "petdotu62": {
        "url": "https://www.amigales.cl/oven-baked-pollo-perros-11-34-kg.html",
        "button_xpath": "-"
    },
    "petdotu64": {
        "url": "https://www.amigales.cl/oven-baked-pollo-perros-senior-11-34-kg.html",
        "button_xpath": "-"
    },
    "petdotu206": {
        "url": "https://www.amigales.cl/papainpet-suplemento.html",
        "button_xpath": "-"
    },
    "petdotu202": {
        "url": "https://www.amigales.cl/shampoo-petever-dragpharma.html",
        "button_xpath": "-"
    },
    "petdotu107": {
        "url": "https://www.amigales.cl/pimocard-5.html",
        "button_xpath": "-"
    },
    "petdotu180": {
        "url": "https://www.amigales.cl/pro-plan-cachorros-raza-mediana.html",
        "button_xpath": "//*[@id=\"option-label-proplan_complete_cachorros-686-item-1684\"]"
    },
    "petdotu187": {
        "url": "https://www.amigales.cl/proplan-gato-urinario.html",
        "button_xpath": "//*[@id=\"option-label-proplan_caturinary_size-1297-item-3565\"]"
    },
    "petdotu192": {
        "url": "https://www.amigales.cl/pro-plan-esterilizado-gatos.html",
        "button_xpath": "//*[@id=\"option-label-proplan_esterilizado_gatos-894-item-2305\"]"
    },
    "petdotu184": {
        "url": "https://www.amigales.cl/pro-plan-perro-adulto-razas-pequenas.html",
        "button_xpath": "//*[@id=\"option-label-proplan_perro_adulto_pequeno-681-item-1668\"]"
    },
    "petdotu179": {
        "url": "https://www.amigales.cl/shampoo-regepipel-plus.html",
        "button_xpath": "-"
    },
    "petdotu5": {
        "url": "https://www.amigales.cl/revolution-plus-antiparasitario-gatos.html",
        "button_xpath": "//*[@id=\"option-label-revolution_plus_gatos_peso-1102-item-2901\"]"
    },
    "petdotu4": {
        "url": "https://www.amigales.cl/revolution-plus-antiparasitario-gatos.html",
        "button_xpath": "//*[@id=\"option-label-revolution_plus_gatos_peso-1102-item-2902\"]"
    },
    "petdotu119": {
        "url": "https://www.amigales.cl/revolution-plus-antiparasitario-gatos.html",
        "button_xpath": "//*[@id=\"option-label-revolution_plus_gatos_peso-1102-item-2903\"]"
    },
    "petdotu27": {
        "url": "https://www.amigales.cl/rimadyl-anti-inflamatorio-100-mg.html",
        "button_xpath": "//*[@id=\"option-label-rimadyl_cienmg_cantidad-827-item-2116\"]"
    },
    "petdotu26": {
        "url": "https://www.amigales.cl/rimadyl-anti-inflamatorio-100-mg.html",
        "button_xpath": "//*[@id=\"option-label-rimadyl_cienmg_cantidad-827-item-2117\"]"
    },
    "petdotu44": {
        "url": "https://www.amigales.cl/royal-canin-mother-baby-cat-1-5kg.html",
        "button_xpath": "-"
    },
    "petdotu45": {
        "url": "https://www.amigales.cl/royal-canin-hypoallergenic-perros-razas-pequenas.html",
        "button_xpath": "Revisar"
    },
    "petdotu46": {
        "url": "https://www.amigales.cl/royal-canin-mini-puppy.html",
        "button_xpath": "//*[@id=\"option-label-royal_mini_size-1461-item-4097\"]"
    },
    "petdotu47": {
        "url": "https://www.amigales.cl/royal-canin-mini-perro-adulto.html",
        "button_xpath": "Revisar"
    },
    "petdotu201": {
        "url": "https://www.amigales.cl/senilpet-cerebral-5-razas-pequenas.html",
        "button_xpath": "-"
    },
    "petdotu207": {
        "url": "https://www.amigales.cl/silimadrag-silimarina-drag-pharma.html",
        "button_xpath": "-"
    },
    "petdotu203": {
        "url": "https://www.amigales.cl/simparica-antiparasitario-perros-1-comprimido.html",
        "button_xpath": "//*[@id=\"option-label-simparica_perros-751-item-1867\"]"
    },
    "petdotu169": {
        "url": "https://www.amigales.cl/simparica-antiparasitario-perros-3-comprimidos.html",
        "button_xpath": "//*[@id=\"option-label-simparica_3_comprimidos_peso-1049-item-2730\"]"
    },
    "petdotu163": {
        "url": "https://www.amigales.cl/simparica-trio-zoetis-3-comprimidos.html",
        "button_xpath": "//*[@id=\"option-label-simparica_trio_sizes-1625-item-4613\"]"
    },
    "petdotu22": {
        "url": "https://www.amigales.cl/simparica-antiparasitario-perros-1-comprimido.html",
        "button_xpath": "//*[@id=\"option-label-simparica_perros-751-item-1869\"]"
    },
    "petdotu23": {
        "url": "https://www.amigales.cl/simparica-antiparasitario-perros-3-comprimidos.html",
        "button_xpath": "//*[@id=\"option-label-simparica_3_comprimidos_peso-1049-item-2732\"]"
    },
    "petdotu25": {
        "url": "https://www.amigales.cl/simparica-antiparasitario-perros-1-comprimido.html",
        "button_xpath": "//*[@id=\"option-label-simparica_perros-751-item-1868\"]"
    },
    "petdotu24": {
        "url": "https://www.amigales.cl/simparica-antiparasitario-perros-3-comprimidos.html",
        "button_xpath": "//*[@id=\"option-label-simparica_3_comprimidos_peso-1049-item-2733\"]"
    },
    "petdotu21": {
        "url": "https://www.amigales.cl/simparica-antiparasitario-perros-1-comprimido.html",
        "button_xpath": "//*[@id=\"option-label-simparica_perros-751-item-1870\"]"
    },
    "petdotu20": {
        "url": "https://www.amigales.cl/simparica-antiparasitario-perros-3-comprimidos.html",
        "button_xpath": "//*[@id=\"option-label-simparica_3_comprimidos_peso-1049-item-2733\"]"
    },
    "petdotu210": {
        "url": "https://www.amigales.cl/superpet-omega-3-6-para-gato.html",
        "button_xpath": "-"
    },
    "petdotu79": {
        "url": "https://www.amigales.cl/synulox-250mg.html",
        "button_xpath": "-"
    },
    "petdotu92": {
        "url": "https://www.amigales.cl/ursovet-drag-pharma.html",
        "button_xpath": "-"
    },
    "petdotu186": {
        "url": "https://www.amigales.cl/glicopan-125-ml.html",
        "button_xpath": "-"
    },
    "petdotu208": {
        "url": "https://www.amigales.cl/hemolitan-pet-suplemento.html",
        "button_xpath": "//*[@id=\"option-label-hemolitan_formato-1094-item-2877\"]"
    },
    "petdotu98": {
        "url": "https://www.amigales.cl/virbac-allercalm-shampoo.html",
        "button_xpath": "-"
    },
    "petdotu100": {
        "url": "https://www.amigales.cl/phisio-anti-olor-auricular.html",
        "button_xpath": "-"
    },
    "petdotu166": {
        "url": "https://www.amigales.cl/virbac-cat-allergy-veterinary-hpm.html",
        "button_xpath": "-"
    },
    "petdotu146": {
        "url": "https://www.amigales.cl/neutered-adult-cat-virbac-hpm.html",
        "button_xpath": "//*[@id=\"option-label-virbac_cat_size-1385-item-3874\"]"
    },
    "petdotu118": {
        "url": "https://www.amigales.cl/perro-allergy-a2-virbac-hpm-intolerancia-alimentaria-pescado.html",
        "button_xpath": "//*[@id=\"option-label-virbac_dog_size-1386-item-3879\"]"
    },
    "petdotu128": {
        "url": "https://www.amigales.cl/perro-weight-loss-diabetes-virbac-hpm.html",
        "button_xpath": "//*[@id=\"option-label-virbac_dog_size-1386-item-3879\"]"
    },
    "petdotu137": {
        "url": "https://www.amigales.cl/perro-weight-loss-control-virbac-hpm.html",
        "button_xpath": "//*[@id=\"option-label-virbac_dog_size-1386-item-3879\"]"
    },
    "petdotu73": {
        "url": "https://www.amigales.cl/silimavet-silimarina-vitanimal.html",
        "button_xpath": "//*[@id=\"option-label-silimarina_cantidad-956-item-2468\"]"
    },
    "petdotu74": {
        "url": "https://www.amigales.cl/silimavet-silimarina-vitanimal.html",
        "button_xpath": "//*[@id=\"option-label-silimarina_cantidad-956-item-2469\"]"
    },
    "petdotu158": {
        "url": "https://www.amigales.cl/hemolivet-vitanimal.html",
        "button_xpath": "-"
    },
    "petdotu86": {
        "url": "https://www.amigales.cl/wanpy-jerky-cordero.html",
        "button_xpath": "-"
    },
    "petdotu600": {
        "url": "https://www.amigales.cl/leonardo-maxigf-gatos.html",
        "button_xpath": "//*[@id=\"option-label-leonardo_maxigf_peso-992-item-2563\"]"
    },
    "petdotu194": {
        "url": "https://www.amigales.cl/acana-wild-coast-perros.html",
        "button_xpath": "//*[@id=\"option-label-acana_wildcoast_perros-906-item-2334\"]"
    },
    "petdotu122": {
        "url": "https://www.amigales.cl/brit-care-cordero-arroz-perro-raza-pequena.html",
        "button_xpath": "//*[@id=\"option-label-brit_cordero_pequena-721-item-1761\"]"
    },
    "petdotu55": {
        "url": "https://www.amigales.cl/brit-care-esterilizado-salud-urinaria-gatos.html",
        "button_xpath": "//*[@id=\"option-label-britcat_missy_peso-877-item-2258\"]"
    },
    "petdotu116": {
        "url": "https://www.amigales.cl/brit-care-salmon-grain-free-perros-razas-grandes.html",
        "button_xpath": "//*[@id=\"option-label-brit_salmonlarge_dog_peso-1026-item-2668\"]"
    },
    "petdotu113": {
        "url": "https://www.amigales.cl/brit-care-cordero-hipoalergenico-junior-grain-free-perros-raza-grande.html",
        "button_xpath": "//*[@id=\"option-label-brit_cordero_juniorlarge-868-item-2231\"]"
    },
     "petdotu140": {
        "url": "https://www.amigales.cl/brit-care-conejo-hipoalergenico-perros-sobrepeso.html",
        "button_xpath": "//*[@id=\"option-label-brit_conejo_perdidapeso-728-item-1787\"]"
    },
      "petdotu178": {
        "url": "https://www.amigales.cl/canigest-combi-16-ml.html",
        "button_xpath": "-"
    },
       "petdotu183": {
        "url": "https://www.amigales.cl/hills-smallbites-adulto-mayor.html",
        "button_xpath": "//*[@id=\"option-label-hills_smalbites_adul7_cantidad-651-item-1577\"]"
    },
        "petdotu114": {
        "url": "https://www.amigales.cl/orijen-small-breed-perros.html",
        "button_xpath": "//*[@id=\"option-label-orijen_smallbreed_size-1336-item-3708\"]"
    },
        
         "petdotu195": {
        "url": "https://www.amigales.cl/paz-pet-modificador-conducta-perros.html",
        "button_xpath": "-"
    },
        "petdotu187": {
        "url": "https://www.amigales.cl/proplan-gato-urinario.html",
        "button_xpath": "//*[@id=\"option-label-proplan_caturinary_size-1297-item-3565\"]"
    },  
        "petdotu108": {
        "url": "https://www.amigales.cl/traumeel-alergias.html",
        "button_xpath": "-"
    },
        "petdotu222": {
        "url": "https://www.amigales.cl/acana-heritage-light-fit-perros.html",
        "button_xpath": "//*[@id=\"option-label-acana_lighfit_perros_cantidad-675-item-1654\"]"
    },
}


results = []

for sku_key, info in sku2.items():
    driver.get(info["url"])
    precio_oferta = "No disponible"
    precio_normal = "No disponible"
    stock = "Con Stock"
    time.sleep(1)
    
    try:
        # Intenta hacer clic en el botón específico para cada SKU si el XPath no es "-"
        if info["button_xpath"] != "-":
            try:
                button = driver.find_element(By.XPATH, info["button_xpath"])
                driver.execute_script("arguments[0].click();", button)
                # button.click()
                time.sleep(1)
            except (NoSuchElementException, ElementClickInterceptedException) as e:
                print(f"No se pudo hacer clic en el botón para el SKU {sku_key} - {e}")
        
        # Intenta obtener el precio de oferta
        try:
            precio_oferta_element = driver.find_element(By.CLASS_NAME, "product-info-price2")  # Cambiar según sea necesario
            precio_oferta = precio_oferta_element.text
            stock_element = driver.find_element(By.XPATH, "/html/body/div[2]/main/div[3]/div/div[1]/div[4]/div[3]")
            stock = stock_element.text
        except NoSuchElementException:
            pass
        
        # Intenta obtener el precio normal
        try:
            precio_normal_element = driver.find_element(By.XPATH, '/html/body/div[2]/main/div[3]/div/div[1]/div[4]/div[1]')  # Cambiar según sea necesario
            precio_normal = precio_normal_element.text
            stock_element = driver.find_element(By.XPATH, "/html/body/div[2]/main/div[3]/div/div[1]/div[4]/div[3]")
            stock = stock_element.text
        except NoSuchElementException:
            pass
        
        if precio_oferta == "No disponible" and precio_normal == "No disponible":
            try:
                # Intentar con otro XPath si no se encuentran los precios anteriores
                precio_normal_element = driver.find_element(By.XPATH, '/html/body/div[2]/main/div[3]/div/div[1]/div[4]/div[1]/span[2]')  # Cambiar según sea necesario
                precio_normal = precio_normal_element.text
                stock_element = driver.find_element(By.XPATH, "/html/body/div[2]/main/div[3]/div/div[1]/div[4]/div[3]")
                stock = stock_element.text
            except NoSuchElementException as e:
                print(f"No se pudo encontrar el precio en la URL {info['url']} - {e}")
        
    except NoSuchElementException as e:
        print(f"Error procesando el SKU {sku_key} en la URL {info['url']} - {e}")
    
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

print(results)
# results = []

# for sku_key, info in sku2.items():
#     driver.get(info["url"])
#     precio_oferta = "No disponible"
#     precio_normal = "No disponible"
#     stock= "Con Stock"
#     time.sleep(1)
    
#     try:
#         # Intenta hacer clic en el botón específico para cada SKU si el XPath no es "-"
#         if info["button_xpath"] != "-":
#             button = driver.find_element(By.XPATH, info["button_xpath"])
#             button.click()
#             time.sleep(1)
        
#         # Intenta obtener el precio de oferta
#         try:
#             precio_oferta_element = driver.find_element(By.CLASS_NAME, "product-info-price2")  # Cambiar según sea necesario
#             precio_oferta = precio_oferta_element.text
#             stock_element= driver.find_element(By.XPATH,"/html/body/div[2]/main/div[3]/div/div[1]/div[4]/div[3]")
#             stock= stock_element.text
#         except NoSuchElementException:
#             pass
        
#         # Intenta obtener el precio normal
#         try:
#             precio_normal_element = driver.find_element(By.XPATH, '/html/body/div[2]/main/div[3]/div/div[1]/div[4]/div[1]')  # Cambiar según sea necesario
#             precio_normal = precio_normal_element.text
#             stock_element= driver.find_element(By.XPATH,"/html/body/div[2]/main/div[3]/div/div[1]/div[4]/div[3]")
#             stock= stock_element.text
#         except NoSuchElementException:
#             pass
        
#         if precio_oferta == "No disponible" and precio_normal == "No disponible":
#             try:
#                 # Intentar con otro XPath si no se encuentran los precios anteriores
#                 precio_normal_element = driver.find_element(By.XPATH, '/html/body/div[2]/main/div[3]/div/div[1]/div[4]/div[1]/span[2]')  # Cambiar según sea necesario
#                 precio_normal = precio_normal_element.text
#                 stock_element= driver.find_element(By.XPATH,"/html/body/div[2]/main/div[3]/div/div[1]/div[4]/div[3]")
#                 stock= stock_element.text
#             except NoSuchElementException as e:
#                 print(f"No se pudo encontrar el precio en la URL {info['url']} - {e}")
        
#     except NoSuchElementException as e:
#         print(f"Error procesando el SKU {sku_key} en la URL {info['url']} - {e}")
    
#     data = {
#         "SKU": sku_key,
#         "Precio": precio_normal,
#         "Precio_oferta": precio_oferta,
#         "Stock":stock
#     }
#     results.append(data)
#     print(data)
#     time.sleep(0.5)

# driver.quit()

# print(results)


# Código para subir los resultados a Google Sheets puede ir aquí
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
							range='amigales!K2',#CAMBIAR
							valueInputOption='USER_ENTERED',
							body={'values':values}).execute()


#Valores que se pasan a Sheets
values = [[item['SKU'], item['Precio'], item['Precio_oferta']] for item in results]
result = sheet.values().update(spreadsheetId=SPREADSHEET_ID,
							range='amigales!A2:D',#CAMBIAR
							valueInputOption='USER_ENTERED',
							body={'values':values}).execute()
print(f"Datos insertados correctamente")

#Valores que se pasan a Sheets
values = [[item['Stock']] for item in results]
result = sheet.values().update(spreadsheetId=SPREADSHEET_ID,
							range='amigales!M2:N',#CAMBIAR
							valueInputOption='USER_ENTERED',
							body={'values':values}).execute()
print(f"Datos insertados correctamente")


df = pd.DataFrame(results)
print(df)
print(df.head)

competitor = "Amigales"  # Cambiar 


# Enviar datos a Google Sheets BBDD
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

# MANDAR DATOS A LA API ----------------------------------------------------------------------------------------------------
# Obtener la última fila con datos en la nueva hoja
result = sheet.values().get(spreadsheetId=NEW_SPREADSHEET_ID, range='apipets!A:A').execute() #Cambiar donde llega la info
values = result.get('values', [])
last_row = len(values) + 1  # Obtener el índice de la última fila vacía

# Convertir resultados a la lista de valores
values = [[row['SKU'], competitor, row['Precio'], row['Precio_oferta'], "Algo hay"] for _, row in df.iterrows()]

# Insertar los resultados en la nueva hoja después de la última fila
update_range = f'apipets!A{last_row}:E{last_row + len(values) - 1}' #Cambiar
result = sheet.values().update(
    spreadsheetId=NEW_SPREADSHEET_ID,
    range=update_range,
    valueInputOption='USER_ENTERED',
    body={'values': values}
).execute()