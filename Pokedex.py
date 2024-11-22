import requests
import os
import json
import csv
from PIL import Image
from io import BytesIO


def get_pokemon_data(pokemon_identifier):
    """
    Realiza una petición a la PokeAPI para obtener los datos de un Pokémon.
    
    Args:
        pokemon_identifier (str|int): Nombre o ID del Pokémon.
    
    Returns:
        dict: Datos del Pokémon en formato JSON si existe.
        None: Si el Pokémon no se encuentra o hay un error en la API.
    """
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_identifier}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 404:
            print(f"Pokémon '{pokemon_identifier}' no encontrado. Verifica el nombre o ID.")
        else:
            print(f"Error HTTP: {http_err}")
    except requests.exceptions.RequestException as err:
        print(f"Error al realizar la petición: {err}")
    return None


def display_pokemon_data(data):
    """
    Muestra la información relevante de un Pokémon.
    
    Args:
        data (dict): Datos del Pokémon en formato JSON.
    """
    print(f"\nNombre: {data['name'].capitalize()}")
    print(f"Peso: {data['weight']} hectogramos")
    print(f"Tamaño: {data['height']} decímetros")
    
    print("\nHabilidades:")
    for ability in data['abilities'][:2]:
        print(f" - {ability['ability']['name']}")
    
    print("\nMovimientos:")
    for move in data['moves'][:5]:  # Muestra solo 5 movimientos para simplicidad
        print(f" - {move['move']['name']}")
    
    print("\nTipos:")
    for poke_type in data['types']:
        print(f" - {poke_type['type']['name']}")
    
    print("\nImagen del Pokémon:")
    print(data['sprites']['front_default'])  # URL de la imagen
    show_image(data['sprites']['front_default'])


def show_image(image_url):
    """
    Descarga y muestra una imagen desde una URL.
    
    Args:
        image_url (str): URL de la imagen a mostrar.
    """
    try:
        response = requests.get(image_url)
        response.raise_for_status()
        img = Image.open(BytesIO(response.content))
        img.show()  # Abre la imagen en el visor predeterminado
    except Exception as e:
        print(f"No se pudo cargar la imagen: {e}")


def save_pokemon_data(pokemon_name, data):
    """
    Guarda los datos del Pokémon en un archivo JSON dentro de la carpeta 'pokedex'.
    
    Args:
        pokemon_name (str): Nombre del Pokémon.
        data (dict): Datos del Pokémon en formato JSON.
    """
    os.makedirs("pokedex", exist_ok=True)  # Crea la carpeta si no existe
    file_path = f"pokedex/{pokemon_name.lower()}.json"

    with open(file_path, "w") as json_file:
        json.dump(data, json_file, indent=4)
    print(f"\nDatos guardados en {file_path}")


def save_to_history(identifier, data):
    """
    Guarda las consultas de Pokémon en un archivo CSV.
    
    Args:
        identifier (str|int): Nombre o ID del Pokémon consultado.
        data (dict): Datos del Pokémon consultado.
    """
    file_exists = os.path.isfile("history.csv")
    with open("history.csv", "a", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["identifier", "name", "weight", "height", "types"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        if not file_exists:
            writer.writeheader()  # Escribir encabezado si el archivo no existe
        
        types = ", ".join([t["type"]["name"] for t in data["types"]])
        writer.writerow({
            "identifier": identifier,
            "name": data["name"],
            "weight": data["weight"],
            "height": data["height"],
            "types": types,
        })
    print("Consulta registrada en el historial (history.csv).")


def main():
    """
    Punto de entrada principal del programa.
    Permite al usuario buscar información sobre un Pokémon por nombre o ID.
    """
    print("¡Bienvenido a la Pokédex!")
    while True:
        identifier = input("\nIntroduce el nombre o ID del Pokémon (o escribe 'salir' para terminar): ").strip()
        
        if identifier.lower() == "salir":
            print("¡Gracias por usar la Pokédex! Hasta la próxima.")
            break
        
        if not identifier.isalnum():  # Validación básica de entrada
            print("Por favor ingresa un nombre o ID válido.")
            continue
        
        data = get_pokemon_data(identifier)
        if data:
            display_pokemon_data(data)
            save_pokemon_data(data["name"], data)
            save_to_history(identifier, data)


if __name__ == "__main__":
    main()
