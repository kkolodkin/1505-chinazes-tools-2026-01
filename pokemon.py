
import random
import requests


def run():
    pokemon_id = random.randint(1, 1025)
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        name = data["name"]
        types = ", ".join(
            item["type"]["name"] for item in data["types"]
        )

        height = data["height"] / 10
        weight = data["weight"] / 10
        hp = data["stats"][0]["base_stat"]

        print("=== Who's That Pokémon? ===")
        print(f"Type: {types}")
        print(f"Height: {height} m")
        print(f"Weight: {weight} kg")
        print(f"HP: {hp}")

        answer = input("\nYour answer: ").strip().lower()

        if answer == name:
            print(f"Correct! It's {name.title()}!")
        else:
            print(f"Wrong! It was {name.title()}.")

    except requests.RequestException as error:
        print(f"API error: {error}")
