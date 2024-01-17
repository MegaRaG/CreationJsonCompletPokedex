import requests

url = "https://tyradex.vercel.app/api/v1/pokemon"
response = requests.get(url)
data = response.json()

pokemon_names = []

for item in data:
    if "name" in item and isinstance(item["name"], str):
        pokemon_names.append(item["name"])
    else:
        print(f"Warning: 'name' for pokedexId {item.get('pokedexId')} is missing or not a string.")

with open("pokemon_names.txt", "w", encoding="utf-8") as f:
    for name in pokemon_names:
        f.write(name + "\n")

print("Noms des Pokémon enregistrés dans pokemon_names.txt")
