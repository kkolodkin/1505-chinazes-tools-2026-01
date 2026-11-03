
import requests


def run():
    url = "https://uselessfacts.jsph.pl/api/v2/facts/random?language=en"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        if data.get("error"):
            print("Не удалось получить шутку.")
            return
            
        print(data["text"])
        
    except requests.RequestException as error:
        print(f"Ошибка при запросе к API: {error}")
    except (ValueError, KeyError) as error:
        print(f"Ошибка при обработке ответа: {error}")
