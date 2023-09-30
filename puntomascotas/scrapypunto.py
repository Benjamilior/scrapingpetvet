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

tipo1 = [
    "https://puntomascotas.cl/cicatrizantes/37170-apoquel-16-mg-x-20-comprimidos-5414736044217.html",
    "https://puntomascotas.cl/cicatrizantes/37171-apoquel-36-mg-x-20-comprimidos-5414736044194.html",
    "https://puntomascotas.cl/cicatrizantes/37172-apoquel-54-mg-x-20-comprimidos-5414736044200.html",
    "https://puntomascotas.cl/farmacia-veterinaria/38466-revolution-6-gatos-hasta-75-kg-7804650310136.html",
    "https://puntomascotas.cl/farmacia-veterinaria/38467-revolution-plus-25-a-5-kg-7804650310136.html",
    "https://puntomascotas.cl/acana/35557-acana-heritage-freshwater-fish-21kg-64992502256.html",
    "https://puntomascotas.cl/acana/35555-acana-heritage-free-run-poultry-21-kg-64992501259.html",
    "https://puntomascotas.cl/simparica/38343-simparica-13-a-25-kg-3-comprimidos.html",
    "https://puntomascotas.cl/simparica/38344-simparica-13-a-25-kg-3-comprimidos.html",
    "https://puntomascotas.cl/simparica/38342-simparica-13-a-25-kg-3-comprimidos.html",
    "https://puntomascotas.cl/simparica/38341-simparica-13-a-25-kg-3-comprimidos.html",
    "https://puntomascotas.cl/simparica/38339-simparica-13-a-25-kg-3-comprimidos.html",
    "https://puntomascotas.cl/simparica/38340-simparica-13-a-25-kg-3-comprimidos.html",
    "https://puntomascotas.cl/farmacia-veterinaria/30520-rimadyl-100-mg-60-comprimidos-7804650310884.html",
    "https://puntomascotas.cl/farmacia-veterinaria/32656-rimadyl-100-mg-14-comprimidos-7804650310891.html",
    "https://puntomascotas.cl/farmacia-veterinaria/34139-bravecto-2-a-45-kg-8713184148957.html",
    "https://puntomascotas.cl/farmacia-veterinaria/34141-bravecto-2-a-45-kg-8713184148964.html",
    "https://puntomascotas.cl/farmacia-veterinaria/34140-bravecto-2-a-45-kg-8713184148971.html",
    "https://puntomascotas.cl/farmacia-veterinaria/38964-bravecto-gato-62-a-125-kg-8713184197696.html",
    "https://puntomascotas.cl/farmacia-veterinaria/34136-bravecto-2-a-45-kg-8713184148988.html",
    "https://puntomascotas.cl/farmacia-veterinaria/38415-bravecto-gato-12-a-28-kg-8713184197689.html",
    "https://puntomascotas.cl/calmante-y-control-ansiedad/35481-spray-calming-felino-beaphar-8711231110896.html",
    "https://puntomascotas.cl/golosinas-para-gatos/37002-golosinas-calmantes-felinas-beaphar-8711231110889.html",
    "https://puntomascotas.cl/calmante-y-control-ansiedad/35483-collar-calming-gatos-beaphar-8711231110902.html",
    "https://puntomascotas.cl/calmante-y-control-ansiedad/35480--tabletas-calamantes-gatos-y-perros-8711231171101.html",
    "https://puntomascotas.cl/farmacia-veterinaria/34964-feliway-difusor-repuesto-48-ml-3411112169603.html",
    "https://puntomascotas.cl/farmacia-veterinaria/30767-feliway-spray-3411112133789.html",
    "https://puntomascotas.cl/farmacia-veterinaria/35604-feliway-difusor-repuesto-48-ml-3411112251230.html",
    "https://puntomascotas.cl/farmacia-veterinaria/35602-feliway-friends-kit-inicial-3411112251186.html",
    "https://puntomascotas.cl/farmacia-veterinaria/30773-dermisolona-7800006005268.html",
    "https://puntomascotas.cl/farmacia-veterinaria/34960-adaptil-collar-large-3411112116652.html",
    "https://puntomascotas.cl/farmacia-veterinaria/34959-adaptil-collar-large-3411112116676.html",
    "https://puntomascotas.cl/farmacia-veterinaria/34200-shampoo-allercalm-7502010422627.html",
    "https://puntomascotas.cl/perros-necesidades-especificas"

]

    
tipo2 = []
tipo3 = []


results = []

#Tipo 1

for url in tipo1:

    driver.get(url)
    try:
        nombresku = driver.find_element("xpath", '/html/body/main/section/div/div/div/div/div/section/div[1]/div[1]/div[2]/section/h1') #CAMBIAR
        precio = driver.find_element("xpath", '/html/body/main/section/div/div/div/div/div/section/div[1]/div[1]/div[2]/section/div[1]/div/div[5]/div/form/div[2]/div[1]/span[1]/span[1]')#CAMBIAR
        
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

      
