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

url = ["https://www.centralvet.cl/alimentos/23807-23083-brit-care-gato-esterilizado-urinary-health-pollo-fresco-.html#/1111111131-peso-2_kg"]


#XPATH ID cambiante para apretar boton y sacar texto

direcciones = ["/html/body/main/section/div[2]/div/section/div[2]/div[1]/div[2]/div[2]/div[2]/form/div[1]/div/ul/li[1]/input",
               "/html/body/main/section/div[2]/div/section/div[2]/div[1]/div[2]/div[2]/div[2]/form/div[1]/div/ul/li[2]/input"]




#Diccion donde se guardan los resultados
resultados=[]


#Apretar los 3 botones y sacar la info de cada uno en una URL
for i in direcciones:
    for a in url:
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
        resultados.append(resultado_dict)

print(resultados)

end_time = time.time()  # Tiempo de finalización de la ejecución

execution_time = end_time - start_time

print(execution_time)

#Quitar el Driver de Chrome
driver.quit()









