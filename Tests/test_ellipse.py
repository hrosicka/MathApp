import unittest
import sys
from math import pi

# setting path
sys.path.append('../PyQtMathApp')
from EllipseCalc import *

class EllipseTest(unittest.TestCase):

    def test_init_valid_axes(self):
        """Tests initialization with valid positive axis lengths."""
        ellipse = Ellipse(5.0, 3.0)
        self.assertEqual(ellipse.semi_major_axis, 5.0)
        self.assertEqual(ellipse.semi_minor_axis, 3.0)

    def test_init_zero_major_axis(self):
        """Tests initialization with zero major axis (raises ValueError)."""
        with self.assertRaises(ValueError) as error:
            Ellipse(0.0, 3.0)
        self.assertEqual(str(error.exception), "Semi-major axis length must be positive.")

    def test_init_zero_minor_axis(self):
        """Tests initialization with zero minor axis (raises ValueError)."""
        with self.assertRaises(ValueError) as error:
            Ellipse(5.0, 0.0)
        self.assertEqual(str(error.exception), "Semi-minor axis length must be positive.")

    def test_init_negative_major_axis(self):
        """Tests initialization with a negative major axis (raises ValueError)."""
        with self.assertRaises(ValueError) as error:
            Ellipse(-2.5, 3.0)
        self.assertEqual(str(error.exception), "Semi-major axis length must be positive.")

    def test_init_negative_minor_axis(self):
        """Tests initialization with a negative minor axis (raises ValueError)."""
        with self.assertRaises(ValueError) as error:
            Ellipse(5.0, -1.0)
        self.assertEqual(str(error.exception), "Semi-minor axis length must be positive.")

    def test_init_non_numeric_major_axis(self):
        """Tests initialization with a non-numeric major axis (raises TypeError)."""
        with self.assertRaises(TypeError) as error:
            Ellipse("hello", 3.0)
        self.assertEqual(str(error.exception), "Semi-major axis length must be a number.")

    def test_init_non_numeric_minor_axis(self):
        """Tests initialization with a non-numeric minor axis (raises TypeError)."""
        with self.assertRaises(TypeError) as error:
            Ellipse(5.0, "world")
        self.assertEqual(str(error.exception), "Semi-minor axis length must be a number.")

    def test_init_very_small_positive_major_axis(self):
        """Tests initialization with a very small positive major axis."""
        ellipse = Ellipse(0.000001, 3.0)
        self.assertAlmostEqual(ellipse.circumference(), round(pi * math.sqrt(2 * (0.000001**2 + 3.0**2)), 5))

    def test_init_very_large_major_axis(self):
        """Tests initialization with a very large major axis."""
        ellipse = Ellipse(1000000.0, 3.0)
        self.assertAlmostEqual(ellipse.circumference(), round(pi * math.sqrt(2 * (1000000.0**2 + 3.0**2)), 5))

    def test_init_empty_string_major_axis(self):
        """Tests initialization with an empty string for major axis (raises TypeError)."""
        with self.assertRaises(TypeError) as error:
            Ellipse("", 3.0)
        self.assertEqual(str(error.exception), "Semi-major axis length must be a number.")

    def test_init_empty_string_minor_axis(self):
        """Tests initialization with an empty string for minor axis (raises TypeError)."""
        with self.assertRaises(TypeError) as error:
            Ellipse(5.0, "")
        self.assertEqual(str(error.exception), "Semi-minor axis length must be a number.")

    def test_circumference(self):
        """Tests circumference calculation for various axis lengths."""
        ellipse = Ellipse(3.0, 1.0)
        expected_circumference = round(pi * math.sqrt(2 * (3.0**2 + 1.0**2)), 5)
        self.assertEqual(ellipse.circumference(), expected_circumference)

        ellipse = Ellipse(8.0, 4.0)
        expected_circumference = round(pi * math.sqrt(2 * (8.0**2 + 4.0**2)), 5)
        self.assertEqual(ellipse.circumference(), expected_circumference)

    def test_area(self):
        """Tests area calculation for various axis lengths."""
        ellipse = Ellipse(2.0, 1.5)
        expected_area = round(pi * 2.0 * 1.5, 5)
        self.assertEqual(ellipse.area(), expected_area)

        ellipse = Ellipse(7.0, 3.0)
        expected_area = round(pi * 7.0 * 3.0, 5)
        self.assertEqual(ellipse.area(), expected_area)

    def test_get_description(self):
        """Tests get_description for different axis lengths."""
        ellipse = Ellipse(4.0, 2.0)
        expected_circumference = "Ellipse with axis {} and {} cm has circumference {:.3f} cm.".format(ellipse.semi_major_axis, ellipse.semi_minor_axis, round(ellipse.circumference(), 3))
        expected_area = "Ellipse with axis {} a {} cm and has area {:.3f} cm2.".format(ellipse.semi_major_axis, ellipse.semi_minor_axis, round(ellipse.area(), 3))
        self.assertEqual(ellipse.get_description(), (expected_circumference, expected_area))

        ellipse = Ellipse(2.5, 1.125)
        expected_circumference = "Ellipse with axis {} and {} cm has circumference {:.3f} cm.".format(ellipse.semi_major_axis, ellipse.semi_minor_axis, round(ellipse.circumference(), 3))
        expected_area = "Ellipse with axis {} a {} cm and has area {:.3f} cm2.".format(ellipse.semi_major_axis, ellipse.semi_minor_axis, round(ellipse.area(), 3))
        self.assertEqual(ellipse.get_description(), (expected_circumference, expected_area))

if __name__ == '__main__':
    unittest.main()