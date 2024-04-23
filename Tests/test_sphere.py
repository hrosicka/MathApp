import unittest
import sys
from math import pi

# setting path
sys.path.append('../PyQtMathApp')
from SphereCalc import *

import unittest
import math

class SphereTest(unittest.TestCase):

    def test_init_valid_radius(self):
        """Tests initialization with a valid positive radius."""
        sphere = Sphere(5.0)
        self.assertEqual(sphere.radius, 5.0)

    def test_init_zero_radius(self):
        """Tests initialization with a zero radius (raises ValueError)."""
        with self.assertRaises(ValueError) as error:
            Sphere(0.0)
        self.assertEqual(str(error.exception), "Radius must be a positive number.")

    def test_init_negative_radius(self):
        """Tests initialization with a negative radius (raises ValueError)."""
        with self.assertRaises(ValueError) as error:
            Sphere(-2.5)
        self.assertEqual(str(error.exception), "Radius must be a positive number.")

    def test_init_non_numeric_radius(self):
        """Tests initialization with a non-numeric radius (raises TypeError)."""
        with self.assertRaises(TypeError) as error:
            Sphere("hello")
        self.assertEqual(str(error.exception), "Radius must be a number.")

    def test_surface_area_positive_radius(self):
        """Tests surface area calculation for a positive radius."""
        sphere = Sphere(3.0)
        expected_surface_area = 4 * math.pi * (3.0**2)
        self.assertAlmostEqual(sphere.surface_area(), expected_surface_area, places=5)

    def test_volume_positive_radius(self):
        """Tests volume calculation for a positive radius."""
        sphere = Sphere(4.0)
        expected_volume = (4.0 / 3.0) * math.pi * (4.0**3)
        self.assertAlmostEqual(sphere.volume(), expected_volume, places=5)

    def test_surface_area_very_small_radius(self):
        """Tests surface area calculation for a very small positive radius."""
        sphere = Sphere(0.000001)  # Extremely small radius
        expected_surface_area = 4 * math.pi * (0.000001**2)
        self.assertAlmostEqual(sphere.surface_area(), expected_surface_area, places=5)

    def test_surface_area_very_large_radius(self):
        """Tests surface area calculation for a very large positive radius."""
        sphere = Sphere(1000000.0)  # Extremely large radius
        expected_surface_area = 4 * math.pi * (1000000.0**2)
        self.assertAlmostEqual(sphere.surface_area(), expected_surface_area, places=5)

    def test_volume_very_small_radius(self):
        """Tests volume calculation for a very small positive radius."""
        sphere = Sphere(0.000001)  # Extremely small radius
        expected_volume = (4.0 / 3.0) * math.pi * (0.000001**3)
        self.assertAlmostEqual(sphere.volume(), expected_volume, places=5)

    def test_volume_very_large_radius(self):
        """Tests volume calculation for a very large positive radius."""
        sphere = Sphere(1000000.0)  # Extremely large radius
        expected_volume = (4.0 / 3.0) * math.pi * (1000000.0**3)
        self.assertAlmostEqual(sphere.volume(), expected_volume, places=5)
                               
    def test_get_description_positive_radius(self):
        """Tests get_description for a positive radius."""
        sphere = Sphere(2.0)
        expected_description = (
            "Sphere with radius {} cm has surface area {:.3f} cm2.".format(
                sphere.radius, round(sphere.surface_area(), 3)),
            "Sphere with radius {} cm has volume {:.3f} cm3.".format(
                sphere.radius, round(sphere.volume(), 3)),)
        self.assertEqual(sphere.get_description(), expected_description)

if __name__ == "__main__":
    unittest.main()
