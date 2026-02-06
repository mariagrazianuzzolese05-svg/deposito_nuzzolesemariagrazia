'''1.Base / Numeri pari e dispari o sequenza Descrizione:
Scrivi un programma che chiede all'utente di inserire un numero o una stringa scegliendo prima quale. Il programma dovrebbe determinare se il numero è pari o dispari e stampare il risultato e se deve ripetere o stampare e poi ripetere.'''

t = True
scelta = input(' scegli numero o parola')


while t==True:  
    match scelta:
        case 'numero':
            valore = int(input("Inserisci il numero da controllare: "))
            if valore % 2==0:
                print('pari')
                r =input('ripetere?')
                if r == 'no':
                    break
                elif r =='si':
                    continue
            else:
                print('dispari')
                r=input('ripetere?')
                if r == 'no':
                        break
                elif r =='si':
                        continue
        case 'parola':
            valore = input("Inserisci la parola da controllare: ")
            if len(valore) % 2==0:
                print('pari')
                r =input('ripetere?')
                if r == 'no':
                    break
                elif r =='si':
                    continue
            else:
                print('dispari')
                r =input('ripetere?')
                if r == 'no':
                    break
                elif r =='si':
                    continue


           

