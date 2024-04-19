class Square:
    """
    This class represents a square and provides methods to calculate 
    its properties like perimeter, area, and informative string descriptions.

    Attributes:
        side_length (float): The side length of the square in centimeters.
    """
    
    def __init__(self, side_length):
        """
        Initializes a Square object.

        Args:
            side_length (float): The side length of the square in centimeters.

        Raises:
            TypeError: If the side_length is not a number.
            ValueError: If the side_length is not a positive number.
        """
        if not isinstance(side_length, (int, float)):
            raise TypeError("Side length must be a number.")
        if side_length <= 0:
            raise ValueError("Side length must be a positive number.")
        self.side_length = side_length

    def circumference(self):
        """
        Calculates and returns the circumference (perimeter) of the square.

        Formula: circumference = 4 * side_length

        Returns:
            float: The circumference (perimeter) of the square in centimeters, 
            rounded to 5 decimal places.
        """
        circumference = 4 * self.side_length
        return round(circumference,5)
    
    def area(self):
        """
        Calculates and returns the area of the square.

        Formula: area = side_length^2

        Returns:
            float: The area of the square in square centimeters, 
            rounded to 5 decimal places.
        """
        area = pow(self.side_length, 2)
        return round(area,5)

    def get_description(self):
        """
        Returns a tuple containing two formatted strings describing the square's 
        circumference and area.

        Returns:
            tuple[str, str]: A tuple containing strings that describe the square's circumference 
            and area in a user-friendly format.
        """
        info_circumference = "Square with side length {} cm has circumference {} cm.".format(self.side_length, round(self.circumference(), 3))
        info_area = "Square with side length {} cm has area {} cm2.".format(self.side_length, round(self.area(), 3))
        return(info_circumference, info_area)
    
# help(Square)
