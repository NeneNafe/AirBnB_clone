#!/usr/bin/python3
from models.amenity import Amenity
"""class that does unittest"""
import unittest


class TestAmenity(unittest.TestCase):
    """This is the test for Amenity class"""
    def test_Amenity(self):
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertEqual(amenity.name, '')
        self.assertIsInstance(amenity.name, str)


if __name__ == "__main__":
    unittest.main()
