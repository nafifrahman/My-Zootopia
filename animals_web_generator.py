import json
import html


def load_data(file_path):
    """Load a JSON file and return Python data."""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def read_template(file_path):
    """Read and return the HTML template."""
    with open(file_path, "r", encoding="utf-8") as handle:
        return handle.read()


def write_html(file_path, content):
    """Write the final HTML content to a file."""
    with open(file_path, "w", encoding="utf-8") as handle:
        handle.write(content)


def serialize_animal(animal_obj):
    name = html.escape(animal_obj.get("name", "Unknown"))
    characteristics = animal_obj.get("characteristics", {})
    locations = animal_obj.get("locations", [])

    output = '<li class="cards__item">\n'
    output += f'  <div class="card__title">{name}</div>\n'
    output += '  <div class="card__text">\n'
    output += '    <ul class="animal-details">\n'

    if "diet" in characteristics:
        output += f'      <li class="animal-details__item"><strong>Diet:</strong> {html.escape(characteristics["diet"])}</li>\n'

    if locations:
        output += f'      <li class="animal-details__item"><strong>Location:</strong> {html.escape(locations[0])}</li>\n'

    if "type" in characteristics:
        output += f'      <li class="animal-details__item"><strong>Type:</strong> {html.escape(characteristics["type"])}</li>\n'

    if "skin_type" in characteristics:
        output += f'      <li class="animal-details__item"><strong>Skin type:</strong> {html.escape(characteristics["skin_type"])}</li>\n'

    output += '    </ul>\n'
    output += '  </div>\n'
    output += '</li>\n'
    return output


def serialize_animals(animals_data):
    """Convert all animals into one HTML string."""
    output = ""

    for animal_obj in animals_data:
        output += serialize_animal(animal_obj)

    return output


def main():
    animals_data = load_data("animals_data.json")
    template = read_template("animals_template.html")
    animals_html = serialize_animals(animals_data)
    final_html = template.replace("__REPLACE_ANIMALS_INFO__", animals_html)
    write_html("animals.html", final_html)
    print("animals.html was created successfully.")


if __name__ == "__main__":
    main()