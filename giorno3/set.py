print("esercizio 1")
a=set()
print(type(a))

print("--------------------------------")

print("esercizio 2")
b={"mela", "banana", "kiwi", "mela"}
print(type(b),b)

print("--------------------------------")

print("esercizio 3")
b.add("pesca")
print(b)

print("--------------------------------")

print("esercizio 4")
b.remove("mela")

print(b)

print("--------------------------------")

print("esercizio 5")
#verificare se l'elemneto  ananas è presente
if "ananas" in b:
    print("l'elemento è presente")
else:
    print("l'elemento non è presente")