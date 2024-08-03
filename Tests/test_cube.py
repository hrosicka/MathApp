import unittest
import sys

# setting path
sys.path.append('../PyQtMathApp')
from CubeCalc import *


class TestSquare(unittest.TestCase):

    def test_init_valid_side_length(self):
        """Tests initialization with a valid positive side length."""
        cube = Cube(5.526)
        self.assertEqual(cube.side_length, 5.526)

    def test_init_zero_side_length(self):
        """Tests initialization with a zero side length (raises ValueError)."""
        with self.assertRaises(ValueError) as error:
            Cube(0.0)
        self.assertEqual(str(error.exception), "Side length must be a positive number.")

    def test_init_negative_side_length(self):
        """Tests initialization with a negative side length (raises ValueError)."""
        with self.assertRaises(ValueError) as error:
            Cube(-2.5)
        self.assertEqual(str(error.exception), "Side length must be a positive number.")

    def test_init_non_numeric_side_length(self):
        """Tests initialization with a non-numeric side length (raises TypeError)."""
        with self.assertRaises(TypeError) as error:
            Cube("test hello")
        self.assertEqual(str(error.exception), "Side length must be a number.")

    def test_surface_area_positive_side_length(self):
        """Tests surface area calculation for a positive side length."""
        cube = Cube(3.0)
        expected_surface_area = 6 * 3.0**2
        self.assertAlmostEqual(cube.surface_area(), expected_surface_area, places=5)

    def test_volume_positive_side_length(self):
        """Tests volume calculation for a positive side length."""
        cube = Cube(4.0)
        expected_volume = 4.0**3
        self.assertAlmostEqual(cube.volume(), expected_volume, places=5)

    def test_surface_area_very_small_side_length(self):
        """Tests surface area calculation for a very small positive side length."""
        cube = Cube(0.000001)  # Extremely small side length
        expected_surface_area = 6 * 0.000001**2
        self.assertAlmostEqual(cube.surface_area(), expected_surface_area, places=5)

    def test_surface_area_very_large_side_length(self):
        """Tests surface area calculation for a very large positive side length."""
        cube = Cube(1000000.0)  # Extremely large side length
        expected_surface_area = 6 * 1000000.0**2
        self.assertAlmostEqual(cube.surface_area(), expected_surface_area, places=5)

    def test_volume_very_small_side_length(self):
        """Tests volume calculation for a very small positive side length."""
        cube = Cube(0.000001)  # Extremely small side length
        expected_volume = 0.000001**3
        self.assertAlmostEqual(cube.volume(), expected_volume, places=5)

    def test_volume_very_large_side_length(self):
        """Tests volume calculation for a very large positive side length."""
        cube = Cube(1000000.0)  # Extremely large side length
        expected_volume = 1000000.0**3
        self.assertAlmostEqual(cube.volume(), expected_volume, places=5)

    def test_get_description_positive_side_length(self):
        """Tests get_description for a positive side length."""
        cube = Cube(2.5)
        expected_description = (
            "Cube with side length 2.5 cm has surface area 37.5 cm2.",
            "Cube with side length 2.5 cm has volume 15.625 cm3.",
        )
        self.assertEqual(cube.get_description(), expected_description)

if __name__ == "__main__":
    unittest.main()