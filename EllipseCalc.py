import math

class Ellipse:
    """
    This class represents an ellipse and provides methods to calculate its properties like circumference and area.

    Attributes:
        semi_major_axis (float): The length of the semi-major axis of the ellipse in centimeters.
        semi_minor_axis (float): The length of the semi-minor axis of the ellipse in centimeters.
    """
    
    def __init__(self, semi_major_axis, semi_minor_axis):
        """
        Initializes an Ellipse object.

        Args:
            semi_major_axis (float): The positive length of the semi-major axis of the ellipse in centimeters.
            semi_minor_axis (float): The positive length of the semi-minor axis of the ellipse in centimeters.

        Raises:
            TypeError: If either axis length is not a number.
            ValueError: If either axis length is not positive.
        """
        if not isinstance(semi_major_axis, (int, float)):
            raise TypeError("Semi-major axis length must be a number.")
        if semi_major_axis <= 0:
            raise ValueError("Semi-major axis length must be positive.")
        if not isinstance(semi_minor_axis, (int, float)):
            raise TypeError("Semi-minor axis length must be a number.")
        if semi_minor_axis <= 0:
            raise ValueError("Semi-minor axis length must be positive.")
        self.semi_major_axis = semi_major_axis
        self.semi_minor_axis = semi_minor_axis

    def circumference(self):
        """
        Calculates and returns the circumference of the ellipse in centimeters.

        Formula: circumference = 2 * PI * sqrt(2 * (a^2 + b^2))

        Returns:
            float: The circumference of the ellipse in centimeters, rounded to 5 decimal places.
        """
        circumference =  math.pi * math.sqrt(2*(math.pow(self.semi_major_axis, 2) + math.pow(self.semi_minor_axis, 2)))
        return round(circumference,5)
    
    def area(self):
        """
        Calculates and returns the area of the ellipse in square centimeters.

        Formula: area = PI * a * b

        Returns:
            float: The area of the ellipse in square centimeters, rounded to 5 decimal places.
        """
        area = math.pi * self.semi_major_axis * self.semi_minor_axis
        return round(area,5)

    def get_description(self):
        """
        Returns a tuple containing two formatted strings describing the ellipse's circumference and area.

        Returns:
            tuple[str, str]: A tuple containing user-friendly descriptions of the ellipse's circumference 
                            and area in centimeters and square centimeters respectively.
        """
        info_circumference = "Ellipse with axis {} and {} cm has circumference {} cm.".format(self.semi_major_axis, self.semi_minor_axis, round(self.circumference(), 3))
        info_area = "Ellipse with axis {} a {} cm and has area {} cm2.".format(self.semi_major_axis, self.semi_minor_axis, round(self.area(), 3))
        return(info_circumference, info_area)
