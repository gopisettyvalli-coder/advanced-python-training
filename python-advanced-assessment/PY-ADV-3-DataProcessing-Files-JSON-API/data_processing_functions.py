import unittest
from data_processing import filter_even_numbers, extract_domain

class TestDataProcessing(unittest.TestCase):

    def test_filter_even_numbers(self):
        result = filter_even_numbers([1, 2, 3, 4, 5])
        self.assertEqual(result, [2, 4])

    def test_extract_domain(self):
        result = extract_domain("user@example.com")
        self.assertEqual(result, "example.com")

if __name__ == "__main__":
    unittest.main()