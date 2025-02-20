#esercizio 1
class persona:
    def __init__(self, nome, eta, sesso, ):
        self.nome = nome
        self.eta = eta
        self.sesso = sesso
    def presentati(self):
        return (f"Ciao mi chiamo {self.nome}, ed ho {self.eta}")

persona1 = persona("marco",20, "maschio")
print(persona1.presentati())

print("----------------------------------------------------------------")

#esercizio 2

class animale():
    def __init__(self, nome, specie, ):
        self.nome = nome
        self.specie = specie

    def verso(self):
        versi = {
            "gatto": "Miao!",
            "cane": "Bau!",
            "mucca": "Muuu!",
            "pecora": "Beeeh!",
            "leone": "Roar!"
        }
        return versi.get(self.specie, "Non ho un verso per questa specie")

animale1=animale("giorgio", "gatto") 
print(animale1.verso())

print("----------------------------------------------------------------")

#esercizio 3
class automobile:
    def __init__(self,marca, modello, anno):
        self.marca = marca
        self.modello = modello
        self.anno = anno
    
    def stampa_dati(self):
        return(f"questa macchina è una: {self.marca} {self.modello} del {self.anno}")
automobile1 = automobile("nissan", "micra", "2007")

print(automobile1.stampa_dati())

print("----------------------------------------------------------------")

#esercizio 4
class impiegato:
    def __init__(self, nome, cognome, matricola, stipendio):
        self.nome = nome
        self.cognome = cognome
        self.matricola = matricola
        self.stipendio = stipendio
    def aumentoStipendio(self):
        self.aumento = (self.stipendio * 10) / 100
        self.stipendio += self.aumento
        return self.stipendio 

impiegato1 = impiegato("Mario", "Rossi", "12345", 3000)
print(f"stipendio {impiegato1.stipendio} stipendio con aumento: {impiegato1.aumentoStipendio()}")

print("----------------------------------------------------------------")
