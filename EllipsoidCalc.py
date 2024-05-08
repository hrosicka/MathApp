import math

class Ellipsoid:
    """
    This class represents an ellipsoid and provides methods to calculate its geometrical properties 
    like surface area and volume. Unlike an ellipse, an ellipsoid does not have a major and minor axis.

    Attributes:
        semi_axis_a (float): The length of the first semi-axis of the ellipsoid in centimeters.
        semi_axis_b (float): The length of the second semi-axis of the ellipsoid in centimeters.
        semi_axis_c (float): The length of the third semi-axis of the ellipsoid in centimeters.
    """
    
    def __init__(self, semi_axis_a, semi_axis_b, semi_axis_c):
        """
        Initializes an Ellipsoid object.

        Args:
            semi_axis_a (float): The positive length of the first semi-axis of the ellipsoid in centimeters.
            semi_axis_b (float): The positive length of the second semi-axis of the ellipsoid in centimeters.
            semi_axis_c (float): The positive length of the third semi-axis of the ellipsoid in centimeters.

        Raises:
            TypeError: If any of the semi-axes are not numbers.
            ValueError: If any of the semi-axes are not positive.
        """
        if not isinstance(semi_axis_a, (int, float)):
            raise TypeError("Semi-axis a must be a number.")
        if semi_axis_a <= 0:
            raise ValueError("Semi-axis a must be positive.")
        if not isinstance(semi_axis_b, (int, float)):
            raise TypeError("Semi-axis b must be a number.")
        if semi_axis_b <= 0:
            raise ValueError("Semi-axis b must be positive.")
        if not isinstance(semi_axis_c, (int, float)):
            raise TypeError("Semi-axis c must be a number.")
        if semi_axis_c <= 0:
            raise ValueError("Semi-axis c must be positive.")
        self.semi_axis_a = semi_axis_a
        self.semi_axis_b = semi_axis_b
        self.semi_axis_c = semi_axis_c

    def surface_area(self):
        """
        Calculates and returns the surface area of the ellipsoid.

        Returns:
        float: The surface area of the ellipsoid in square centimeters.
        """
        surface_area = 4 * math.pi * pow((pow(self.semi_axis_a * self.semi_axis_b, 1.6075) + pow(self.semi_axis_a * self.semi_axis_c, 1.6075)
                                            + pow(self.semi_axis_b * self.semi_axis_c, 1.6075)) / 3, 1 / 1.6075);
        return round(surface_area, 5)
    
    def volume(self):
        """
        Calculates and returns the volume of the ellipsoid in cubic centimeters.

        Formula: 4/3 * PI * radius_a * radius_b * radius_c

        Returns:
            float: The volume of the ellipsoid in cubic centimeters, rounded to 5 decimal places.
        """
        volume = (4 / 3) * math.pi * self.semi_axis_a * self.semi_axis_b * self.semi_axis_c
        return round(volume, 5)

    def get_description(self):
        """
        Returns a tuple containing two formatted strings describing the ellipse's circumference and area.

        Returns:
            tuple[str, str]: A tuple containing user-friendly descriptions of the ellipse's circumference 
                            and area in centimeters and square centimeters respectively.
        """
        surface_area_info = "Surface area of the ellipsoid with axis {} and {} and {} cm is {:.3f} cm2.".format(self.semi_axis_a, self.semi_axis_b, self.semi_axis_c, round(self.surface_area(), 3))
        volume_info = "Volume of the ellipsoid with axis {} and {} and {} cm is {:.3f} cm3.".format(self.semi_axis_a, self.semi_axis_b, self.semi_axis_c, round(self.volume(), 3))
        return(surface_area_info, volume_info)