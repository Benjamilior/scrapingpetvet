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

SPREADSHEET_ID_API = '1S8jzZl4UehXDJxWuHfTSLftBnq3CKUXhgRGrJIShyhE'  
competitor = "Petvet"  
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
    "44577385971873": "https://petvet.cl/products/nexgard-spectra-3-6-7-5kg-3-comprimidos.js",
    "42708471808161": "https://petvet.cl/products/nexgard-spectra-3-6-7-5kg-1-comprimido.js",
    "42738555453601": "https://petvet.cl/products/bravecto-perro-40-56kg-1400mg.js",
    "41857347190945": "https://petvet.cl/products/canine-adult-7-small-bites.js",
    "41633900232865": "https://petvet.cl/products/simparica-2-5-5kg-10mg-1-comprimido.js",
    "43577664241825": "https://petvet.cl/products/simparica-2-5-5kg-10mg-3-comprimidos.js",
    "43584104792225": "https://petvet.cl/products/simparica-trio-20-40-kg-3-comprimidos.js",
    "44329056895137": "https://petvet.cl/products/josera-miniwell-10kg.js",
    "43094808625313": "https://petvet.cl/products/leonardo-adulto-senior.js",
    "43094794338465": "https://petvet.cl/products/leonardo-adulto-pato.js",
    "43191176495265": "https://petvet.cl/products/belcando-finest-light.js",
    "43090610749601": "https://petvet.cl/products/drontal-plus-perro-hasta-35kg-1-comprimido.js",
    "42361890668705": "https://petvet.cl/products/drontal-gato-2-comprimidos.js",
    "42738689900705": "https://petvet.cl/products/advocate-perro-10-25kg-2-5ml.js",
    "43724309790881": "https://petvet.cl/products/advocate-perro-25-40kg-4-0ml.js",
    "42738689704097": "https://petvet.cl/products/advocate-perro-4-10kg-1-0ml.js",
    "42463428378785": "https://petvet.cl/products/canigest-combi-16ml.js",
    "41896974680225": "https://petvet.cl/products/meloxivet.js",
    "43893233680545": "https://petvet.cl/products/nutrience-original-gato-adulto.js",
    "43785612230817": "https://petvet.cl/products/virbac-hpm-allergy-cat-3-kg.js",
    "42392893620385": "https://petvet.cl/products/clindabone-165-mg-20-comprimidos.js",
    "43899282456737": "https://petvet.cl/products/bravery-perro-adulto-pollo-razas-medianas-y-grandes.js",
    "43596331090081": "https://petvet.cl/products/pro-plan-gato-urinario.js",
    "42463321850017": "https://petvet.cl/products/nutribound-perro-150-ml.js",
    "43893240627361": "https://petvet.cl/products/nutrience-original-gato-adulto-indoor.js",
    "40152480219297": "https://petvet.cl/products/regepipel-plus.js",
    "43854457536673": "https://petvet.cl/products/pro-plan-puppy-razas-medianas-15kg.js",
    "43707310964897": "https://petvet.cl/products/hematon-b12-elixir-perros-y-gatos-100ml.js",
    "42361910132897": "https://petvet.cl/products/glicopan-perros-y-gatos.js",
    "43596331057313": "https://petvet.cl/products/pro-plan-gato-urinario.js",
    "44181000421537": "https://petvet.cl/products/purina-excellent-cachorro-15kg.js",
    "43156268744865": "https://petvet.cl/products/purina-excellent-perro-adulto-pollo-arroz.js",
    "43596219056289": "https://petvet.cl/products/pro-plan-gato-adulto-esterilizado.js",
    "42310076858529": "https://petvet.cl/products/doguivit-senior-30-comprimidos.js",
    "40152479039649": "https://petvet.cl/products/paz-pet-suspension-oral.js",
    "40152448958625": "https://petvet.cl/products/naxpet-10-mg-10-comprimidos.js",
    "44279760748705": "https://petvet.cl/products/vetgastril-50-ml.js",
    "42463409701025": "https://petvet.cl/products/senilpet-cerebral-5-x-60-comp.js",
    "40152459051169": "https://petvet.cl/products/petever-forte-shampoo-150ml.js",
    "42271737249953": "https://petvet.cl/products/adaptil-repuesto-48-ml.js",
    "40152478777505": "https://petvet.cl/products/papainpet.js",
    "40152485757089": "https://petvet.cl/products/silimadrag-suspension.js",
    "42361911541921": "https://petvet.cl/products/hemolitan-perros-y-gatos.js",
    "40152488312993": "https://petvet.cl/products/superpet-omega-gato.js",
    "43596385386657": "https://petvet.cl/products/pro-plan-sensitive-skin-razas-pequenas-3kg.js",
    "41857592361121": "https://petvet.cl/products/apoquel-16mg-20-comp.js",
    "41857592754337": "https://petvet.cl/products/apoquel-3-6-mg-20-comp.js",
    "41857597014177": "https://petvet.cl/products/apoquel-5-4-mg-20-comp.js",
    "42033421123745": "https://petvet.cl/products/acana-free-run-poultry-perro.js",
    "43111864369313": "https://petvet.cl/products/acana-puppy-junior-perro.js",
    "41689298796705": "https://petvet.cl/products/prairie-poultry-perro.js",
    "41857724350625": "https://petvet.cl/products/bountiful-catch-gato.js",
    "41689377341601": "https://petvet.cl/products/duck-pear-perro.js",
    "43111863189665": "https://petvet.cl/products/acana-freshwater-fish-perro.js",
    "42423305797793": "https://petvet.cl/products/acana-light-fit-2-kg-1.js",
    "42033421156513": "https://petvet.cl/products/wild-coast-perro.js",
    "42423280697505": "https://petvet.cl/products/first-feast-gato.js",
    "40152493490337": "https://petvet.cl/products/mother-and-babycat.js",
    "40152491622561": "https://petvet.cl/products/canino-hypoallergenic.js",
    "42708472463521": "https://petvet.cl/products/nexgard-spectra-7-6-15kg-1-comprimido.js",
    "44577414611105": "https://petvet.cl/products/nexgard-spectra-7-6-15kg-3-comprimidos.js",
    "42708470136993": "https://petvet.cl/products/nexgard-spectra-15-30kg-1-comprimido.js",
    "44577353695393": "https://petvet.cl/products/nexgard-spectra-15-30kg-3-comprimidos.js",
    "44577401274529": "https://petvet.cl/products/nexgard-spectra-30-60kg-3-comprimidos.js",
    "42730103144609": "https://petvet.cl/products/nexgard-spectra-30-60kg-1-comprimido.js",
    "43771918090401": "https://petvet.cl/products/bravecto-plus-gato-1-2-2-8kg-112-5mg.js",
    "43771996864673": "https://petvet.cl/products/bravecto-plus-gato-2-8-6-25kg-250mg.js",
    "42738538872993": "https://petvet.cl/products/bravecto-perro-2-4-5kg-112-5mg.js",
    "42738539692193": "https://petvet.cl/products/bravecto-perro-4-5-10kg-250mg.js",
    "42738543263905": "https://petvet.cl/products/bravecto-perro-10-20kg-500mg.js",
    "42738545557665": "https://petvet.cl/products/bravecto-perro-20-40kg-1-000mg.js",
    "42324007878817": "https://petvet.cl/products/americalitter-ultra-odor-seal.js",
    "44388326178977": "https://petvet.cl/products/america-litter-ultra-odor-seal-lavanda-15kg.js",
    "42271448629409": "https://petvet.cl/products/brit-care-gf-puppy-salmon.js",
    "42271606767777": "https://petvet.cl/products/brit-care-adult-small-breed-l-r.js",
    "42271434178721": "https://petvet.cl/products/brit-care-adult-medium-breed-lamb-hypoallergenic.js",
    "42271541362849": "https://petvet.cl/products/brit-care-puppy-l-r.js",
    "42271560237217": "https://petvet.cl/products/brit-care-weight-loss-rabbit.js",
    "42271478841505": "https://petvet.cl/products/brit-care-gf-senior-light-salmon.js",
    "42271548801185": "https://petvet.cl/products/brit-care-senior-lamb.js",
    "44487570981025":"https://petvet.cl/products/josera-light-vital-12-5kg.js",
    "43411814285473": "https://petvet.cl/products/brit-care-adult-large-breed-salmon.js",
    "42423170367649": "https://petvet.cl/products/brit-care-cat-gf-sterilized-urinary.js",
    "43019722981537": "https://petvet.cl/products/brit-care-cat-gf-sterilized-weight-control.js",
    "44042326245537": "https://petvet.cl/products/brit-care-junior-large-breed-salmon.js",
    "43091932020897": "https://petvet.cl/products/brit-care-junior-large-breed-lamb.js",
    "43019722096801": "https://petvet.cl/products/brit-care-cat-gf-kitten-healthy-growth-development.js",
    "43019722326177": "https://petvet.cl/products/brit-care-cat-gf-haircare-healthy-shiny-coat.js",
    "42271444631713": "https://petvet.cl/products/brit-care-adult-salmon.js",
    "42271444598945":"https://petvet.cl/products/brit-care-adult-salmon.js",
    "43083183095969": "https://petvet.cl/products/brit-care-cat-senior-weight-control.js",
    "42271448662177": "https://petvet.cl/products/brit-care-gf-puppy-salmon.js",
    "43487989072033": "https://petvet.cl/products/brit-care-adult-sensitive-venado.js",
    "42271560269985": "https://petvet.cl/products/brit-care-weight-loss-rabbit.js",
    "42423170334881": "https://petvet.cl/products/brit-care-cat-gf-sterilized-urinary.js",
    "42271606800545": "https://petvet.cl/products/brit-care-adult-small-breed-l-r.js",
    "40087240835233": "https://petvet.cl/products/rimadyl.js",
    "40159957549217": "https://petvet.cl/products/rimadyl.js",
    "40087277830305": "https://petvet.cl/products/revolution-plus-gato-1-25-2-5kg-0-25ml.js",
    "42738646745249": "https://petvet.cl/products/revolution-plus-gato-2-5-5kg-0-5ml.js",
    "43830181560481": "https://petvet.cl/products/revolution-plus-gato-5-10kg-1ml.js",
    "42785343013025": "https://petvet.cl/products/bil-jac-selected-adult-dog-food.js",
    "41981042000033": "https://petvet.cl/products/hills-prescription-diet-canine-c-d-7-98-kg.js",
    "41633978810529": "https://petvet.cl/products/simparica-10-20kg-40mg-1-comprimido.js",
    "43577667354785": "https://petvet.cl/products/simparica-10-20kg-40mg-3-comprimidos.js",
    "43577665388705": "https://petvet.cl/products/simparica-5-10kg-20mg-3-comprimidos.js",
    "41633916944545": "https://petvet.cl/products/simparica-5-10kg-20mg-1-comprimido.js",
    "43577669910689": "https://petvet.cl/products/simparica-20-40kg-80mg-3-comprimidos.js",
    "43584104792225":"https://petvet.cl/products/simparica-trio-20-40kg-3-comprimidos.js",
    "40152468979873": "https://petvet.cl/products/hills-canine-adulto-de-razas-pequenas-2-04-kg.js",
    "41634051162273":"https://petvet.cl/products/simparica-20-40kg-80mg-1-comprimido.js",
    "40087248470177": "https://petvet.cl/products/mixantip-plus.js",
    "40087248437409": "https://petvet.cl/products/mixantip-plus.js",
    "42785360314529": "https://petvet.cl/products/bil-jac-puppy-select-formula.js",
    "41857368359073": "https://petvet.cl/products/canine-adult-metabolic-7-98-kg.js",
    "42392861278369": "https://petvet.cl/products/adaptil-collar-perro.js",
    "42392861245601": "https://petvet.cl/products/adaptil-collar-perro.js",
    "43037801152673": "https://petvet.cl/products/oven-baked-adulto-pescado-11-34-kg.js",
    "43037801087137": "https://petvet.cl/products/oven-baked-adulto-pollo-11-34-kg.js",
    "43037801218209": "https://petvet.cl/products/oven-baked-senior-11-34-kg.js",
    "40087214227617": "https://petvet.cl/products/arena-traper.js",
    "42361913311393": "https://petvet.cl/products/silimarina-vitanimal-120mg.js",
    "42361913344161": "https://petvet.cl/products/silimarina-vitanimal-120mg.js",
    "40159961317537": "https://petvet.cl/products/alimento-fit-formula-cachorro-10kg.js",
    "40159961383073": "https://petvet.cl/products/alimento-fit-formula-gato-10kg.js",
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
    "43888860692641": "https://petvet.cl/products/josera-light-vital-12-5kg.js",
    "43888923771041": "https://petvet.cl/products/josera-gato-naturelle-2kg.js",
    "44042727424161": "https://petvet.cl/products/josera-balance-12-5kg.js",
    "41689363579041": "https://petvet.cl/products/acana-free-run-poultry-perro.js",
    "44537640386721": "https://petvet.cl/products/acana-pork-squash-perro.js",
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
    "40087273341089": "https://petvet.cl/products/advantage-gato-hasta-4kg-0-4ml.js",
    "42738744393889": "https://petvet.cl/products/advantage-gato-4-8kg-0-8ml.js",
    "40159957221537": "https://petvet.cl/products/drontal-plus-perro-hasta-10kg-2-comprimidos.js",
    "44054704259233": "https://petvet.cl/products/neptra-solucion-otica.js",
    "44279072227489": "https://petvet.cl/products/osteodrag-ha-30-comprimidos.js",
    "41646114996385": "https://petvet.cl/products/advocate-gato-hasta-4kg-0-4ml.js",
    "42738659557537": "https://petvet.cl/products/advocate-gato-4-8kg-0-8ml.js",
    "41857461190817": "https://petvet.cl/products/oftavet-5-ml.js",
    "43830826074273": "https://petvet.cl/products/hemolivet-30-comprimidos.js",
    "42366871928993": "https://petvet.cl/products/cerenia-24-mg-x-4-comp.js",
    "43591189987489": "https://petvet.cl/products/canigest-combi-32ml.js",
    "44309699166369":"https://petvet.cl/products/fit-formula-light-20-kg.js",
    "44430172684449":"https://petvet.cl/products/nexgard-combo-gato-0-8-2-5kg.js",
    "44427832033441":"https://petvet.cl/products/nexgard-combo-gato-2-5-7-5kg.js",
    "44453910380705":"https://petvet.cl/products/leonardo-adulto-gf-maxi.js"
    
}
urls3={
    "petdotu197": {
    "43683672457377": "https://petvet.cl/products/acana-indoor-entree-gato.js"
},

"petdotu194": {
    "41689309708449": "https://petvet.cl/products/wild-coast-perro.js"
},

"petdotu176": {
    "41689274712225": "https://petvet.cl/products/wild-atlantic-gato.js"
},

"petdotu172": {
    "44577385971873": "https://petvet.cl/products/nexgard-spectra-3-6-7-5kg-3-comprimidos.js"
},

"petdotu189": {
    "42708471808161": "https://petvet.cl/products/nexgard-spectra-3-6-7-5kg-1-comprimido.js"
},

"petdotu181": {
    "42738555453601": "https://petvet.cl/products/bravecto-perro-40-56kg-1400mg.js"
},

"petdotu183": {
    "41857347190945": "https://petvet.cl/products/canine-adult-7-small-bites.js"
},

"petdotu203": {
    "41633900232865": "https://petvet.cl/products/simparica-2-5-5kg-10mg-1-comprimido.js"
},

"petdotu169": {
    "43577664241825": "https://petvet.cl/products/simparica-2-5-5kg-10mg-3-comprimidos.js"
},

"petdotu163": {
    "43584104792225": "https://petvet.cl/products/simparica-trio-20-40kg-3-comprimidos.js"
},

"petdotu209": {
    "44329056895137": "https://petvet.cl/products/josera-miniwell-10kg.js"
},

"petdotu161": {
    "43094808625313": "https://petvet.cl/products/leonardo-adulto-senior.js"
},

"petdotu164": {
    "43094794338465": "https://petvet.cl/products/leonardo-adulto-pato.js"
},

"petdotu170": {
    "43191176495265": "https://petvet.cl/products/belcando-finest-light.js"
},

"petdotu185": {
    "43090610749601": "https://petvet.cl/products/drontal-plus-perro-hasta-35kg-1-comprimido.js"
},

"petdotu188": {
    "42361890668705": "https://petvet.cl/products/drontal-gato-2-comprimidos.js"
},

"petdotu177": {
    "42738689900705": "https://petvet.cl/products/advocate-perro-10-25kg-2-5ml.js"
},

"petdotu196": {
    "43724309790881": "https://petvet.cl/products/advocate-perro-25-40kg-4-0ml.js"
},

"petdotu199": {
    "42738689704097": "https://petvet.cl/products/advocate-perro-4-10kg-1-0ml.js"
},

"petdotu178": {
    "42463428378785": "https://petvet.cl/products/canigest-combi-16ml.js"
},

"petdotu162": {
    "41896974680225": "https://petvet.cl/products/meloxivet.js"
},

"petdotu165": {
    "43893233680545": "https://petvet.cl/products/nutrience-original-gato-adulto.js"
},

"petdotu166": {
    "43785612230817": "https://petvet.cl/products/virbac-hpm-allergy-cat-3-kg.js"
},

"petdotu167": {
    "42392893620385": "https://petvet.cl/products/clindabone-165-mg-20-comprimidos.js"
},

"petdotu171": {
    "43899282456737": "https://petvet.cl/products/bravery-perro-adulto-pollo-razas-medianas-y-grandes.js"
},

"petdotu173": {
    "43596331090081": "https://petvet.cl/products/pro-plan-gato-urinario.js"
},

"petdotu174": {
    "42463321850017": "https://petvet.cl/products/nutribound-perro-150-ml.js"
},

"petdotu175": {
    "43893240627361": "https://petvet.cl/products/nutrience-original-gato-adulto-indoor.js"
},

"petdotu179": {
    "40152480219297": "https://petvet.cl/products/regepipel-plus.js"
},

"petdotu180": {
    "43854457536673": "https://petvet.cl/products/pro-plan-puppy-razas-medianas-15kg.js"
},

"petdotu182": {
    "43707310964897": "https://petvet.cl/products/hematon-b12-elixir-perros-y-gatos-100ml.js"
},

"petdotu186": {
    "42361910132897": "https://petvet.cl/products/glicopan-perros-y-gatos.js"
},

"petdotu187": {
    "43596331057313": "https://petvet.cl/products/pro-plan-gato-urinario.js"
},

"petdotu190": {
    "44181000421537": "https://petvet.cl/products/purina-excellent-cachorro-15kg.js"
},

"petdotu191": {
    "43156268744865": "https://petvet.cl/products/purina-excellent-perro-adulto-pollo-arroz.js"
},

"petdotu192": {
    "43596219056289": "https://petvet.cl/products/pro-plan-gato-adulto-esterilizado.js"
},

"petdotu193": {
    "42310076858529": "https://petvet.cl/products/doguivit-senior-30-comprimidos.js"
},

"petdotu195": {
    "40152479039649": "https://petvet.cl/products/paz-pet-suspension-oral.js"
},

"petdotu198": {
    "40152448958625": "https://petvet.cl/products/naxpet-10-mg-10-comprimidos.js"
},

"petdotu200": {
    "44279760748705": "https://petvet.cl/products/vetgastril-50-ml.js"
},

"petdotu201": {
    "42463409701025": "https://petvet.cl/products/senilpet-cerebral-5-x-60-comp.js"
},

"petdotu202": {
    "40152459051169": "https://petvet.cl/products/petever-forte-shampoo-150ml.js"
},

"petdotu205": {
    "42271737249953": "https://petvet.cl/products/adaptil-repuesto-48-ml.js"
},

"petdotu206": {
    "40152478777505": "https://petvet.cl/products/papainpet.js"
},

"petdotu207": {
    "40152485757089": "https://petvet.cl/products/silimadrag-suspension.js"
},

"petdotu208": {
    "42361911541921": "https://petvet.cl/products/hemolitan-perros-y-gatos.js"
},

"petdotu210": {
    "40152488312993": "https://petvet.cl/products/superpet-omega-gato.js"
},

"petdotu184": {
    "43596385386657": "https://petvet.cl/products/pro-plan-sensitive-skin-razas-pequenas-3kg.js"
},

"petdotu1": {
    "41857592361121": "https://petvet.cl/products/apoquel-16mg-20-comp.js"
},

"petdotu2": {
    "41857592754337": "https://petvet.cl/products/apoquel-3-6-mg-20-comp.js"
},

"petdotu3": {
    "41857597014177": "https://petvet.cl/products/apoquel-5-4-mg-20-comp.js"
},

"petdotu12": {
    "42033421123745": "https://petvet.cl/products/acana-free-run-poultry-perro.js"
},

"petdotu8": {
    "43111864369313": "https://petvet.cl/products/acana-puppy-junior-perro.js"
},

"petdotu6": {
    "41689298796705": "https://petvet.cl/products/prairie-poultry-perro.js"
},

"petdotu9": {
    "41857724350625": "https://petvet.cl/products/bountiful-catch-gato.js"
},

"petdotu14": {
    "41689377341601": "https://petvet.cl/products/duck-pear-perro.js"
},

"petdotu11": {
    "43111863189665": "https://petvet.cl/products/acana-freshwater-fish-perro.js"
},

"petdotu222": {
    "42423305797793": "https://petvet.cl/products/acana-light-fit-2-kg-1.js"
},

"petdotu7": {
    "42033421156513": "https://petvet.cl/products/wild-coast-perro.js"
},

"petdotu10": {
    "42423280697505": "https://petvet.cl/products/first-feast-gato.js"
},

"petdotu44": {
    "40152493490337": "https://petvet.cl/products/mother-and-babycat.js"
},

"petdotu45": {
    "40152491622561": "https://petvet.cl/products/canino-hypoallergenic.js"
},

"petdotu68": {
    "42708472463521": "https://petvet.cl/products/nexgard-spectra-7-6-15kg-1-comprimido.js"
},

"petdotu67": {
    "44577414611105": "https://petvet.cl/products/nexgard-spectra-7-6-15kg-3-comprimidos.js"
},

"petdotu70": {
    "42708470136993": "https://petvet.cl/products/nexgard-spectra-15-30kg-1-comprimido.js"
},

"petdotu69": {
    "44577353695393": "https://petvet.cl/products/nexgard-spectra-15-30kg-3-comprimidos.js"
},

"petdotu138": {
    "44577401274529": "https://petvet.cl/products/nexgard-spectra-30-60kg-3-comprimidos.js"
},

"petdotu147": {
    "42730103144609": "https://petvet.cl/products/nexgard-spectra-30-60kg-1-comprimido.js"
},

"petdotu33": {
    "43771918090401": "https://petvet.cl/products/bravecto-plus-gato-1-2-2-8kg-112-5mg.js"
},

"petdotu148": {
    "43771996864673": "https://petvet.cl/products/bravecto-plus-gato-2-8-6-25kg-250mg.js"
},

"petdotu32": {
    "42738538872993": "https://petvet.cl/products/bravecto-perro-2-4-5kg-112-5mg.js"
},

"petdotu30": {
    "42738539692193": "https://petvet.cl/products/bravecto-perro-4-5-10kg-250mg.js"
},

"petdotu29": {
    "42738543263905": "https://petvet.cl/products/bravecto-perro-10-20kg-500mg.js"
},

"petdotu28": {
    "42738545557665": "https://petvet.cl/products/bravecto-perro-20-40kg-1-000mg.js"
},

"petdotu84": {
    "42324007878817": "https://petvet.cl/products/americalitter-ultra-odor-seal.js"
},

"petdotu72": {
    "44388326178977": "https://petvet.cl/products/america-litter-ultra-odor-seal-lavanda-15kg.js"
},

"petdotu58": {
    "42271448629409": "https://petvet.cl/products/brit-care-gf-puppy-salmon.js"
},

"petdotu52": {
    "42271606767777": "https://petvet.cl/products/brit-care-adult-small-breed-l-r.js"
},

"petdotu53": {
    "42271434178721": "https://petvet.cl/products/brit-care-adult-medium-breed-lamb-hypoallergenic.js"
},

"petdotu106": {
    "42271541362849": "https://petvet.cl/products/brit-care-puppy-l-r.js"
},

"petdotu56": {
    "42271560237217": "https://petvet.cl/products/brit-care-weight-loss-rabbit.js"
},

"petdotu59": {
    "42271478841505": "https://petvet.cl/products/brit-care-gf-senior-light-salmon.js"
},

"petdotu51": {
    "42271548801185": "https://petvet.cl/products/brit-care-senior-lamb.js"
},

"petdotu156": {
    "44487570981025": "https://petvet.cl/products/josera-light-vital-12-5kg.js"
},

"petdotu116": {
    "43411814285473": "https://petvet.cl/products/brit-care-adult-large-breed-salmon.js"
},

"petdotu55": {
    "42423170367649": "https://petvet.cl/products/brit-care-cat-gf-sterilized-urinary.js"
},

"petdotu110": {
    "43019722981537": "https://petvet.cl/products/brit-care-cat-gf-sterilized-weight-control.js"
},

"petdotu123": {
    "44042326245537": "https://petvet.cl/products/brit-care-junior-large-breed-salmon.js"
},

"petdotu113": {
    "43091932020897": "https://petvet.cl/products/brit-care-junior-large-breed-lamb.js"
},

"petdotu127": {
    "43019722096801": "https://petvet.cl/products/brit-care-cat-gf-kitten-healthy-growth-development.js"
},

"petdotu130": {
    "43019722326177": "https://petvet.cl/products/brit-care-cat-gf-haircare-healthy-shiny-coat.js"
},

"petdotu133": {
    "42271444631713": "https://petvet.cl/products/brit-care-adult-salmon.js"
},

"petdotu57": {
    "42271444598945": "https://petvet.cl/products/brit-care-adult-salmon.js"
},

"petdotu134": {
    "43083183095969": "https://petvet.cl/products/brit-care-cat-senior-weight-control.js"
},

"petdotu136": {
    "42271448662177": "https://petvet.cl/products/brit-care-gf-puppy-salmon.js"
},

"petdotu139": {
    "43487989072033": "https://petvet.cl/products/brit-care-adult-sensitive-venado.js"
},

"petdotu140": {
    "42271560269985": "https://petvet.cl/products/brit-care-weight-loss-rabbit.js"
},

"petdotu155": {
    "42423170334881": "https://petvet.cl/products/brit-care-cat-gf-sterilized-urinary.js"
},

"petdotu122": {
    "42271606800545": "https://petvet.cl/products/brit-care-adult-small-breed-l-r.js"
},

"petdotu27": {
    "40087240835233": "https://petvet.cl/products/rimadyl.js"
},

"petdotu26": {
    "40159957549217": "https://petvet.cl/products/rimadyl.js"
},

"petdotu5": {
    "40087277830305": "https://petvet.cl/products/revolution-plus-gato-1-25-2-5kg-0-25ml.js"
},

"petdotu4": {
    "42738646745249": "https://petvet.cl/products/revolution-plus-gato-2-5-5kg-0-5ml.js"
},

"petdotu119": {
    "43830181560481": "https://petvet.cl/products/revolution-plus-gato-5-10kg-1ml.js"
},

"petdotu48": {
    "42785343013025": "https://petvet.cl/products/bil-jac-selected-adult-dog-food.js"
},

"petdotu99": {
    "41981042000033": "https://petvet.cl/products/hills-prescription-diet-canine-c-d-7-98-kg.js"
},

"petdotu22": {
    "41633978810529": "https://petvet.cl/products/simparica-10-20kg-40mg-1-comprimido.js"
},

"petdotu23": {
    "43577667354785": "https://petvet.cl/products/simparica-10-20kg-40mg-3-comprimidos.js"
},

"petdotu24": {
    "43577665388705": "https://petvet.cl/products/simparica-5-10kg-20mg-3-comprimidos.js"
},

"petdotu25": {
    "41633916944545": "https://petvet.cl/products/simparica-5-10kg-20mg-1-comprimido.js"
},

"petdotu20": {
    "43577669910689": "https://petvet.cl/products/simparica-20-40kg-80mg-3-comprimidos.js"
},

"petdotu88": {
    "40152468979873": "https://petvet.cl/products/hills-canine-adulto-de-razas-pequenas-2-04-kg.js"
},

"petdotu21": {
    "41634051162273": "https://petvet.cl/products/simparica-20-40kg-80mg-1-comprimido.js"
},

"petdotu61": {
    "40087248470177": "https://petvet.cl/products/mixantip-plus.js"
},

"petdotu60": {
    "40087248437409": "https://petvet.cl/products/mixantip-plus.js"
},

"petdotu50": {
    "42785360314529": "https://petvet.cl/products/bil-jac-puppy-select-formula.js"
},

"petdotu85": {
    "41857368359073": "https://petvet.cl/products/canine-adult-metabolic-7-98-kg.js"
},

"petdotu97": {
    "42392861278369": "https://petvet.cl/products/adaptil-collar-perro.js"
},

"petdotu96": {
    "42392861245601": "https://petvet.cl/products/adaptil-collar-perro.js"
},

"petdotu63": {
    "43037801152673": "https://petvet.cl/products/oven-baked-adulto-pescado-11-34-kg.js"
},

"petdotu62": {
    "43037801087137": "https://petvet.cl/products/oven-baked-adulto-pollo-11-34-kg.js"
},

"petdotu64": {
    "43037801218209": "https://petvet.cl/products/oven-baked-senior-11-34-kg.js"
},

"petdotu78": {
    "40087214227617": "https://petvet.cl/products/arena-traper.js"
},

"petdotu73": {
    "42361913311393": "https://petvet.cl/products/silimarina-vitanimal-120mg.js"
},

"petdotu74": {
    "42361913344161": "https://petvet.cl/products/silimarina-vitanimal-120mg.js"
},

"petdotu18": {
    "40159961317537": "https://petvet.cl/products/alimento-fit-formula-cachorro-10kg.js"
},

"petdotu15": {
    "40159961383073": "https://petvet.cl/products/alimento-fit-formula-gato-10kg.js"
},

"petdotu82": {
    "40152463147169": "https://petvet.cl/products/artritabs.js"
},

"petdotu93": {
    "40152464588961": "https://petvet.cl/products/adaptil.js"
},

"petdotu42": {
    "40087277043873": "https://petvet.cl/products/feliway-classic.js"
},

"petdotu43": {
    "40087277338785": "https://petvet.cl/products/feliway-friends.js"
},

"petdotu40": {
    "40087277600929": "https://petvet.cl/products/feliway-spray.js"
},

"petdotu39": {
    "41715631194273": "https://petvet.cl/products/feliway-classic-repuesto-48-ml.js"
},

"petdotu66": {
    "40152475599009": "https://petvet.cl/products/laveta-taurina-gatos-50-ml.js"
},

"petdotu65": {
    "40152475238561": "https://petvet.cl/products/laveta-carnitina-perros-50ml.js"
},

"petdotu49": {
    "42785365131425": "https://petvet.cl/products/bil-jac-small-breed-adult-2-7-kg.js"
},

"petdotu83": {
    "40152471437473": "https://petvet.cl/products/condrovet-30-comp.js"
},

"petdotu77": {
    "42008137629857": "https://petvet.cl/products/oxtrin-condroprotector-30-comp.js"
},

"petdotu98": {
    "42463441125537": "https://petvet.cl/products/allercalm-250-ml.js"
},

"petdotu41": {
    "41715635650721": "https://petvet.cl/products/feliway-friends-repuesto.js"
},

"petdotu34": {
    "40152476713121": "https://petvet.cl/products/calming-spot-on-gatos.js"
},

"petdotu35": {
    "40087281172641": "https://petvet.cl/products/calming-spray.js"
},

"petdotu86": {
    "41556602650785": "https://petvet.cl/products/wanpy2.js"
},

"petdotu94": {
    "41896962752673": "https://petvet.cl/products/ohm-modulador-de-ansiedad-perros-y-gatos.js"
},

"petdotu81": {
    "40152452071585": "https://petvet.cl/products/calmer.js"
},

"petdotu89": {
    "42471476134049": "https://petvet.cl/products/sucravet-10-100-ml.js"
},

"petdotu36": {
    "40087280287905": "https://petvet.cl/products/calming-treats-gato.js"
},

"petdotu38": {
    "40087281074337": "https://petvet.cl/products/calming-tableta.js"
},

"petdotu37": {
    "40087282319521": "https://petvet.cl/products/calming-colllar-gato.js"
},

"petdotu79": {
    "40476213674145": "https://petvet.cl/products/synulox250mg.js"
},

"petdotu92": {
    "42874800144545": "https://petvet.cl/products/ursovet-60-ml.js"
},

"petdotu71": {
    "41654177792161": "https://petvet.cl/products/florafix-pet.js"
},

"petdotu75": {
    "40152477597857": "https://petvet.cl/products/naxpet-0-4-suspension-oral.js"
},

"petdotu17": {
    "41896955117729": "https://petvet.cl/products/fit-formula-adulto-20-kg.js"
},

"petdotu16": {
    "41896954822817": "https://petvet.cl/products/fit-formula-senior-20-kg.js"
},

"petdotu19": {
    "40159961252001": "https://petvet.cl/products/fit-adulto-razas-pequenas.js"
},

"petdotu126": {
    "40152495685793": "https://petvet.cl/products/fit-formula-senior-razas-pequenas.js"
},

"petdotu76": {
    "41065522004129": "https://petvet.cl/products/pederol-aerosol.js"
},

"petdotu87": {
    "42392930091169": "https://petvet.cl/products/itraskin-suspension-120-ml.js"
},

"petdotu91": {
    "42361854394529": "https://petvet.cl/products/dermisolona-suspension.js"
},

"petdotu90": {
    "42271785713825": "https://petvet.cl/products/pacifor-gotas-10-ml.js"
},

"petdotu95": {
    "42361853804705": "https://petvet.cl/products/dermisolona-comp-x-10.js"
},

"petdotu100": {
    "42713335824545": "https://petvet.cl/products/phisio-anti-olor-limpiador-auricular-virbac-100ml.js"
},

"petdotu109": {
    "43925724266657": "https://petvet.cl/products/josera-festival-12-5kg.js"
},

"petdotu120": {
    "43888893034657": "https://petvet.cl/products/josera-ente-kartoffel-12-5kg.js"
},

"petdotu117": {
    "43888873275553": "https://petvet.cl/products/josera-josidog-regular-18kg.js"
},

"petdotu124": {
    "43888931307681": "https://petvet.cl/products/josera-gato-naturecat.js"
},

"petdotu156": {
    "43888860692641": "https://petvet.cl/products/josera-light-vital-12-5kg.js"
},

"petdotu141": {
    "43888923771041": "https://petvet.cl/products/josera-gato-naturelle-2kg.js"
},

"petdotu144": {
    "44042727424161": "https://petvet.cl/products/josera-balance-12-5kg.js"
},

"petdotu160": {
    "41689363579041": "https://petvet.cl/products/acana-free-run-poultry-perro.js"
},

"petdotu121": {
    "44537640386721": "https://petvet.cl/products/acana-pork-squash-perro.js"
},

"petdotu151": {
    "43094808592545": "https://petvet.cl/products/leonardo-adulto-senior.js"
},

"petdotu152": {
    "43094807543969": "https://petvet.cl/products/leonardo-adulto-light.js"
},

"petdotu131": {
    "44044562399393": "https://petvet.cl/products/orijen-pupy-perro-cachorro.js"
},

"petdotu153": {
    "43238489948321": "https://petvet.cl/products/orijen-original-gato.js"
},

"petdotu114": {
    "43513906102433": "https://petvet.cl/products/orijen-perro-razas-pequenas.js"
},

"petdotu132": {
    "43191190782113": "https://petvet.cl/products/belcando-finest-grain-free-senior.js"
},

"petdotu146": {
    "43749564645537": "https://petvet.cl/products/virbac-hpm-adult-neutered-cat.js"
},

"petdotu118": {
    "43750029230241": "https://petvet.cl/products/virbac-hpm-dog-allergy.js"
},

"petdotu128": {
    "43942971113633": "https://petvet.cl/products/virbac-hpm-dog-weight-loss-diabetes.js"
},

"petdotu137": {
    "44397883162785": "https://petvet.cl/products/virbac-hpm-dog-weight-loss-control-12-kgs.js"
},

"petdotu125": {
    "43384186437793": "https://petvet.cl/products/america-litter-clean-pawz.js"
},

"petdotu105": {
    "43156259471521": "https://petvet.cl/products/purina-excellent-perro-adulto-skin-care-salmon.js"
},

"petdotu107": {
    "43356432924833": "https://petvet.cl/products/pimocard-5-20-comprimidos.js"
},

"petdotu108": {
    "42361852821665": "https://petvet.cl/products/traumeel-modulador-de-inflamacion-y-dolor.js"
},

"petdotu112": {
    "42361852854433": "https://petvet.cl/products/traumeel-modulador-de-inflamacion-y-dolor.js"
},

"petdotu129": {
    "43852825165985": "https://petvet.cl/products/galliprant-100-mg-30-comprimidos.js"
},

"petdotu142": {
    "40087273341089": "https://petvet.cl/products/advantage-gato-hasta-4kg-0-4ml.js"
},

"petdotu135": {
    "42738744393889": "https://petvet.cl/products/advantage-gato-4-8kg-0-8ml.js"
},

"petdotu143": {
    "40159957221537": "https://petvet.cl/products/drontal-plus-perro-hasta-10kg-2-comprimidos.js"
},

"petdotu145": {
    "44054704259233": "https://petvet.cl/products/neptra-solucion-otica.js"
},

"petdotu150": {
    "44279072227489": "https://petvet.cl/products/osteodrag-ha-30-comprimidos.js"
},

"petdotu149": {
    "41646114996385": "https://petvet.cl/products/advocate-gato-hasta-4kg-0-4ml.js"
},

"petdotu115": {
    "42738659557537": "https://petvet.cl/products/advocate-gato-4-8kg-0-8ml.js"
},

"petdotu157": {
    "41857461190817": "https://petvet.cl/products/oftavet-5-ml.js"
},

"petdotu158": {
    "43830826074273": "https://petvet.cl/products/hemolivet-30-comprimidos.js"
},

"petdotu159": {
    "42366871928993": "https://petvet.cl/products/cerenia-24-mg-x-4-comp.js"
},

"petdotu154": {
    "43591189987489": "https://petvet.cl/products/canigest-combi-32ml.js"
},

"petdotu13": {
    "44309699166369": "https://petvet.cl/products/fit-formula-light-20-kg.js"
},

"petdotu204": {
    "44430172684449": "https://petvet.cl/products/nexgard-combo-gato-0-8-2-5kg.js"
},

"petdotu168": {
    "44427832033441": "https://petvet.cl/products/nexgard-combo-gato-2-5-7-5kg.js"
},

"petdotu600": {
    "44453910380705": "https://petvet.cl/products/leonardo-adulto-gf-maxi.js"
}
}
urls2={    "petdotu197": {
    "43683672457377": "https://petvet.cl/products/acana-indoor-entree-gato.js"
},

"petdotu194": {
    "41689309708449": "https://petvet.cl/products/wild-coast-perro.js"
}
}
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

# Ejecutar la función fetch_data para cada producto en urls2
for product_key, product_info in urls3.items():
    for product_id, product_url in product_info.items():
        fetch_data(product_id, product_url)
NEW_SPREADSHEET_ID = '1lLfl_jSGUEtitfsezo_zz53Bn2zAzID73VtxIi4dKRo'
# Aquí puedes ver los datos extraídos
print(price_data)
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

# Valores que se pasan a Sheets
values = [[item['SKU'], competitor,item['Price'],item['Compare_at_Price'],item['Available']] for item in price_data]
result = sheet.values().update(
    spreadsheetId=SPREADSHEET_ID_API,
    range='apipets!A2:E1000',  # CAMBIAR
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
  # ID de la nueva hoja de cálculo
result = sheet.values().get(spreadsheetId=NEW_SPREADSHEET_ID, range='petvet!A:A').execute()  # Cambiar donde llega la info
values = result.get('values', [])
last_row = len(values) + 1  # Obtener el índice de la última fila vacía
values = [[item['SKU'],item['competitor'], item['Price'],item['Compare_at_Price']] for item in price_data]
print(values)
update_range = f'petvet!A{last_row}:E{last_row + len(values) - 1}'  # Cambiar
result = sheet.values().update(
    spreadsheetId=NEW_SPREADSHEET_ID,
    range=update_range,
    valueInputOption='USER_ENTERED',
    body={'values': values}
).execute()

print(f"Datos insertados correctamente en la nueva hoja de Google Sheets en el rango {update_range}")
# MANDAR DATOS A LA API ----------------------------------------------------------------------------------------------------
SPREADSHEET_ID_API = '1S8jzZl4UehXDJxWuHfTSLftBnq3CKUXhgRGrJIShyhE'  
result = sheet.values().get(spreadsheetId=SPREADSHEET_ID_API, range='apipets!A:A').execute() #Cambiar donde llega la info
values = result.get('values', [])
last_row = len(values) + 1  # Obtener el índice de la última fila vacía
values = [[item['SKU'], item['Price'],item['Compare_at_Price'],item['Available']] for item in price_data]
print(values)
update_ranges = f'apipets!A{last_row}:E{last_row + len(values) - 1}'
result = sheet.values().update(
    spreadsheetId=SPREADSHEET_ID_API,
    range=update_ranges,
    valueInputOption='USER_ENTERED',
    body={'values': values}
).execute()

print(f"Datos insertados correctamente en la nueva hoja de Google Sheets en el rango {update_ranges}")