#es1
#squadra di calcio creazione
xy = input('che sesso sei?')
età = input('sei maggiorenne o minorenne?')
if xy.lower() == "femmina":
    print('sei candidata alla squadra a')
    if età == 'minorenne':
        print('allora vai nella squadra a under 18')
    else:
        print('benvenuta nella squadra a major')
elif xy.lower() == 'maschio':
    print('sei candidata alla squadra b')
    if età == 'minorenne':
        print('allora vai nella squadra a under 18')
    else:
        print('benvenuta nella squadra a major')
else:
    print('allora puoi far parte del pubblico')

    
#es2
a = ['pippo', 'baudo', 18, 'nubile']
b = input('vuoi modificare lista?')
if b == 'si':
    c = input('vuoi aggiungere,modificare o eliminare?')
    if c == 'aggiungere':
        a.insert(28, 1)
        print(a)
    elif c == 'modificare':
    #modificare lista
        a[2] = 5
        print(a)
    elif c== 'eliminare':
        a.clear(4)
        print(a)
else:
    print('ciao')

#es3
a = input('sei registrato?')
if a == 'no':
    input('inserire id')
    print('id registrato')
    b = input('continuare?')
    if b == 'si':
        input('inserire età')
        print('dato inserito')
    elif b== 'no':
        print('operazione di rgistrazione fallita')
else:
    print('bentornato')







