import requests
import json

data = [
    {
        "sku": "petdotu1",
        "tienda": "Central Vet",
        "price": 47150.0,
        "stock": 1
    },
    {
        "sku": "petdotu2",
        "tienda": "Central Vet",
        "price": 39900.0,
        "stock": 0
    }
    
]

# URL de la API
api_url = "https://dotupetpublic-production.up.railway.app/bulk_update_prices"

# Enviar el JSON a la API
response = requests.put(api_url, json=data)

# Verificar la respuesta
if response.status_code == 200:
    print("Datos enviados exitosamente.")
    print(response.json())  # Muestra la respuesta de la API si es JSON
else:
    print(f"Error al enviar datos: {response.status_code} - {response.text}")


