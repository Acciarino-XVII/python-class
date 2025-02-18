#esercizio 1
print("esercizio 1")
numero1= int(input("inserisci un numero "))
if numero1 > 0: 
    print("il numero è positivo")
print("-------------------------------")

print("esercizio2")
numero1=int(input("inserire un numero:  "))
numero2= int(input("inserire il secondo numero: "))
if numero1 > numero2:
    print("il primo numero è maggiore ")
print("il secondo numero è maggiore")
print("-------------------------------")

print("esercizio 3")
string=str(input("inserisci una stringa "))
if len(string) == 0:
    print("la stringa è vuota")
print("la stringa non è vuota")
print("-------------------------------")

print("esercizio 4")
numero1=int(input("inserisci il numero "))
if numero1 % 2 == 0:
    print("il numero è pari")
print("il numero è dispari ")
print("-------------------------------")

print("esercizio 5")
char=str(input("inserisci una lettera "))
if char == "a" or "e" or "i" or "o" or "u":
    print("la lettera è una vocale")
print("la lettera è una consonante")
print("-------------------------------")


print("esercizio 6")
numero1 = int(input("inserisci un numero "))
if 1>=numero1<=10:
    print("il numero è compreso tra 1 e 10")
print("il numero non è compreso tra 1 e 10")
print("-------------------------------")

print("esercizio 7")
numero1 = int(input("inserisci un numero: "))
if numero1>=10:
    print("il numero è  maggiore di 10")
elif numero1 == 10:
    print("il numero è uguale a 10")
elif numero1 < 10:
    print("il numero è minore di 10")
print("-------------------------------")



