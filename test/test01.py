from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
import json
import pandas as pd


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

url = "https://www.amigales.cl/acana-wild-coast-perros.html" #petdotu7
driver.get(url)


#XPATH ID cambiante para apretar boton y sacar texto

direcciones = ['option-label-acana_wildcoast_perros-906-item-2334',
'option-label-acana_wildcoast_perros-906-item-2335',
'option-label-acana_wildcoast_perros-906-item-2336']

sku = {'option-label-acana_wildcoast_perros-906-item-2334':'petdotu101',
'option-label-acana_wildcoast_perros-906-item-2335':'petdotu102',
'option-label-acana_wildcoast_perros-906-item-2336': 'petdotu7'}

#Apretar Boton#
resultados=[]


#Apretar los 3 botones y sacar la info de cada uno en una URL
for url in direcciones:
    #Apretar Boton
    boton = driver.find_element(By.ID,url)
    boton.click()
    # time.sleep(5)
    #Seleccionar todos los Xpath Extradiables#
    
    nombresku = driver.find_element("xpath", '/html/body/div[2]/main/div[3]/div/div[1]/div[1]/h1/span')# Puede Cambiar de URL a URL
    precio = driver.find_element("xpath", '/html/body/div[2]/main/div[3]/div/div[1]/div[4]/div[1]/span/span/span[2]/span') #Este XPATH debe ser (IDEALMENTE) siempre igual
    tipoalimento = driver.find_element(By.ID, url) #ESTE HAY QUE ENCONTRAR SIEMPRE
    # print(nombresku.text + " " + tipoalimento.text + " " + precio.text)
    sku_propuesto = sku.get(url, 'SKU Desconocido')  # Obtener el SKU propuesto del diccionario de afuera
    resultado_dict = {
        'sku': sku_propuesto,
        'nombre': nombresku.text,
        'tipo_alimento': tipoalimento.text,
        'precio':precio.text
    }
    resultados.append(resultado_dict)

    
print(resultados)





    
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




