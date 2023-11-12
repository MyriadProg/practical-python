# test_stock.py
# Exercise 8.1

import unittest
import stock

class TestStock(unittest.TestCase):

    # code that tests instance creation
    def test_create(self):
        s = stock.Stock('GOOG', 100, 490.1)
        self.assertEqual(s.name, 'GOOG')
        self.assertEqual(s.shares, 100)
        self.assertEqual(s.price, 490.1)
    
    # Make sure the s.cost property returns the correct value (49010.0)
    def test_cost(self):
        s = stock.Stock('GOOG', 100, 490.1)
        self.assertEqual(s.cost, 49010.0)
    
    # Make sure the s.sell() method works correctly
    def test_sell(self):
        s = stock.Stock('GOOG', 100, 490.1)
        s.sell(50)
        self.assertEqual(s.shares, 50)
    
    # Make sure that the s.shares attribute can’t be set to a non-integer value.
    def test_bad_shares(self):
        s = stock.Stock('GOOG', 100, 490.1)
        self.assertRaises(TypeError, s.shares, '100')

if __name__ == '__main__':
    unittest.main()