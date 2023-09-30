from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import json
import pandas as pd
import os


sku = {
        'option-label-acana_wildcoast_perros-906-item-2334': 'petdotu101',
        'option-label-acana_wildcoast_perros-906-item-2335': 'petdotu102',
        'option-label-acana_wildcoast_perros-906-item-2336': 'petdotu7',
        "option-label-apoquel_zoetis_contenido-785-item-1983":"petdotu2",
        "option-label-apoquel_zoetis_contenido-785-item-1984":"petdotu3",
        "option-label-apoquel_zoetis_contenido-785-item-1985":"petdotu4"
}

start_time = time.time()  # Tiempo de inicio de la ejecución

def scrape_website_data(url_def,direcciones_def):
    # Configurar las opciones de Chrome
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Ver el Navegador
    chrome_options.add_argument("--window-size=1920x1080")

    driver = webdriver.Chrome(options=chrome_options)

    resultados = []

    driver.get(url_def) #ojo aca habian problemas

    for url_def in direcciones_def:
       
        boton = driver.find_element(By.ID, url_def)
        boton.click()

        nombresku = driver.find_element("xpath", '/html/body/div[2]/main/div[3]/div/div[1]/div[1]/h1/span')
        precio = driver.find_element("xpath", '/html/body/div[2]/main/div[3]/div/div[1]/div[4]/div[1]/span/span/span[2]/span')
        tipoalimento = driver.find_element(By.ID, url_def)

        sku_propuesto = sku.get(url_def, 'SKU Desconocido') #para buscar el sku correspondiente
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
    # with open("scraped_data01.json", "w") as f:
    #     json.dump(resultados, f, indent=4)

    return resultados

#Ejecutar la función con la lista de URLs a procesar
# url_list = ['https://www.amigales.cl/acana-wild-coast-perros.html']


# Acana Wild Coast Perro#
url = 'https://www.amigales.cl/acana-wild-coast-perros.html'

direcciones = ['option-label-acana_wildcoast_perros-906-item-2334','option-label-acana_wildcoast_perros-906-item-2335','option-label-acana_wildcoast_perros-906-item-2336']

scraped_data = scrape_website_data (url, direcciones)

print(scraped_data)
# Crear un DataFrame desde la lista de resultados
df_resultados = pd.DataFrame(scraped_data)
# Exportar el DataFrame a un archivo Excel
df_resultados.to_excel("scraped_data01.xlsx", index=False)


#Apoquel 
url2 = "https://www.amigales.cl/apoquel-zoetis-20-comprimidos.html"
direcciones2 = ["option-label-apoquel_zoetis_contenido-785-item-1983","option-label-apoquel_zoetis_contenido-785-item-1984","option-label-apoquel_zoetis_contenido-785-item-1985"]
scraped_data2 = scrape_website_data (url2, direcciones2)
# print(scraped_data2)
# Crear un DataFrame desde la lista de resultados
df_resultados = pd.DataFrame(scraped_data2)
# Exportar el DataFrame a un archivo Excel
df_resultados.to_excel("scraped_data02.xlsx", index=False)



# Calcula el tiempo de Ejecucion
end_time = time.time()
execution_time = end_time - start_time
# print("Tiempo de ejecución: %.2f segundos" % execution_time)


