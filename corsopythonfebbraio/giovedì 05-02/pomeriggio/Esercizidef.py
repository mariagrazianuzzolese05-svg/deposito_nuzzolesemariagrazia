#genrerare n casuali da 1 a 100
#utente tenta di indovinare
#a ogni tentativo si ripete  fino a quando non si indovina o si esce

import random
def nmaggiore(b, a):
    return b - a

def nminore(a, b):
    return a - b

n =int(input('che numero è?'))

numero_casuale = random.randint(1, 100)

while n != numero_casuale:

    if n > numero_casuale:
        diff = nmaggiore(n, numero_casuale)
        print('Troppo alto! La differenza è:', diff)
        x =input('inserisci nuovo numero:')
        n = int(x)
        
    else:
        diff = nminore(numero_casuale, n)
        print('Troppo basso! La differenza è:', diff)

        x =int(input('inserisci nuovo numero:'))
        n = int(x)
        
print('bingo')
