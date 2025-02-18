#esercizio 1
print("esercizio 1")
stringa = "ciao mondo"
print("la stringa prima della conversione: ",stringa, "\n la stringa dopo la conversione: ", stringa.upper()) 

#esercizio 2
print("esercizio 2")
stringa = "benvenuti a roma"
print("la stringa prima della conversione: ",stringa, "\n la stringa dopo la conversione: ", stringa.lower())

#esercizio 3
print("esercizio 3")

stringa = "Il meglio deve ancora venire"
#split della stringa
stringa.split()

#esercizio 4
print("esercizio 4")
stringa = "Hello World"
print("la stringa prima della conversione: ",stringa, "\n la stringa dopo la conversione: ", stringa.replace("World", "Python"))

#esercizo 5
print("esercizio 5")
stringa = " Ciao "
print("la stringa prima della conversione: ",stringa, "\n la stringa dopo la conversione: ", stringa.strip())

#esercizio 6
print("esercizio 6")
stringa = "abcdefg"
print("i primi tre caratteri di stringa", stringa[0],stringa[1],stringa[2])

#esercizio 7
print("esercizio 7")
stringa = "python"
print("la stringa comincia con py?")
print(stringa.startswith("py"))

#esercizio 8 
print("esercizio 8")
stringa = "ciao mondo"
print("contiamo quante volte si ripete 'o' nella stringa")
print(stringa.count("o"))

#esercizio 9 
print("esercizio 9")
stringa = "ciao mondo"
print(stringa[-1],stringa[-2],stringa[-3],stringa[-4])

#soatituisci caratteri
print(stringa.replace("o", "k"))
