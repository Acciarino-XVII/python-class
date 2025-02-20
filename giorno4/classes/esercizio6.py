class Cibo:
    def __init__(self, nome):
        self.__nome = nome
    def get_nome(self):
        
        return self.__nome


#CLASSE VEGETALE DERIVA DA CIBO
class Vegetale(Cibo):
    def __init__(self, nome, tipo):
        super().__init__(nome)
        self.__tipo = tipo
    def get_tipo(self):
       
        return self.__tipo


#SOTTOCLASSI DI VEGETALE
class Frutta(Vegetale):
    def __init__(self, nome):
        super().__init__(nome, "Frutto")
    
    def get_frutta_info(self):   
       
        return f"{self.get_nome()} è un {self.get_tipo()}"        
    
    

class Verdura(Vegetale):
    def __init__(self,nome):
        super().__init__(nome, "verdura")
    
    def get_verdura_info(self):
      
        return f"{self.get_nome()} è una {self.get_tipo()}"
    

#CLASSE ANIMALE CHE EREDITA DA CIBO
class  Animale(Cibo):
    def __init__(self, nome, tipo):
        super().__init__(nome)
        self.__tipo = tipo
        
    def get_tipo(self):
        return self.__tipo

#CLASSE PESCE CEH DERIVA DA ANIMALE
class Pesce(Animale):
    def __init__(self, nome):
        super().__init__(nome, "Pesce")
    
    def get_pesce_info(self):
        
        return f"{self.get_nome()} è un {self.get_tipo()}"
        
        
#CLASSE CARNE CHE EREDITA DA ANIMALE
class Carne(Animale):
    def __init__(self,nome):
        super().__init__(nome, "Carne")
        
    def get_carne_info(self):
        
        return f"{self.get_nome()} è un tipo di {self.get_tipo()}"


#ESEMPIO DI UTILIZZO

# Creazione di oggetti per testare il codice
mela = Frutta("Mela")
carota = Verdura("Carota")
salmone = Pesce("Salmone")
bistecca = Carne("Bistecca")

# Stampa delle info per ognuno

print(mela.get_frutta_info())
print(carota.get_verdura_info())
print(salmone.get_pesce_info())
print(bistecca.get_carne_info())