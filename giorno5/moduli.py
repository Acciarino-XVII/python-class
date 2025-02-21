import math
import random
import altro_modulo as Am
import modulo as m
import datetime
#esercizio 1
#calcola la radice quadrata di un numero
def radiceQuad(numero):
    return math.sqrt(numero)
numero = float(input("Inserisci un numero: "))

print(radiceQuad(numero))

print("---------------------------------")
#esercizio 2
#genera un numero casuale tra 1 10

numeroCasuale = random.randint(1, 10)
print("Numero casuale tra 1 e 10: ", numeroCasuale)

print("---------------------------------")
#esercizio 3



for numero in m.lista_numeri:
    print(numero)

print("---------------------------------")

#esercizio 4

for numero in Am.lista_numeri:
    print(numero)

print("---------------------------------")

#esercizio 5

datacorrente = datetime.datetime.now()
print("Data corrente: ", datacorrente)
print("---------------------------------")

#esercizio 6
print("stampare L in formato dd/mm/yyyy")
datacorrente = datetime.datetime.now()
datacorrente = datacorrente.strftime("%d/%m/%Y")
print("Data corrente: ", datacorrente)

#esercizio 7
print("differenza tra due date")
def chiedi_data():
    data_str = input("Inserisci una data nel formato dd/mm/yyyy: ")
    return datetime.datetime.strptime(data_str, "%d/%m/%Y")

#chiedi all'utente di inserire le due date

data1 = chiedi_data()
data2 = chiedi_data()

if data1 > data2:
    differenza = data1 - data2
    print("La differenza è: ", differenza.days, "giorni")
else:
    differenza = data2 - data1
    print("La differenza è: ", differenza.days, "giorni")

print("---------------------------------")

#esercizio 8
numero = float(input("inserisci un numero: "))
print(pow(numero, 3))

print("---------------------------------")

#esercizio 9
numero = 25
print(math.sqrt(numero))

print("---------------------------------")

#esercizio 10
numero = 10.4
print("il numero prima del round è", numero)
print("il numero dopo il round è", math.floor(numero))

print("---------------------------------")

#esercizio 11
numero = 10.4

print("Il numero prima della conversione in intero è", numero)
print("il numero dopo la conversione in intero è", math.ceil(numero))


print("---------------------------------")

#esercizio 12  

numero = 10

print("Il numero prima del fattoriale è:", numero)
print("il numero dopo il fattoriale è : ", math.factorial(numero))

print("---------------------------------")

#esercizio 13
lista = [1, 2, 3, 4, 5]
print("la lista è: ", lista)
print("argomento randommico lista:" , random.choice(lista))

print("---------------------------------")

#esercizio 14

def estrai_elemento_random(seq):
    if isinstance(seq, dict):  # Se la sequenza è un dizionario
        # Estrai una chiave casuale e restituisci la coppia chiave-valore
        chiave = random.choice(list(seq.keys()))
        return chiave, seq[chiave]
    else:
        # Per le altre sequenze (liste, tuple, etc.)
        return random.choice(seq)

# Lista, dizionario e insieme
lista = [1, 2, 3, 4, 5]
dictionary = {"nome": "Mario", "cognome": "Rossi", "eta": 30}
insieme = (1, 2, 3, 4, 5)

# Stampa i risultati
print("elemento estratto da lista:", estrai_elemento_random(lista))
print("elemento estratto da dizionario:", estrai_elemento_random(dictionary))
print("elemento estratto da insieme:", estrai_elemento_random(insieme))

print("---------------------------------")

#esercizio 15
random1 = random.randint(0,6)
random2 = random.randint(5,10)
random3 = random.randrange(0,11,3)
data1 = chiedi_data()
data2 = chiedi_data()

#data casuale tra due date

def random_date(data1, data2):
    # Verifica che data1 sia la data più recente
    if data1 > data2:
        delta = data1 - data2
        giorni_casuali = random.randint(1, delta.days)
        return data2 + datetime.timedelta(days=giorni_casuali)
    
    # Verifica che data2 sia la data più recente
    elif data2 > data1:
        delta = data2 - data1
        giorni_casuali = random.randint(1, delta.days)
        return data1 + datetime.timedelta(days=giorni_casuali)
    
    # Se sono uguali, restituisci la data
    else: 
        return data1

# Esempio di date
data1 = datetime.date(2025, 5, 1)
data2 = datetime.date(2025, 6, 1)

# Stampa una data casuale tra data1 e data2
print(random_date(data1, data2))

print("---------------------------------")

#esercizio 16
print("lista: ", lista)
lista = random.shuffle(lista)
print("lista shuffled: ", lista)

print("---------------------------------")

#esercizio 17
numfloar = random.uniform(0,1)
print("numero float casuale tra 0 e 1: ", numfloar)

print("---------------------------------")

#esercizio 18

#Scrivere un programma Python per creare una lista di numeri interi casuali e selezionare casualmente più elementi da tale lista.

#esercizio 19

def stampa_data_corrente():
    datacorrente = datetime.datetime.now()
    return datacorrente.strftime("%d/%m/%Y/%H:%M:%S")


def stampa_anno_corrente():
    datacorrente = datetime.datetime.now()
    return datacorrente.year()

def stampa_mese_corrente():
    datacorrente = datetime.datetime.now()
    return datacorrente.month()

def stampanumero_settimana_corrente():
    datacorrente = datetime.datetime.now()
    return datacorrente.weekday()
def stampa_giorno_settimana_corrente():
    datacorrente = datetime.datetime.now()
    return datacorrente.day()
def stampa_giorno_dell_anno():
    datacorrente = datetime.datetime.now()
    return datacorrente.dayofyear()
def stampa_giorno_del_mese():
    datacorrente = datetime.datetime.now()
    return datacorrente.dayofmonth()

def stampa_giorno_della_settimana():
    datacorrente = datetime.datetime.now()
    return datacorrente.weekday() + 1

print("data corrente completa:", stampa_data_corrente()   )
print("anno corrente:", stampa_anno_corrente())
print("mese corrente:", stampa_mese_corrente())
print("numero settimana corrente:", stampanumero_settimana_corrente())
print("gionro della settimana corrente:", stampa_giorno_settimana_corrente())
print("giorno dell'anno corrente:", stampa_giorno_dell_anno())
print("giorno del mese corrente:", stampa_giorno_del_mese())
print("giorno della settimana corrente:", stampa_giorno_della_settimana())

print("---------------------------------")


