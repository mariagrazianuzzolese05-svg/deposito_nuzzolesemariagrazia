#if
x = 10
y = 20
if x<y:
    print("bravo")

#se non vero ma solo if
z = 20
r = 10
if z<y:
    print("bravo")

#else,elif,if annidato
etàmg = input("quanti anni ho?")
etày =input("quanti anni ha y?")
if etàmg>etày:
    print('sono più grande')
    if etàmg == etày:
        print('abbiamo la stessa età')
    elif etàmg != etày:
        print('abbiamo età differenti')
elif etàmg < etày:
    print('sei più piccolo')
else:
    print('errore')

#match
comando = input('inserisci nome')
match comando:
    case 'mariagrazia':
        print('mariagrazia è passata')
    case 'rossana':
        print('rossana è passata')
    case _:
        print('nessun id selezionato')
