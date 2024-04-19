import unittest
import sys

# setting path
sys.path.append('../PyQtMathApp')
from SquareCalc import *


class TestSquare(unittest.TestCase):

    def test_init_valid_side_length(self):
        """Tests initialization with a valid positive side length."""
        square = Square(5.0)
        self.assertEqual(square.side_length, 5.0)

    def test_init_zero_side_length(self):
        """Tests initialization with zero side length (raises ValueError)."""
        with self.assertRaises(ValueError) as error:
            Square(0.0)
        self.assertEqual(str(error.exception), "Side length must be a positive number.")

    def test_init_negative_side_length(self):
        """Tests initialization with a negative side length (raises ValueError)."""
        with self.assertRaises(ValueError) as error:
            Square(-2.5)
        self.assertEqual(str(error.exception), "Side length must be a positive number.")

    def test_init_non_numeric_side_length(self):
        """Tests initialization with a non-numeric side length (raises TypeError)."""
        with self.assertRaises(TypeError) as error:
            Square("hello")
        self.assertEqual(str(error.exception), "Side length must be a number.")

    def test_circumference(self):
        """Tests circumference calculation for various side lengths."""
        square = Square(3.0)
        expected_circumference = 4 * 3.0
        self.assertEqual(square.circumference(), expected_circumference)

        square = Square(8.0)
        expected_circumference = 4 * 8.0
        self.assertEqual(square.circumference(), expected_circumference)

    def test_area(self):
        """Tests area calculation for various side lengths."""
        square = Square(2.0)
        expected_area = 2.0 * 2.0
        self.assertEqual(square.area(), expected_area)

        square = Square(7.0)
        expected_area = 7.0 * 7.0
        self.assertEqual(square.area(), expected_area)

    def test_circumference_small_side_length(self):
        """Tests circumference calculation for a very small side length."""
        square = Square(0.001)
        expected_circumference = 0.004
        self.assertAlmostEqual(square.circumference(), expected_circumference, delta=0.0001)

    def test_circumference_large_side_length(self):
        """Tests circumference calculation for a very large side length."""
        square = Square(1000.0)
        expected_circumference = 4000.0
        self.assertAlmostEqual(square.circumference(), expected_circumference)

    def test_area_small_side_length(self):
        """Tests area calculation for a very small side length."""
        square = Square(0.001)
        expected_area = 0.000001
        self.assertAlmostEqual(square.area(), expected_area, delta=0.000001)

    def test_area_large_side_length(self):
        """Tests area calculation for a very large side length."""
        square = Square(10000.0)
        expected_area = 100000000.0
        self.assertAlmostEqual(square.area(), expected_area)

    def test_get_description(self):
        """Tests get_description for different side lengths."""
        square = Square(4.0)
        expected_circumference = "Square with side length {} cm has circumference {:.1f} cm.".format(square.side_length, round(square.circumference(), 3))
        expected_area = "Square with side length {} cm has area {:.1f} cm2.".format(square.side_length, round(square.area(), 3))
        self.assertEqual(square.get_description(), (expected_circumference, expected_area))

        square = Square(2.5)
        expected_circumference = "Square with side length {} cm has circumference {:.1f} cm.".format(square.side_length, round(square.circumference(), 3))
        expected_area = "Square with side length {} cm has area {:.2f} cm2.".format(square.side_length, round(square.area(), 3))
        self.assertEqual(square.get_description(), (expected_circumference, expected_area))

if __name__ == '__main__':
  unittest.main()
