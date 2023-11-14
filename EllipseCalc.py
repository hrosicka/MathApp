import math

class Elipsa:
    """ 
    Třída pro vytvoření a získání vlastností elipsy

    Metody počítají obvod, obsah. Výsledky lze získat jako stringy - v tuple

    Výsledek je vypsán v centimetrech, proto musí být vstup také v centimetrech
    """
    
    def __init__(self, a, b):
        """
        Konstruktor elipsy - parametrem je poloměr r v centimetrech
        """
        self.a = a
        self.b = b

    def obvod(self):
        """
        Metoda pro výpočet obvodu elipsy v centimetrech

        Obvod elipsy: o = PI*(2*(a^2 + b^2))^1/2
        """
        obv =  math.pi * math.sqrt(math.pow(self.a, 2) + math.pow(self.b, 2),2)
        return round(obv,5)
    
    def obsah(self):
        """
        Metoda pro výpočet obsahu elipsy v centimetrech

        Obsah kruhu: S = PI*a*b
        """
        obs = math.pi * self.a * self.b
        return round(obs,5)

    def vypis(self):
        """
        Metoda pro vypsání obsahu a obvodu elipsy - v centimetrech

        Vrací 2 řetězce - tuple formát - v pořadí obvod, obsah

        Zaokrouhleno na 3 desetinná místa
        """
        textObvod = "Elipsa o poloosách {} a {} cm má obvod {} cm.".format(self.a, self.b, round(self.obvod(), 3))
        textObsah = "Elipsa o poloosách {} a {} cm má obsah {} cm2.".format(self.a, self.b, round(self.obsah(), 3))
        return(textObvod, textObsah)
