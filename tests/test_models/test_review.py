#!/usr/bin/python3
"""class that does unittest"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """This is the test for Review class"""
    def test_Review(self):
        review = Review()
        self.assertIsInstance(review, Review)
        self.assertIsInstance(review.place_id, str)
        self.assertIsInstance(review.user_id, str)
        self.assertEqual(review.text, '')
        self.assertEqual(review.user_id, '')
        self.assertEqual(review.place_id, '')


if __name__ == "__main__":
    unittest.main()