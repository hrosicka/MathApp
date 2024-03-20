import math

class Circle:
    """
    This class represents a circle and provides methods to calculate 
    its properties like circumference, area, and informative string descriptions.

    Attributes:
        radius (float): The radius of the circle in centimeters.
    """
    
    def __init__(self, radius):
        """
        Initializes a Circle object.

        Args:
            radius (float): The radius of the circle in centimeters.

        Raises:
            TypeError: If the radius is not a number.
            ValueError: If the radius is not a positive number.
        """
        if not isinstance(radius, (int, float)):
            raise TypeError("Radius must be a number.")
        if radius <= 0:
            raise ValueError("Radius must be a positive number.")
        self.radius = radius

    def circumference(self):
        """
        Calculates and returns the circumference of the circle.

        Formula: circumference = 2 * pi * radius

        Returns:
            float: The circumference of the circle in centimeters, rounded to 5 decimal places.
        """
        circumference = 2 * math.pi * self.radius
        return round(circumference,5)
    
    def area(self):
        """
        Calculates and returns the area of the circle.

        Formula: area = pi * radius^2

        Returns:
            float: The area of the circle in square centimeters, rounded to 5 decimal places.
        """
        area = math.pi * pow(self.radius, 2)
        return round(area,5)

    def get_description(self):
        """
        Returns a tuple containing two formatted strings describing the circle's 
        circumference and area.

        Returns:
            tuple[str, str]: A tuple containing strings that describe the circle's circumference 
                            and area in a user-friendly format.
        """
        info_circumference = "Circle with radius {} cm has circumference {} cm.".format(self.radius, round(self.circumference(), 3))
        info_area = "Circle with radius {} cm has area {} cm2.".format(self.radius, round(self.area(), 3))
        return(info_circumference, info_area)

# help(Circle)
