import json

def load_data(file_path):
    """Load a JSON file."""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


animals_data = load_data("animals_data.json")

for animal_data in animals_data:
    if "name" in animal_data:
        print(f'Name: {animal_data["name"]}')

    if "diet" in animal_data["characteristics"]:
        print(f'Diet: {animal_data["characteristics"]["diet"]}')

    if "locations" in animal_data and animal_data["locations"]:
        print(f'Location: {animal_data["locations"][0]}')

    if "type" in animal_data["characteristics"]:
        print(f'Type: {animal_data["characteristics"]["type"]}')

    print()