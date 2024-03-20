class Cube:
    """
    This class represents a 3D cube and provides methods to calculate its geometrical properties 
    like surface area and volume.

    Attributes:
        side_length (float): The length of a side of the cube in centimeters. 
    """
    
    def __init__(self, side_length):
        """
        Initializes a Cube object.

        Args:
            side_length (float): The positive length of a side of the cube in centimeters.

        Raises:
            TypeError: If the side_length is not a number.
            ValueError: If the side_length is not positive.
        """
        if not isinstance(side_length, (int, float)):
            raise TypeError("Side length must be a number.")
        if side_length <= 0:
            raise ValueError("Side length must be a positive number.")
        self.side_length = side_length

    def surface_area(self):
        """
        Calculates and returns the total surface area of the cube in square centimeters.

        Formula: surface area = 6 * side_length^2

        Returns:
            float: The surface area of the cube in square centimeters, rounded to 5 decimal places.
        """
        surface_area = 6 * pow(self.side_length,2)
        return round(surface_area, 5)
    
    def volume(self):
        """
        Calculates and returns the volume of the cube in cubic centimeters.

        Formula: volume = side_length^3

        Returns:
            float: The volume of the cube in cubic centimeters, rounded to 5 decimal places.
        """
        volume = pow(self.side_length, 3)
        return round(volume, 5)

    def get_description(self):
        """
        Returns a tuple containing two formatted strings describing the cube's surface area and volume.

        Returns:
            tuple[str, str]: A tuple containing user-friendly descriptions of the cube's surface area 
                            and volume in square centimeters and cubic centimeters respectively.
        """
        surface_area_info = "Cube with side length {} cm has surface area {} cm2.".format(self.side_length, round(self.surface_area(),3))
        volume_info = "Cube with side length {} cm has volume {} cm3.".format(self.side_length, round(self.volume(),3))
        return(surface_area_info, volume_info)

# help(Cube)