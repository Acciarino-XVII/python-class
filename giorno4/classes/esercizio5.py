class veicolo:
    def __init__ (self, marca, modello, anno):
        self.marca = marca
        self.modello = modello
        self.anno = anno
    def accellera(self):
        print("accellera")
    def frena(self):
        print("frena")
    def __str__(self):
        return f"{self.marca} {self.modello} {self.anno}"

class auto(veicolo):
    def __init__ (self, marca, modello, anno, colore):
        super().__init__(marca, modello, anno)
        self.colore = colore
    def cambia_colore(self):
        nuovo_colore = input("inserisci il nuovo colore ")
        self.colore = nuovo_colore
    def __str__(self):
        return f"{super().__str__()} - colore: {self.colore}" #ritorna tutti gli attributi di veicolo + colore


#esempio di utilizzo       

auto1 = auto("nissan", 
             "gtr-r34",
             1999, 
             "midnight purple" )
print(auto1)

auto1.cambia_colore()
print(auto1)