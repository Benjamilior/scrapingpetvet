from google.oauth2 import service_account
from googleapiclient.discovery import build
import datetime
import pandas as pd

# Autenticación y construcción del servicio de la API

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
KEY = 'key.json'

SPREADSHEET_ID = '1PrHE2FBeBhQnVYeCLQclLqj_tiIOq7z3JuMAG-2aAXg'

# Cargar credenciales de servicio
creds = service_account.Credentials.from_service_account_file(KEY, scopes=SCOPES)

# Construir el servicio
service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()

# Definir los rangos que deseas obtener
ranges = ['Verificador!B2:B207', 'Verificador!BZ2:CA207']

# Lista para almacenar los resultados de cada rango
all_values = []

# Realizar la solicitud para obtener los valores de cada rango
for range_name in ranges:
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=range_name).execute()
    values = result.get('values', [])
    all_values.append(values)

# Verificar y mostrar los resultados
for i, values in enumerate(all_values):
    if not values:
        print(f'No se encontraron datos en el rango {ranges[i]}.')
    else:
        print(f'Datos del rango {ranges[i]}:')
        for row in values:
            print(row)
            
# Fecha de Extracción
now = datetime.datetime.now()
now_str = now.strftime('%Y-%m-%d %H:%M:%S')

# Convertir los datos obtenidos a un DataFrame de pandas
# Convertir la lista de listas a un DataFrame
data = [item for sublist in all_values for item in sublist]
df = pd.DataFrame(data)

# Mostrar el DataFrame para verificación
print(df)

# Escribir los datos en otra hoja de Google Sheets
# Preparar los datos como una lista de listas para la API de Google Sheets
data_to_write = [[now_str] + row for row in df.values.tolist()]

NEW_SPREADSHEET_ID = '1lLfl_jSGUEtitfsezo_zz53Bn2zAzID73VtxIi4dKRo'

# Obtener la última fila con datos en la nueva hoja
result = sheet.values().get(spreadsheetId=NEW_SPREADSHEET_ID, range='Estado!A:A').execute()
values = result.get('values', [])
last_row = len(values) + 1

# Insertar los resultados en la nueva hoja después de la última fila
update_range = f'Estado!A{last_row}:E{last_row + len(data_to_write) - 1}'
result = sheet.values().update(
    spreadsheetId=NEW_SPREADSHEET_ID,
    range=update_range,
    valueInputOption='USER_ENTERED',
    body={'values': data_to_write}
).execute()

print('Datos actualizados en la hoja de cálculo.')
