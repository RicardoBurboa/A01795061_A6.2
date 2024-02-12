"""Módulos de JSONs, generar IDs y un helper para cargar achivos JSON."""
import json
import uuid
from abstraction_helper import load_json_file
from reservation import Reservation


class Hotel:
    """Clase del hotel."""
    def __init__(self, hotel_file_path="database/hotels.json"):
        self.hotel_file_path = hotel_file_path

    def create_hotel(self, hotel_name):
        """Función para registrar un nuevo hotel."""
        file_name = self.hotel_file_path
        hotel_json = load_json_file(file_name)
        hotels = hotel_json["hotels"]
        hotel_ids = set(hotel["hotel_id"] for hotel in hotels)

        # Se genera una ID única para el hotel.
        new_hotel_id = str(uuid.uuid4())

        # Checa si el ID generado ya existe, regenerar en caso de necesitarse.
        while new_hotel_id in hotel_ids:
            new_hotel_id = str(uuid.uuid4())

        if hotel_name == "":
            raise ValueError("El nombre del hotel está vacío.")

        if isinstance(hotel_name, int):
            raise ValueError("El hotel tiene que ser un string, no un número.")

        # Diccionario del nuevo hotel.
        new_hotel = {
            "hotel_id": new_hotel_id,
            "hotel_name": hotel_name
        }

        hotels.append(new_hotel)

        # Escribir el nuevo registro al archivo.
        with open(file_name, 'w', encoding="UTF-8") as f:
            json.dump(hotel_json, f, indent=4)

    def delete_hotel(self, hotel_id):
        """Función para borrar un hotel."""
        file_name = self.hotel_file_path
        hotel_json = load_json_file(file_name)
        hotels = hotel_json["hotels"]
        hotel_ids = set(hotel["hotel_id"] for hotel in hotels)

        if hotel_id == "":
            raise ValueError("El ID está vacío.")

        if isinstance(hotel_id, int):
            raise ValueError("El ID tiene que ser un string, no un número.")

        if hotel_id in hotel_ids:
            for hotel in hotels:
                if hotel["hotel_id"] == hotel_id:
                    hotels.remove(hotel)
            with open(file_name, 'w', encoding="UTF-8") as f:
                json.dump(hotel_json, f, indent=4)
                print(f"Fue borrado el hotel con el ID: {hotel_id}")
        else:
            raise KeyError(f"No hay un hotel con el ID: {hotel_id}")

    def display_hotel_info(self, hotel_id):
        """Función para mostrar la información de un hotel."""
        file_name = self.hotel_file_path
        hotel_json = load_json_file(file_name)
        hotels = hotel_json["hotels"]
        hotel_ids = set(hotel["hotel_id"] for hotel in hotels)

        if hotel_id == "":
            raise ValueError("El ID está vacío.")

        if isinstance(hotel_id, int):
            raise ValueError("El ID tiene que ser un string, no un número.")

        if hotel_id in hotel_ids:
            for hotel in hotels:
                if hotel["hotel_id"] == hotel_id:
                    hotel_name = hotel["hotel_name"]
                    print(f"ID: {hotel_id}")
                    print(f"Nombre: {hotel_name}")
        else:
            raise KeyError(f"No hay un hotel con el ID: {hotel_id}")

    def modify_hotel_info(self, hotel_id, hotel_name):
        """Función para modificar la información de un hotel."""
        file_name = self.hotel_file_path
        hotel_json = load_json_file(file_name)
        hotels = hotel_json["hotels"]
        hotel_ids = set(hotel["hotel_id"] for hotel in hotels)

        if hotel_id == "":
            raise ValueError("El ID está vacío.")

        if hotel_name == "":
            raise ValueError("El nuevo nombre del hotel está vacío.")

        if isinstance(hotel_id, int):
            raise ValueError("El ID tiene que ser un string, no un número.")

        if isinstance(hotel_name, int):
            raise ValueError("El hotel tiene que ser un string, no un número.")

        if hotel_id in hotel_ids:
            for hotel in hotels:
                if hotel["hotel_id"] == hotel_id:
                    hotel["hotel_name"] = hotel_name
            with open(file_name, 'w', encoding="UTF-8") as f:
                json.dump(hotel_json, f, indent=4)
                print(f"Fue modificado el hotelcon el ID: {hotel_id}")
        else:
            raise KeyError(f"No hay un hotel con el ID: {hotel_id}")

    def reserve_room(self, hotel_id, customer_id, room_number):
        """Función para reservar una habitación."""
        if hotel_id == "":
            raise ValueError("El ID del hotel está vacío.")

        if customer_id == "":
            raise ValueError("El ID del cliente está vacío.")

        if room_number == "":
            raise ValueError("El número de habitación está vacío.")

        reservation = Reservation()
        reservation.cr_res(hotel_id, customer_id, room_number)

    def cancel_reserv(self, reservation_id):
        """Función para cancelar una reservación."""
        if reservation_id == "":
            raise ValueError("El ID del hotel está vacío.")

        reservation = Reservation()
        reservation.cancel_reserv(reservation_id)
