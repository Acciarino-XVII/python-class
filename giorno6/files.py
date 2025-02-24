import os

f = open("file.txt", "r")
# print(f.read())

# print(f.read(10))
print(f.read())
# funzione readline --> viene utilizzata con un testo su più righe
for riga in f:
    print(riga)

#chiudo l'accesso al file
f.close()

f=open("file.txt", "w",encoding="utf-8" )
#sovrascrivo il contenuto del file
# f.write("signorina python")
f.write("aggiungo la riga signor sistemi \n")
f.close()

f=open("file.txt", "r")

print(f.read())

#creare un nuovo file txt
#possiamo usare il parametro "w" oppure "x", 
# "x" crea un nuovo file se non esiste 
#"w" sovascrive un file esistente altrimenti

f=open("nuvo_file.txt", "w")
f.close()

#os ha il metodo remove() che permette di cancellare un file

os.remove("nuvo_file.txt")
print("il file 'nuovo file.txt' is removed")

if os.path.exists("nuvo_file.txt"):
    os.remove("nuvo_file.txt")
    print("il file 'nuvo_file.txt' is removed")
else:
    print("il file 'nuvo_file.txt' non è presente ")

#os.rmdir("nome della cartella o path") rimuove una directory


