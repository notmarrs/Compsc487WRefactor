from fraction import Fraction
import unittest


class TestMyFraction(unittest.TestCase):
    def setUp(self):
        self.x = MyFraction(1, 2)
        self.y = MyFraction(2, 3)

    # Test 1: Test the get_num method
    def test_get_num(self):
        self.assertEqual(self.x.get_num(), 1)

    # Test 2: Test the get_den method
    def test_get_den(self):
        self.assertEqual(self.y.get_den(), 3)

    # Test 3: Test subtraction (__sub__)
    def test_subtraction(self):
        z = self.x - self.y
        self.assertEqual(z, MyFraction(-1, 6))

    # Test 4: Test multiplication (__mul__)
    def test_multiplication(self):
        z = self.x * self.y
        self.assertEqual(z, MyFraction(1, 3))

    # Test 5: Test division (__truediv__)
    def test_division(self):
        z = self.x / self.y
        self.assertEqual(z, MyFraction(3, 4))

    # Test 6: Test if raising an exception for non-integer values
    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            alpha = MyFraction(1.2, 2.2)

    # Test 7: Test the creation of a fraction with a negative denominator
    def test_negative_denominator(self):
        beta = MyFraction(3, -5)
        self.assertEqual(beta, MyFraction(-3, 5))

    # Test 8: Test addition (__add__) with different scenarios
    def test_addition(self):
        # Test radd (right add)
        self.assertEqual(self.x + 1, MyFraction(3, 2))

        # Test iadd (in-place add)
        for i in range(self.y.get_den()):
            self.x += i
        self.assertEqual(self.x, MyFraction(7, 2))

    # Test 9: Test comparison operators (__gt__, __ge__, __lt__, __le__, __ne__)
    def test_comparison_operators(self):
        self.assertFalse(self.x > self.y)
        self.assertFalse(self.x >= self.y)
        self.assertTrue(self.x < self.y)
        self.assertTrue(self.x <= self.y)
        self.assertTrue(self.x != self.y)
