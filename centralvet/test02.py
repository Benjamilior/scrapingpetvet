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

url = "https://www.centralvet.cl/alimentos-de-prescripcion-veterinaria/22768-21711-hills-prescription-diet-rd-para-perros-reduccion-del-peso-a-pedido.html#/1111111259-peso-79_kg" 
driver.get(url)


#XPATH ID cambiante para apretar boton y sacar texto

direcciones = ["/html/body/main/section/div[2]/div/section/div[2]/div[1]/div[2]/div[2]/div[2]/form/div[1]/div/ul/li[1]/input",
"/html/body/main/section/div[2]/div/section/div[2]/div[1]/div[2]/div[2]/div[2]/form/div[1]/div/ul/li[2]/input",
"/html/body/main/section/div[2]/div/section/div[2]/div[1]/div[2]/div[2]/div[2]/form/div[1]/div/ul/li[3]/input"]

#Apretar Boton#
resultados=[]

# Apretar los 3 botones y sacar la info de cada uno en una URL



end_time = time.time()  # Tiempo de finalización de la ejecución

execution_time = end_time - start_time

#Quitar el Driver de Chrome
driver.quit()






