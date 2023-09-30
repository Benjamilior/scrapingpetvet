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
tipo12 = ["https://bestforpets.cl/tienda/farmacia-para-perros/5388-11515-apoquel.html",
    "https://bestforpets.cl/tienda/farmacia-para-perros/5388-11513-apoquel.html"
    ]
tipo1 = [
    "https://bestforpets.cl/tienda/farmacia-para-perros/5388-11515-apoquel.html",
    "https://bestforpets.cl/tienda/farmacia-para-perros/5388-11513-apoquel.html",
    "https://bestforpets.cl/tienda/farmacia-para-perros/5388-11514-apoquel.html",
    "https://bestforpets.cl/tienda/antiparasitarios-para-gatos/4564--revolution-plus-05-ml.html",
    "https://bestforpets.cl/tienda/antiparasitarios-para-gatos/4563--revolution-plus-025-ml.html",
    "https://bestforpets.cl/tienda/alimento-acana-para-perros/3738-5736-acana-classic-prairie-poultry.html",
    "https://bestforpets.cl/tienda/alimento-acana-para-perros/3739-5739-acana-classic-wild-coast.html",
    "https://bestforpets.cl/tienda/alimento-acana-para-perros/3411-4955-acana-puppy-junior.html",
    "https://bestforpets.cl/tienda/alimento-acana-para-gatos/4949-10599-acana-bountiful-catch-cat.html",
    "https://bestforpets.cl/tienda/alimento-acana-para-gatos/4947-10593-acana-first-feast-kitten.html",
    "https://bestforpets.cl/tienda/alimento-acana-para-perros/2781-3519-acana-freshwater-fish.html",
    "https://bestforpets.cl/tienda/alimento-acana-para-perros/2780-3516-acana-free-run-poultry.html",
    "https://bestforpets.cl/tienda/alimento-acana-para-perros/3412-4958-acana-light-fit.html",
    "https://bestforpets.cl/tienda/alimento-acana-para-perros/2784-3529-acana-duck-pear.html",
    "https://bestforpets.cl/tienda/ver-todas-las-marcas-para-gatos/3418-4964-fit-formula-gato.html",
    "https://bestforpets.cl/tienda/alimento-fit-formula-para-perros/3417-4963-fit-formula-senior.html",
    "https://bestforpets.cl/tienda/alimento-fit-formula-para-perros/3415-4961-fit-formula-adulto.html",
    "https://bestforpets.cl/tienda/alimento-fit-formula-para-perros/3413-4959-fit-formula-cachorro.html",
    "https://bestforpets.cl/tienda/alimento-fit-formula-para-perros/3414-4960-fit-formula-adulto-raza-peque%C3%B1a.html",
    "https://bestforpets.cl/tienda/farmacia-para-perros/5390--rimadyl-masticable-100mg-60-tabletas.html",
    "https://bestforpets.cl/tienda/antiestres-y-educacion-para-gatos/3349--beaphar-calming-home-spray.html",
    "https://bestforpets.cl/tienda/antiestres-y-educacion-para-gatos/3350--beaphar-calming-cat-treats.html",
    "https://bestforpets.cl/tienda/antiestres-y-educacion-para-gatos/3347--beaphar-calming-collar-for-cats.html",
    "https://bestforpets.cl/tienda/antiestres-y-educacion-para-gatos/3351--beaphar-calming-tablets.html",
    "https://bestforpets.cl/tienda/antiestres-y-educacion-para-gatos/2474--feliway-difusor.html",
    "https://bestforpets.cl/tienda/antiestres-y-educacion-para-gatos/2854--feliway-friends-repuesto-difusor.html",
    "https://bestforpets.cl/tienda/antiestres-y-educacion-para-gatos/2853--feliway-friends-difusor.html",
    "https://bestforpets.cl/tienda/alimento-royal-canin-para-gatos/184-111-royal-canin-mother-babycat.html",
    "https://bestforpets.cl/tienda/royal-canin/251-145-royal-canin-hypoallergenic-canino.html",
    "https://bestforpets.cl/tienda/royal-canin/214-889-royal-canin-mini-puppy.html",
    "https://bestforpets.cl/tienda/royal-canin/215-891-royal-canin-mini-adult-canino.html",
    "https://bestforpets.cl/tienda/alimento-bil-jac-para-perros/2334-2521-bil-jac-adult-select-formula.html",
    "https://bestforpets.cl/tienda/alimento-bil-jac-para-perros/2338-6673-bil-jac-small-breed-adult.html",
    "https://bestforpets.cl/tienda/alimento-especial-cachorros/2336-2527-bil-jac-puppy-select-formula.html",
    "https://bestforpets.cl/tienda/alimento-brit-care-para-perros/2839-3724-brit-care-senior-lamb-rice.html",
    "https://bestforpets.cl/tienda/alimento-brit-care-para-perros/2836-3718-brit-care-adult-small-breed-lamb-rice.html",
    "https://bestforpets.cl/tienda/alimento-brit-care-para-perros/2834-3714-brit-care-puppy-lamb-hypoallergenic.html",
    "https://bestforpets.cl/tienda/alimento-brit-care-para-gatos/4694-9812-brit-care-cat-sterilized-urinary.html",
    "https://bestforpets.cl/tienda/alimento-brit-care-para-perros/2350-2559-brit-care-weight-loss-rabbit-hypoallergenic.html",
    "https://bestforpets.cl/tienda/alimento-brit-care-para-perros/2345-2546-brit-care-adult-salmon-grain-free.html",
    "https://bestforpets.cl/tienda/alimento-brit-care-para-perros/2343-2540-brit-care-puppy-salmon-grain-free.html",
    "https://bestforpets.cl/tienda/alimento-brit-care-para-perros/2349-2556-brit-care-senior-light-salmon-grain-free.html",
    "https://bestforpets.cl/tienda/alimento-oven-baked-para-perros/3205-4517-oven-baked-tradition-adult-all-breeds-chicken.html",
    "https://bestforpets.cl/tienda/alimento-oven-baked-para-perros/3207-4520-oven-baked-tradition-adult-all-breeds-fish.html",
    "https://bestforpets.cl/tienda/alimento-oven-baked-para-perros/3643-5381-oven-baked-tradition-senior-weight-management-deboned-chicken-all-breeds.html",
    "https://bestforpets.cl/tienda/suplementos-y-vitaminas-para-perros/702--beaphar-laveta-carnitina.html",
    "https://bestforpets.cl/tienda/suplementos-y-vitaminas-para-gatos/572--beaphar-laveta-taurina.html",
    "https://bestforpets.cl/tienda/farmacia-para-perros/5400--naxpet%C2%AE-soluci%C3%B3n-oral-20ml.html",
    "https://bestforpets.cl/tienda/farmacia-para-perros/5389--synulox.html",
    "https://bestforpets.cl/tienda/arena-para-gatos/2949-6763-odour-buster-original.html",
    "https://bestforpets.cl/tienda/arena-para-gatos/2902-3857-america-litter-ultra-odor-seal.html",
    "https://bestforpets.cl/tienda/farmacia/1793--ursovet-suspensi%C3%B3n-oral.html",
    "https://bestforpets.cl/tienda/adiestramiento-y-educacion/2478-2831-adaptil-collar.html"
]


    
tipo2 = []
tipo3 = []

results = []

#Tipo 1

for url in tipo1:

    driver.get(url)
    try:
        nombresku = driver.find_element("xpath", '/html/body/main/header/section/div/div[1]/div[1]/section/div[1]/div[2]/h4') #CAMBIAR
        precio = driver.find_element("xpath", '/html/body/main/header/section/div/div[1]/div[1]/section/div[1]/div[2]/div[2]/div[1]/div[1]/span')#CAMBIAR
        
        
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

      
