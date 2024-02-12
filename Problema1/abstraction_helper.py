"""Módulo de archivos tipo JSON."""
import json


def load_json_file(filename):
    """Función que carga un archivo JSON."""
    try:
        with open(filename, 'r', encoding="UTF-8") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Error: Archivo '{filename}' no encontrado.")
        return {}
    except json.JSONDecodeError:
        print(f"Error: Formato JSON inválido en archivo '{filename}'.")
        return {}
