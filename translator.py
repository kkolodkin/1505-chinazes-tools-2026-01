import requests
text = input("Введите текст на английском языке (до 200 символов): ")
if not text or len(text) > 200:
    print("Ошибка, текст пустой или превышает 200 символов.")
else:
    url = "https://api.mymemory.translated.net/get"
    params = {"q": text,  "langpair": "en|ru"}
    try:
        data = requests.get(url, params=params, timeout=10).json()
        print(data["responseData"]["translatedText"])
    except Exception:
        print("Произошла ошибка при выполнении запроса или переводе.")
