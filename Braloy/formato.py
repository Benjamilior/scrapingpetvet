import pandas as pd
import json

# Ruta al archivo Excel y nombre de la hoja específica
archivo_excel = 'Book1.xlsx'
nombre_hoja = 'Sheet1'#CAMBIAR

# Leer el archivo Excel y convertirlo en un diccionario
try:
    datos_excel = pd.read_excel(archivo_excel, sheet_name=nombre_hoja)
    diccionario_resultante = dict(zip(datos_excel['SKU'], datos_excel['Braloy']))#CAMBIAR
    print("Datos del archivo Excel convertidos a diccionario:")
    print(diccionario_resultante)

    # Guardar el diccionario en un archivo JSON
    ruta_archivo_json = 'resultadosanta.json'#CAMBIAR
    with open(ruta_archivo_json, 'w') as archivo_json:
        json.dump(diccionario_resultante, archivo_json)
        print(f"Diccionario guardado en '{ruta_archivo_json}'.")

except FileNotFoundError:
    print(f"No se encontró el archivo '{archivo_excel}'. Por favor, verifica la ruta y el nombre del archivo.")
except Exception as e:
    print(f"Ocurrió un error: {e}")
