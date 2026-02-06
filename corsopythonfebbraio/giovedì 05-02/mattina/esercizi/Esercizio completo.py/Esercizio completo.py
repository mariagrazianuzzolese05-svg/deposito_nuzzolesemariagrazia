'''Esercizio Completo

Descrizione: Scrivi un programma che chieda all'utente di inserire un numero intero positivo n. Il programma deve poi eseguire le seguenti operazioni:

Utilizzare un ciclo while per garantire che l'utente inserisca un numero positivo. Se l'utente inserisce un numero negativo o zero, il programma deve continuare a chiedere un numero fino a quando non viene inserito un numero positivo.
Utilizzare un ciclo for con range per calcolare e stampare la somma dei numeri pari da 1 a n.
Utilizzare un ciclo for per stampare tutti i numeri dispari da 1 a n.
Utilizzare una struttura if per determinare se n è un numero primo. Un numero primo è divisibile solo per 1 e per se stesso. Il programma deve stampare se n è primo o no.'''

inserisci =int(input('inserisci intero'))
while inserisci < 0:
    if inserisci < 0:
        inserisci = int(input('Inserisci di nuovo un intero positivo: '))
    else:
        break
limite =int(input('limite range?'))
lista = [*range(inserisci, limite,1)]
conteggio = 0
for n in range(inserisci, limite,1):
    if n % 2 == 0:
        conteggio = conteggio + 1
        print('pari')
    elif n % 2 != 0:
        dispari = [n for n in lista]
        print('dispari')
        break

for i in range(2,inserisci):
            if inserisci % i == 0:
                print('non è primo')
            else:
                print('primo')
    