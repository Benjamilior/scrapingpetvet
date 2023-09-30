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

urls = ["https://www.centralvet.cl/farmacia-veterinaria/21003-apoquel-16-mg-zoetis-20-comprimidos-venta-con-receta.html"]

tipo1 = [
    "https://www.centralvet.cl/farmacia-veterinaria/21003-apoquel-16-mg-zoetis-20-comprimidos-venta-con-receta.html",
    "https://www.centralvet.cl/farmacia-veterinaria/21001-apoquel-36mg-zoetis-venta-con-receta.html",
    "https://www.centralvet.cl/farmacia-veterinaria/21002-apoquel-54mg-zoetis-venta-con-receta.html",
    "https://www.centralvet.cl/para-perros/22003-simparica-antiparasitario-perros-entre-5-a-10kg-3-dosis-zoetis.html",
    "https://www.centralvet.cl/para-perros/21810-simparica-antiparasitario-perros-entre-5-a-10-kg-1-dosis-zoetis.html",
    "https://www.centralvet.cl/farmacia-para-perros/6297-rimadyl-100-mg-carprofeno-14-tabletas-anti-inflamatorio-zoetis.html",
    "https://www.centralvet.cl/farmacia-para-perros/7784-bravecto-masticable-contra-pulgasgarrapatas-45-a-10kg.html",
    "https://www.centralvet.cl/farmacia-para-perros/7777-bravecto-masticable-contra-pulgasgarrapatas-2-a-45kg.html",
    "https://www.centralvet.cl/farmacia-para-gatos/21230-calming-home-spray-ambiental-para-gatos-y-perros-125-ml-beaphar.html",
    "https://www.centralvet.cl/farmacia-para-gatos/21232-calming-treats-para-gatos-35g-beaphar.html",
    "https://www.centralvet.cl/farmacia-para-gatos/21229-calming-collar-para-gatos-100-natural-beaphar.html",
    "https://www.centralvet.cl/farmacia-para-gatos/22615-calming-tablets-para-gatos-y-perros-20-tabletas-beaphar.html",
    "https://www.centralvet.cl/repuestos/6890-feliway-classic-repuesto-para-difusor-48-ml.html",
    "https://www.centralvet.cl/bienestar/18610-felifriend-feliway-friends-repuesto-para-difusor-48ml.html",
    "https://www.centralvet.cl/accesorios-y-bienestar/16558-feliway-classic-difusor-electrico-48-ml.html",
    "https://www.centralvet.cl/alimentos-de-prescripcion-veterinaria/4932-royal-canin-hipoalergenico-hypoallergenic-para-perro-2-kg.html",
    "https://www.centralvet.cl/alimentos/5451-21425-royal-canin-mini-adulto.html#/1111111116-peso-25_kg",
    "https://www.centralvet.cl/alimentos/6764-bil-jac-select-small-breed-perros-adultos-27kg.html",
    "https://www.centralvet.cl/perros-senior/23799-brit-care-perro-senior-cordero-y-arroz-12kg.html",
    "https://www.centralvet.cl/productos-para-perros/20784-brit-care-perro-adulto-small-breed-cordero-y-arroz-75kg.html",
    "https://www.centralvet.cl/farmacia-para-perros/6204-mixantip-plus-pomo-15g-tratamientos-dermatologicos.html",
    "https://www.centralvet.cl/farmacia-para-gatos/6335-laveta-taurina-suplemento-vitaminico-para-gatos.html",
    "https://www.centralvet.cl/farmacia-para-perros/21271-florafix-pet-probiotico-para-mascotas-15g.html",
    "https://www.centralvet.cl/farmacia-para-perros/21223-silimarina-vitanimal-caja-30-comprimidos.html",
    "https://www.centralvet.cl/farmacia-para-perros/9810-silimarina-vitanimal-frasco-90-comprimidos.html",
    "https://www.centralvet.cl/farmacia-para-perros/9523-synulox-10-comprimidos-venta-con-receta-zoetis.html",
    "https://www.centralvet.cl/farmacia-veterinaria/22564-calmer-30-ml-spray-ayuda-a-tranquilizar-baja-la-ansiedad-aromvet-aromaterapia.html",
    "https://www.centralvet.cl/farmacia-para-perros/6025-condrovet-condroprotector-para-perros-30-comprimidos.html",
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
    "https://www.centralvet.cl/farmacia-para-gatos/6184-limpiador-oidos-phisio-antiolor-virbac-frasco-100-ml.html1"
]
tipo2 = ["https://www.centralvet.cl/inicio/22462-21454-acana-classic-prairie-poultry-para-perros.html#/1111111133-peso-113_kg",
"https://www.centralvet.cl/alimentos-de-prescripcion-veterinaria/22768-21711-hills-prescription-diet-rd-para-perros-reduccion-del-peso-a-pedido.html#/1111111259-peso-79_kg"]
tipo3 = ["https://www.centralvet.cl/inicio/21072-21305-brit-care-perro-adulto-medium-breed-cordero-y-arroz.html#/1111111130-peso-12_kg",
"https://www.centralvet.cl/alimentos/23807-23083-brit-care-gato-esterilizado-urinary-health-pollo-fresco-.html#/1111111131-peso-2_kg"]


results = []

# driver.get("https://www.amigales.cl/condrovet-30-comprimidos.html")

for url in tipo1:

    driver.get(url)
    try:
        nombresku = driver.find_element("xpath", '/html/body/main/section/div[2]/div/section/div[2]/div[1]/div[2]/div[1]/h1/span') #Cambiar 
        precio = driver.find_element("xpath", '/html/body/main/section/div[2]/div/section/div[2]/div[1]/div[2]/div[1]/div/div[2]/div/span[1]/span')#Cambiar
        
        print(nombresku.text + " " + precio.text)
        data = {
                "Nombre SKU": nombresku.text,
                "Precio": precio.text
            }

            # Add the dictionary to the results list
        results.append(data)

    except Exception as e:
        print(f"Error en la URL {url}: {str(e)}")

#Apretar los 3 botones y sacar la info de cada uno en una URL
for i in direccionestipo2:
    for a in tipo2:
        driver.get(a)  # Cambia la URL para cada botón

        # Apretar el botón correspondiente
        boton = driver.find_element(By.XPATH, i)  # Puedes usar "url" para ubicar el botón si es único en cada página
        boton.click()
        time.sleep(1)

        # Seleccionar todos los Xpath Extradiables
        nombresku = driver.find_element(By.XPATH, '/html/body/main/section/div[2]/div/section/div[2]/div[1]/div[2]/div[1]/h1/span')
        price = driver.find_element_by_class_name('product-price')
        tipoalimento = driver.find_element(By.XPATH, i)

        resultado_dict = {
            'nombre': nombresku.text,
            'tipo_alimento': tipoalimento.text,
            'precio': price.text
        }
        results.append(resultado_dict)

#Apretar 2 botones y sacar la info de cada uno en una URL  
for i in direccionestipo3:
    for a in tipo3:
        driver.get(a)  # Cambia la URL para cada botón

        # Apretar el botón correspondiente
        boton = driver.find_element(By.XPATH, i)  # Puedes usar "url" para ubicar el botón si es único en cada página
        boton.click()
        time.sleep(1)

        # Seleccionar todos los Xpath Extradiables
        nombresku = driver.find_element(By.XPATH, '/html/body/main/section/div[2]/div/section/div[2]/div[1]/div[2]/div[1]/h1/span')
        price = driver.find_element_by_class_name('product-price')
        tipoalimento = driver.find_element(By.XPATH, i)

        resultado_dict = {
            'nombre': nombresku.text,
            'tipo_alimento': tipoalimento.text,
            'precio': price.text
        }
        results.append(resultado_dict)
        

driver.quit()

print(results)
end_time = time.time()  # Tiempo de finalización de la ejecución

execution_time = end_time - start_time

print("Tiempo de ejecución: %.2f segundos" % execution_time)

      
