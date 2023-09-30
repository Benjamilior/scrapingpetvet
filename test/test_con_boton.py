#Codigo para sacar el precio de producto donde la pagina tiene Boton
import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By





#Ejecutador del Codigo

# PATH = "C:\\Program Files (x86)\\chromedriver.exe"
PATH = "/Users/benjammunoz/Desktop/Dotu/chromedriver.exe"

# Configurar las opciones de Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")  # Ver el Navegador
chrome_options.add_argument("--window-size=1920x1080")

start_time = time.time()  # Tiempo de inicio de la ejecución

driver = webdriver.Chrome(options=chrome_options)

#URLs


urls = [
    
    "https://www.amigales.cl/snacks-calmantes-gatos.html",
    "https://www.amigales.cl/collar-calmante-gatos.html",
    "https://www.amigales.cl/tabletas-calmantes-beaphar.html",
    "https://www.amigales.cl/feliway-classic-repuesto.html",
    "https://www.amigales.cl/feliway-classic-spray.html",
    "https://www.amigales.cl/feliway-friends-repuesto.html",
    "https://www.amigales.cl/feliway-classic-difusor-repuesto.html",
    "https://www.amigales.cl/feliway-friends-difusor-repuesto.html",
    "https://www.amigales.cl/biljac-adultselect-perros.html",
    "https://www.amigales.cl/alimento-bil-jac-puppy-select-cachorros.html",
    "https://www.amigales.cl/brit-care-cordero-arroz-senior.html",
    "https://www.amigales.cl/brit-care-cordero-arroz-perro-raza-pequena.html",
    "https://www.amigales.cl/brit-care-cordero-perros-raza-mediana.html",
    "https://www.amigales.cl/brit-care-cordero-hipoalergenico-cachorros.html",
    "https://www.amigales.cl/brit-care-conejo-hipoalergenico-perros-sobrepeso.html",
    "https://www.amigales.cl/brit-cachorros-salmon-papas.html",
    "https://www.amigales.cl/brit-care-salmon-light-grain-free-perros-senior.html",
    "https://www.amigales.cl/catalog/product/view/id/5199/s/mixantip-plus-crema/category/2/",
    "https://www.amigales.cl/oven-baked-pollo-perros-11-34-kg.html",
    "https://www.amigales.cl/oven-baked-pescado-perros-11-34-kg.html",
    "https://www.amigales.cl/oven-baked-pollo-perros-senior-11-34-kg.html",
    "https://www.amigales.cl/beaphar-laveta-carnitina.html",
    "https://www.amigales.cl/beaphar-laveta-taurina.html",
    "https://www.amigales.cl/florafix-15g.html",
    "https://www.amigales.cl/silimavet-silimarina-vitanimal.html",
    "https://www.amigales.cl/naxpet-solucion-oral.html",
    "https://www.amigales.cl/oxtrin.html",
    "https://www.amigales.cl/synulox-250mg.html",
    "https://www.amigales.cl/calmer-calma.html",
    "https://www.amigales.cl/artri-tabs-60-tabletas.html",
    "https://www.amigales.cl/condrovet-30-comprimidos.html",
    "https://www.amigales.cl/arena-sanitaria-america-litter-ultra-odor-seal.html",
    "https://www.amigales.cl/hills-metabolic-perros.html", 
    "https://www.amigales.cl/wanpy-jerky-cordero.html",
    "https://www.amigales.cl/itraskin-suspension-oral.html",
    "https://www.amigales.cl/hills-small-paws-cachorros.html", 
    "https://www.amigales.cl/sucravet.html",
    "https://www.amigales.cl/dermisolona-30-ml-solucion-oral.html",
    "https://www.amigales.cl/ursovet-drag-pharma.html",
    "https://www.amigales.cl/adaptil-difusor-repuesto.html",
    "https://www.amigales.cl/ohm-comprimidos-calmantes-perros-gatos.html",
    "https://www.amigales.cl/dermisolona-20mg-10-comprimidos.html",
    "https://www.amigales.cl/collar-adaptil.html",
    "https://www.amigales.cl/virbac-allercalm-shampoo.html",
    "https://www.amigales.cl/hills-rd-perros.html", 
    "https://www.amigales.cl/phisio-anti-olor-auricular.html"
]

results = []

# driver.get("https://www.amigales.cl/condrovet-30-comprimidos.html")

for url in urls:

    driver.get(url)
    try:
        nombresku = driver.find_element("xpath", '/html/body/div[2]/main/div[3]/div/div[1]/div[1]/h1/span')
        precio = driver.find_element("xpath", '/html/body/div[2]/main/div[3]/div/div[1]/div[4]/div[1]/span/span/span')
        


        print(nombresku.text + " " + precio.text)
        data = {
                "Nombre SKU": nombresku.text,
                "Precio": precio.text
            }

            # Add the dictionary to the results list
        results.append(data)

    except Exception as e:
        print(f"Error en la URL: {url} - {e}")


    
driver.quit()


# Save the results to a JSON file

with open("scraped_data.json", "w") as f:
    json.dump(results, f, indent=4)

end_time = time.time()  # Tiempo de finalización de la ejecución

execution_time = end_time - start_time

print("Tiempo de ejecución: %.2f segundos" % execution_time)

      



