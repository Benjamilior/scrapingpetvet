from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Configurar las opciones de Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")  # Ejecutar Chrome en modo headless (sin interfaz gráfica)
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument("--timeout=30")  # Cambia 30 por el valor de tiempo de espera deseado en segundos


# Ruta al archivo chromedriver (ajústala según tu ubicación)
chromedriver_path = "/usr/local/bin/chromedriver"

# Crear una instancia del controlador Chrome
driver = webdriver.Chrome(executable_path=chromedriver_path, options=chrome_options)

# URL a la página web que deseas visitar
url = "https://masmetrics.com/reportes/"
driver.get(url)

# Obtener el título de la página
titulo_pagina = driver.title
print("Título de la página:", titulo_pagina)

# Cerrar el navegador
driver.quit()
