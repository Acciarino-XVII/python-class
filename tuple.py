print("esercizio 1")
a=tuple()
print(type(a))

print("--------------------------------")

print("esercizio 2")
b=tuple("mela","banana","kiw")

print("--------------------------------")

print("esercizio 3")
print(" l'elemento è: ", b[1])
indice=b.index("banana")

print("--------------------------------")

print("esercizio 4")

c=b[:2]

print(f"La tupla 'c' è: {c}")

print("esercizio 5")
if "ananas" in b:
    print("l'elemento 'ananas' è presente nella tupla")
else:
    print("l'elemento 'ananas' non è presente nella tupla")

print("--------------------------------")

print("esercizio 6")
print("la lunghezza della tupla 'b' è: ", len(b))

print("--------------------------------")

print("esercizio 7/8")
d=tuple("pesca", "arancia")
frutta=b+c

print(f"La tupla 'frutta' è: {frutta}")
count = frutta.count("mela")
print(count)

print("--------------------------------")

