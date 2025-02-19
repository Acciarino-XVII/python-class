import random

print("esercizio 1")
i=1
while i < 11:
    print(i)
    i+=1
print("-----------------------------------")

print("esercizio 2")
i=0
n=int(input("inserisci il numero n dei primi numeri "))
num=0
while i < n:
    num=i+num
    print("somma= ",num)
    i+=1

print("esercizio 3")
i=2
n=10
while i < n:
    print(i)
    i +=2

print("-----------------------------------")


print("esercizio 4")
numero=random.randint(1,10)
print(numero)
scelta=0
while scelta != numero:
    scelta=int(input("indovina il numero "))
    print("non hai indovinato")
print("hai indovinato")
print("-----------------------------------")

print("esercizio 5 ")

print("")
str=input("inserisci una stringa ")
n=len(str)+1
i=-1
while i > n*-1:
    print(str[i],end="")
    i -= 1
print()
print("-----------------------------------")


print("esercizio 6")
i=11
n=0
while i > n:
    print(i)
    i-=1
print("-----------------------------------")

print("esercizio 7")
i=0
numero=int(input("inserisci il numero "))
n=int(input("inserisci n"))

while i < n:
    numero=numero*i
    i +=1
print("-----------------------------------")

print("esercizio 8")

numeri = input("Inserisci una lista di numeri interi separati da spazio: ")


lista_numeri = list(map(int, numeri.split()))


somma = 0
i = 0


while i < len(lista_numeri):
    somma += lista_numeri[i]
    i += 1


print("La somma dei numeri è:", somma)

print("-----------------------------------")

print("esercizo 9")
stringa=(input("inserisci una stringa"))
i=0

while i < len(stringa):
    if stringa[i] not in ("a", "e", "i", "o", "u"):        
        print(stringa[i])
        i+=1
    else:
        print("")
        i+=1
print("-----------------------------------")


