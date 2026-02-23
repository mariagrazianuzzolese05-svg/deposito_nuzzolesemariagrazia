import numpy as np
'''Utilizza la funzione np.arange per creare un array di numeri interi da 10 a 49.
Verifica il tipo di dato dell'array e stampa il risultato.
Cambia il tipo di dato dell'array in float64 e verifica di nuovo il tipo di dato.
Stampa la forma dell'array.'''

#arr = np.arange(10,49,1)
#print(arr.dtype)
#print(arr)

#arr.dtype='float64'
#arr=arr.astype('float64')#Restituisce una copia dell'array con il tipo di dati specificato
#print(arr.dtype)

'''Crea un array NumPy 1D di 20 numeri interi casuali compresi tra 10 e 50.
Utilizza lo slicing per estrarre i primi 10 elementi dell'array.
Utilizza lo slicing per estrarre gli ultimi 5 elementi dell'array.
Utilizza lo slicing per estrarre gli elementi dall'indice 5 all'indice 15 (escluso).
Utilizza lo slicing per estrarre ogni terzo elemento dell'array.
Modifica, tramite slicing, gli elementi dall'indice 5 all'indice 10 (escluso) assegnando loro il valore 99.
Stampa l'array originale e tutti i sottoarray ottenuti tramite slicing.'''
'''arr = np.arange(10,50,1)
print(arr)
print(arr[:11])
print(arr[-5:])
print(arr[5:15])
print(arr[0::3])
arr[5:10]=99
print(arr)'''

'''Crea una matrice NumPy 2D di dimensioni 6x6 contenente numeri interi casuali compresi tra 1 e 100.
Estrai la sotto-matrice centrale 4x4 dalla matrice originale.
Inverti le righe della matrice estratta (cioè, la prima riga diventa l'ultima,
 la seconda diventa la penultima, e così via).
Estrai la diagonale principale della matrice invertita e crea un array 1D contenente questi elementi.
Sostituisci tutti gli elementi della matrice invertita che sono multipli di 3 con il valore -1.
Stampa la matrice originale, la sotto-matrice centrale estratta, la matrice invertita,
 la diagonale principale e la matrice invertita modificata.'''
import random
matrice=np.random.randint(1, 101, size=(6, 6))
print(matrice)
sotto_matrice = matrice[1:5, 1:5]
print(sotto_matrice)
matrice_invertita = sotto_matrice[::-1, :]
print(matrice_invertita)
diagonale = np.diag(matrice_invertita)
print(diagonale)

m = (matrice_invertita % 3 == 0)
#boolean indexing
matrice_invertita[m] = -1
print(matrice_invertita)