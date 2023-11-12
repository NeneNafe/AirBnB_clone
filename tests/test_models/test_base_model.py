from models.base_model import BaseModel
"""doing some unittesting for BaseModel"""
import unittest
import uuid
from datetime import datetime, timedelta


class TestBaseModel(unittest.TestCase):
    """this is a class that does the test for basemodel"""
    pass
    # def test_Base(self):
    #     b1 = BaseModel()
    #     self.assertTrue(hasattr(b1, 'created_at'))
    #     self.assertTrue(hasattr(b1, 'updated_at'))
    #     delay = timedelta(seconds=1)
    #     timediff = datetime.now() - b1.created_at
    #     self.assertTrue(timediff < delay)
    #     self.assertIsInstance(b1.id, str)
    #     self.assertIsInstance(b1.created_at, datetime)
    #     self.assertIsInstance(b1.updated_at, datetime)
    #     self.assertRegex(
    #         b1.id,
    #         r'^[0-9a-fA-F]{8}-'
    #         r'[0-9a-fA-F]{4}-'
    #         r'[0-9a-fA-F]{4}-'
    #         r'[0-9a-fA-F]{4}-'
    #         r'[0-9a-fA-F]{12}$'
    #     )


if __name__ == "__main__":
    unittest.main()
