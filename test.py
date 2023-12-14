import unittest
from src.solution import calculate_minimal_cost

class TestCalculateMinimumCost(unittest.TestCase):
    
    def test_example_1(self):
        prices = [50, 20, 30, 17, 100]
        discount = 10
        self.assertEqual(calculate_minimal_cost(prices, discount), 207.00)

    def test_example_2(self):
        prices = [1, 2, 3, 4, 5, 6, 7]
        discount = 100
        self.assertEqual(calculate_minimal_cost(prices, discount), 15.00)

    def test_example_3(self):
        prices = [1, 1, 1]
        discount = 33
        self.assertEqual(calculate_minimal_cost(prices, discount), 2.67)

if __name__ == '__main__':
    unittest.main()