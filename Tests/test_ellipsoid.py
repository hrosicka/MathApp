import unittest
import sys
from math import pi

# setting path
sys.path.append('../PyQtMathApp')
from EllipsoidCalc import *

class EllipsoidTest(unittest.TestCase):

    def test_init_valid_dimensions(self):
        """Tests initialization with valid positive semi-axes."""
        ellipsoid = Ellipsoid(5.0, 3.0, 2.0)
        self.assertEqual(ellipsoid.semi_axis_a, 5.0)
        self.assertEqual(ellipsoid.semi_axis_b, 3.0)
        self.assertEqual(ellipsoid.semi_axis_c, 2.0)

    def test_init_zero_semi_axis_a(self):
        """Tests initialization with zero semi-axis a (raises ValueError)."""
        with self.assertRaises(ValueError) as error:
            Ellipsoid(0.0, 5.0, 2.0)
        self.assertEqual(str(error.exception), "Semi-axis a must be positive.")

    def test_init_zero_semi_axis_b(self):
        """Tests initialization with zero semi-axis b (raises ValueError)."""
        with self.assertRaises(ValueError) as error:
            Ellipsoid(10.0, 0.0, 2.0)
        self.assertEqual(str(error.exception), "Semi-axis b must be positive.")

    def test_init_zero_semi_axis_c(self):
        """Tests initialization with zero semi-axis c (raises ValueError)."""
        with self.assertRaises(ValueError) as error:
            Ellipsoid(10.0, 5.0, 0.0)
        self.assertEqual(str(error.exception), "Semi-axis c must be positive.")

    def test_init_negative_semi_axis_a(self):
        """Tests initialization with a negative semi-axis a (raises ValueError)."""
        with self.assertRaises(ValueError) as error:
            Ellipsoid(-2.5, 3.0, 2.0)
        self.assertEqual(str(error.exception), "Semi-axis a must be positive.")

    def test_init_negative_semi_axis_b(self):
        """Tests initialization with a negative semi-axis b (raises ValueError)."""
        with self.assertRaises(ValueError) as error:
            Ellipsoid(4.0, -2.5, 2.0)
        self.assertEqual(str(error.exception), "Semi-axis b must be positive.")

    def test_init_negative_semi_axis_c(self):
        """Tests initialization with a negative semi-axis c (raises ValueError)."""
        with self.assertRaises(ValueError) as error:
            Ellipsoid(10.0, 5.0, -2.0)
        self.assertEqual(str(error.exception), "Semi-axis c must be positive.")

    def test_init_non_numeric_semi_axis_a(self):
        """Tests initialization with a non-numeric semi-axis a (raises TypeError)."""
        with self.assertRaises(TypeError) as error:
            Ellipsoid("hello", 5.0, 2.0)
        self.assertEqual(str(error.exception), "Semi-axis a must be a number.")

    def test_init_non_numeric_semi_axis_b(self):
        """Tests initialization with a non-numeric semi-axis b (raises TypeError)."""
        with self.assertRaises(TypeError) as error:
            Ellipsoid(10.0, "hello", 2.0)
        self.assertEqual(str(error.exception), "Semi-axis b must be a number.")

    def test_init_non_numeric_semi_axis_c(self):
        """Tests initialization with a non-numeric semi-axis c (raises TypeError)."""
        with self.assertRaises(TypeError) as error:
            Ellipsoid(10.0, 5.0, "hello")
        self.assertEqual(str(error.exception), "Semi-axis c must be a number.")

    def test_surface_area_positive_dimensions(self):
        """Tests surface area calculation for positive semi-axes."""
        expected_surface_area = 48.97193
        ellipsoid = Ellipsoid(3.0, 2.0, 1.0)
        self.assertAlmostEqual(ellipsoid.surface_area(), expected_surface_area, places=5)

    def test_volume_positive_dimensions(self):
        """Tests volume calculation for positive semi-axes."""
        expected_volume = (4.0 / 3.0) * pi * (3.0 * 2.0 * 1.0)
        ellipsoid = Ellipsoid(3.0, 2.0, 1.0)
        self.assertAlmostEqual(ellipsoid.volume(), expected_volume, places=5)

    def test_surface_area_very_small_dimensions(self):
        """Tests surface area calculation for very small positive dimensions."""
        expected_surface_area = 0.0  # Very small dimensions result in near-zero surface area
        ellipsoid = Ellipsoid(0.0001, 0.0002, 0.0003)
        self.assertAlmostEqual(ellipsoid.surface_area(), expected_surface_area, places=5)

    def test_surface_area_very_large_dimensions(self):
        """Tests surface area calculation for very large positive dimensions."""
        expected_surface_area = 3742681.81
        ellipsoid = Ellipsoid(1000, 500, 200)
        self.assertAlmostEqual(ellipsoid.surface_area(), expected_surface_area, places=2)

    def test_volume_very_small_dimensions(self):
        """Tests volume calculation for very small positive dimensions."""
        expected_volume = 0.0  # Very small dimensions result in near-zero volume
        ellipsoid = Ellipsoid(0.0001, 0.0002, 0.0003)
        self.assertAlmostEqual(ellipsoid.volume(), expected_volume, places=5)

    def test_volume_very_large_dimensions(self):
        """Tests volume calculation for very large positive dimensions."""
        # Expected volume will be very large, adjust tolerance accordingly
        expected_volume = 418879020.47864
        ellipsoid = Ellipsoid(1000, 500, 200)
        self.assertAlmostEqual(ellipsoid.volume(), expected_volume, places=5)

    def test_get_description_positive_dimensions(self):
        """Tests get_description for positive semi-axes."""
        ellipsoid = Ellipsoid(2.0, 3.0, 1.0)
        expected_description = (
            "Surface area of the ellipsoid with axis {} and {} and {} cm is {:.3f} cm2.".format(
                ellipsoid.semi_axis_a, ellipsoid.semi_axis_b, ellipsoid.semi_axis_c, round(ellipsoid.surface_area(), 3)),
            "Volume of the ellipsoid with axis {} and {} and {} cm is {:.3f} cm3.".format(
                ellipsoid.semi_axis_a, ellipsoid.semi_axis_b, ellipsoid.semi_axis_c, round(ellipsoid.volume(), 3)),
        )
        self.assertEqual(ellipsoid.get_description(), expected_description)

if __name__ == "__main__":
  unittest.main()