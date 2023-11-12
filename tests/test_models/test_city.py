#!/usr/bin/python3
"""class that does unittest"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """This is the test for City class"""
    def test_city(self):
        city = City()
        self.assertIsInstance(city, City)
        self.assertIsInstance(city.name, str)
        self.assertIsInstance(city.id, str)
        self.assertEqual(city.name, '')
        self.assertRegex(
            city.id,
            r'^[0-9a-fA-F]{8}-'
            r'[0-9a-fA-F]{4}-'
            r'[0-9a-fA-F]{4}-'
            r'[0-9a-fA-F]{4}-'
            r'[0-9a-fA-F]{12}$'
        )


if __name__ == "__main__":
    unittest.main()
