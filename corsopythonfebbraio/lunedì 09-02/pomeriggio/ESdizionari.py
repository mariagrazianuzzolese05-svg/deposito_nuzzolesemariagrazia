'''Esercizio: Sistema di Gestione Negozio

Lo scopo di questo esercizio è implementare un sistema di gestione per 
un negozio che deve interagire con clienti, gestire l'inventario e permettere
 agli amministratori di supervisionare le operazioni. Il sistema sarà strutturato 
 in tre parti principali:
Gestione Clienti:
I clienti possono visualizzare gli articoli disponibili in inventario.
I clienti possono selezionare e acquistare articoli dall'inventario.
Il sistema tiene traccia degli acquisti dei clienti.
Gestione dell'Inventario:
Gli articoli in magazzino sono elencati con il nome, il prezzo e la quantità.
È possibile aggiungere nuovi articoli all'inventario.
Gli articoli possono essere rimossi o aggiornati (ad es., cambiare prezzo o quantità).
Amministrazione:
l'analisi del negozio da parte degli amministratori.
Gli amministratori possono visualizzare lo stato corrente dell'inventario.
Il sistema tiene traccia dei guadagni totali.
Puoi pre inserire gli amministratori non i clienti
Il sistema dovrebbe permettere di simulare un'interazione base tra il cliente e il negozio
dopo un login e una registrazione, nonché fornire gli strumenti necessari per la manutenzione
 e l'analisi del negozio da parte degli amministratori.'''

#DISCLAIMER:le righe segnate lì ho chiesto a gemini come fare,sopratutto la creazione del self.catalogo e il calcolo del guadagno


#Gli articoli in magazzino sono elencati con il nome, il prezzo e la quantità.
# possibile aggiungere nuovi articoli all'inventario.

class Negozio:
    def __init__(self):
        self.catalogo = {
            "carta": {"prezzo": 5, "quantita": 10},
            "penna": {"prezzo": 1, "quantita": 20}}
        self.guada=(100)
    def aggiugere(self):
        x=input("quale artggiungere")
        y=input('quanto costa')
        z=int(input("quanti pezzi"))
        self.catalogo[x] = {"prezzo": y, "quantita": z}
        print(x,y,z,'aggiunti')
#Gli articoli possono essere rimossi o aggiornati (ad es., cambiare prezzo o quantità).
    def rimuovi(self):
        x=input("quale rimuovere")
        y=input('quanto costa')
        z=int(input("quanti pezzi"))
        del self.catalogo[x]
        print(x,y,z,'rimossi')
    def aggiorna(self):
        h=input('cosa vuoi aggonrare?')
        if h=='articolo':
            p=input('in cosa cambiarlo')
            self.catalogo[h] = p
            print('fatto')
        elif h=='prezzo':
            p=input('in cosa cambiarlo')
            self.catalogo["articolo"]=p
            print('fatto')
        elif h=='quantita':
            p=input('in cosa cambiarlo')
            self.catalogo["articolo"]=p
            print('fatto')
#l'analisi del negozio da parte degli amministratori.
class Amministrazione:
    def __init__(self):
        self.guada=(100)
        self.passwordadmin=(1111)
    def registraadmin(self):
        regist=int(input('che password creare'))
        self.password(regist)
        print('admin registrato')
    def login(self):
        log=int(input('inserisci password'))
        if log==self.passwordadmin:
            print('benvenuto')
        else:
            admin1.registraadmin()


    def visuallizza(self):
        print(negoz.catalogo)
    
    def guadagno(self):
        print(self.guada)

#I clienti possono visualizzare gli articoli disponibili in inventario.
class Utente:
    def __init__(self):
        self.password=(1234)
   
    def login(self):
        x=input('inserire password')
        if x==self.password:
            print('benvenuto')

    def visuallizza(self):
        print(negoz.catalogo)
    
    def registra(self):
            regist=int(input('che password creare'))
            self.password(regist)
            print('utente registrato')

    def logic(self):
        log=int(input('inserisci password'))
        if log==self.password:
            print('benvenuto')
        else:
            utente1.registra()
            
        
#I clienti possono selezionare e acquistare articoli dall'inventario.
    def acquista(self):
       scelta=input('cosa vuoi acquistare?')
       if scelta in negoz.catalogo:
           qt=int(input('quanti ne vuoi'))
           prezzotot=negoz.catalogo[scelta]["prezzo"]*qt
           print('sono', prezzotot, 'da pagare')
#Il sistema tiene traccia degli acquisti dei clienti. yield


admin1=Amministrazione()
negoz=Negozio()
utente1=Utente()
t=True
while t==True:
    x=input('sei un negozio o un utente o admin')
    if x=='negozio':
        cosa=input('cosa vuoi fare')
        match cosa:
            case 'aggiungere':
                negoz.aggiugere()
            case 'rimuovi':
                negoz.rimuovi()
            case 'aggiorna':
                negoz.aggiorna()
    elif x=='utente':
        utente1.logic()
        cosa=input('cosa vuoi fare')
        match cosa:
            case 'visuallizza':
                utente1.visuallizza()
            case 'acquista':
                utente1.acquista()
    elif x=='admin':
        cosa=input('cosa vuoi fare')
        match cosa:
            case 'visualizza catalogo':
                admin1.visuallizza()
            case 'vedi guadagno':
                admin1.guada
        





 