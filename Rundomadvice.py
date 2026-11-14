import requests

def get_random_advice():
    url = "https://api.adviceslip.com/advice"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        advice = data.get("slip", {}).get("advice", "Совет не найден")
        return advice
    except requests.exceptions.RequestException as e:
        return f"Ошибка при запросе к API: {e}"

def main():
    print("Случайный совет дня:")
    print(get_random_advice())
if __name__ == "__main__":
    main()
