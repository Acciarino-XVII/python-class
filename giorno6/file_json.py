import json

x ='{"nome": "mario", "cognome": "Rossi", "eta": 30}'

#per trasformare una stringa json in un dicti utilizzo la funzione loads()
y = json.loads(x)
print(y)
print(type(y))

#per fare l'inverso, utilizzo la funzione dumps()
j =  json.dumps(y)

print(j)
print(type(j))

#quali altri tipi di dato posso convertire in json?

#lists
print(json.dumps(["ciao", "malloppo", "mela"]))

#tuple
print(json.dumps(("ciao", "malloppo", "mela")))

#strnghe
print(json.dumps(("ciao malloppo mela")))
#int float e bool
utente = {"nome": "Giuseppe", 
          "cognome": "Rossi", 
          "eta": 35, 
          "altezza": 1.75, 
          "brainrotted": True}

#dumps accetta acnhe dei parametri
#parametro indendt m----> iindenta le coppie chiave-valore
print(json.dumps(utente, indent=4))

#parametro separetors, --> modifica il separatore chiave-valore
#primo parametro separa le coppie chiave valore, il secondo separa chiave e valore
print(json.dumps(utente, indent=4, separators=(",","|")))

#parametro sort_keys -->serve a ordinarere le chaìavi in ordine cresencte o decrescente 
print(json.dumps(utente, indent=4, separators=(",","|"), sort_keys=True))#con True ordina in modo crescente


