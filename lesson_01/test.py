import unittest
from lesson_01.main import add, subtract, multiply, divide, check, divide_0

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 5), 7)
        self.assertEqual(add(3, 7), 10)

    def test_subtract(self):
        self.assertEqual(subtract(7, 4), 3)
        self.assertEqual(subtract(4, 2), 2)

    def test_multiply(self):
        self.assertEqual(multiply(2, 5), 10)
        self.assertEqual(multiply(3, 6), 18)

    def test_divide(self):
        self.assertEqual(divide(4, 2), 2)
        self.assertEqual(divide(20, 5), 4)

    def test_check(self):
        self.assertTrue(check(2))
        self.assertTrue(check(6))
        self.assertTrue(check(220))

        self.assertFalse(check(1))
        self.assertFalse(check(3))
        self.assertFalse(check(57))

    def test_divide_success(self):
        self.assertEqual(divide_0(10, 2), 5)
        self.assertEqual(divide_0(6, 3), 2)
        self.assertEqual(divide_0(70, 2), 35)

    def test_divide_by_zero(self):
        self.assertRaises(ValueError, divide_0, 6, 0)



if __name__ == '__main__':
    unittest.main()

