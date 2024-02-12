"""Módulos de JSONs, generar IDs y un helper para cargar achivos JSON."""
import json
import uuid
from abstraction_helper import load_json_file


class Customer:
    """Clase del cliente."""
    def __init__(self, customer_file_path="database/customers.json"):
        self.customer_file_path = customer_file_path

    def create_customer(self, customer_name):
        """Función para registrar un nuevo cliente."""
        file_name = self.customer_file_path
        customer_json = load_json_file(file_name)
        customers = customer_json["customers"]
        customer_ids = set(customer["customer_id"] for customer in customers)

        # Se genera una ID única para el cliente.
        new_customer_id = str(uuid.uuid4())

        # Checa si el ID generado ya existe, regenerar en caso de necesitarse.
        while new_customer_id in customer_ids:
            new_customer_id = str(uuid.uuid4())

        if customer_name == "":
            raise ValueError("El nombre del cliente está vacío.")

        if isinstance(customer_name, int):
            raise ValueError("Cliente tiene que ser un string, no un número.")

        # Diccionario del nuevo cliente.
        new_customer = {
            "customer_id": new_customer_id,
            "customer_name": customer_name
        }

        customers.append(new_customer)

        # Escribir el nuevo registro al archivo.
        with open(file_name, 'w', encoding="UTF-8") as f:
            json.dump(customer_json, f, indent=4)

    def delete_customer(self, customer_id):
        """Función para borrar un cliente."""
        file_name = self.customer_file_path
        customer_json = load_json_file(file_name)
        customers = customer_json["customers"]
        customer_ids = set(customer["customer_id"] for customer in customers)

        if customer_id == "":
            raise ValueError("El ID está vacío.")

        if isinstance(customer_id, int):
            raise ValueError("El ID tiene que ser un string, no un número.")

        if customer_id in customer_ids:
            for customer in customers:
                if customer["customer_id"] == customer_id:
                    customers.remove(customer)
            with open(file_name, 'w', encoding="UTF-8") as f:
                json.dump(customer_json, f, indent=4)
                print(f"Fue borrado el cliente con el ID: {customer_id}")
        else:
            raise KeyError(f"No hay un cliente con el ID: {customer_id}")

    def display_customer_info(self, customer_id):
        """Función para mostrar la información de un cliente."""
        file_name = self.customer_file_path
        customer_json = load_json_file(file_name)
        customers = customer_json["customers"]
        customer_ids = set(customer["customer_id"] for customer in customers)

        if customer_id == "":
            raise ValueError("El ID está vacío.")

        if isinstance(customer_id, int):
            raise ValueError("El ID tiene que ser un string, no un número.")

        if customer_id in customer_ids:
            for customer in customers:
                if customer["customer_id"] == customer_id:
                    customer_name = customer["customer_name"]
                    print(f"ID: {customer_id}")
                    print(f"Nombre: {customer_name}")
        else:
            raise KeyError(f"No hay un cliente con el ID: {customer_id}")

    def mod_customer_info(self, customer_id, customer_name):
        """Función para modificar la información de un cliente."""
        file_name = self.customer_file_path
        customer_json = load_json_file(file_name)
        customers = customer_json["customers"]
        customer_ids = set(customer["customer_id"] for customer in customers)

        if customer_id == "":
            raise ValueError("El ID está vacío.")

        if customer_name == "":
            raise ValueError("El nuevo nombre del hotel está vacío.")

        if isinstance(customer_id, int):
            raise ValueError("El ID tiene que ser un string, no un número.")

        if isinstance(customer_name, int):
            raise ValueError("El hotel tiene que ser un string, no un número.")

        if customer_id in customer_ids:
            for customer in customers:
                if customer["customer_id"] == customer_id:
                    customer["customer_name"] = customer_name
            with open(file_name, 'w', encoding="UTF-8") as f:
                json.dump(customer_json, f, indent=4)
                print(f"Fue modificado el cliente con el ID: {customer_id}")
        else:
            raise KeyError(f"No hay un cliente con el ID: {customer_id}")
