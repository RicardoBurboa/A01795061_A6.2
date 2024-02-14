"""Módulos de pruebas unitarias y función para importar clases."""
import unittest
import json
from hotel import Hotel
from reservation import Reservation


class TestHotel(unittest.TestCase):
    """Clase de pruebas."""
    def setUp(self):
        """Función para establecer las instancias de las clases."""
        self.hotel = Hotel()
        self.reservation = Reservation()

    def test_create_hotel(self):
        """Función para probar la creación de un hotel."""
        hotel_name = "Nombre de Prueba"
        self.hotel.create_hotel(hotel_name)

        with open("database/hotels.json", "r", encoding="UTF-8") as f:
            hotel_json = json.load(f)
            hotels = hotel_json["hotels"]
            last_hotel = hotels[-1]
            last_hotel_name = last_hotel["hotel_name"]

            self.assertEqual(last_hotel_name, hotel_name)

        self.assertRaises(ValueError, self.hotel.create_hotel, "")
        self.assertRaises(ValueError, self.hotel.create_hotel, 10)

    def test_delete_hotel(self):
        """Función para probar el borrado de un hotel."""
        self.assertRaises(KeyError, self.hotel.delete_hotel, "test-id")
        self.assertRaises(ValueError, self.hotel.delete_hotel, "")
        self.assertRaises(ValueError, self.hotel.delete_hotel, 10)

    def test_display_hotel_info(self):
        """Función para probar el despliegue de información de un hotel."""
        self.assertRaises(KeyError, self.hotel.display_hotel_info, "t")
        self.assertRaises(ValueError, self.hotel.display_hotel_info, "")
        self.assertRaises(ValueError, self.hotel.display_hotel_info, 10)

    def test_mod_hotel_info(self):
        """Función para probar la modificación de un hotel."""
        self.assertRaises(KeyError, self.hotel.modify_hotel_info, "t", "N")
        self.assertRaises(ValueError, self.hotel.modify_hotel_info, "", "N")
        self.assertRaises(ValueError, self.hotel.modify_hotel_info, "t", "")
        self.assertRaises(ValueError, self.hotel.modify_hotel_info, 10, "N")
        self.assertRaises(ValueError, self.hotel.modify_hotel_info, "t", 10)

    def test_reserve_room(self):
        """Función para probar la reservación de una habitación."""
        self.assertRaises(ValueError, self.hotel.reserve_room, "", "c", "n")
        self.assertRaises(ValueError, self.hotel.reserve_room, "h", "", "n")
        self.assertRaises(ValueError, self.hotel.reserve_room, "h", "c", "")

        self.assertRaises(ValueError, self.reservation.__init__, "test")
        self.assertRaises(ValueError, self.reservation.__init__, "")
        self.assertRaises(ValueError, self.reservation.cr_res, "", "c", "n")
        self.assertRaises(ValueError, self.reservation.cr_res, "h", "", "n")
        self.assertRaises(ValueError, self.reservation.cr_res, "h", "c", "")
        self.assertRaises(ValueError, self.reservation.cr_res, 10, "c", "h")
        self.assertRaises(ValueError, self.reservation.cr_res, "h", 10, "h")
        self.assertRaises(ValueError, self.reservation.cr_res, "h", "c", 10)
        self.assertRaises(ValueError, self.reservation.cr_res, [], "c", "h")
        self.assertRaises(ValueError, self.reservation.cr_res, "h", [], "h")
        self.assertRaises(ValueError, self.reservation.cr_res, "h", "c", [])

    def test_cancel_reserv(self):
        """Función para probar la cancelación de una reservación."""
        self.assertRaises(ValueError, self.hotel.cancel_reserv, "", "c", "n")
        self.assertRaises(ValueError, self.hotel.cancel_reserv, "h", "", "n")
        self.assertRaises(ValueError, self.hotel.cancel_reserv, "h", "c", "")
        self.assertRaises(ValueError, self.reservation.__init__, "test")
        self.assertRaises(ValueError, self.reservation.__init__, "")
        self.assertRaises(ValueError, self.reservation.cancel_reserv, "")
        self.assertRaises(ValueError, self.reservation.cancel_reserv, 10)
        self.assertRaises(ValueError, self.reservation.cancel_reserv, [])
        self.assertRaises(ValueError, self.reservation.cancel_reserv, {})
        self.assertRaises(ValueError, self.reservation.cancel_reserv, True)
        self.assertRaises(ValueError, self.reservation.cancel_reserv, 10.1)
        self.assertRaises(ValueError, self.reservation.cancel_reserv, (1, 0))
        self.assertRaises(ValueError, self.reservation.cancel_reserv, set())


if __name__ == "__main__":
    unittest.main()
