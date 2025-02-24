#import os
#programma per lavorare con i files

#accedo in creazione al file
file =  open("ilMioFile.txt", "w")

l = ["ciao a tutti", "\nquesto è un nuovo file", "\ncreato da codice con una lista"]

#scrivo i dati nel file
file.write("NUOVO FILE:\n")
file.writelines(l)

#chiudo il file 
file.close()
file = open("ilMioFile.txt", "r")

#leggo tutto il file
print(file.read())

#sposto il cursore al primo carattere dopo la lerrutra
file.seek(0)
print("stampa di readline(2)", file.readline(2))

file.seek(0)
print("stampa di readlines()", file.readlines())

print(file.tell())
#chiudo il file
file.close()
