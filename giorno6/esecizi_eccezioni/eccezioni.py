#Scrivere un programma Python per gestire l'eccezione 
# ZeroDivisionError quando si divide un numero per zero.

num1 = int(input("Inserisci un numero: "))
num2 = int(input("Inserisci un numero: "))

try: 
    num1 / num2
except ZeroDivisionError:
    print("non puoi dividere per zero!")

print("----------------------------------------------------------------")

print("esercizio 2")

def valerror(num1):
    tipo = type(num1)
    if tipo == int:
        print("numero valido")
    else:
        raise ValueError("Devi inserire un numero intero")
    
a= int(input("Inserisci un numero intero: "))
try:
    valerror(num1)

except ValueError:
   
    print("Devi inserire un numero intero")
    

print("--------------------------------")

print("esercizio 3  ")

#Scrivere un programma Python che apre un file e gestisce 
# l'eccezione FileNotFoundError se il file non esiste.

try:
    file = open("filenonesistente.txt", "r")

except FileNotFoundError:
    print("File non trovato!")


print("--------------------------------")

print("esercizio 4")

#Scrivete un programma Python che chieda 
# all'utente di inserire due numeri e 
# sollevi l'eccezione TypeError se gli input non sono numerici.

def raise_error(num1, num2):
    if num1.isdigit() and num2.isdigit():
        return"daje"
    else:
        raise TypeError("Devi inserire due numeri numerici!")


try:
    num1 = (input("Inserisci un numero: "))
    num2 = (input("Inserisci un altro numero: "))
    raise_error(num1, num2)
    
except TypeError:
    print("Devi inserire due numeri numerici!")

print("----------------------------------------------------------------")

print("esercizio 5")

#Scrivete un programma Python che apra un file in lettura 
# e gestisca l'eccezione PermissionError in caso di problemi 
# di autorizzazione.

