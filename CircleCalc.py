import math

class Kruh:
    """ 
    Třída pro vytvoření a získání vlastností kruhu

    Metody počítají obvod, obsah. Výsledky lze získat jako stringy - v tuple

    Výsledek je vypsán v centimetrech, proto musí být vstup také v centimetrech
    """
    
    def __init__(self, r):
        """
        Konstruktor kruhu - parametrem je poloměr r v centimetrech
        """
        self.r = r

    def obvod(self):
        """
        Metoda pro výpočet obvodu kruhu v centimetrech

        Obvod kruhu: o = 2*PI*r
        """
        obv = 2 * math.pi * self.r
        return obv
    
    def obsah(self):
        """
        Metoda pro výpočet obsahu kruhu v centimetrech

        Obsah kruhu: S = PI*r^2
        """
        obs = math.pi * pow(self.r, 2)
        return obs

    def vypis(self):
        """
        Metoda pro vypsání obsahu a obvodu kruhu - v centimetrech

        Vrací 2 řetězce - tuple formát - v pořadí obvod, obsah

        Zaokrouhleno na 3 desetinná místa
        """
        textObvod = "Kruh o poloměru {} cm má obvod {} cm.".format(self.r, round(self.obvod(), 3))
        textObsah = "Kruh o poloměru {} cm má obsah {} cm2.".format(self.r, round(self.obsah(), 3))
        return(textObvod, textObsah)

# help(Kruh)