from fizzbuzz.fizzbuzz import fizzbuzz

import unittest

class FizzbuzzTest(unittest.TestCase):
    def test_3_is_Fizz(self):    
        number = 3
        result = fizzbuzz(number)
        self.assertEqual(result, "Fizz")

    def test_5_is_Buzz(self):    
        number = 5
        result = fizzbuzz(number)
        self.assertEqual(result ,"Buzz")
    