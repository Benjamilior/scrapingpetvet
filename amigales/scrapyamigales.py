#Codigo para sacar el precio de producto donde la pagina no tiene boton 
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


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
tipo13 = [ "https://www.amigales.cl/acana-first-feas-gatitos.html",
    "https://www.amigales.cl/fit-formula-gato-adulto-10kg.html",
    "https://www.amigales.cl/fit-formula-perro-senior.html",
    "https://www.amigales.cl/fit-formula-perro-adulto-20kg.html",
    "https://www.amigales.cl/fit-formula-cachorro-10kg.html",
    "https://www.amigales.cl/beaphar-calmingspot-gatos.html",
    "https://www.amigales.cl/snacks-calmantes-gatos.html"]
tipo13 = ["https://laikamascotas.cl/producto/matisse-alimento-para-gato-castrado-salmon?sku=7898939952704"]
tipo1 = [
    "https://www.amigales.cl/acana-first-feas-gatitos.html",
    "https://www.amigales.cl/fit-formula-gato-adulto-10kg.html",
    "https://www.amigales.cl/fit-formula-perro-senior.html",
    "https://www.amigales.cl/fit-formula-perro-adulto-20kg.html",
    "https://www.amigales.cl/fit-formula-cachorro-10kg.html",
    "https://www.amigales.cl/beaphar-calmingspot-gatos.html",
    "https://www.amigales.cl/snacks-calmantes-gatos.html",
    "https://www.amigales.cl/collar-calmante-gatos.html",
    "https://www.amigales.cl/tabletas-calmantes-beaphar.html",
    "https://www.amigales.cl/feliway-classic-repuesto.html",
    "https://www.amigales.cl/feliway-classic-spray.html",
    "https://www.amigales.cl/feliway-friends-repuesto.html",
    "https://www.amigales.cl/feliway-classic-difusor-repuesto.html",
    "https://www.amigales.cl/feliway-friends-difusor-repuesto.html",
    "https://www.amigales.cl/brit-care-cordero-perros-raza-mediana.html",
    "https://www.amigales.cl/brit-care-conejo-hipoalergenico-perros-sobrepeso.html",
    "https://www.amigales.cl/oven-baked-pollo-perros-11-34-kg.html",
    "https://www.amigales.cl/oven-baked-pescado-perros-11-34-kg.html",
    "https://www.amigales.cl/oven-baked-pollo-perros-senior-11-34-kg.html",
    "https://www.amigales.cl/beaphar-laveta-carnitina.html",
    "https://www.amigales.cl/beaphar-laveta-taurina.html",
    "https://www.amigales.cl/florafix-15g.html",
    "https://www.amigales.cl/naxpet-solucion-oral.html",
    "https://www.amigales.cl/oxtrin.html",
    "https://www.amigales.cl/synulox-250mg.html",
    "https://www.amigales.cl/calmer-calma.html",
    "https://www.amigales.cl/artri-tabs-60-tabletas.html",
    "https://www.amigales.cl/condrovet-30-comprimidos.html",
    "https://www.amigales.cl/wanpy-jerky-cordero.html",
    "https://www.amigales.cl/itraskin-suspension-oral.html",
    "https://www.amigales.cl/sucravet.html",
    "https://www.amigales.cl/dermisolona-30-ml-solucion-oral.html",
    "https://www.amigales.cl/ursovet-drag-pharma.html",
    "https://www.amigales.cl/adaptil-difusor-repuesto.html",
    "https://www.amigales.cl/ohm-comprimidos-calmantes-perros-gatos.html",
    "https://www.amigales.cl/dermisolona-20mg-10-comprimidos.html",
    "https://www.amigales.cl/virbac-allercalm-shampoo.html",
    "https://www.amigales.cl/phisio-anti-olor-auricular.html"
]


    
tipo2 = ["https://www.centralvet.cl/inicio/22462-21454-acana-classic-prairie-poultry-para-perros.html#/1111111133-peso-113_kg",
"https://www.centralvet.cl/alimentos-de-prescripcion-veterinaria/22768-21711-hills-prescription-diet-rd-para-perros-reduccion-del-peso-a-pedido.html#/1111111259-peso-79_kg"]
tipo3 = ["https://www.centralvet.cl/inicio/21072-21305-brit-care-perro-adulto-medium-breed-cordero-y-arroz.html#/1111111130-peso-12_kg",
"https://www.centralvet.cl/alimentos/23807-23083-brit-care-gato-esterilizado-urinary-health-pollo-fresco-.html#/1111111131-peso-2_kg"]


results = []

#Tipo 1

for url in tipo1:

    driver.get(url)
    try:
        nombresku = driver.find_element("xpath", '/html/body/div[2]/main/div[3]/div/div[1]/div[1]/h1/span') #CAMBIAR
        precio = driver.find_element("xpath", '/html/body/div[2]/main/div[3]/div/div[1]/div[4]/div[1]/span/span/span')#CAMBIAR
        
        
        print(nombresku.text + " " + precio.text)
        data = {
                "Nombre SKU": nombresku.text,
                "Precio": precio.text
            }

            # Add the dictionary to the results list
        results.append(data)

    except Exception as e:
        print(f"Error en la URL {url}: {str(e)}")

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

      
