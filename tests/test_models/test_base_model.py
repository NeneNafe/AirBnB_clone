from models.base_model import BaseModel
"""doing some unittesting for BaseModel"""
import unittest
import uuid
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """this is a class that does the test for basemodel"""
    def testBase(self):
        b1 = BaseModel()
        self.assertIsInstance(b1.id, str)
        self.assertIsInstance(b1.created_at, datetime)
        self.assertIsInstance(b1.updated_at, datetime)