import math

class Koule:
    """ 
    Třída pro vytvoření a získání vlastností koule

    Metody počítají povrch, objem. Výsledky lze získat jako stringy - v tuple

    Výsledek je vypsán v centimetrech, proto musí být vstup také v centimetrech
    """
    
    def __init__(self, r):
        """
        Konstruktor koule - parametrem je poloměr r v centimetrech
        """
        self.r = r

    def povrch(self):
        """
        Metoda pro výpočet povrchu koule v centimetrech

        Povrch koule: S = 4*PI*r^2
        """
        pov = 4 * math.pi * pow(self.r,2)
        return round(pov,5)
    
    def objem(self):
        """
        Metoda pro výpočet objemu koule v centimetrech

        Objem koule: V = 4/3*PI*r^3
        """
        obj = 4 * math.pi*pow(self.r, 3) / 3
        return round(obj,5)

    def vypis(self):
        """
        Metoda pro vypsání povrchu a objemu koule - v centimetrech

        Vrací 2 řetězce - tuple formát - v pořadí povrch, objem

        Zaokrouhleno na 3 desetinná místa
        """
        textPovrch = "Koule o poloměru {} cm má povrch {} cm2.".format(self.r, round(self.povrch(),3))
        textObjem = "Koule o poloměru {} cm má objem {} cm3.".format(self.r, round(self.objem(),3))
        return(textPovrch, textObjem)

# help(Koule)