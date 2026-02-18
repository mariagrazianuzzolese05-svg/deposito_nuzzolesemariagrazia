'''Scrivete un programma che genera 5 numeri
casuali e li salva su un file,
l’utente dovrà cercare di indovinarne almeno 2 oppure
avrà perso. '''

#genera 5 numeri in una lista

from random import randint  #importiamo solo num int

numeri = []  #lista vuota dei 5 numeri che il sistema genererà

for i in range(0,5): #ripeto il ciclo 5 volte
    numero = randint(1, 50) #per ogni ciclo sceglie un num random
    numeri.append(numero)  #aggiungo num alla lista vuota creata


#salvare numeri in un file file3.txt 

def scrivifile(lista):
    stringa = ",".join(str(numero) for numero in lista)
    with open("file3.txt","w") as file:
        file.write(stringa) #per ogni numero dentro la lista trasformalo in stringa e uniscili con una virgola e scrivili nel file, questo perchè file.write accetta solo stringhe
#".".join = mette una virgola tra ogni elemento della lista #file.write accetta solo stringhe
scrivifile(numeri)

print("I numeri generati sono stati savalti su file3.txt")


#--main 
#prima leggiamo il file

with open("file3.txt", "r") as file: 
    contenuto = file.read()

print(contenuto)

#chiediamo all'utente di indovinare almeno due numeri
print("prova ad indovinare almeno 2 (da 1 a 50) dei 5 numeri generati dal sistema")
indovinati = 0

for i in range(5):  #ciclo deve ripetersi 5 volte
    tentativo = int(input("inserisci un numero: ")) #chiediamo il numero all'utente
    if tentativo in numeri:
        print("hai indovintato")
        indovinati += 1
    else:
        print("Riprova")

if indovinati >= 2:
    print("hai vinto, hai indovinato", indovinati, "numeri")
else:
    print("hai perso, hai indovinato", indovinati, "numeri")







