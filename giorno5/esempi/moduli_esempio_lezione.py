#i moduloi --> un modulo è un file python che contiene codice riutilizzabile (funzioni, classi, variabili, ecc.)
#possono essere considerati delle librerie
import es_moduli as modulo

modulo.saluta("luca")

# Si può impostare un alias per il modulo utilizzando as quando lo importi

#posso importare solo parte di un modulo

from es_moduli import saluta 

saluta("vincenzo")

#posso importare piu funzion per volta con: from  es_ moduli import saluta, altra_funzione, ecc.
