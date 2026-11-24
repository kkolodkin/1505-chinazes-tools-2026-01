import requests
def run(): 
    response = requests.get(
        "https://api.restcountries.com/countries/v5/names.common/Canada",
        headers={"Authorization": "Bearer rc_live_demo"},
        timeout=10,
    )

    country = response.json()["data"]["objects"][0]

    print("Название:", country["names"]["common"])
    print("Официальное название:", country["names"]["official"])
    print("Столица:", country["capitals"][0]["name"])
    print("Регион:", country["region"])
    print("Население:", country["population"])
    print("Площадь, км²:", country["area"]["kilometers"])
    print("Валюта:", country["currencies"][0]["name"])
    print("Языки:", ", ".join(lang["name"] for lang in country["languages"]))
