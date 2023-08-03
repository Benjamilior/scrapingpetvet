from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import json
import pandas as pd


sku = {
        'option-label-acana_wildcoast_perros-906-item-2334': 'petdotu101',
        'option-label-acana_wildcoast_perros-906-item-2335': 'petdotu102',
        'option-label-acana_wildcoast_perros-906-item-2336': 'petdotu7'
}

start_time = time.time()  # Tiempo de inicio de la ejecución

def scrape_website_data(url_def,direccioness):
    # Configurar las opciones de Chrome
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Ver el Navegador
    chrome_options.add_argument("--window-size=1920x1080")

    driver = webdriver.Chrome(options=chrome_options)

    resultados = []


    for url_def in direcciones:
        driver.get(url)
        boton = driver.find_element(By.ID, url_def)
        boton.click()

        nombresku = driver.find_element("xpath", '/html/body/div[2]/main/div[3]/div/div[1]/div[1]/h1/span')
        precio = driver.find_element("xpath", '/html/body/div[2]/main/div[3]/div/div[1]/div[4]/div[1]/span/span/span[2]/span')
        tipoalimento = driver.find_element(By.ID, url_def)

        sku_propuesto = sku.get(url_def, 'SKU Desconocido')
        resultado_dict = {
            'sku': sku_propuesto,
            'nombre': nombresku.text,
            'tipo_alimento': tipoalimento.text,
            'precio': precio.text
        }
        resultados.append(resultado_dict)

    #Quitar el Driver de Chrome
    driver.quit()

    #Exportando Datos en JSON
    with open("scraped_data01.json", "w") as f:
        json.dump(resultados, f, indent=4)

    # Crear un DataFrame desde la lista de resultados
    df_resultados = pd.DataFrame(resultados)

    # Exportar el DataFrame a un archivo Excel
    df_resultados.to_excel("scraped_data01.xlsx", index=False)


    return resultados

#Ejecutar la función con la lista de URLs a procesar
# url_list = ['https://www.amigales.cl/acana-wild-coast-perros.html']


#Acana Wild Coast Perro
url = 'https://www.amigales.cl/acana-wild-coast-perros.html'

direcciones = ['option-label-acana_wildcoast_perros-906-item-2334',
'option-label-acana_wildcoast_perros-906-item-2335',
'option-label-acana_wildcoast_perros-906-item-2336']


scraped_data = scrape_website_data ("https://www.amigales.cl/acana-wild-coast-perros.html", direcciones)
print(scraped_data)


# Calcula el tiempo de Ejecucion
end_time = time.time()
execution_time = end_time - start_time
print("Tiempo de ejecución: %.2f segundos" % execution_time)