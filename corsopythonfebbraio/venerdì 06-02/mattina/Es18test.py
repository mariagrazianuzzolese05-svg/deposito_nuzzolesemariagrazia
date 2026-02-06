'''18.Esercizio 2:  Funzioni e Liste
Definisca una funzione chiamata conta_vocali. 
 
 La funzione deve: 
 
 ricevere una stringa come parametro 
 
 contare quante vocali contiene (a, e, i, o, u) 
 
 restituire il numero totale di vocali 
 
 
 
 Nel programma principale: 
 
 chiedi all’utente di inserire una parola 
 
 chiama la funzione 
 
 stampa il numero di vocali trovate'''
#Definisca una funzione chiamata conta_vocali.


def conta_vocali(parola:str):
    tot= 0
    vocali= 'aeiou'
    
#Nel programma principale: chiedi all’utente di inserire una parola

    for inserisci in parola:
    
        if inserisci in vocali:
            tot+=1
            
    return tot
inserisci = input('inserisci parola:')
            
#chiama la funzione
risultato = conta_vocali(inserisci)
print(risultato)



