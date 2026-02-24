'''Creare un array NumPy di 15 elementi contenente numeri casuali compresi tra 1 e 100.

Calcolare e stampare la somma di tutti gli elementi dell'array.

Calcolare e stampare la media di tutti gli elementi dell'array.'''
import numpy as np
'''arr=np.random.randint(1,100,size=15)
sum = np.sum(arr)
media=np.mean(arr)
print(sum)
print(media)'''

'''Esercizio 2: Manipolazione di Array Multidimensionali
Creare una matrice 5x5 contenente numeri interi sequenziali da 1 a 25.
Estrarre e stampare la seconda colonna della matrice.
Estrarre e stampare la terza riga della matrice.
Calcolare e stampare la somma degli elementi della diagonale principale della matrice.
'''
'''arr=np.random.randint(1,25,size=(5,5))
print(arr,'arr')
print(arr[:, 1],'colonna')
print(arr[1, :],'riga')
diagonale=np.diag(arr)
print(diagonale,'diag')
sum=np.sum(diagonale)
print(sum)'''

'''Creare un array NumPy di forma (4, 4) contenente numeri casuali interi tra 10 e 50.
Utilizzare fancy indexing per selezionare e stampare gli elementi agli indici (0, 1), (1, 3), (2, 2) e (3, 0).
Utilizzare fancy indexing per selezionare e stampare tutte le righe dispari dell'array
(considerando la numerazione delle righe che parte da 0).
Modificare gli elementi selezionati nel primo punto dell'esercizio aggiungendo 10 al loro valore.'''
arr=np.random.randint(1,5,size=(4,4))
indici=[(0, 1), (1, 3), (2, 2),(3, 0)]
print(arr[indici])
indici_dispari = [[0, 2, 4]]
riga = arr[indici_dispari]
print(riga)
arr[indici] +=10
print(arr)

