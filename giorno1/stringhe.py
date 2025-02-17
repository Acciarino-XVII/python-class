#dichiarazione di una stringa

x="ciao"
y="ciao"
frase="il mio nome è 'paolo'"

#dichiarazione stringa multiriga
z='''
questa è una 
stringa 
multiriga'''
#si può accedere ad ogni carattere di una stringa 
print("La stringa x è:", x)
print("il primo carattere della strniga in x è:", x[0])

#si possono contare il numero di lettere di una stringa

print("la lunghezza della stringa z è:", len(z))
#--------------------------------------

string="casa"

print("la stringa e'", string.upper())
print("la stringa e'", string.lower())
print('''
    la stringa con la funzione
      strip toglie gli spazi
      inizio e fine stringa
      ''', string.strip())

#funzione replace
#replace sostituisce una determina lettera con un altra
# sostituisci string casa  in coso

print("cambio casa in coso\n", string.replace('a', 'o'))

print("cambio casa in coro\n", string.replace('asa', 'oro'))
print(string).upper()