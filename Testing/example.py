import unittest

from fraction import Fraction

class Calculator:
    @staticmethod
    def add(a,b):
        return a+b
    

class TestFraction(unittest.TestCase):
    def test_addition(self):
        f1 = Fraction(1,2)
        f2 = Fraction(1,3)
        self.assertEqual(str(f1+f2), "5/6")

class TestCalculator(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(Calculator.add(2, 3), 5)
        self.assertEqual(Calculator.add(-2, -3), -5)
        self.assertEqual(Calculator.add(9999999999999999999999999999999999999999999999999999999999999,12121541535478762138941814394168413549841321843218), 10000000000000000000012121541535478762138941814394168413549841321843217)

if "__name__" == "__main__":
    unittest.main()