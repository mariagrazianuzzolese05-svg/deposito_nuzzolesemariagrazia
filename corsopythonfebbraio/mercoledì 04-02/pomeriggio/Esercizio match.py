#es1
età = int(input('quanti anni hai'))
match età:
    case _:
        if età > 18:
            print('buona visione')
        else:
            print('non puoi vedere il film')

#es2
o = int(input('inserire numero'))
u = int(input('inserire numero'))
calcolo = input('che operazione vuoi fare?')
match calcolo:
    case 'addizione':
       print(o + u)
    case 'sottrazione':
        print(o - u)
    case 'moltiplicazione':
        print(o * u)
    case 'divisione':
        if u == 0:
            print('errore')
        else:
            print('o / u')
    case _:
        print('operazione non valida')
