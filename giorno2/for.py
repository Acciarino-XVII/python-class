# print("esericizio 1")
# lista=["good kid M.A.A.D city", "gnx", "damn"]
# for elemento in lista:
#     print(elemento)
# print("----------------------------------")

# print("esercizio 2")

# n=11
# for i in range(1,n):
#     print(i)
# print("----------------------------------")

print("esercizio 3")
lista=[1,2,3,4,5,6,7,8,9]
somma=0
for elemento in lista:
    somma=somma+elemento
print("il totale della somma delle liste è: ",somma)
print("----------------------------------")

print("esercizio 4")
for i in range(0,20,2):
    print(i)
print("----------------------------------")

print("esercizio 5")
stringa=input("inserici una stringa: ")
for i in range(len(stringa)):
    print(stringa[i])
print("--------------------------------")

print("esercizio 6")
lista=[1,2,3,4,5,6,7,8,9]
media=0
for elemento in lista:
    media=media+elemento
media=media/len(lista)
print(media)

print("----------------------------------")

print("esercizio 6 variante con lista in input")

n=int(input("inserisci la lunghezza della lista: "))
lista=[]
for _ in range(n):
    numero=int(input("inserisci il numero "+str(_+1)+": "))
    lista.append(numero)
for elemento in lista:
    media=media+elemento
media=media/n
print(media)