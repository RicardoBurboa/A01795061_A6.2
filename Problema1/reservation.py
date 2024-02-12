"""Módulos de JSONs, generar IDs y un helper para cargar achivos JSON."""
import json
import uuid
from abstraction_helper import load_json_file


class Reservation:
    """Clase de la reservación."""
    def __init__(self, reservation_file_path="database/reservations.json"):
        if reservation_file_path != "database/reservations.json":
            raise ValueError("El nombre de la base de datos fue modificado.")
        if reservation_file_path == "":
            raise FileNotFoundError("No se encontró la base de datos.")

        self.reservation_file_path = reservation_file_path

    def cr_res(self, hotel_id, customer_id, room):
        """Función para registrar una nueva reservación."""
        if hotel_id == "":
            raise ValueError("El ID del hotel está vacío.")

        if customer_id == "":
            raise ValueError("El ID del cliente está vacío.")

        if room == "":
            raise ValueError("El número de habitación está vacío.")

        if isinstance(hotel_id, int):
            raise ValueError("El ID tiene que ser un string, no un número.")

        if isinstance(customer_id, int):
            raise ValueError("El ID tiene que ser un string, no un número.")

        if isinstance(room, int):
            raise ValueError("Room tiene que ser un string, no un número.")

        if isinstance(hotel_id, list):
            raise ValueError("El ID tiene que ser un string, no una lista.")

        if isinstance(customer_id, list):
            raise ValueError("El ID tiene que ser un string, no una lista.")

        if isinstance(room, list):
            raise ValueError("Room tiene que ser un string, no una lista.")

        file_name = self.reservation_file_path
        reservation_json = load_json_file(file_name)
        reservations = reservation_json["reservations"]
        reservation_ids = set(rsrv["reservation_id"] for rsrv in reservations)

        # Se genera una ID única para la reservación.
        new_reservation_id = str(uuid.uuid4())

        # Checa si el ID generado ya existe, regenerar en caso de necesitarse.
        while new_reservation_id in reservation_ids:
            new_reservation_id = str(uuid.uuid4())

        # Diccionario de la nueva reservación.
        new_reservation = {"reservation_id": new_reservation_id,
                           "room": room,
                           "hotel_id": hotel_id,
                           "customer_id": customer_id
                           }

        reservations.append(new_reservation)

        # Escribir el nuevo registro al archivo.
        with open(file_name, 'w', encoding="UTF-8") as f:
            json.dump(reservation_json, f, indent=4)

    def cancel_reserv(self, reservation_id):
        """Función para cancelar una reservación"""
        file_name = self.reservation_file_path
        reservation_json = load_json_file(file_name)
        reservations = reservation_json["reservations"]
        reservation_ids = set(rsrv["reservation_id"] for rsrv in reservations)

        if reservation_id == "":
            raise ValueError("El ID de la reservación está vacía.")

        if isinstance(reservation_id, int):
            raise ValueError("El ID tiene que ser un string, no un número.")

        if isinstance(reservation_id, list):
            raise ValueError("El ID tiene que ser un string, no una lista.")

        if isinstance(reservation_id, dict):
            raise ValueError("El ID tiene que ser un string, no un dict.")

        if isinstance(reservation_id, bool):
            raise ValueError("El ID tiene que ser un string, no un booleano.")

        if isinstance(reservation_id, float):
            raise ValueError("El ID tiene que ser un string, no un booleano.")

        if isinstance(reservation_id, tuple):
            raise ValueError("El ID tiene que ser un string, no un booleano.")

        if isinstance(reservation_id, set):
            raise ValueError("El ID tiene que ser un string, no un booleano.")

        if reservation_id in reservation_ids:
            for reservation in reservations:
                if reservation["reservation_id"] == reservation_id:
                    reservations.remove(reservation)
            with open(file_name, 'w', encoding="UTF-8") as f:
                json.dump(reservation_json, f, indent=4)
                print(f"Se canceló la reservación con el ID: {reservation_id}")
        else:
            raise KeyError(f"No hay reservación con el ID: {reservation_id}")
