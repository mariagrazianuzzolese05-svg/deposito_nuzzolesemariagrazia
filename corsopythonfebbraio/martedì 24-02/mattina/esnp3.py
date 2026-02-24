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
arr=np.random.randint(1,25,size=(5,5))
print(arr,'arr')
print(arr[:, 1],'colonna')
print(arr[1, :],'riga')
diagonale=np.diag(arr)
print(diagonale,'diag')
sum=np.sum(diagonale)
print(sum)