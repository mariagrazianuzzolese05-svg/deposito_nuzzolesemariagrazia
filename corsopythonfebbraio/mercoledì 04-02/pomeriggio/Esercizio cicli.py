#es 1
w = 'si'
continua = True
while continua:
    numero =int(input('inserisci numero'))
    for i in range(numero,-1,-1):
        print(i)
        
    w = input('vuoi continuare?')
    if w.lower() == 'no':
        continua = False
        print('ciao')
#es2
pari = []
c = 0
while c < 5:
    n=int(input('inserisci numero'))
    if n % 2 == 0:
        print("Il numero è pari")
        pari.append(n)
        c += 1
    else:
        print("Il numero non è pari")

print("Hai inserito 5 numeri pari:", pari)




  


