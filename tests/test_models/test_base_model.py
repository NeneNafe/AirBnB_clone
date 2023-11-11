from models.base_model import BaseModel
"""doing some unittesting for BaseModel"""
import unittest
import uuid
from datetime import datetime, timedelta


class TestBaseModel(unittest.TestCase):
    """this is a class that does the test for basemodel"""
    def testBase(self):
        b1 = BaseModel()
        self.assertTrue(hasattr(b1, 'created_at'))
        self.assertTrue(hasattr(b1, 'updated_at'))
        delay = timedelta(seconds=1)
        timediff = datetime.now() - b1.created_at
        self.assertTrue(timediff < delay)
        #self.assertAlmostEqual(b1.created_at, datetime.now())
        self.assertIsInstance(b1.id, str)
        self.assertIsInstance(b1.created_at, datetime)
        self.assertIsInstance(b1.updated_at, datetime)