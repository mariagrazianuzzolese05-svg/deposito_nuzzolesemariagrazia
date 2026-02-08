'''.Avanzato/ Fattori comuni Descrizione:
Chiedi all'utente di inserire due numeri. Il programma dovrebbe determinare e stampare i fattori comuni di entrambi i numeri. Se non ci sono fattori comuni oltre 1, dovrebbe stampare "I numeri sono coprimi". La stessa cosa ma anche per due stringhe (.equal ) e chiedere se deve ripetere ma sono “ complementari” solo se hanno tutte le lettere in comune (es:abs/ sab)
'''
x =input('numero o parola')
t = True
fattoricomuni =set()
match x:
    case 'numero':
        while t ==True:
            n = int(input("Inserisci un numero: "))
            b = int(input("Inserisci un numero: "))
            set1 = {i for i in range(1, n + 1) if n % i == 0}
            set2 = {y for y in range(1, b + 1) if b % y == 0}
            fattoricomuni = set1.intersection(set2)
            if fattoricomuni== {1}:
                    print('cooprimi')
            else:
                print(fattoricomuni)
            risposta = input("Vuoi analizzare altri numeri? ").lower()
            if risposta == 'no':
                print("Programma terminato.")
                t = False
                
    case 'parola':
          while t ==True:
            n =(input("Inserisci una parola: "))
            b =(input("Inserisci una parola: "))
            if n ==b:
                    print('complementari')
            else:
                print('no comlementari')
            risposta = input("Vuoi analizzare altre parole?").lower()
            if risposta == 'no':
                print("Programma terminato.")
                t = False