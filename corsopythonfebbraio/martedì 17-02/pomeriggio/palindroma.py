'''Scrivete un programma che utilizza una funzione che accetta
come parametro una stringa passata dall’utente e restituisce in
risposta se è palindroma o no.
Esempio:
‘I topi non avevano nipoti’ è palindroma
‘Ciao’ non è palindroma'''

x=input('inserisci parola')
x="".join(x.split()).lower()  #per usare frasi prima le splitiamo e poi le riattachiaml grazie a "".join che le riattacca senza spazzi  
#formula:s=s di n-1-i per ogni i che appartengono all'intervallo da 0 a n/2
for i in range(len(x) // 2):
    if x[i] != x[len(x) - 1 - i]:
        print('no palindroma',x)
        break
    else:
        print('palindroma',x)
        break
    #si poteva fare anche facendo la x invertita e vedere se fosse ugale alla x iniziale
