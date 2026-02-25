'''Crea un array di 12 numeri equidistanti tra 0 e 1 usando linspace.

Cambia la forma dell'array a una matrice 3x4.

Genera una matrice 3x4 di numeri casuali tra 0 e 1.

Calcola e stampa la somma degli elementi di entrambe le matrici.

'''
import numpy as np
'''arr = np.linspace(0, 1,12)
print(arr)
reshaped_arr = arr.reshape((3, 4))
print(reshaped_arr)
random_arr = np.random.rand(3, 4)  
print(random_arr)
sum = np.sum(arr)
print("somma arr:", sum)
sum1 = np.sum(reshaped_arr)
print("somma reshaped:", sum1)
sum2 = np.sum(random_arr)
print("somma random:", sum2)'''

'''Utilizza np.linspace per creare un array di 50 numeri equidistanti tra 0 e 10.
Utilizza np.random.random per creare un array di 50 numeri casuali compresi tra 0 e 1.
Somma i due array elemento per elemento per ottenere un nuovo array.
Calcola la somma totale degli elementi del nuovo array.
Calcola la somma degli elementi del nuovo array che sono maggiori di 5.
Stampa gli array originali, il nuovo array risultante dalla somma e le somme calcolate.
Salva i dati su un file TXT a ogni giro
Rendi ripetibile il processo complessivo
Chiedi se si vuole sovrascrivere il TXT o no.
'''
while True:
    arr = np.linspace(0,10,50)
    print(arr)
    matricer= np.random.random(50)
    #somma=arr+matricer
    sum = np.add(arr, matricer)
    #print(somma,'somma')
    print(sum,'sum')
    sum2 = np.sum(sum)
    print(sum2,'sum2')
    maggiori= arr[arr > 5] 
    sum3 = np.sum(maggiori)
    print(sum3,'sum3')
    '''riga= {
        "arr": arr,
        "sum": sum,
        "sum2": sum2,
        "sum3": sum3
    }'''
    with open("operazioni.txt","w") as f:
        
        f.write(f"arr: {arr.tolist()}\n")
        f.write(f"sum: {sum.tolist()}\n")
        f.write(f"sum3: {sum2}\n")
        f.write(f"sum3: {sum3}\n")
    
    scelta=input('continuare?')
    if scelta=='no':
        break


