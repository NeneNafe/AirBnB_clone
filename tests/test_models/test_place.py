#!/usr/bin/python3
"""class that does unittest"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """This is the test for Place class"""
    def test_place(self):
        place = Place()
        self.assertIsInstance(place, Place)
        self.assertEqual(place.name, '')
        self.assertIsInstance(place.user_id, str)
        self.assertIsInstance(place.city_id, str)
        self.assertIsInstance(place.amenity_ids, str)
        self.assertEqual(place.description, '')
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, '')


if __name__ == "__main__":
    unittest.main()
