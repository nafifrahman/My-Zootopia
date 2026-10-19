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


def serialize_animal(animal_obj):
    """Convert one animal dictionary into an HTML card."""
    output = '<li class="cards__item">\n'
    output += f'  <div class="card__title">{animal_obj["name"]}</div>\n'
    output += '  <p class="card__text">\n'

    characteristics = animal_obj["characteristics"]

    if "diet" in characteristics:
        output += f'    <strong>Diet:</strong> {characteristics["diet"]}<br/>\n'

    if "locations" in animal_obj and animal_obj["locations"]:
        output += f'    <strong>Location:</strong> {animal_obj["locations"][0]}<br/>\n'

    if "type" in characteristics:
        output += f'    <strong>Type:</strong> {characteristics["type"]}<br/>\n'

    output += "  </p>\n"
    output += "</li>\n"

    return output


def main():
    animals_data = load_data("animals_data.json")
    template = read_template("animals_template.html")

    output = ""

    for animal_data in animals_data:
        output += serialize_animal(animal_data)

    final_html = template.replace("__REPLACE_ANIMALS_INFO__", output)

    write_html("animals.html", final_html)


if __name__ == "__main__":
    main()