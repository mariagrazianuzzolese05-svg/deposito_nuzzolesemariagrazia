'''Il sistema deve includere una classe Pacco con: 
codice (stringa), peso (numero) e stato (es. "in magazzino",
 "in consegna", "consegnato"), con un metodo per mostrare le
   info e un metodo per cambiare stato.

Deve esserci una classe Magazzino che contiene 
una lista (o dizionario) di pacchi e permette di
 aggiungere un pacco, cercarlo per codice, e mostrare 
 tutti i pacchi in un certo stato.

Deve esserci infine una classe GestorePacchi che usa il
 magazzino per mettere un pacco “in consegna”, segnare un 
 pacco come “consegnato” e calcolare il peso totale dei 
 pacchi ancora non consegnati.

Nel programma principale crea almeno 5 pacchi,
inseriscili nel magazzino, cambia lo stato di alcuni pacchi
 (almeno una consegna avviata e una consegna completata) 
 e stampa: elenco pacchi “in magazzino”, elenco pacchi
“in consegna” e il peso totale dei pacchi non ancora consegnati.'''

class Pacco:
    def __init__(self, codice:str,peso:int,stato:str):
        self.codice=codice
        self.peso=peso
        self.stato=stato
# metodo per mostrare le info
    def vedi_info(self):
        print('le info del pacco sono:',self.codice, self.peso,self.stato)
#metodo per cambiare stato.
    def cambia_stato(self):
        c=input('vuoi cambiare stato?')
        if c=='si':
            cc=input('impostare nuovo stato')
            match cc:
                case 'in consegna':
                    self.stato= 'in consegna'
                    print('pacco stato cambiato in:',self.stato)
                case 'in magazzino':
                    self.stato= 'in magazzino'
                    print('pacco stato cambiato in:',self.stato)
                case 'consegnato':
                    self.stato= 'consegnato'
                    print('pacco stato cambiato in:',self.stato)
#classe Magazzino 
class Magazzino:
    def __init__(self):
        self.magazzino = {
            "pacco1": {"codice": "aaaa", "peso": 1, "stato": "in magazzino"},
            "pacco2": {"codice": "bbbb", "peso": 2, "stato": "in magazzino"},
            "pacco3": {"codice": "cccc", "peso": 3, "stato": "in magazzino"},
            "pacco4": {"codice": "dddd", "peso": 4, "stato": "in magazzino"},
            "pacco5": {"codice": "eeee", "peso": 5, "stato": "in magazzino"},
            }
#aggiungere un pacco, cercarlo per codice, e mostrare 
# #tutti i pacchi in un certo stato.''' 
    def aggiungere_pacco(self):
        nuovon=input("nome nuovo pacco")
        nuovoc=input("codice nuovo pacco")
        nuovop=input("peso nuovo pacco")
        nuovos=input('stato nuovo pacco')
        self.magazzino[nuovon] = {"codice": nuovoc, "peso": nuovop, "stato":nuovos}
        print(nuovon,"aggiunto con peso",nuovop,"e",nuovos)

'''classe GestorePacchi che usa il
 magazzino per mettere un pacco “in consegna”, segnare un 
 pacco come “consegnato”'''
class Gestore_Pacchi:
    def __init__(self, magazzino_da_usare):
        self.mag=magazzino_da_usare

    def modifica_stato(self):
        modificas=input('vuoi modificare stato?')
        if modificas=='si':
            qualep=input('quale pacco modificare stato')
            match qualep:
                case 'pacco1':
                    opzione=input('in cosegna o consegnato')
                    if opzione=='in consegna':
 #Magazzino o altro?
                       mag.magazzino['pacco1'] = opzione
                       print('pacco1 stato modificato in',opzione)
                case 'pacco2':
                    opzione=input('in cosegna o consegnato')
                    if opzione=='in consegna':
                        Magazzino.magazzino['pacco1'] = opzione
                        print('pacco1 stato modificato in',opzione)
                case 'pacco3':
                    opzione=input('in cosegna o consegnato')
                    if opzione=='in consegna':
                        Magazzino.magazzino['pacco1'] = opzione
                        print('pacco1 stato modificato in',opzione)
                case 'pacco4':
                    opzione=input('in cosegna o consegnato')
                    if opzione=='in consegna':
                        Magazzino.magazzino['pacco1'] = opzione
                        print('pacco1 stato modificato in',opzione)
                case 'pacco5':
                    opzione=input('in cosegna o consegnato')
                    if opzione=='in consegna':
                        Magazzino.magazzino['pacco1'] = opzione
                        print('pacco1 stato modificato in',opzione)
# e calcolare il peso totale dei pacchi ancora non consegnati.
    def calcolo_peso(self):
        pesotot = 0
        for i in mag.magazzino:
            y = mag.magazzino[i]
            if  y ["stato"] != "consegnato":
                pesotot +=mag.magazzino[i]["peso"]#importante devo mettere mag.mazzino
        print(pesotot)
'''Nel programma principale crea almeno 5 pacchi,
inseriscili nel magazzino, cambia lo stato di alcuni pacchi
 (almeno una consegna avviata e una consegna completata) 
 e stampa: elenco pacchi “in magazzino”, elenco pacchi
“in consegna” e il peso totale dei pacchi non ancora consegnati.'''
mag=Magazzino()
#aggiungere pacchi e trasformare in lista magazzino(da vedere questo)
#fai main
gestore=Gestore_Pacchi(mag)
pacco6=Pacco('aaaa',2,'in magazzino')
while True:
    scelta=input('cosa vuoi fare')
    match scelta:
        case 'calcolo peso':
            gestore.calcolo_peso()
            altro=input('altro?')
            if altro=='no':
                break
        case 'modifica stato':
            gestore.modifica_stato()
            altro=input('altro?')
            if altro=='no':
                break
        case 'cambia stato':
            pacco6.cambia_stato()
            altro=input('altro?')
            if altro=='no':
                break
        case 'aggiungere pacco':
            mag.aggiungere_pacco()
            altro=input('altro?')
            if altro=='no':
                break
        case 'vedi info':
            pacco6.vedi_info()
            altro=input('altro?')
            if altro=='no':
                break




