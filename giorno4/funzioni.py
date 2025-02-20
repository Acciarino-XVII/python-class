def esercizio1(lista):
    #scrivi una fun. che prende in input una lista di numer
    #e resriruisce la somma di tutti gli elementi
    return sum(lista)

def esercizio2(stringa):
    #scrivi una fun. che prende in input una strina 
    #e restituisce la stringa invertita
    n=len(stringa)+1
    i=-1
    inverted=[]
    while i > n*-1:
        inverted.append(stringa[i])
        i -= 1
    return ''.join(inverted)
    
stringa = input("inserisci la stringa: ")
stringa = esercizio2(stringa)
print(stringa)

#esercizio 2 semplificato
def esercizio2semplificato(stringa):
    return stringa[::-1]

def esercizio3(lista, lettera):
    parole_filt = []
    lettera =lettera.lower()
    
    for parola in lista:
        if parola.lower().startswith(lettera):
            parole_filt.append(parola)
    
    return parole_filt
lista=["banana","ananas","mela"]
lettera = input("inserisci la lettera da filtrare: ")
print(esercizio3(lista,lettera))
#----------------------------------------------------------------
listanum=[1,2,3,4,5,6,7,8,9]
def esercizio4(lista):
    numparo=[]
    for num in lista:
        if num % 2 == 0:
            numparo.append(num)
    return numparo

print(esercizio4(listanum))

#----------------------------------------------------------------

def esercizio5(lista):
    lunghezza = int
    for elemento in lista:
        lunghezza +=1
    return lunghezza
stringa=input("inserisci una stringa")
listaes5 = ["banana",1,2,3,4]
print("La lunghezza della stringa è:", esercizio5(stringa))
print("la lunghezza della lista_es5 è:",esercizio5(listaes5))

#esercizio 6
def esercizio6(lista):
    return max(lista)

print("Il numero massimo nella lista_es5 è:", esercizio6(listaes5))

#----------------------------------------------------------------

#esercizio 7
def esercizio7(lista):
    lunghezzaMax = 0
    for parola in lista:
        if len(parola)>lunghezzaMax:
            lunghezzaMax = len(parola)
    return lunghezzaMax

print("La parola più lunga nella lista è:", esercizio7(lista))

#----------------------------------------------------------------

def esercizio8(lista):
    somma = sum(lista)
    media = somma / len(lista)
    return media

print("La media dei numeri nella lista è:", esercizio8(listanum))

#----------------------------------------------------------------

def esercizio9(stringa):
    key = ""
    value = ""
    dizionario=dict({})
    for lettera in stringa:
        value=stringa.count(lettera)
        key=lettera
        dizionario.update({key:value})
    return dizionario
stringa = input("inserisci una stringa: ")

print("Il dizionario è:", esercizio9(stringa))

#----------------------------------------------------------------

def esercizio10(metri):
    # Fattori di conversione
    conversioni = {
        "miglia": metri / 1609.344,
        "iarde": metri * 1.09361,
        "piedi": metri * 3.28084,
        "pollici": metri * 39.3701
    }
    return conversioni  # Restituiamo il dizionario con le conversioni

# Esempio di utilizzo
metri = float(input("Inserisci il valore in metri: "))
risultati = esercizio10(metri)

# Stampiamo i risultati
print("Conversioni:")
for unita, valore in risultati.items():
    print(f"{unita.capitalize()}: {valore:.4f}")
        
        
