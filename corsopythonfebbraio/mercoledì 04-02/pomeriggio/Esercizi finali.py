""" #es1
c= int(input('numero:'))
if c % 2 == 0:
        print('è pari')
else:
    print('è dispari')

#es2
n= True
while n== True:
    numero =int(input('inserisci numero'))
    for i in range(numero,-1,-1):
        print(i)
        continua = True
        if 
        ripeti = input("Vuoi ripetere? (si/no): ")

#es3
s = [1, 2, 3]
for i in s**2:
     print(s) """

#es4
g = []
scelta = "si"
continua = True
while scelta == "si":
     v = int(input('inserisci valore'))
     g.append(v)
     scelta =input('vuoi continuare?')

if len(g)==0:
            print("Lista vuota")
else:
    massimo = g[0]
    for n in g:
            if n > massimo:
             massimo = n
    
    conteggio = 0
           
    while n < len(g):
                conteggio += 1
    print("Numero massimo:", massimo)
    print("Numero di elementi:", conteggio)
                