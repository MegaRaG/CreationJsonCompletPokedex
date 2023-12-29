import requests
import pandas as pd
import json

# Récupération des données de l'API
url = "https://tyradex.vercel.app/api/v1/pokemon"
response = requests.get(url)
data = response.json()

# Liste pour stocker les données transformées
transformed_data = []

# Parcourir chaque élément dans les données récupérées
for item in data:
    # Vérifier si "types" est une liste
    if isinstance(item["types"], list):
        # Vérifier si "evolution" est non nul
        if item["evolution"] is not None:
            transformed_item = {
                "id": item["pokedexId"],
                "name": item["name"]["fr"],
                "type": [type_item["name"] for type_item in item["types"]],
                "description": item["category"],
                "image_url": item["sprites"]["regular"],
                "evolutions": {
                    "before": [evolution["pokedexId"] for evolution in item["evolution"]["pre"]] if item["evolution"].get("pre") is not None else [],
                    "after": [evolution["pokedexId"] for evolution in item["evolution"]["next"]] if item["evolution"].get("next") is not None else []
                }
            }
        else:
            # Si "evolution" est None, traiter ou ignorer cet élément selon votre choix
            print(f"Warning: 'evolution' for pokedexId {item['pokedexId']} is None.")
            continue
    else:
        # Si "types" n'est pas une liste, vous pouvez décider de gérer cela d'une manière qui vous convient.
        print(f"Warning: 'types' for pokedexId {item['pokedexId']} is not a list.")
        continue  # Ceci saute à l'itération suivante dans la boucle
    
    transformed_data.append(transformed_item)

# Convertir la liste transformée en un DataFrame
df = pd.DataFrame(transformed_data)

# Enregistrement des données transformées au format JSON
df.to_json("pokemon_transformed.json", orient="records")
