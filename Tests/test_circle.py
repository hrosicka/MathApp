import unittest
import sys
from math import pi

# setting path
sys.path.append('../PyQtMathApp')
from CircleCalc import *


class CircleTest(unittest.TestCase):

    def test_init_valid_radius(self):
        """Tests initialization with a valid positive radius."""
        circle = Circle(5.0)
        self.assertEqual(circle.radius, 5.0)

    def test_init_radius_zero(self):
        """Tests initialization with radius zero (raises ValueError)."""
        with self.assertRaises(ValueError) as error:
           Circle(0.0)
        self.assertEqual(str(error.exception), "Radius must be a positive number.")

    def test_init_negative_radius(self):
        """Tests initialization with a negative radius (raises ValueError)."""
        with self.assertRaises(ValueError) as error:
            Circle(-2.5)
        self.assertEqual(str(error.exception), "Radius must be a positive number.")

    def test_init_non_numeric_radius(self):
        """Tests initialization with a non-numeric radius (raises TypeError)."""
        with self.assertRaises(TypeError) as error:
            Circle("hello")
        self.assertEqual(str(error.exception), "Radius must be a number.")

    def test_circumference(self):
        """Tests circumference calculation for various radii."""
        circle = Circle(3.0)
        self.assertEqual(circle.circumference(), round(2 * pi * 3.0, 5))

        circle = Circle(10.0)
        self.assertEqual(circle.circumference(), round(2 * pi * 10.0, 5))

    def test_area(self):
        """Tests area calculation for various radii."""
        circle = Circle(2.0)
        self.assertEqual(circle.area(), round(pi * 2.0**2, 5))

        circle = Circle(7.0)
        self.assertEqual(circle.area(), round(pi * 7.0**2, 5))

    def test_circumference_very_small_radius(self):
        """Tests circumference calculation for a very small positive radius."""
        circle = Circle(0.000001)  # Extremely small radius
        expected_circumference = round(2 * pi * 0.000001, 5)
        self.assertAlmostEqual(circle.circumference(), expected_circumference, places=5)

    def test_circumference_very_large_radius(self):
        """Tests circumference calculation for a very large positive radius."""
        circle = Circle(1000000.0)  # Extremely large radius
        expected_circumference = round(2 * pi * 1000000.0, 5)
        self.assertAlmostEqual(circle.circumference(), expected_circumference, places=5)

    def test_area_very_small_radius(self):
        """Tests area calculation for a very small positive radius."""
        circle = Circle(0.000001)  # Extremely small radius
        expected_area = round(pi * (0.000001**2), 5)
        self.assertAlmostEqual(circle.area(), expected_area, places=5)

    def test_area_very_large_radius(self):
        """Tests area calculation for a very large positive radius."""
        circle = Circle(1000000.0)  # Extremely large radius
        expected_area = round(pi * (1000000.0**2), 5)
        self.assertAlmostEqual(circle.area(), expected_area, places=5)

    def test_get_description(self):
        """Tests get_description for different radii."""
        circle = Circle(4.0)
        expected_circumference = "Circle with radius 4.0 cm has circumference {:.3f} cm.".format(circle.circumference())
        expected_area = "Circle with radius 4.0 cm has area {:.3f} cm2.".format(circle.area())
        self.assertEqual(circle.get_description(), (expected_circumference, expected_area))

        circle = Circle(1.578)
        expected_circumference = "Circle with radius 1.578 cm has circumference {:.3f} cm.".format(circle.circumference())
        expected_area = "Circle with radius 1.578 cm has area {:.3f} cm2.".format(circle.area())
        self.assertEqual(circle.get_description(), (expected_circumference, expected_area))


if __name__ == '__main__':
    unittest.main()