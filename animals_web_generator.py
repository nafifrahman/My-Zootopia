import json


def load_data(file_path):
    """Load a JSON file."""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def read_template(file_path):
    """Read an HTML template file."""
    with open(file_path, "r", encoding="utf-8") as handle:
        return handle.read()


def write_html(file_path, content):
    """Write content into an HTML file."""
    with open(file_path, "w", encoding="utf-8") as handle:
        handle.write(content)


animals_data = load_data("animals_data.json")
template = read_template("animals_template.html")

output = ""

for animal_data in animals_data:
    if "name" in animal_data:
        output += f'Name: {animal_data["name"]}\n'

    if "diet" in animal_data["characteristics"]:
        output += f'Diet: {animal_data["characteristics"]["diet"]}\n'

    if "locations" in animal_data and animal_data["locations"]:
        output += f'Location: {animal_data["locations"][0]}\n'

    if "type" in animal_data["characteristics"]:
        output += f'Type: {animal_data["characteristics"]["type"]}\n'

    output += "\n"

final_html = template.replace("__REPLACE_ANIMALS_INFO__", output)

write_html("animals.html", final_html)