'''create un programma che richiede all’utente tre numeri
 e verifica la presenza di almeno due numeri uguali, se non 
 ci sono ci restituisce il numero più grande dei tre'''

x=int(input('primo numero'))
y=int(input('secondo numero'))
z=int(input('terzo numero'))

if x==y:
    print(' numeri', x,y,'sono uguali')
elif y==z:
    print(' numeri', z,y,'sono uguali')
elif x==z:
    print(' numeri', x,z,'sono uguali')
elif x > y and x > z and x!=y and y!=z and x!=z:
    print(x, 'è il piu grande')
elif y >z and y > x and x!=y and y!=z and x!=z:
    print(y, 'è il più grande')
elif z >y and z > x and x!=y and y!=z and x!=z:
    print(z, 'è il più grande')
else:
    print('sono tutti uguali')

