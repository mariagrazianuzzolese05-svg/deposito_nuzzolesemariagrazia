'''Scrivi un programma che esegua le seguenti operazioni:

Chiedi all'utente di inserire un numero intero positivo n. Se l'utente inserisce un numero negativo o zero, continua a chiedere un numero fino a quando non viene inserito un numero positivo.
Genera una lista di numeri interi casuali tra 1 e n (incluso). La lunghezza della lista deve essere n.
Utilizza un ciclo for per calcolare e stampare la somma dei numeri pari nella lista.
Utilizza un ciclo for per stampare tutti i numeri dispari nella lista.
Utilizza una funzione per determinare se un numero è primo. La funzione deve restituire True se il numero è primo, altrimenti False.
Utilizza un ciclo for per stampare tutti i numeri primi nella lista.
Infine, utilizza una struttura if per determinare se la somma di tutti i numeri nella lista è un numero primo e stampa il risultato

'''
#es 1
inserisci =int(input('inserisci intero'))
while inserisci <= 0:
    if inserisci < 0:
        inserisci = int(input('Inserisci di nuovo un intero positivo: '))
    else:
        break
#es 2
import random
lista = []
for i in range(inserisci):
    numero_casuale = random.randint(1,inserisci)
    lista.append(numero_casuale)
print(lista)
#es3
sommap =0
sommad =0    
for y in lista:
    
    if y%2== 0:
        sommap += y
        print(sommap)

#es4 
    else:
        print(y)
print(sommap)
        
#es5-6
boolean= False
primi = []
if inserisci < 2:
        print(False)

    
for i in range(2, inserisci):
    if inserisci % i == 0:
        print(False)
    else:
        print(True)
        primi.append(inserisci)
        print(primi)
#es7
somma=0
for r in lista:
    somma+=r
print(somma)

    




