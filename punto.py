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
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
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


sku = {
    "petdotu160": "https://puntomascotas.cl/acana/35554-acana-heritage-free-run-poultry-21-kg-064992501136.html",
    "petdotu197": "https://puntomascotas.cl/acana/41102-acana-cat-indoor-entree-18kg-064992613044.html",
    "petdotu121": "https://puntomascotas.cl/acana/36905-acana-para-perros-pork-squash-1135-kg-064992714017.html",
    "petdotu176": "https://puntomascotas.cl/acana/37039-wild-atlantic-gato-18-kg-064992685119.html",
    "petdotu97": "https://puntomascotas.cl/farmacia-veterinaria/34959-adaptil-collar-large-3411112116676.html",
    "petdotu96": "https://puntomascotas.cl/farmacia-veterinaria/34960-adaptil-collar-large-3411112116652.html",
    "petdotu93": "https://puntomascotas.cl/farmacia-veterinaria/34961-adaptil-difusor-y-repuesto-de-48-ml-3411112169252.html",
    "petdotu205": "https://puntomascotas.cl/farmacia-veterinaria/34962-adaptil-difusor-y-repuesto-de-48-ml-3411112169344.html",
    "petdotu135": "https://puntomascotas.cl/farmacia-veterinaria/34910-advantage-para-gatos-hasta-4kg-4007221042914.html",
    "petdotu142": "https://puntomascotas.cl/farmacia-veterinaria/32878-advantage-para-gatos-hasta-4kg-7702123000907.html",
    "petdotu149": "https://puntomascotas.cl/antiparasitario-doble-funcion-interno-y-externo/37165-advocate-gato-y-huron-menor-de-4kg-4007221048329.html",
    "petdotu115": "https://puntomascotas.cl/antiparasitario-doble-funcion-interno-y-externo/37166-advocate-gato-4-a-8-kg-4007221048336.html",
    "petdotu199": "https://puntomascotas.cl/antiparasitario-doble-funcion-interno-y-externo/38425-advocate-perro-4-a-10-kg-4007221052654.html",
    "petdotu177": "https://puntomascotas.cl/antiparasitario-doble-funcion-interno-y-externo/38426-advocate-perro-10-a-25-kg-4007221052661.html",
    "petdotu196": "https://puntomascotas.cl/antiparasitario-doble-funcion-interno-y-externo/38427-advocate-perro-25-a-40-kg-4007221052647.html",
    "petdotu98": "https://puntomascotas.cl/farmacia-veterinaria/34200-shampoo-allercalm-7502010422627.html",
    "petdotu125": "https://puntomascotas.cl/arenas-y-banos-sanitarios/40292-arena-sanitaria-americalitter-ultra-odor-seal-7-kg-6956131000508.html",
    "petdotu84": "https://puntomascotas.cl/arenas-y-banos-sanitarios/40179-arena-america-litter-odor-seal-lavanda-15-kg-6956131001864.html",
    "petdotu72": "https://puntomascotas.cl/arenas-y-banos-sanitarios/36238-arena-cat-performance-9-kg-6956131001321.html",
    "petdotu1": "https://puntomascotas.cl/cicatrizantes/37170-apoquel-16-mg-x-20-comprimidos-5414736044217.html",
    "petdotu2": "https://puntomascotas.cl/cicatrizantes/37171-apoquel-36-mg-x-20-comprimidos-5414736044194.html",
    "petdotu3": "https://puntomascotas.cl/cicatrizantes/37172-apoquel-54-mg-x-20-comprimidos-5414736044200.html",
    "petdotu82": "https://puntomascotas.cl/inicio/35487-artritabs-complex-60-comp-714193699711.html",
    "petdotu132": "https://puntomascotas.cl/dogs/38880-belcando-finest-light-125kg-4002633558121.html",
    "petdotu170": "https://puntomascotas.cl/dogs/38880-belcando-finest-light-125kg-4002633558121.html",
    "petdotu9": "https://puntomascotas.cl/acana/41337-acana-bountiful-catch-gatos-45-kg-064992612108.html",
    "petdotu181": "https://puntomascotas.cl/farmacia-veterinaria/34142-bravecto-2-a-45-kg-8713184148940.html",
    "petdotu28": "https://puntomascotas.cl/farmacia-veterinaria/34139-bravecto-2-a-45-kg-8713184148957.html",
    "petdotu32": "https://puntomascotas.cl/farmacia-veterinaria/34136-bravecto-2-a-45-kg-8713184148988.html",
    "petdotu30": "https://puntomascotas.cl/farmacia-veterinaria/34140-bravecto-2-a-45-kg-8713184148971.html",
    "petdotu29": "https://puntomascotas.cl/farmacia-veterinaria/34141-bravecto-2-a-45-kg-8713184148964.html",
    "petdotu148": "https://puntomascotas.cl/farmacia-veterinaria/38964-bravecto-gato-62-a-125-kg-8713184194640.html",
    "petdotu53": "https://puntomascotas.cl/brit-care/35717-brit-care-adult-medium-cordero-y-arroz-8595602509928.html",
    "petdotu122": "https://puntomascotas.cl/brit-care/36997-brit-care-dog-adult-libre-de-grano-salmon-razas-grandes-3-kg-8595602558902.html",
    "petdotu52": "https://puntomascotas.cl/brit-care/35714-brit-care-adult-small-cordero-y-arroz-1-kg-8595602509881.html",
    "petdotu130": "https://puntomascotas.cl/cats/38989-brit-care-grain-free-haircare-7-kg-8595602540877.html",
    "petdotu127": "https://puntomascotas.cl/brit-care/38982-brit-care-grain-free-kitten-healthy-growth-2kg-8595602540679.html",
    "petdotu134": "https://puntomascotas.cl/gato-senior/38985-brit-care-grain-free-senior-weigth-control-7-kg-8595602540938.html",
    "petdotu155": "https://puntomascotas.cl/cats/38992-brit-care-sterilized-urinary-2-kg-8595602540730.html",
    "petdotu55": "https://puntomascotas.cl/cats/38991-brit-care-sterilized-urinary-7-kg-8595602540723.html",
    "petdotu110": "https://puntomascotas.cl/cats/38994-brit-care-grain-free-sterilized-weight-control-7-kg-8595602540785.html",
    "petdotu116": "https://puntomascotas.cl/brit-care/35374-brit-care-libre-de-granos-junior-large-breed-salmon-12kg-8595602558865.html",
    "petdotu57": "https://puntomascotas.cl/brit-care/35376-brit-care-libre-de-grano-adult-salmon-12kg-8595602510139.html",
    "petdotu133": "https://puntomascotas.cl/brit-care/35375-brit-care-libre-de-grano-adult-salmon-3kg-8595602558841.html",
    "petdotu58": "https://puntomascotas.cl/brit-care/35372-brit-care-puppy-salmon-papas-8595602510047.html",
    "petdotu136": "https://puntomascotas.cl/brit-care/35371-brit-care-libre-de-granos-puppy-salmon-y-papa-3kg-8595602558810.html",
    "petdotu59": "https://puntomascotas.cl/brit-care/35380-brit-care-libre-de-granos-senior-y-light-salmon-12-kg-8595602510269.html",
    "petdotu139": "https://puntomascotas.cl/brit-care/36947-brit-care-sensitive-venison-and-potato-12-kg-8595602559138.html",
    "petdotu106": "https://puntomascotas.cl/brit-care/35708-brit-care-puppy-large-cordero-y-arroz-8595602558957.html",
    "petdotu113": "https://puntomascotas.cl/brit-care/35711-brit-care-junior-large-cordero-y-arroz-12-kg-8595602559046.html",
    "petdotu123": "https://puntomascotas.cl/brit-care/35374-brit-care-libre-de-granos-junior-large-breed-salmon-12kg-8595602558865.html",
    "petdotu51": "https://puntomascotas.cl/brit-care/35723-brit-care-senior-cordero-y-arroz-1-kg-8595602510009.html",
    "petdotu56": "https://puntomascotas.cl/brit-care/35378-brit-care-weight-loss-conejo-y-arroz-12kg-8595602510313.html",
    "petdotu140": "https://puntomascotas.cl/brit-care/35377-brit-care-weight-loss-conejo-y-arroz-3kg-8595602559176.html",
    "petdotu204": "https://puntomascotas.cl/farmacia-veterinaria/41295-nexgard-combo-antiparasitario-interno-y-externo-para-gatos-08-25-kg-4064951005718.html",
    "petdotu168": "https://puntomascotas.cl/farmacia-veterinaria/41296-nexgard-combo-antiparasitario-interno-y-externo-para-gatos-25-75-kg-4064951007040.html",
    "petdotu81": "https://puntomascotas.cl/calmante-y-control-ansiedad/38995-calmer-spray-calamante-30ml-7804613901845.html",
    "petdotu37": "https://puntomascotas.cl/calmante-y-control-ansiedad/35483-collar-calming-gatos-beaphar-8711231110902.html",
    "petdotu178": "https://puntomascotas.cl/inicio/39089-canigest-combi-16ml-5391504342303.html",
    "petdotu154": "https://puntomascotas.cl/inicio/39984-canigest-combi-16ml-5391504342297.html",
    "petdotu159": "https://puntomascotas.cl/farmacia-veterinaria/30597-cerenia-24-mg-4-comprimidos-7804650310334.html",
    "petdotu167": "https://puntomascotas.cl/farmacia-veterinaria/30531-clindabone-clindamicina-165mg-7800006006364.html",
    "petdotu83": "https://puntomascotas.cl/farmacia-veterinaria/30465-condrovet-comprimidos-7800006005619.html",
    "petdotu95": "https://puntomascotas.cl/farmacia-veterinaria/30773-dermisolona-7800006005268.html",
    "petdotu91": "https://puntomascotas.cl/farmacia-veterinaria/34167-dermisolona-jarabe-04-30-ml-7800006009891.html",
    "petdotu193": "https://puntomascotas.cl/farmacia-veterinaria/34548-doguivit-senior-comprimidos--7800006003769.html",
    "petdotu188": "https://puntomascotas.cl/farmacia-veterinaria/34158-drontal-cats-5420036971221.html",
    "petdotu143": "https://puntomascotas.cl/farmacia-veterinaria/30753-drontal-plus-10kg-2-tabletas-7805750400895.html",
    "petdotu185": "https://puntomascotas.cl/farmacia-veterinaria/32420-drontal-plus-saborizado-35-kg-1-tableta-7891106003704.html",
    "petdotu14": "https://puntomascotas.cl/acana/41197-acana-para-perros-duck-pears-2-kg-064992713973.html",
    "petdotu190": "https://puntomascotas.cl/perros-cachorro/33125--purina-excellent-cachorro-razas-medianas-y-grandes-15-kg-8445291021945.html",
    "petdotu191": "https://puntomascotas.cl/dogs/33123-purina-excellent-adult-razas-medianas-y-grandes-15kg-7613035951525.html",
    "petdotu105": "https://puntomascotas.cl/dogs/38374-purina-excellent-adulto-salmon-skin-care-15-kg-7613287016904.html",
    "petdotu42": "https://puntomascotas.cl/farmacia-veterinaria/34963-feliway-difusor-repuesto-48-ml-3411112169498.html",
    "petdotu43": "https://puntomascotas.cl/farmacia-veterinaria/35602-feliway-friends-kit-inicial-3411112251186.html",
    "petdotu41": "https://puntomascotas.cl/farmacia-veterinaria/35604-feliway-difusor-repuesto-48-ml-3411112251230.html",
    "petdotu39": "https://puntomascotas.cl/farmacia-veterinaria/34964-feliway-difusor-repuesto-48-ml-3411112169603.html",
    "petdotu40": "https://puntomascotas.cl/farmacia-veterinaria/30767-feliway-spray-3411112133789.html",
    "petdotu10": "https://puntomascotas.cl/cats/41261-acana-cat-first-feast-cat-18kg-064992610043.html",
    "petdotu71": "https://puntomascotas.cl/farmacia-veterinaria/35477-mira-canis-3547735477.html",
    "petdotu12": "https://puntomascotas.cl/acana/35555-acana-heritage-free-run-poultry-21-kg-64992501259.html",
    "petdotu11": "https://puntomascotas.cl/acana/35557-acana-heritage-freshwater-fish-21kg-64992502256.html",
    "petdotu129": "https://puntomascotas.cl/farmacia-veterinaria/41044-galliprant-100mg-5420036980261.html",
    "petdotu186": "https://puntomascotas.cl/farmacia-veterinaria/32884-glicopan-pet-125ml-7898053580883.html",
    "petdotu182": "https://puntomascotas.cl/farmacia-veterinaria/35364-hematon-b12-elixir-7730407023830.html",
    "petdotu208": "https://puntomascotas.cl/suplementos/38296-hemolitan-60-ml-7898053580623.html",
    "petdotu158": "https://puntomascotas.cl/suplementos/39842-hemolivet-30-comprimidos-961882701716.html",
    "petdotu183": "https://puntomascotas.cl/hills/37446-hills-adult-7-small-bites-68-kg-052742057569.html",
    "petdotu87": "https://puntomascotas.cl/farmacia-veterinaria/30460-itraskin-60ml-suspension-oral-7800006007132.html",
    "petdotu65": "https://puntomascotas.cl/farmacia-veterinaria/30771-laveta-carnitina-perros-8711231114283.html",
    "petdotu66": "https://puntomascotas.cl/farmacia-veterinaria/30770-laveta-taurina-gatos-8711231114306.html",
    "petdotu164": "https://puntomascotas.cl/cats/38919-leonardo-adult-duck-75kg-4002633758323.html",
    "petdotu152": "https://puntomascotas.cl/cats/38921-leonardo-adult-light-75kg-4002633758828.html",
    "petdotu151": "https://puntomascotas.cl/cats/38922-leonardo-adult-senior-2kg-4002633758910.html",
    "petdotu161": "https://puntomascotas.cl/cats/38923-leonardo-adult-senior-75kg-4002633758927.html",
    "petdotu162": "https://puntomascotas.cl/analgesicos-y-antiinflamatorios/37480-meloxivet-7800006010330.html",
    "petdotu60": "https://puntomascotas.cl/farmacia-veterinaria/33556-mixantip-plus-crema-50gr-7800006008221.html",
    "petdotu75": "https://puntomascotas.cl/farmacia-veterinaria/30437-naxpet-jarabe-7800006006814.html",
    "petdotu198": "https://puntomascotas.cl/farmacia-veterinaria/30438-naxpet-10mg-comprimidos-7800006002410.html",
    "petdotu145": "https://puntomascotas.cl/farmacia-veterinaria/39055-pet-otic-solucion-100ml-4007221052333.html",
    "petdotu70": "https://puntomascotas.cl/nexgard-spectra/37494-nexgard-spectra-301-a-60-kg-7809599501935.html",
    "petdotu69": "https://puntomascotas.cl/nexgard-spectra/37701-nexgard-spectra-301-a-60-kg-7809599501980.html",
    "petdotu189": "https://puntomascotas.cl/nexgard-spectra/37493-nexgard-spectra-301-a-60-kg-7809599501911.html",
    "petdotu172": "https://puntomascotas.cl/nexgard-spectra/37703-nexgard-spectra-301-a-60-kg-7809599501966.html",
    "petdotu147": "https://puntomascotas.cl/nexgard-spectra/37492-nexgard-spectra-301-a-60-kg-7809599501942.html",
    "petdotu138": "https://puntomascotas.cl/nexgard-spectra/37704-nexgard-spectra-301-a-60-kg-7809599501997.html",
    "petdotu68": "https://puntomascotas.cl/nexgard-spectra/37496-nexgard-spectra-301-a-60-kg-7809599501928.html",
    "petdotu67": "https://puntomascotas.cl/nexgard-spectra/37705-nexgard-spectra-301-a-60-kg-7809599501973.html",
    "petdotu174": "https://puntomascotas.cl/suplementos/36573-nutribound-perro-150-ml-7502010426861.html",
    "petdotu165": "https://puntomascotas.cl/nutrience/30728-nutrience-gato-adulto-original-272-kg-015561524629.html",
    "petdotu175": "https://puntomascotas.cl/nutrience/36528-nutrience-gato-adulto-original-272-kg-015561524728.html",
    "petdotu157": "https://puntomascotas.cl/farmacia-veterinaria/30486-oftavet-7800006008238.html",
    "petdotu94": "https://puntomascotas.cl/calmante-y-control-ansiedad/37444-ohm-modulador-de-ansiedad-7798042366804.html",
    "petdotu114": "https://puntomascotas.cl/orijen/41040-orijen-perro-small-breed-45-kg-064992580100.html",
    "petdotu150": "https://puntomascotas.cl/farmacia-veterinaria/40660-suplemento-osteodrag-ha-30-comprimidos-7800006011269.html",
    "petdotu77": "https://puntomascotas.cl/farmacia-veterinaria/30749-oxtrin-comprimidos-7797600000600.html",
    "petdotu206": "https://puntomascotas.cl/farmacia-veterinaria/30769-papainpet-7800006010170.html",
    "petdotu195": "https://puntomascotas.cl/farmacia-veterinaria/30418-paz-pet-suspension-oral-60ml-7800006005589.html",
    "petdotu202": "https://puntomascotas.cl/farmacia-veterinaria/30463-petever-forte-150ml-7800006001291.html",
    "petdotu100": "https://puntomascotas.cl/farmacia-veterinaria/35518-phisio-anti-olor-limpiador-auricular-100-ml-7502010422641.html",
    "petdotu107": "https://puntomascotas.cl/necesidades-especiales/39932-pimocard-pimobedan-5-mg-7798042367740.html",
    "petdotu192": "https://puntomascotas.cl/cats/35589-pro-plan-cat-sterilized-75kg-7613039947661.html",
    "petdotu187": "https://puntomascotas.cl/cats/30022-pro-plan-cat-urinary-care-protection-3-kg-7613039947111.html",
    "petdotu173": "https://puntomascotas.cl/cats/33511-pro-plan-cat-urinary-care-protection-15-kg--7613039947739.html",
    "petdotu184": "https://puntomascotas.cl/dogs/30024-pro-plan-aduto-small-breed-3-kg--7613287029195.html",
    "petdotu180": "https://puntomascotas.cl/dogs/140-pro-plan-puppy-complete-protection-con-optistartplus-15-kg--7613287028549.html",
    "petdotu179": "https://puntomascotas.cl/farmacia-veterinaria/30462-regepipel-plus-shampoo-150ml-7800006005169.html",
    "petdotu5": "https://puntomascotas.cl/farmacia-veterinaria/38467-revolution-plus-25-a-5-kg-7804650310136.html",
    "petdotu4": "https://puntomascotas.cl/farmacia-veterinaria/38466-revolution-6-gatos-hasta-75-kg-7804650310136.html",
    "petdotu119": "https://puntomascotas.cl/farmacia-veterinaria/41287-revolution-plus-5-kg-a-10-kg-5414736045276.html",
    "petdotu27": "https://puntomascotas.cl/farmacia-veterinaria/32656-rimadyl-100-mg-14-comprimidos-7804650310891.html",
    "petdotu201": "https://puntomascotas.cl/farmacia-veterinaria/35748-senilpet-7800006009983.html",
    "petdotu207": "https://puntomascotas.cl/farmacia-veterinaria/37044-slimavet-90-comprimidos-7800006010217.html",
    "petdotu73": "https://puntomascotas.cl/farmacia-veterinaria/37025-silimavet-silimarina-30-comprimidos-0761887135476.html",
    "petdotu74": "https://puntomascotas.cl/farmacia-veterinaria/35652-slimavet-90-comprimidos-761778204082.html",
    "petdotu203": "https://puntomascotas.cl/simparica/38338-simparica-13-a-25-kg-3-comprimidos-7804650311133.html",
    "petdotu169": "https://puntomascotas.cl/simparica/38337-simparica-13-a-25-kg-3-comprimidos-7804650311065.html",
    "petdotu25": "https://puntomascotas.cl/simparica/38340-simparica-13-a-25-kg-3-comprimidos.html",
    "petdotu24": "https://puntomascotas.cl/simparica/38339-simparica-13-a-25-kg-3-comprimidos.html",
    "petdotu22": "https://puntomascotas.cl/simparica/38342-simparica-13-a-25-kg-3-comprimidos.html",
    "petdotu23": "https://puntomascotas.cl/simparica/38341-simparica-13-a-25-kg-3-comprimidos.html",
    "petdotu21": "https://puntomascotas.cl/simparica/38344-simparica-13-a-25-kg-3-comprimidos.html",
    "petdotu20": "https://puntomascotas.cl/simparica/38343-simparica-13-a-25-kg-3-comprimidos.html",
    "petdotu163": "https://puntomascotas.cl/simparica/38343-simparica-13-a-25-kg-3-comprimidos-7804650311096.html",
    "petdotu89": "https://puntomascotas.cl/gastro-enterico/36346-sucravet-100ml-7804605270874.html",
    "petdotu210": "https://puntomascotas.cl/farmacia-veterinaria/30499-omega-superpet-gato-125ml-7800006004926.html",
    "petdotu79": "https://puntomascotas.cl/farmacia-veterinaria/30600-synulox-250--7804650310952.html",
    "petdotu108": "https://puntomascotas.cl/inicio/39146-engystol-gotas-30ml-veterinario-7800093000832.html",
    "petdotu112": "https://puntomascotas.cl/inicio/39731-traumeel-veterinario-250-tabletas-7800093000955.html",
    "petdotu92": "https://puntomascotas.cl/farmacia-veterinaria/30442-ursovet-60ml-7800006007033.html",
    "petdotu200": "https://puntomascotas.cl/farmacia-veterinaria/39830-vetgastril-50ml-8414042005435.html",
    "petdotu166": "https://puntomascotas.cl/hpm/41196-hpm-virbac-gato-allergy-hypoallergy-3kg-3561963601996.html",
    "petdotu146": "https://puntomascotas.cl/hpm/34763-alimento-hpm-cat-adult-neutered-15kg-3561963600616.html",
    "petdotu128": "https://puntomascotas.cl/hpm/35951-hpm-perro-weight-loss-diabetes-12kg-3561963639937.html",
    "petdotu33": "https://puntomascotas.cl/farmacia-veterinaria/38415-bravecto-gato-12-a-28-kg-8713184197689.html",
    "petdotu31": "https://puntomascotas.cl/farmacia-veterinaria/38964-bravecto-gato-62-a-125-kg-8713184197696.html",
    "petdotu54": "https://puntomascotas.cl/brit-care/35708-brit-care-puppy-large-cordero-y-arroz-8595602509799.html",
    "petdotu34": "https://puntomascotas.cl/farmacia-veterinaria/34773-pipeta-calmante-para-perros-3-unidades-8711231105489.html",
    "petdotu35": "https://puntomascotas.cl/calmante-y-control-ansiedad/35481-spray-calming-felino-beaphar-8711231110896.html",
    "petdotu38": "https://puntomascotas.cl/calmante-y-control-ansiedad/35480--tabletas-calamantes-gatos-y-perros-8711231171101.html",
    "petdotu36": "https://puntomascotas.cl/golosinas-para-gatos/37002-golosinas-calmantes-felinas-beaphar-8711231110889.html",
    "petdotu88": "https://puntomascotas.cl/dogs/33177-hills-adulto-small-toy-204kg-52742909608.html",
    "petdotu85": "https://puntomascotas.cl/dogs/32876-hills-canine-prescription-diet-metabolic-27-kg-52742195209.html",
    "petdotu45": "https://puntomascotas.cl/dogs/30118-royal-canin-vet-diet-canino-hypoallergenic-canine-2kg-7896181213543.html",
    "petdotu47": "https://puntomascotas.cl/perros-adulto/35340-royal-canin-mini-adulto-3kg-7896181297857.html",
    "petdotu46": "https://puntomascotas.cl/dogs/30068-royal-canin-mini-puppy-3kg-7790187339620.html",
    "petdotu99": "https://puntomascotas.cl/perros-necesidades-especificas/32018-hills-canine-prescription-diet-r-d-798kg-52742862507.html",
    "petdotu61": "https://puntomascotas.cl/farmacia-veterinaria/30441-mixantip-plus-crema-15gr-7800006003455.html",
    "petdotu44": "https://puntomascotas.cl/cats/35445-royal-canin-growth-mother-babycat-15kg-7790187340305.html",
    "petdotu80": "https://puntomascotas.cl/arenas-y-banos-sanitarios/36402-arena-odour-buster-original-14-kg-895792000273.html",
    "petdotu62": "https://puntomascotas.cl/oven-baked/37104-oven-baked-adult-pollo-todas-las-razas-1134kg-669066001651.html",
    "petdotu63": "https://puntomascotas.cl/oven-baked/37115-oven-baked-perro-adulto-todas-las-razas-pescado-1134kg-669066001781.html",
    "petdotu90": "https://puntomascotas.cl/farmacia-veterinaria/30444-pacifor-gotas-10ml-7800006000294.html",
    "petdotu76": "https://puntomascotas.cl/farmacia-veterinaria/34417-pederol-250ml-8436529621938.html",
    "petdotu26": "https://puntomascotas.cl/farmacia-veterinaria/30520-rimadyl-100-mg-60-comprimidos-7804650310884.html",
    "petdotu86": "https://puntomascotas.cl/wanpy/37019-wanpy-lamb-100-grs-6927749840046.html",
    "petdotu600": "https://puntomascotas.cl/cats/38927-leonardo-adult-gf-maxi-75kg-4002633758521.html"
}
sku2 = {"petdotu1": "https://puntomascotas.cl/cicatrizantes/37170-apoquel-16-mg-x-20-comprimidos-5414736044217.html"}


results = []

for sku_key, url in sku.items():
    driver.get(url)
    precio_oferta = "No disponible"    
    precio_normal = "No disponible"
    stock= "Con Stock"
    try:
        # Intenta obtener el precio de oferta
        precio_oferta_element = driver.find_element("xpath", '/html/body/main/section/div/div/div/div/div/section/div[1]/div[1]/div[2]/section/div[1]/div/div[5]/div/form/div[2]/div[1]/span[1]/span[1]') #Cambiar
        precio_oferta = precio_oferta_element.text  # Guarda el precio de oferta
        stock_element= driver.find_element(By.XPATH,"/html/body/main/section/div/div/div/div/div/section/div[1]/div[1]/div[2]/section/div[1]/div/div[2]")
        stock=stock_element.text
    except NoSuchElementException:
        pass  # Si no se encuentra el precio de oferta, se continuará con el siguiente bloque de código

    try:
        # Intenta obtener el precio normal
        precio_oferta_element = driver.find_element("xpath", '/html/body/main/section/div/div/div/div/div/section/div[1]/div[1]/div[2]/section/div[1]/div/div[5]/div/form/div[2]/div[1]/span[1]/span[1]') #Cambiar
        precio_oferta = precio_oferta_element.text  # Guarda el precio de oferta
        stock_element= driver.find_element(By.XPATH,"/html/body/main/section/div/div/div/div/div/section/div[1]/div[1]/div[2]/section/div[1]/div/div[2]")
        stock=stock_element.text
    except NoSuchElementException:
        pass  # Si no se encuentra el precio normal, se continuará con el siguiente bloque de código

    if precio_oferta == "No disponible" and precio_normal == "No disponible":
        try:
            precio_oferta_element = driver.find_element("xpath", '/html/body/main/section/div/div/div/div/div/section/div[1]/div[1]/div[2]/section/div[1]/div/div[5]/div/form/div[2]/div[1]/span[1]/span[1]') #Cambiar
            precio_oferta = precio_oferta_element.text  # Guarda el precio de oferta
            stock_element= driver.find_element(By.XPATH,"/html/body/main/section/div/div/div/div/div/section/div[1]/div[1]/div[2]/section/div[1]/div/div[2]")
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
print(df)
print(df.head)

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
							range='puntomascotas!K2',#CAMBIAR
							valueInputOption='USER_ENTERED',
							body={'values':values}).execute()


#Valores que se pasan a Sheets
values = [[item['SKU'], item['Precio'],item['Precio_oferta']] for item in results]
result = sheet.values().update(spreadsheetId=SPREADSHEET_ID,
							range='puntomascotas!A2:C',#CAMBIAR
							valueInputOption='USER_ENTERED',
							body={'values':values}).execute()
print(f"Datos insertados correctamente")        

#Valores que se pasan a Sheets
values = [[item['Stock']] for item in results]
result = sheet.values().update(spreadsheetId=SPREADSHEET_ID,
							range='puntomascotas!M2:N',#CAMBIAR
							valueInputOption='USER_ENTERED',
							body={'values':values}).execute()
print(f"Datos insertados correctamente")        


competitor = "Punto Mascotas"  # Cambiar 
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
values = [[row['SKU'], competitor,row['Precio_oferta'], row['Precio'], now_str] for _, row in df.iterrows()]

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
values = [[row['SKU'], competitor, row['Precio'], row['Precio_oferta'], row["Stock"]] for _, row in df.iterrows()]

# Insertar los resultados en la nueva hoja después de la última fila
update_range = f'apipets!A{last_row}:E{last_row + len(values) - 1}' #Cambiar
result = sheet.values().update(
    spreadsheetId=NEW_SPREADSHEET_ID,
    range=update_range,
    valueInputOption='USER_ENTERED',
    body={'values': values}
).execute()
