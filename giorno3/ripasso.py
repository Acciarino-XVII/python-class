print("esercizio 1")
a=float(input("inserisci il primo numero: "))

b=float(input("inserisci il secondo numero: "))

if a>b:
    print("il primo numero è maggiore")
elif a<b:
    print("il secondo numero è maggiore")
else:
    print("i due numeri sono uguali")

print("---------------------------------")

print("esercizio 2")

a=float(input("inserisci il primo numero: "))

b=float(input("inserisci il secondo numero: "))

c=float(input("inserisci il terzo numero: "))

if a>b and a>c:
    print("il primo numero è il più grande")

elif b>a and b>c:
    print("il secondo numero è il più grande")
elif c>a and c>b:
    print("il terzo numero è il più grande")
else:
    print("tutti i numeri sono uguali")

print("---------------------------------")

print("esercizio 3")
numeri=[1,2,3,4,5,6,7,8,9]
massimo=max(numeri)
print("la lista è", numeri)
print("il numero massimo nella lista è", massimo)

print("---------------------------------")

print("esercizio 4")
risultato = numeri[0]
for numero in numeri:
    risultato=risultato*numero
print("il prodotto di tutti i numeri della lista:\n", numeri,"è", risultato)

print("---------------------------------")

print("esercizio 5")
scelta=input("inserisci il valore che vuoi controllare: ")
if scelta in numeri:
    print("Il numero", scelta, "è presente nella lista")
else:
    print("Il numero", scelta, "non è presente nella lista")
#per risolvere i problemi di casting in una lista di diversi elementi:
# def converti_tipo(valore)
#     try:
#         return int(valore)
#     except ValueError:
#         try:
#             return float(valore)
#         except ValueError:
#             if valore.lower() == "true":
#                 return True #converte l'input true in booleano True
#             elif valore.lower() == "false":
#                 return False #converte l'input false in booleano False
#         return valore #se non è nessuno dei valore precedenti è una stringa, di conseguenza rimane invariato

# valore=converti_tipo(scelta)
# if valore in numeri:
#     print("il valore scelto è presente nella lista")
# else:
#     print("il valore scelto non è presente nella lista")

print("---------------------------------")

print("esercizio 6")
i=0
quadrato = float
for i in range(1,16):
    quadrato = i**2
    print("il quadrato di", i, "è", quadrato)
print("fine elaborazione")

print("---------------------------------")

print("esercizio 7")

i=0
numeri = []

for i in range(5):
    numero = float(input("inserisci il",i+1,"numero: "))
    numeri.append(numero)
somma = sum(numeri)
media = somma / len(numeri)
print("la media dei numeri è:", media)
print("la somma dei numeri è:",somma)

print("---------------------------------")
