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


#BOTON#

boton = driver.find_element(By.ID, 'option-label-acana_wildcoast_perros-906-item-2334') # ESTE DEBE ITERAR POR CADA OCASION
# botones = driver.find_elements_by_class_name("swatch-option.text")
botones = driver.find_element(By.CSS_SELECTOR, ".swatch-option.text")


botones.click()

# boton.click()
# time.sleep(5)

#Seleccionar todos los Xpath Extradiables#
# nombresku = driver.find_element("xpath", '/html/body/div[2]/main/div[3]/div/div[1]/div[1]/h1/span')
# precio = driver.find_element("xpath", '/html/body/div[2]/main/div[3]/div/div[1]/div[4]/div[1]/span/span/span[2]/span')
# tipoalimento = driver.find_element(By.ID, 'option-label-acana_wildcoast_perros-906-item-2334') #ESTE HAY QUE ENCONTRAR SIEMPRE

informacion_boton1 = botones[0].get_attribute("aria-label")
print(informacion_boton1)


# print(nombresku.text + " " + tipoalimento.text + " " + precio.text)


driver.quit()


# Calcula el tiempo de Ejecucion

end_time = time.time()  

execution_time = end_time - start_time

print("Tiempo de ejecución: %.2f segundos" % execution_time)





