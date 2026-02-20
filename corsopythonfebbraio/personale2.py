#testa o croce
import random
import time
from termcolor import colored
#scelta=input('testa o croce ')

'''rint('hai scelto',scelta)
time.sleep(1)
print("l'avversario lancia la moneta,cosa uscirà?")
time.sleep(0.5)
print('---ATTENDERE PREGO----')'''

avversario= random.choice(["testa","croce"])
while True:
    try:
        avversario = random.choice(["testa", "croce"])
        scelta=input('testa o croce ')
        print('hai scelto',scelta)
        time.sleep(1)
        print("l'avversario lancia la moneta,cosa uscirà?")
        time.sleep(0.5)
        print('---ATTENDERE PREGO----')
        
                 
        if scelta.isdigit():
            z=input('è un numero,riprovare?')
            if z=='no':
                print('grazie per aver giocato')

        elif scelta not in ["testa", "croce"]:
            print('non è tra le opzioni')
            z=input('non è tra le opzioni,riprovare?')
            if z=='no':
                print('grazie per aver giocato')
        
        elif scelta in ["testa", "croce"]:
            if scelta==avversario:
                print(colored(f"Hai scelto {scelta}, hai vinto!", "green"))
                z = input('Rigiocare? (si/no): ')
                if z=='no':
                    print('grazie per aver giocato')
                    break
            else:
                print(colored(f"Hai scelto {scelta}, hai perso!", "red"))
                z = input('Riprovare? (si/no): ')
                if z=='no':
                    print('grazie per aver giocato')
                    break 
        
    except:
        print('errore')