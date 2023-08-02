from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
import json


#Ejecutador del Codigo

PATH = "C:\\Program Files (x86)\\chromedriver.exe"

# Configurar las opciones de Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")  # Ver el Navegador
chrome_options.add_argument("--window-size=1920x1080")

start_time = time.time()  # Tiempo de inicio de la ejecución

driver = webdriver.Chrome(options=chrome_options)

#URLsx
# https://www.amigales.cl/revolution-plus-antiparasitario-gatos.html
# https://www.amigales.cl/acana-prairie-poultry-perros.html
# https://www.amigales.cl/acana-wild-coast-perros.html

url = "https://www.amigales.cl/acana-wild-coast-perros.html"
driver.get(url)

#XPATH ID cambiante para apretar boton y sacar texto

urls = ['option-label-acana_wildcoast_perros-906-item-2334',
'option-label-acana_wildcoast_perros-906-item-2335',
'option-label-acana_wildcoast_perros-906-item-2336']

#Apretar Boton#

for url in urls:
    lista = []
    boton = driver.find_element(By.ID,url)
    boton.click()
    time.sleep(5)
    #Seleccionar todos los Xpath Extradiables#
    nombresku = driver.find_element("xpath", '/html/body/div[2]/main/div[3]/div/div[1]/div[1]/h1/span')
    precio = driver.find_element("xpath", '/html/body/div[2]/main/div[3]/div/div[1]/div[4]/div[1]/span/span/span[2]/span') #Este XPATH debe ser siempre igual
    tipoalimento = driver.find_element(By.ID, url) #ESTE HAY QUE ENCONTRAR SIEMPRE
    print(nombresku.text + " " + tipoalimento.text + " " + precio.text)
    lista.extend([nombresku.text])
    print(lista)


driver.quit()


# Calcula el tiempo de Ejecucion

end_time = time.time()  

execution_time = end_time - start_time

print("Tiempo de ejecución: %.2f segundos" % execution_time)




