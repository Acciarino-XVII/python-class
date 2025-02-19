print("esercizio 1")
a={}
print("--------------------------------")

print("esercizio 2")
a= {"nome" : "Mario", 
    "cognome" : "Rossi", 
    "età" : 30}

print("--------------------------------")

print("esercizio 3")
print(a["età"])

print("--------------------------------")

print("esercizio 4")

a["email"] = "mario.rossi@email.com"

print("--------------------------------")

print("esercizio 5")
a.pop("cognome")
print(a)

print("--------------------------------")

print("esercizio 6")
keys=a.keys()
print(keys)
print(a)

print("--------------------------------")

print("esercizio 7")
values=a.values()
print(values)

print("--------------------------------")

print("esercizio 8")
a["età"] = 25
print(a)

print("--------------------------------")

print("esercizio 9")
i=0
for elements in a.items():
    print(i)
    print(elements)
    i+=1
...