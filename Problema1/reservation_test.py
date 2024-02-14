"""Módulos de pruebas unitarias y función para importar clases."""
import unittest
import json
from reservation import Reservation


class TestReservation(unittest.TestCase):
    """Clase de pruebas."""
    def setUp(self):
        """Función para establecer las instancias de las clases."""
        self.reservation = Reservation()

    def test_constructor(self):
        """Función para probar el constructor."""
        self.assertRaises(ValueError, self.reservation.__init__, "test")
        self.assertRaises(ValueError, self.reservation.__init__, "")

    def test_create_reservation(self):
        """Función para probar la creación de una reservación."""
        hotel_id = "104e5e0a-05df-4d7a-9b23-e0b7c99362a4"
        customer_id = "b61ffc9c-78e6-46d7-9e81-f1c0e9a38ef2"
        room = "2"
        self.reservation.cr_res(hotel_id, customer_id, room)

        with open("database/reservations.json", "r", encoding="UTF-8") as f:
            reservation_json = json.load(f)
            reservations = reservation_json["reservations"]
            last_reservation = reservations[-1]
            last_reservation_customer_id = last_reservation["customer_id"]

            self.assertEqual(last_reservation_customer_id, customer_id)

        self.assertRaises(ValueError, self.reservation.cr_res, "", "c", "n")
        self.assertRaises(ValueError, self.reservation.cr_res, "h", "", "n")
        self.assertRaises(ValueError, self.reservation.cr_res, "h", "c", "")
        self.assertRaises(ValueError, self.reservation.cr_res, 10, "c", "n")
        self.assertRaises(ValueError, self.reservation.cr_res, "h", 10, "n")
        self.assertRaises(ValueError, self.reservation.cr_res, "h", "c", 10)
        self.assertRaises(ValueError, self.reservation.cr_res, [], "c", "n")
        self.assertRaises(ValueError, self.reservation.cr_res, "h", [], "n")
        self.assertRaises(ValueError, self.reservation.cr_res, "h", "c", [])

    def test_cancel_reservation(self):
        """Función para probar la cancelación de una reservación."""
        self.assertRaises(KeyError, self.reservation.cancel_reserv, "t")
        self.assertRaises(ValueError, self.reservation.cancel_reserv, "")
        self.assertRaises(ValueError, self.reservation.cancel_reserv, [])
        self.assertRaises(ValueError, self.reservation.cancel_reserv, {})
        self.assertRaises(ValueError, self.reservation.cancel_reserv, True)
        self.assertRaises(ValueError, self.reservation.cancel_reserv, 10.1)
        self.assertRaises(ValueError, self.reservation.cancel_reserv, (1, 0))
        self.assertRaises(ValueError, self.reservation.cancel_reserv, set())


if __name__ == "__main__":
    unittest.main()
