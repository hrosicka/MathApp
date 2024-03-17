import math

class Kruh:
    """
    Class representing a circle. 
    It allows calculating the circumference, area, and other properties.

    Attributes:
        radius (float): The radius of the circle in centimeters.

    Methods:
        obvod() -> float: Returns the circumference of the circle in centimeters.
        obsah() -> float: Returns the area of the circle in square centimeters.
        vypis() -> tuple[str, str]: Returns a pair of strings with information about the circle (circumference, area).
    """
    
    def __init__(self, r):
        """
        Konstruktor kruhu - parametrem je poloměr r v centimetrech
        """
        self.r = r

    def obvod(self):
        """
        Calculates and returns the circumference of the circle.

        Formula: circumference = 2 * PI * radius

        Returns:
            float: The circumference of the circle in centimeters.
        """
        obv = 2 * math.pi * self.r
        return round(obv,5)
    
    def obsah(self):
        """
        Calculates and returns the area of the circle.

        Formula: area = PI * radius^2

        Returns:
            float: The area of the circle in square centimeters.
        """
        obs = math.pi * pow(self.r, 2)
        return round(obs,5)

    def vypis(self):
        """
        Returns a pair of strings with information about the circle (circumference, area).

        Returns:
            tuple[str, str]: A pair of strings with information about the circle's circumference and area.
        """
        textObvod = "Kruh o poloměru {} cm má obvod {} cm.".format(self.r, round(self.obvod(), 3))
        textObsah = "Kruh o poloměru {} cm má obsah {} cm2.".format(self.r, round(self.obsah(), 3))
        return(textObvod, textObsah)

# help(Kruh)