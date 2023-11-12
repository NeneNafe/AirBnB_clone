#!/usr/bin/python3
"""class that does unittest"""
import unittest
from models.state import State


class TestUser(unittest.TestCase):
    """This is the test for State class"""
    def test_state(self):
        state = State()
        self.assertIsInstance(state, State)
        self.assertEqual(state.name, '')


if __name__ == "__main__":
    unittest.main()
