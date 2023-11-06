class Krychle:
    """ 
    Třída pro vytvoření a získání vlastností krychle

    Metody počítají povrch, objem. Výsledky lze získat jako stringy - v tuple

    Výsledek je vypsán v centimetrech, proto musí být vstup také v centimetrech
    """
    
    def __init__(self, a):
        """
        Konstruktor krychle - parametrem je strana a v centimetrech
        """
        self.a = a

    def povrch(self):
        """
        Metoda pro výpočet povrchu krychle v centimetrech

        Povrch krychle: S = 6*a*^2
        """
        pov = 6 * pow(self.a,2)
        return round(pov, 5)
    
    def objem(self):
        """
        Metoda pro výpočet objemu krychle v centimetrech

        Objem krychle: V = a^3
        """
        obj = pow(self.a, 3)
        return round(obj, 5)

    def vypis(self):
        """
        Metoda pro vypsání povrchu a objemu krychle - v centimetrech

        Vrací 2 řetězce - tuple formát - v pořadí povrch, objem

        Zaokrouhleno na 3 desetinná místa
        """
        textPovrch = "Krychle o hraně {} cm má povrch {} cm2.".format(self.a, round(self.povrch(),3))
        textObjem = "Krychle o hraně {} cm má objem {} cm3.".format(self.a, round(self.objem(),3))
        return(textPovrch, textObjem)

# help(Krychle)