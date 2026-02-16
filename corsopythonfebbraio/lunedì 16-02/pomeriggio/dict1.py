'''Scrivete un programma che chiede una stringa all’utente e
restituisce un dizionario rappresentante la "frequenza di
comparsa" di ciascun carattere componente la stringa.
Esempio:
Stringa "ababcc",
Risultato
{"a": 2, "b": 2, "c": 2}'''
count=0
diz={}
x=input('stringa:')
for el in x:
    if el not in diz:
        #diz[el] = 1
        #diz[el] = diz.setdefault(el, 1) 
        diz.setdefault(el, 1) 
        #print('--',diz)
    else:
        diz[el] += 1
print(diz)
#per ogni el in x se non c'è nel dict diciamo che l'elemento compare 1 volta se no si conta