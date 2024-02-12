"""Módulos de pruebas unitarias y función para importar clases."""
import unittest
import json
from customer import Customer


class TestCustomer(unittest.TestCase):
    """Clase de pruebas."""
    def setUp(self):
        """Función para establecer las instancias de las clases."""
        self.customer = Customer()

    def test_create_customer(self):
        """Función para probar la creación de un cliente."""
        customer_name = "Nombre de Prueba"
        self.customer.create_customer(customer_name)

        with open("database/customers.json", "r", encoding="UTF-8") as f:
            customer_json = json.load(f)
            customers = customer_json["customers"]
            last_customer = customers[-1]
            last_customer_name = last_customer["customer_name"]

            self.assertEqual(last_customer_name, customer_name)

        self.assertRaises(ValueError, self.customer.create_customer, "")
        self.assertRaises(ValueError, self.customer.create_customer, 10)

    def test_delete_customer(self):
        """Función para probar el borrado de un cliente."""
        self.assertRaises(KeyError, self.customer.delete_customer, "test-id")
        self.assertRaises(ValueError, self.customer.delete_customer, "")
        self.assertRaises(ValueError, self.customer.delete_customer, 10)

    def test_display_customer_info(self):
        """Función para probar el despliegue de información de un cliente."""
        self.assertRaises(KeyError, self.customer.display_customer_info, "t")
        self.assertRaises(ValueError, self.customer.display_customer_info, "")
        self.assertRaises(ValueError, self.customer.display_customer_info, 10)

    def test_mod_customer_info(self):
        """Función para probar la modificación de un cliente."""
        self.assertRaises(KeyError, self.customer.mod_customer_info, "t", "J")
        self.assertRaises(ValueError, self.customer.mod_customer_info, "", "N")
        self.assertRaises(ValueError, self.customer.mod_customer_info, "t", "")
        self.assertRaises(ValueError, self.customer.mod_customer_info, 10, "N")
        self.assertRaises(ValueError, self.customer.mod_customer_info, "t", 10)


if __name__ == "__main__":
    unittest.main()
