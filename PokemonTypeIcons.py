import requests
import os

# Liste des types de Pokémon en anglais
types_pokemon_english = ["Normal", "Fire", "Water", "Grass", "Electric", "Ice", 
                         "Fighting", "Poison", "Ground", "Flying", "Psychic", 
                         "Bug", "Rock", "Ghost", "Dragon", "Dark", "Steel", "Fairy"]

# Liste des noms correspondants en français
types_pokemon_french = ["Normal", "Feu", "Eau", "Plante", "Électrik", "Glace", 
                        "Combat", "Poison", "Sol", "Vol", "Psy", "Insecte", 
                        "Roche", "Spectre", "Dragon", "Ténèbres", "Acier", "Fée"]

# Base URL pour les icônes des types de Pokémon
base_url = "https://raw.githubusercontent.com/partywhale/pokemon-type-icons/main/icons/"

# Dossier de destination pour sauvegarder les icônes
destination_folder = "Icons"

# Créer le dossier s'il n'existe pas
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Télécharger chaque icône pour chaque type de Pokémon en anglais et les renommer en français
for type_eng, type_fr in zip(types_pokemon_english, types_pokemon_french):
    # Construire l'URL pour le type de Pokémon en anglais
    type_url = f"{base_url}{type_eng.lower()}.svg"
    
    # Nom du fichier pour sauvegarder l'icône (en utilisant le nom français)
    filename = os.path.join(destination_folder, f"{type_fr.lower()}.svg")
    
    # Télécharger l'icône du type de Pokémon
    response = requests.get(type_url)
    
    try:
        with open(filename, 'wb') as file:
            file.write(response.content)
        print(f"Téléchargé: {filename}")
    except Exception as e:
        print(f"Échec du téléchargement de {filename}. Erreur: {e}")

print("Téléchargement terminé!")
