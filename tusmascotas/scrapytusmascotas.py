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



#URLs
tipo1 = ["https://www.tusmascotas.cl/product/apoquel-16mg-oclacitinib/"]
# tipo1 = [
#     "https://www.tusmascotas.cl/product/apoquel-16mg-oclacitinib/",
#     "https://www.tusmascotas.cl/product/apoquel-3-6mg-oclacitinib-20-comprimidos/",
#     "https://www.tusmascotas.cl/product/apoquel-54mg-oclacitinib-receta-requerida/",
#     "https://www.tusmascotas.cl/product/revolution-plus-0-50ml/",
#     "https://www.tusmascotas.cl/product/revolution-plus-0-25ml/",
#     "https://www.tusmascotas.cl/product/acana-classic-praire-poultry/",
#     "https://www.tusmascotas.cl/product/acana-classic-wild-coast/",
#     "https://www.tusmascotas.cl/product/acana-heritage-puppy-junior-1135kg/",
#     "https://www.tusmascotas.cl/product/acana-bountiful-cath-cat-45-kg/",
#     "https://www.tusmascotas.cl/product/first-feast-cat-acana/",
#     "https://www.tusmascotas.cl/product/acana-heritage-freshwater-fish-trucha-arcoiris-bagre-azul-y-perca-dorada-113-kg/",
#     "https://www.tusmascotas.cl/product/acana-heritage-free-run-poultry-pollo-pavo-y-huevo-113-kg/",
#     "https://www.tusmascotas.cl/product/acana-heritage-light-fit-formula-11-35kg/",
#     "https://www.tusmascotas.cl/product/acana-duck-and-pear-2/",
#     "https://www.tusmascotas.cl/product/simparica-antiparasitario-externo-1-comprimido-101-kg-a-20-kg/",
#     "https://www.tusmascotas.cl/product/simparica-antiparasitario-externo-3-comprimidos-10-kg-a-20-kg/",
#     "https://www.tusmascotas.cl/product/simparica-antiparasitario-externo-1-comprimido-51-kg-a-10-kg/",
#     "https://www.tusmascotas.cl/product/rimadyl-carprofeno-100mg/",
#     "https://www.tusmascotas.cl/product/bravecto-antiparasitario-externo-para-perros-20-kg-a-40-kg/",
#     "https://www.tusmascotas.cl/product/bravecto-antiparasitario-externo-para-perros-10-kg-a-20-kg/",
#     "https://www.tusmascotas.cl/product/bravecto-antiparasitario-externo-para-perros-45-kg-a-10-kg/",
#     "https://www.tusmascotas.cl/product/bravecto-gatos-250mg-28-625kg/",
#     "https://www.tusmascotas.cl/product/bravecto-antiparasitario-externo-para-perros-2-kg-a-45-kg/",
#     "https://www.tusmascotas.cl/product/bravecto-antiparasitario-externo-para-gatos-12-kg-a-28-kg/",
#     "https://www.tusmascotas.cl/product/pipeta-calming-spot-on-gato/",
#     "https://www.tusmascotas.cl/product/calming-home-spray-125-ml/",
#     "https://www.tusmascotas.cl/product/calming-cat-treats-35gr/",
#     "https://www.tusmascotas.cl/product/calming-tabletas-de-beaphar-20-und-dog-cat/",
#     "https://www.tusmascotas.cl/product/feliway-spray/",
#     "https://www.tusmascotas.cl/product/feliway-friends-repuesto/",
#     "https://www.tusmascotas.cl/product/feliway-difusor-mas-repuesto/",
#     "https://www.tusmascotas.cl/product/feliway-friends-difusor-mas-repuesto/",
#     "https://www.tusmascotas.cl/product/mother-and-babycat-3/",
#     "https://www.tusmascotas.cl/product/bil-jac-small-breed-adult-2-7kg/",
#     "https://www.tusmascotas.cl/product/bil-jac-puppy-dog-food-13-6kg/",
#     "https://www.tusmascotas.cl/product/brit-perro-senior-lamb-y-rice-12kgs/",
#     "https://www.tusmascotas.cl/product/brit-adult-small-breed/",
#     "https://www.tusmascotas.cl/product/brit-medium-breed-lambrice/",
#     "https://www.tusmascotas.cl/product/brit-perro-puppy-cordero-y-arroz-12kg/",
#     "https://www.tusmascotas.cl/product/brit-care-cat-grain-free-sterilized-urinary-sabor-a-chicken-7kg-c-100903909/",
#     "https://www.tusmascotas.cl/product/brit-perro-weight-loss-conejo-y-arroz-12-kg/",
#     "https://www.tusmascotas.cl/product/brit-adulto-salmon-3/",
#     "https://www.tusmascotas.cl/product/brit-puppy-salmon/",
#     "https://www.tusmascotas.cl/product/mixantip-plus-50gr/",
#     "https://www.tusmascotas.cl/product/mixantip-plus-15-g/",
#     "https://www.tusmascotas.cl/product/oven-baked-tradition-adult-2/",
#     "https://www.tusmascotas.cl/product/oven-baked-tradition/",
#     "https://www.tusmascotas.cl/product/laveta-carnitine-50ml/",
#     "https://www.tusmascotas.cl/product/laveta-taurina-50ml/",
#     "https://www.tusmascotas.cl/product/nexgard-spectra-76-15kg-3-comprimidos/",
#     "https://www.tusmascotas.cl/product/nexgard-spectra-76-15kg-1-comprimido/",
#     "https://www.tusmascotas.cl/product/nexgard-spectra-151-30kg-1-comprimido/",
#     "https://www.tusmascotas.cl/product/nexgard-spectra-151-30kg-3-comprimidos/",
#     "https://www.amigales.cl/florafix-15g.html",
#     "https://www.tusmascotas.cl/product/silimarina-vitanimal-30-comprimidos/",
#     "https://www.tusmascotas.cl/product/silimarina-90-comprimidos/",
#     "https://www.tusmascotas.cl/product/jarabe-naxpet-ketoprofeno-20ml/",
#     "https://www.tusmascotas.cl/product/oxtrin-30-comprimidos/",
#     "https://www.tusmascotas.cl/product/synulox-antibiotico-10-comprimidos-receta-requerida/",
#     "https://www.tusmascotas.cl/product/odour-buster-original-14kg-arena-santiaria-para-gatos/",
#     "https://www.tusmascotas.cl/product/calmer-para-perros-gatos/",
#     "https://www.tusmascotas.cl/product/artri-tabs-60-comprimidos/",
#     "https://www.tusmascotas.cl/product/wanpy-lamb-jerky/",
#     "https://www.tusmascotas.cl/product/itraskin-suspension-oral-120-ml-receta-requerida/",
#     "https://www.tusmascotas.cl/product/sucravet-sucralfato-100ml/",
#     "https://www.tusmascotas.cl/product/ursovet-suspension-oral-60ml/",
#     "https://www.tusmascotas.cl/product/adaptil-difusor-mas-repuesto/",
#     "https://www.tusmascotas.cl/product/ohm-pastillas-calmantes/",
#     "https://www.tusmascotas.cl/product/dermisolona-10-comp-20-mg/",
#     "https://www.tusmascotas.cl/product/adaptil-collar-s-m/",
#     "https://www.tusmascotas.cl/product/adaptil-collar-m-l/",
#     "https://www.tusmascotas.cl/product/allercalm-250-ml/",
#     "https://www.tusmascotas.cl/product/virbac-phisio-anti-olor-orejas-100-ml/"
# ]
tipo2 = []
tipo3 = []

#Diccionario para guardar los datos
results = []

#Tipo 1

for url in tipo1:

    driver.get(url)
    try:
        nombresku = driver.find_element("xpath", '/html/body/div[1]/div[1]/div/div/div/div[2]/div[1]/div[2]/div/div/div[2]/div/h1') #CAMBIAR
        # precio = driver.find_element("xpath", '/html/body/div[1]/div[1]/div/div/div/div[2]/div[3]/div/div/div/div[1]/div/div[1]/div/div/div/span[1]/ins/span/bdi')#CAMBIAR
        precio = driver.find_element(By.CLASS_NAME,"rrp-sale")
        
        data = {
                "Nombre SKU": nombresku.text,
                "Precio": precio.text
            }

            # Add the dictionary to the results list
        results.append(data)

    except Exception as e:
        print(f"No hay Stock de {url}: {str(e)}")

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

      
