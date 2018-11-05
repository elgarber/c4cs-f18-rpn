import unittest
import rpn

class TestBasics(unittest.TestCase):
    def test_add(self):
        result = rpn.calculate("1 1 +")
        self.assertEqual(2, result)

    def test_sub(self):
        result = rpn.calculate('4 3 -')
        self.assertEqual(1, result)

    def test_mul(self):
        result = rpn.calculate('4 3 *')
        self.assertEqual(12, result)

    def test_div(self):
        result = rpn.calculate('4 2 /')
        self.assertEqual(2, result)
    
    def test_chain(self):
        result = rpn.calculate('1 1 + 2 *')
        self.assertEqual(4, result)

    def test_power(self):
        result = rpn.calculate('2 4 ^')
        self.assertEqual(16, result)

    def test_rotate(self):
        result = rpn.calculate('5 2 rl ^')
        self.assertEqual(32, result)i

    def test_and(self):
        result = rpn.calculate('1 2 and')
        self.assertEqual(0, result)

    def test_or(self):
        result = rpn.calculate('3 5 or')
        self.assertEqual(7, result)

    def test_xor(self):
        result = rpn.calculate('3 5 xor')
        self.assertEqual(6, result)

