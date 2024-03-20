import math

class Sphere:
    """
    This class represents a sphere and provides methods to calculate 
    its properties like surface area, volume, and informative string descriptions.

    Attributes:
        radius (float): The radius of the sphere in centimeters.
    """
    
    def __init__(self, radius):
        """
        Initializes a Sphere object.

        Args:
            radius (float): The radius of the sphere in centimeters.

        Raises:
            TypeError: If the radius is not a number.
            ValueError: If the radius is not a positive number.
        """
        if not isinstance(radius, (int, float)):
            raise TypeError("Radius must be a number.")
        if radius <= 0:
            raise ValueError("Radius must be a positive number.")
        self.radius = radius

    def surface_area(self):
        """
        Calculates and returns the surface area of the sphere.

        Formula: surface area = 4 * pi * radius^2

        Returns:
            float: The surface area of the sphere in square centimeters, 
            rounded to 5 decimal places.
        """
        surface_area = 4 * math.pi * pow(self.radius,2)
        return round(surface_area,5)
    
    def volume(self):
        """
        Calculates and returns the volume of the sphere.

        Formula: volume = 4/3 * pi * radius^3

        Returns:
            float: The volume of the sphere in cubic centimeters, 
            rounded to 5 decimal places.
        """
        volume = 4 * math.pi*pow(self.radius, 3) / 3
        return round(volume,5)

    def get_description(self):
        """
        Returns a tuple containing two formatted strings describing the sphere's 
        surface area and volume.

        Returns:
            tuple[str, str]: A tuple containing strings that describe the sphere's 
            surface area and volume in a user-friendly format.
        """
        surface_area_info = "Sphere with radius {} cm has surface area {} cm2.".format(self.radius, round(self.surface_area(),3))
        volume_info = "Sphere with radius {} cm has volume {} cm3.".format(self.radius, round(self.volume(),3))
        return(surface_area_info, volume_info)

# help(Sphere)
