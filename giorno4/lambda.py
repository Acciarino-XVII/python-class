# print("esercizio 1")
# quadrato = lambda x: print("il quadrato è",x**2)

# print(quadrato(int(input("inserisci il numero: "))))

# print("----------------------------------------------------------------")
# print ("esercizio 2")
# lista2x = lambda lista: list(map(lambda x: x*2, lista)) #list converte tutto in lista, map applica x * 2 ad ogni elemento


# lista = [1, 2, 3, 4, 5]
# print("la lista moltiplicata per 2 è: ", lista2x(lista))

# print("----------------------------------------------------------------")

print("esercizio 3")

listac = lambda lista: list(map(lambda parola: parola.startswith("c"), lista))

lista_stringhe = ["cane", "gatto", "coniglio", "pollo", "topo"]

print("Le stringhe che iniziano con 'c' sono: ", listac(lista_stringhe))

print("----------------------------------------------------------------")

print("esercizio 4")

sumquadrato = lambda x,y : (x**2)+(y**2)
num1 = float(input("inserisci il primo numero: "))
num2 = float(input("inserisci il secondo numero: "))

print("somma dei quadrati di",num1,"e",num2,"è:",sumquadrato(num1, num2))

print("-------------------------------------------------------")
