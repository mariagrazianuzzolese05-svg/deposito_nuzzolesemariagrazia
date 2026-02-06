'''2.Intermedio/ Numeri primi in un intervallo :
Chiedi all'utente di inserire due numeri che definiscono un intervallo (es 10 e 50). Il programma dovrebbe stampare tutti i numeri primi compresi in quell'intervallo o i numeri non primi o entrambi divisi a tua scelta, salvandoli in due aggregazioni differenti e chiedere se deve ripetere'''
limite = int(input('che limite vuoi?'))
start = int(input('da che numero partire?'))
lista = [*range(start, limite,1)]
t = True
while t== True:
    a =input("pari,dispari o entrambi")
    if a== 'pari':
        for n in lista:
            if n % 2==0:
                print('pari')
                r = input('ripetere?')
            
    elif a=='entrambi':
        
            pari = [n for n in lista if n % 2 == 0]
            dispari = [n for n in lista if n % 2 != 0]
          

    else:
        print('dispari')
        r = input('ripetere?')
