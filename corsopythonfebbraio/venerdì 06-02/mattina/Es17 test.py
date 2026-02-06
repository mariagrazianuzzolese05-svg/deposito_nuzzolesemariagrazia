'''17.Esercizio 1:  Condizioni e cicli
Chieda all’utente di inserire un numero intero positivo. 
 
 Usi un ciclo for per stampare tutti i numeri da 1 fino al numero inserito. 
 
 Per ogni numero: 
 
 stampi "pari" se il numero è pari 
 
 stampi "dispari" se il numero è dispari 
 
 
 
 Se l’utente inserisce un numero minore o uguale a zero, il programma deve stampare un messaggio di errore'''

#Chieda all’utente di inserire un numero intero positivo. 
n= int(input('inserisci numero positivo:'))
#Usi un ciclo for per stampare tutti i numeri da 1 fino al numero inserito.
for i in range(1,n,1):
    if i %2==0:
        print('pari')
#Se l’utente inserisce un numero minore o uguale a zero, il programma deve stampare un messaggio di errore
    elif i <=0:
        print('errore')

    else:
        print('dispari')
print(*range(1,n))

