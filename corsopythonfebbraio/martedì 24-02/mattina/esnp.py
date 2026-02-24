'''Crea un array NumPy (ndarray) utilizzando np.arange con valori da 0 a 49. più altre 50 posizioni casuali tra 49 e 101.
Stampa l’array, il suo dtype e la sua shape.
Modifica il tipo di dato (dtype) dell’array in float64.
Verifica e stampa di nuovo dtype e shape.
Utilizza lo slicing per ottenere:
i primi 10 elementi
gli ultimi 7 elementi
gli elementi dall’indice 5 all’indice 20 escluso
ogni quarto elemento dell'array
Modifica tramite slicing gli elementi dall’indice 10 a 15 (escluso) assegnando loro il valore 999.
Utilizza la fancy indexing per selezionare:
gli elementi in posizione [0, 3, 7, 12, 25, 33, 48]
tutti gli elementi pari dell’array utilizzando una maschera booleana
tutti gli elementi maggiori della media dell'array
Stampa:
l’array originale dopo tutte le modifiche
tutti i sotto-array ottenuti tramite slicing e fancy indexin'''

import numpy as np
#import random
parte1=np.arange(0,50)
parte2=np.random.randint(49,101, size=50)#crreati 50 numeri
#arr=parte1+parte2 #somma
arr = np.concatenate((parte1, parte2))
#arr=np.append(parte1, parte2)
print(arr)
print(arr.dtype)
print(arr.shape)
arr=arr.astype('float64')
print(arr.dtype)
print(arr.shape)

print(arr[:11])
print(arr[-7:])
print(arr[5:20])
print(arr[::4])

arr_modificato = arr.copy()#creo copia così stampo tutto
arr_modificato[10:15]=999
print(arr_modificato,'modificato')

indici=[0, 3, 7, 12, 25, 33, 48]
print(arr[indici],'con indici')

pari = (arr % 2 == 0)
arrm=arr[pari]
#pari([)arr % 3 == 0)
print(arrm,'pari')

media = np.mean(arr)
print('---',media,'----')
#armean=arr[arr[arr>media]]
#print(armean)
print(arr[arr > media],'media')