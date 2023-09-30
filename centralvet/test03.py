from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
# import json
# import pandas as pd


#Ejecutador del Driver

# # PATH = "C:\\Program Files (x86)\\chromedriver.exe"
# PATH = "/Users/benjammunoz/Desktop/Dotu/chromedriver"
PATH = "/usr/local/bin/chromedriver"

# Configurar las opciones de Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")  # Ver el Navegador
chrome_options.add_argument("--window-size=1920x1080")

start_time = time.time()  # Tiempo de inicio de la ejecución

driver = webdriver.Chrome(options=chrome_options)


#URL Para Sacar Info

# Lista de enlaces
url = [
    "https://www.centralvet.cl/farmacia-veterinaria/21003-apoquel-16-mg-zoetis-20-comprimidos-venta-con-receta.html",
    "https://www.centralvet.cl/farmacia-veterinaria/21001-apoquel-36mg-zoetis-venta-con-receta.html",
    "https://www.centralvet.cl/farmacia-veterinaria/21002-apoquel-54mg-zoetis-venta-con-receta.html",
    "https://www.centralvet.cl/higiene-para-gatos/23523-revolution-plus-para-gatos-entre-25-y-5-kg-antiparasitario-zoetis.html",
    "https://www.centralvet.cl/higiene-para-gatos/23522-revolution-plus-para-gatos-entre-125-y-25-kg-antiparasitario-zoetis.html",
    "https://www.centralvet.cl/inicio/22462-21454-acana-classic-prairie-poultry-para-perros.html#/1111111133-peso-113_kg",
    "https://www.centralvet.cl/inicio/24478-23756-acana-duck-pear-singles-formula-perro.html#/1111111133-peso-113_kg",
    "https://www.centralvet.cl/para-perros/21812-simparica-antiparasitario-perros-entre-10-a-20-kg-1-dosis-zoetis.html",
    "https://www.centralvet.cl/para-perros/22003-simparica-antiparasitario-perros-entre-5-a-10kg-3-dosis-zoetis.html",
    "https://www.centralvet.cl/para-perros/21810-simparica-antiparasitario-perros-entre-5-a-10-kg-1-dosis-zoetis.html",
    "https://www.centralvet.cl/farmacia-para-perros/9452-rimadyl-100-mg-carprofeno-60-tabletas-anti-inflamatorio-zoetis.html",
    "https://www.centralvet.cl/farmacia-para-perros/6297-rimadyl-100-mg-carprofeno-14-tabletas-anti-inflamatorio-zoetis.html",
    "https://www.centralvet.cl/farmacia-para-perros/7781-bravecto-masticable-contra-pulgasgarrapatas-20-a-40kg.html",
    "https://www.centralvet.cl/farmacia-para-perros/7784-bravecto-masticable-contra-pulgasgarrapatas-45-a-10kg.html",
    "https://www.centralvet.cl/farmacia-para-perros/7777-bravecto-masticable-contra-pulgasgarrapatas-2-a-45kg.html",
    "https://www.centralvet.cl/farmacia-para-gatos/21230-calming-home-spray-ambiental-para-gatos-y-perros-125-ml-beaphar.html",
    "https://www.centralvet.cl/farmacia-para-gatos/21232-calming-treats-para-gatos-35g-beaphar.html",
    "https://www.centralvet.cl/farmacia-para-gatos/21229-calming-collar-para-gatos-100-natural-beaphar.html",
    "https://www.centralvet.cl/farmacia-para-gatos/22615-calming-tablets-para-gatos-y-perros-20-tabletas-beaphar.html",
    "https://www.centralvet.cl/repuestos/6890-feliway-classic-repuesto-para-difusor-48-ml.html",
    "https://www.centralvet.cl/bienestar/6892-feliway-classic-spray-para-problemas-de-comportamiento-en-gatos-60-ml.html",
    "https://www.centralvet.cl/bienestar/18610-felifriend-feliway-friends-repuesto-para-difusor-48ml.html",
    "https://www.centralvet.cl/accesorios-y-bienestar/16558-feliway-classic-difusor-electrico-48-ml.html",
    "https://www.centralvet.cl/alimentos-de-prescripcion-veterinaria/4932-royal-canin-hipoalergenico-hypoallergenic-para-perro-2-kg.html",
    "https://www.centralvet.cl/alimentos/5451-21425-royal-canin-mini-adulto.html#/1111111116-peso-25_kg",
    "https://www.centralvet.cl/alimentos/6764-bil-jac-select-small-breed-perros-adultos-27kg.html",
    "https://www.centralvet.cl/perros-senior/23799-brit-care-perro-senior-cordero-y-arroz-12kg.html",
    "https://www.centralvet.cl/productos-para-perros/20784-brit-care-perro-adulto-small-breed-cordero-y-arroz-75kg.html",
    "https://www.centralvet.cl/inicio/21072-21305-brit-care-perro-adulto-medium-breed-cordero-y-arroz.html#/1111111130-peso-12_kg",
    "https://www.centralvet.cl/alimentos/23807-23083-brit-care-gato-esterilizado-urinary-health-pollo-fresco-.html#/1111111131-peso-2_kg",
    "https://www.centralvet.cl/farmacia-para-perros/6204-mixantip-plus-pomo-15g-tratamientos-dermatologicos.html",
    "https://www.centralvet.cl/farmacia-para-perros/6175-laveta-carnitina-suplemento-vitaminico-para-perros.html",
    "https://www.centralvet.cl/farmacia-para-gatos/6335-laveta-taurina-suplemento-vitaminico-para-gatos.html",
    "https://www.centralvet.cl/farmacia-para-perros/21271-florafix-pet-probiotico-para-mascotas-15g.html",
    "https://www.centralvet.cl/farmacia-para-perros/21223-silimarina-vitanimal-caja-30-comprimidos.html",
    "https://www.centralvet.cl/farmacia-para-perros/9810-silimarina-vitanimal-frasco-90-comprimidos.html",
    "https://www.centralvet.cl/farmacia-para-perros/9523-synulox-10-comprimidos-venta-con-receta-zoetis.html",
    "https://www.centralvet.cl/farmacia-veterinaria/22564-calmer-30-ml-spray-ayuda-a-tranquilizar-baja-la-ansiedad-aromvet-aromaterapia.html",
    "https://www.centralvet.cl/farmacia-para-perros/6025-condrovet-condroprotector-para-perros-30-comprimidos.html",
    "https://www.centralvet.cl/arena-sanitaria/21338-arena-sanitaria-americalitter-7kg-ultra-odor-seal.html",
    "https://www.centralvet.cl/farmacia-para-perros/6158-itraskin-jarabe-120-ml-antifungico-para-perros-y-gatos.html",
    "https://www.centralvet.cl/alimentos/24262-hills-science-diet-adulto-small-paws-para-adultos-toy-2kg.html",
    "https://www.centralvet.cl/farmacia-para-perros/10671-sucravet-sucralfato-10-100-ml-perros-y-gatos.html",
    "https://www.centralvet.cl/farmacia-para-perros/6252-pacifor-tranquilizante-solucion-oral-10-ml-receta.html",
    "https://www.centralvet.cl/farmacia-para-perros/8072-dermisolona-30-ml-jarabe-suspension-oral.html",
    "https://www.centralvet.cl/farmacia-para-perros/15783-adaptil-difusor-con-kit-de-iniciacion.html",
    "https://www.centralvet.cl/farmacia-para-perros/21498-ohm-biomodulador-de-ansiedad-21-comprimidos-holliday.html",
    "https://www.centralvet.cl/farmacia-para-perros/6044-dermisolona-prednisolona-20-mg-10-comprimidos.html",
    "https://www.centralvet.cl/farmacia-para-perros/21239-adaptil-collar-para-perros-raza-mediana-grande.html",
    "https://www.centralvet.cl/farmacia-para-perros/5959-allercalm-shampoo-medicado-virbac-frasco-250-ml.html",
    "https://www.centralvet.cl/alimentos-de-prescripcion-veterinaria/22768-21711-hills-prescription-diet-rd-para-perros-reduccion-del-peso-a-pedido.html#/1111111259-peso-79_kg",
    "https://www.centralvet.cl/farmacia-para-perros/6204-mixantip-plus-pomo-15g-tratamientos-dermatologicos.html",
    "https://www.centralvet.cl/farmacia-para-perros/6158-itraskin-jarabe-120-ml-antifungico-para-perros-y-gatos.html",
    "https://www.centralvet.cl/alimentos/24262-hills-science-diet-adulto-small-paws-para-adultos-toy-2kg.html",
    "https://www.centralvet.cl/farmacia-para-perros/10671-sucravet-sucralfato-10-100-ml-perros-y-gatos.html",
    "https://www.centralvet.cl/farmacia-para-perros/6252-pacifor-tranquilizante-solucion-oral-10-ml-receta.html",
    "https://www.centralvet.cl/farmacia-para-perros/8072-dermisolona-30-ml-jarabe-suspension-oral.html",
    "https://www.centralvet.cl/farmacia-para-perros/15783-adaptil-difusor-con-kit-de-iniciacion.html",
    "https://www.centralvet.cl/farmacia-para-perros/21498-ohm-biomodulador-de-ansiedad-21-comprimidos-holliday.html",
    "https://www.centralvet.cl/farmacia-para-perros/6044-dermisolona-prednisolona-20-mg-10-comprimidos.html",
    "https://www.centralvet.cl/farmacia-para-perros/21239-adaptil-collar-para-perros-raza-mediana-grande.html",
    "https://www.centralvet.cl/farmacia-para-perros/5959-allercalm-shampoo-medicado-virbac-frasco-250-ml.html",
    "https://www.centralvet.cl/alimentos-de-prescripcion-veterinaria/22768-21711-hills-prescription-diet-rd-para-perros-reduccion-del-peso-a-pedido.html#/1111111259-peso-79_kg"
]
#XPATH ID cambiante para apretar boton y sacar texto

# direcciones = ['option-label-acana_wildcoast_perros-906-item-2334',
# 'option-label-acana_wildcoast_perros-906-item-2335',
# 'option-label-acana_wildcoast_perros-906-item-2336']

direcciones = ["/html/body/main/section/div[2]/div/section/div[2]/div[1]/div[2]/div[2]/div[2]/form/div[1]/div/ul/li[1]/input",
"/html/body/main/section/div[2]/div/section/div[2]/div[1]/div[2]/div[2]/div[2]/form/div[1]/div/ul/li[2]/input",
"/html/body/main/section/div[2]/div/section/div[2]/div[1]/div[2]/div[2]/div[2]/form/div[1]/div/ul/li[3]/input"]



#Apretar Boton#
resultados=[]


#Apretar los 3 botones y sacar la info de cada uno en una URL
for i in url:
    if driver.get("url") >0 :
        driver.get("https://www.centralvet.cl/farmacia-para-perros/5959-allercalm-shampoo-medicado-virbac-frasco-250-ml.html")  # Cambia la URL para cada botón
   
        nombresku = driver.find_element(By.XPATH, '/html/body/main/section/div[2]/div/section/div[2]/div[1]/div[2]/div[1]/h1/span')
        precio = driver.find_element(By.XPATH, '/html/body/main/section/div[2]/div/section/div[2]/div[1]/div[2]/div[1]/div/div[2]/div/span[1]/span')
        tipoalimento = driver.find_element(By.XPATH, "/html/body/main/section/div[2]/div/section/div[2]/div[1]/div[2]/div[2]/div[2]/form/div[1]/div/ul/li[1]/input")

        resultado_dict = {
            'nombre': nombresku.text,
            'tipo_alimento': tipoalimento.text,
            'precio': precio.text
        }
        resultados.append(resultado_dict)

print(resultados)

end_time = time.time()  # Tiempo de finalización de la ejecución

execution_time = end_time - start_time

print(execution_time)


    
#Quitar el Driver de Chrome
driver.quit()


#Exportando Datos en JSON

# with open("scraped_data01.json", "w") as f:
#     json.dump(resultados, f, indent=4)

# # Crear un DataFrame desde la lista de resultados
# df_resultados = pd.DataFrame(resultados)

# # Exportar el DataFrame a un archivo Excel
# df_resultados.to_excel("scraped_data01.xlsx", index=False)

# # Calcula el tiempo de Ejecucion

# end_time = time.time()  

# execution_time = end_time - start_time

# print("Tiempo de ejecución: %.2f segundos" % execution_time)




