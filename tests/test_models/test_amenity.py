#!/usr/bin/python3
"""class that does unittest"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """This is the test for Amenity class"""
    def test_Amenity(self):
        amenity = Amenity()
        amenity2 = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertEqual(amenity.name, '')
        self.assertEqual(amenity, amenity2)


if __name__ == "__main__":
    unittest.main()
