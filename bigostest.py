import requests

payload = { 'api_key': 'f4347ae0e3007dc00754faa32b2889ed', 'url': 'https://www.tusmascotas.cl/product/adaptil-collar-m-l/', 'autoparse': True, 'country_code': 'us', 'device_type': 'desktop' }
r = requests.get('https://api.scraperapi.com/', params=payload)
print(r.text)
