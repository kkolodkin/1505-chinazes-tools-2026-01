import requests

BASE_URL = "https://restcountries.com"
COUNTRY_NAME = "France"
TOKEN = "rc_live_demo"

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/json"
}

try:
    response = requests.get(f"{BASE_URL}/{COUNTRY_NAME}", headers=headers)
    
    if response.status_code == 200:
        country_data = response.json()[0]
        
        print(f"Официальное название: {country_data['name']['official']}")
        print(f"Столица: {', '.join(country_data['capital'])}")
        print(f"Регион: {country_data['region']}")
        print(f"Население: {country_data['population']:,} чел.")
        print(f"Флаг (ссылка): {country_data['flags']['png']}")
    else:
        print(f"Ошибка при получении данных: Код {response.status_code}")

except Exception as e:
    print(f"Произошла ошибка при подключении: {e}")
