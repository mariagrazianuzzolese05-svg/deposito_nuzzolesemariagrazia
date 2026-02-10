'''Obiettivo: Creare una classe Ristorante che permetta di gestire alcune funzionalità di base .
Requisiti:
Definizione della Classe:
Creare una classe chiamata Ristorante.
La classe dovrebbe avere un costruttore __init__ che accetta due parametri: nome (nome del ristorante) e tipo_cucina (tipo di cucina offerta).
Definire un attributo aperto che indica se il ristorante è aperto o chiuso. Questo attributo deve essere impostato su False di default (cioè, il ristorante è chiuso).
Un Lista o + menu dove dentro ci sono i piatti e prezzi che ha il ristorante
Metodi della Classe:
descrivi_ristorante(): Un metodo che stampa una frase descrivendo il ristorante, includendo il nome e il tipo di cucina.
stato_apertura(): Un metodo che stampa se il ristorante è aperto o chiuso.
apri_ristorante(): Un metodo che imposta l'attributo aperto su True e stampa un messaggio che indica che il ristorante è ora aperto.
chiudi_ristorante(): Un metodo che imposta l'attributo aperto su False e stampa un messaggio che indica che il ristorante è ora chiuso.
aggiungi_al_menu(): Un metodo per aggiungere piatti al menu
togli_dal_menu(): Un metodo per togliere piatti al menu
stampa_menu(): Un metodo per stampare il menu
Testare la Classe:
Creare un'istanza della classe Ristorante, passando i valori appropriati al costruttore.
Testare tutti i metodi creati per assicurarsi che funzionino come previsto.'''

#Creare una classe chiamata Ristorante.
#_init__ che accetta due parametri: nome (nome del ristorante) e tipo_cucina (tipo di cucina offerta).
class Ristorante:
     #Definire un attributo aperto che indica se il ristorante è aperto o chiuso
    def __init__(self, nome, tipo_cucina):
        self.domicilio=False #extra (vedi riga 68)
        self.aperto = False
        self.nome =nome
        self.tipo_cucina =tipo_cucina
       
        #Un Lista o + menu dove dentro ci sono i piatti e prezzi che ha il ristorante
        self.menu= ["lasagna","pizza"]
        self.prezzi =[10, 20]
#Metodi della Classe:
#Un metodo che stampa una frase descrivendo il ristorante, includendo il nome e il tipo di cucina.
    def descrizione(self):
        return ("questo ristorante si chiama", self.nome, "e si occupa di cucina" ,self.tipo_cucina)
#stato_apertura(): Un metodo che stampa se il ristorante è aperto o chiuso.
    def stato_apertura(self):
        if self.aperto==False:
            print('chiuso')
        else:
            print('aperto')
#apri_ristorante(): Un metodo che imposta l'attributo aperto su True e stampa un messaggio che indica che il ristorante è ora aperto.
    def apri_ristorante(self):
        self.aperto = True
        print('il ristorante è aperto')
#chiudi_ristorante(): Un metodo che imposta l'attributo aperto su False e stampa un messaggio che indica che il ristorante è ora chiuso.
    def chiudi_ristorante(self):
        self.aperto = False
        print('il ristorante èchiuso')
#aggiungi_al_menu(): Un metodo per aggiungere piatti al menu
    def  aggiungi_menu(self):
        if self.aperto==False:
            print('il ristorante è chiuso,non si può')
        else:
            x=input("quale piatto aggiungere")
            self.menu.append(x)
            y=input('quanto costa')
            self.prezzi.append(y)
            print(x,y,"aggiunti con successo")
#togli_dal_menu(): Un metodo per togliere piatti al menu
    def togli_menu(self):
        if self.aperto==False:
            print('il ristorante è chiuso,non si può')
        else:
            x=input('quale piatto togliere')
            self.menu.remove(x)
            y=input('quanto costava')
            self.prezzi.remove(y)
            print('eliminato con successo')
#stampa_menu(): Un metodo per stampare il menu
    def stampa_menu(self):
        print('questi sono i piatti',self.menu, 'e questi i prezzi',self.prezzi)
#extra:asporto o domicilio e di base fanno d'asporto a meno che non venga detto di volere il domicilio
    def asporto(self):
        if self.aperto==False:
            print('il ristorante è chiuso,non si può')
        else:
            a=input('asporto o domicilio')
            if a =='domicilio':
                d=input('selezionare via')
                c=int(input('inserire civico'))
                print('stiamo arrivando')
            else:
                print('vi aspettiamo')

#Creare un'istanza della classe Ristorante, passando i valori appropriati al costruttore.
rist=Ristorante('da mirko','italiana')
print(rist.descrizione()) 
rist.apri_ristorante()
rist.stato_apertura()
rist.asporto() #extra
rist.aggiungi_menu()
rist.stampa_menu()
rist.togli_menu()
rist.stampa_menu()
rist.chiudi_ristorante()
rist.stato_apertura()
