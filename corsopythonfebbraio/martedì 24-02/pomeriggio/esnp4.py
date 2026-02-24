'''Parte UNO: Scrivere un Sistema che utilizza NumPy per gestire una matrice 2D. 
Il programma deve presentare un menu interattivo che consente all'utente di eseguire
varie operazioni sulla matrice. Le operazioni disponibili includono, ogni volta che 
il sistema conclude un calcolo va salvato su un file txt:

Creare una nuova matrice 2D di dimensioni specificate da utente con numeri casuali.
Estrarre e stampare la sotto-matrice centrale.
Trasporre la matrice e stamparla.
Calcolare e stampare la somma di tutti gli elementi della matrice.
Uscire dal programma o ripetere .
'''
import numpy as np
while True:
    righe=int(input('quante righe'))
    colonne=int(input('quante colonne'))
    matrice=np.random.rand(righe,colonne)
    sotto_matrice = matrice[1:-1, 1:-1]
    trasposta=np.transpose(matrice)
    somma=np.sum(matrice)
    with open("operazioninp.txt","w") as f:
        
        f.write(f"arr: {matrice}\n")
        f.write(f"sum: {sotto_matrice}\n")
        f.write(f"sum3: {trasposta}\n")
        f.write(f"sum3: {somma}\n")
    with open("operazioninp.txt","r") as file:
        contenuto = file.read()
    scelta=input('uscire o creare nuova matrice?')
    if scelta=='uscire':
        break
    else:
        print('creare seconda matrice')
        righe2=int(input('quante righe per nuova matrice'))
        colonne2=it(input('quante colonne per nuova matrice))

'''Parte DUE: Andare a specializzare per aggiungere nuove operazioni:
Moltiplicazione Element-wise con un'altra Matrice: L'utente può scegliere di creare una 
seconda matrice delle stesse dimensioni della prima e moltiplicarle elemento per elemento
e stampare il risultato.
Calcolo della Media degli Elementi della Matrice: Calcolare e stampare la media di tutti 
gli elementi della matrice.
'''

