import unittest
from app import calculate_average_score, is_passed


class TestApp(unittest.TestCase):

    def test_average(self):
        self.assertEqual(calculate_average_score([100, 50]), 75)

    def test_empty(self):
        self.assertEqual(calculate_average_score([]), 0)

    def test_passed(self):
        self.assertTrue(is_passed(60))

    def test_not_passed(self):
        self.assertFalse(is_passed(50))


if __name__ == "__main__":
    unittest.main()
