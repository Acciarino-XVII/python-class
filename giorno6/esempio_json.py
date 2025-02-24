import json

cliente = {"nome": "Giuseppe", "cognome": "Rossi", "eta": 35, "articoli": ["tavolo", "lampada", "letto"]}

nuovo = open("test.json", "w")
json.dump(cliente, nuovo)
#chiudo il file
nuovo.close()

#accedo in lettura al file

file=open("test.json", "r")
dati = json.load(file)

print(dati)
#chisura file
file.close()

#---------AGGIORNO JSON----------

file =  open("test.json", "r"+)
#r+ accesso sia in leettura che  scrittura

#trasforare in dict
dati= json.load(file)
#aggiornare in dic
    
#converitrein json