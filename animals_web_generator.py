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
    """Convert one animal dictionary into an HTML card."""
    name = html.escape(animal_obj.get("name", "Unknown"))
    characteristics = animal_obj.get("characteristics", {})
    locations = animal_obj.get("locations", [])

    output = '<li class="cards__item">\n'
    output += f'  <div class="card__title">{name}</div>\n'
    output += '  <p class="card__text">\n'

    if "diet" in characteristics:
        output += f'    <strong>Diet:</strong> {html.escape(characteristics["diet"])}<br/>\n'

    if locations:
        output += f'    <strong>Location:</strong> {html.escape(locations[0])}<br/>\n'

    if "type" in characteristics:
        output += f'    <strong>Type:</strong> {html.escape(characteristics["type"])}<br/>\n'

    if "skin_type" in characteristics:
        output += f'    <strong>Skin type:</strong> {html.escape(characteristics["skin_type"])}<br/>\n'

    if "lifespan" in characteristics:
        output += f'    <strong>Lifespan:</strong> {html.escape(characteristics["lifespan"])}<br/>\n'

    if "top_speed" in characteristics:
        output += f'    <strong>Top speed:</strong> {html.escape(characteristics["top_speed"])}<br/>\n'

    output += '  </p>\n'
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