#!/usr/bin/python3
"""class that does unittest"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """This is the test for User class"""
    def test_user(self):
        user = User()
        self.assertIsInstance(user, User)
        self.assertEqual(user.email, '')
        self.assertEqual(user.password, '')
        self.assertEqual(user.last_name, '')


if __name__ == "__main__":
    unittest.main()
