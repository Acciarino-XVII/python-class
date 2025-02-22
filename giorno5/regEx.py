import re

#Controlla se due stringhe date in input contengono 00181. 
#Farsi restituire un valore booleano.
print("esercizio1")

stringa1 = "00181ciaoo"
stringa2 = "signor sistemi"

def check00181(stringa):
    pattern = r'(00181)'
    
    return bool(re.search(pattern, stringa))

print(check00181(stringa1))
print(check00181(stringa2))


print("------------------------------------")

print("esercizio2")

#Sostituire tutte le occorrenze di 5 con 'cinque' per la seguente stringa: 
# 

stringa = "Hanno mangiato 5 mele e 5 arance"
print(stringa)

stringa = re.sub(r"\b5\b", "cinque", stringa)
print("stringa con regEx\n" + stringa)

print("------------------------------------")

print("esercizio 3")
#Sostituire solo la prima occorrenza di [spazio] con 9 per la seguente stringa: 
# “Oggi è una bella giornata di sole.”
replace_space = "Oggi è una bella giornata di sole."
replace_space = re.sub("\s", "9", replace_space, 1)
print(replace_space)

print("------------------------------------")

print("esercizio 4")

items = ['Gol', 'Giocatore', 'User', 'Sedia', 'Windows', 'Dado']

pattern = r"[WA]"

filtred_items = [s for s in items if re.search(pattern, s)]
print(filtred_items)

print("------------------------------------")

print("esercizio 5")

items = ['Gol', 'Giocatore', 'User', 'Sedia', 'Windows', 'Dado']
pattern = r"(?=.*a)(?=.*d)"

filtred_items = [s for s in items if re.search(pattern, s)]
print(filtred_items)

print("------------------------------------")

print("esercizio 6")
stringa = "Data una stringa in input, generare una lista che contenga la stringa divisa ad ogni occorrenza di lettera g."
filtred_stringa = re.split(r"g", stringa)

print(filtred_stringa)


print("------------------------------------")

print("esercizio 7")



print("------------------------------------")
