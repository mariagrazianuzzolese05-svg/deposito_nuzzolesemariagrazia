'''Scrivete un programma che chiede all'utente una
serie di parole e restituisce solo le vocali e 
l’indice della vocale all’interno delle parole.'''

vocaliparola='aeiou'
'''count=0
parole=[]
while count<3:
    x=input('inserisci parola')
    parole.append(x)
    count+=1
print('finito')'''
parole=['ciao','gg','tutti']
parole2=[]
for parola in parole:
    posizione=0
    while posizione<len(parola):
        if parola[posizione] in vocaliparola:  #parola[posizione] sta dicendo di controllare la posizione della parola
            print(parola,parola[posizione],posizione)
        posizione+=1
 #si può usare enumerate
       



#vocaliparola=['aeiou']

'''for parola in range(3):#meglio sui numeri
    x=input('inserisci parola')
    parole.append(x)
print('finito')'''

'''for parola in parole:
    if 'aeiou' in parola:
        vocaliparola.append(parola)
print(vocaliparola) '''''  

#vocali=[parola for parola in parole if vocaliparola in parola]



