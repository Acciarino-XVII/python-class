import json

print("esercizio 1")
file = open("file.txt", "r")
print(file.read())
file.seek(0)
file.close()
print("----------------------------------------------------------------")

print("esercizio 2")

file = open("file.txt", "a")

file.write(input("Inserisci una linea: ") + "\n")
file.close()
file = open("file.txt", "r")
print(file.read())
file.close()
print("----------------------------------------------------------------")

print("esercizio 3")
#aprire file origine in lettura
fileorigine = open("file.txt", "r")

#aprire file destinazione in scrittura (se non esiste, viene creato)
filedestinazione = open("file2.txt", "w")

#copia del file origine in file destinazione
contenutofile = fileorigine.read()
filedestinazione.write(contenutofile)

#chiusura di destinazione
filedestinazione.close()

#apertura di file destinazione in lettura
filedestinazione = open("file2.txt", "r")
#riposrto il cursore al inizio del file
filedestinazione.seek(0)

#ristampa del contenuto del file destinazione
print("file copiato: ", )
print(filedestinazione.read())
#chiusura dei files
fileorigine.close()
filedestinazione.close()

print("----------------------------------------------------------------")

print("esercizio 4")

utente = {"nome": "Giuseppe", 
          "cognome": "Rossi", 
          "eta": 35, 
          "altezza": 1.75, 
          "brainrotted": True}

#scrittura del dizionario in un file json
x = open("file_json.json", "w")
json.dump(utente, x)
x.close()

x=open("file_json.json", "r")
print(f"Dizionario: {x.read()} scritto nel file json.")
x.close()

print("----------------------------------------------------------------")

print("esercizio 5")

file = open("file.txt", "r")
for line in file.readlines():
    print(line)
print("----------------------------------------------------------------")

print("esercizio 6")

users = {'001': "Marco", '002': "Monica", '003': "Giovanni"}

file = open("file_json.json", "a")
json.dump(users, file, indent=4)
print(f"Dizionario: {users} scritto nel file json.")

file.close()

file = open("file_json.json", "r")
print(file.read())

file.close()

print("----------------------------------------------------------------")

print("esercizio 7")

#Scrivere un programma per leggere le prime n righe di un file.

file = open("file.txt", "r")

righe = int(input("Quante righe vuoi leggere? "))

for i in range(righe):
    print(file.readline(), end="")

file.close()

print("----------------------------------------------------------------")

print("esercizio 8")

#Scrivere un programma per aggiungere testo in un file già presente e visualizzare il risultato.

file = open("file.txt", "a")

aggiunta = input("Inserisci il testo da aggiungere: ")

file.write(aggiunta + "\n")

file.close()

file = open("file.txt", "r")

print("Contenuto del file:")

for line in file.readlines():
    print(line, end="")

file.close()

print("----------------------------------------------------------------")

print("esercizio 9")

#Scrivi un programma che legga il contenuto di un file di testo
#  e lo copi in un altro file, 
# invertendo l’ordine delle righe 
# (cercare in autonomia la funzione adatta a risolvere l’esercizio).
testo = open("file.txt", "r")
testoCopia = open("file_copia.txt", "w")

righe = str(testo.read())


testoCopia.writelines(reversed(righe))

testo.close()
testoCopia.close()

testoCopia = open("file_copia.txt", "r")

print("--------------------------------")

print("esercizio 10")

#Scrivere un programma  per scrivere ogni elemento  di una lista in un file separato.

lista = ["uno", "due", "tre", "quattro", "cinque"]
    
file = open("file.txt", "a")

for i in lista:
    file.write(i + "\n")
    
file.close()

print("--------------------------------")

print("esercizio 11")

file = open("file.json", "w")

utente = {"nome": "Giuseppe", 
          "cognome": "Rossi", 
          "eta": 35, 
          "altezza": 1.75, 
          "brainrotted": True
          }

print(json.dumps(utente, indent=4, sort_keys=True))#con True ordina in modo crescente




