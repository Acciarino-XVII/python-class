class Animale:
    def __init__(self, nome):
        self.__nome = nome  # Attributo privato

    def get_nome(self):
        return self.__nome  # Metodo per ottenere il nome dell'animale

    def descrizione(self):
        return f"{self.__nome} è un animale."


# **Classi per i vertebrati**
class Vertebrato(Animale):
    def __init__(self, nome):
        super().__init__(nome)

    def descrizione(self):
        return f"{self.get_nome()} è un vertebrato."


class Mammifero(Vertebrato):
    def descrizione(self):
        return f"{self.get_nome()} è un mammifero."


class Uccello(Vertebrato):
    def descrizione(self):
        return f"{self.get_nome()} è un uccello."


class Rettile(Vertebrato):
    def descrizione(self):
        return f"{self.get_nome()} è un rettile."


class Pesce(Vertebrato):
    def descrizione(self):
        return f"{self.get_nome()} è un pesce."


class Anfibio(Vertebrato):
    def descrizione(self):
        return f"{self.get_nome()} è un anfibio."


# **Classi per gli invertebrati**
class Invertebrato(Animale):
    def __init__(self, nome):
        super().__init__(nome)

    def descrizione(self):
        return f"{self.get_nome()} è un invertebrato."


class Verme(Invertebrato):
    def descrizione(self):
        return f"{self.get_nome()} è un verme."


class Mollusco(Invertebrato):
    def descrizione(self):
        return f"{self.get_nome()} è un mollusco."


class Antropode(Invertebrato):
    def descrizione(self):
        return f"{self.get_nome()} è un antropode."


# **Sottoclassi di Antropode**
class Crostaceo(Antropode):
    def descrizione(self):
        return f"{self.get_nome()} è un crostaceo."


class Insetto(Antropode):
    def descrizione(self):
        return f"{self.get_nome()} è un insetto."


class Aracnide(Antropode):
    def descrizione(self):
        return f"{self.get_nome()} è un aracnide."


# **Esempi di oggetti**
cane = Mammifero("Cane")
aquila = Uccello("Aquila")
serpente = Rettile("Serpente")
tonno = Pesce("Tonno")
rana = Anfibio("Rana")
lombrico = Verme("Lombrico")
polpo = Mollusco("Polpo")
granchio = Crostaceo("Granchio")
ape = Insetto("Ape")
ragno = Aracnide("Ragno")

# **Stampa delle descrizioni**
print(cane.descrizione())
print(aquila.descrizione())
print(serpente.descrizione())
print(tonno.descrizione())
print(rana.descrizione())
print(lombrico.descrizione())
print(polpo.descrizione())
print(granchio.descrizione())
print(ape.descrizione())
print(ragno.descrizione())
