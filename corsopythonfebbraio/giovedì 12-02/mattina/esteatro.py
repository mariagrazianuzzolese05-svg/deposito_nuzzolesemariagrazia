'''Andiamo a creare un sistema ripetibile che simuli un teatro:

Classe Base: Posto
Attributi privati:
_numero (intero): il numero del posto.
_fila (stringa): la fila in cui si trova il posto.
_occupato (booleano): stato del posto, se è occupato (True) o libero (False).
Metodi:
__init__(numero, fila): inizializza il posto impostando _occupato a False.
prenota(): prenota il posto se non è già occupato; in caso contrario, segnala che il posto è già occupato.
libera(): libera il posto se è occupato; altrimenti segnala che il posto non era prenotato.
Getter: per recuperare il numero, la fila e lo stato (occupato/libero).
Classi Derivate
PostoVIP:
Attributi aggiuntivi: servizi_extra (ad es. una lista di servizi come “Accesso al lounge”, “Servizio in posto”).
Metodi:
Sovrascrive il metodo prenota() per gestire, oltre alla prenotazione, l’attivazione dei servizi extra.
PostoStandard:
Attributi aggiuntivi: costo (un valore numerico che rappresenta il costo della prenotazione, ad esempio per prenotazione online).
Metodi:
Può sovrascrivere prenota() per includere la visualizzazione del costo o altre particolarità della prenotazione.
Classe Teatro
Attributi:
_posti: una lista contenente tutti gli oggetti posti (sia VIP che Standard).
Metodi:
aggiungi_posto(posto): per aggiungere un nuovo posto alla lista.
prenota_posto(numero, fila): cerca nella lista il posto corrispondente al numero e alla fila indicati e, se lo trova, invoca il metodo prenota() sul posto.
stampa_posti_occupati(): stampa tutti i posti che risultano occupati.'''

'''Classe Base: Posto
Attributi privati:
_numero (intero): il numero del posto.
_fila (stringa): la fila in cui si trova il posto.
_occupato (booleano): stato del posto, se è occupato (True) o libero (False).'''
occ=['libero','occupato','occupato']
listaposti=[1,2,3]
listafile=['a','b','c']
serviziextra=['bagnovip','aperitivo','allinclusive']
class Posto:
    def __init__(self, numero:int, fila:str,occupato):
        self.__numero=numero
        self.__fila=fila
        self.occupato=occupato
        self.occupato=False
#prenota(): prenota il posto se non è già occupato; in caso contrario, segnala che il posto è già occupato.
    def setprenota(self,nuovoposto, nuovafila):
        self.nuovoposto=nuovoposto
        self.nuovafila=nuovafila
        while True:
                print('prenotatosedile numero',self.nuovoposto,self.nuovafila)
                altro=input('altro?')
                if altro=='no':
                    break
                
#libera(): libera il posto se è occupato; altrimenti segnala che il posto non era prenotato.
    def setlibera(self,nuovoposto, nuovafila):
        self.nuovoposto=nuovoposto
        self.nuovafila=nuovafila
        while True:
            which=int(input('quale fila vuoi liberare'))
            if which in listafile:
                p=int(input('quale posto?'))
                if p in listafile:
                    ora=input('liberato osedile numero',self.nuovoposto,self.nuovafila,'altro?')
                    if ora=='no':
                        False
                else:
                    print('informazione mancante')
            else:
                print('non era prenotato')
#'''Getter: per recuperare il numero, la fila e lo stato (occupato/libero).'''
    def getposto(self,nuovoposto,nuovafila):
        self.nuovoposto=nuovoposto
        self.nuovafila=nuovafila
        print(self.nuovoposto,self.nuovafila)    

'''PostoStandard:
Attributi aggiuntivi: costo (un valore numerico che rappresenta il costo della prenotazione, ad esempio per prenotazione online).'''
class PostoStandard(Posto):
    def __init__(self, numero, fila, occupato,costo):
        self.__costo=costo
        super().__init__(numero, fila, occupato)
    def getposto(self, nuovoposto, nuovafila,costo):
        self.__costo=costo
        super().getposto(nuovoposto, nuovafila,costo)
    

class PostoVip(PostoStandard):
    def __init__(self, numero, fila, occupato, costo,serviziextra):
        super().__init__(numero, fila, occupato, costo)
        self.serviziextra=serviziextra
#'''Metodi:Sovrascrive il metodo prenota() per gestire, oltre alla prenotazione, l’attivazione dei servizi extra.'''
    def setprenota(self, nuovoposto, nuovafila,serviziextra):
        self.serviziextra=serviziextra
        super().setprenota(nuovoposto, nuovafila)
        print('prenotato postovip',self.nuovoposto,self.nuovafila,self.serviziextra)


'''Classe Teatro
Attributi:
_posti: una lista contenente tutti gli oggetti posti (sia VIP che Standard).
Metodi:
aggiungi_posto(posto): per aggiungere un nuovo posto alla lista.
prenota_posto(numero, fila): cerca nella lista il posto corrispondente al numero
 e alla fila indicati e, se lo trova, invoca il metodo prenota() sul posto.
stampa_posti_occupati(): stampa tutti i posti che risultano occupati.'''
class Teatro(Posto):#avrebbe più senso il contrario però ok
    def __init__(self,posti):
        self.__posti=posti
    def aggiungi(self,nuovoposto,nuovafila):
        self.nuovoposto=nuovoposto
        self.nuovafila=nuovafila
        listaposti.append(nuovoposto)
        listafile.append(nuovafila)
        print(self.nuovoposto,self.nuovafila,'aggiunti a',listaposti,listafile)
    def stampa(self,occupato):
        self.occupato=occupato
        self.occupato=False
        if self.occupato==True:
            print(self.occupato)
        else:
            print('libero')
    def setprenota(self, nuovoposto, nuovafila):
        return super().setprenota(nuovoposto, nuovafila)
'''
prenota_posto(numero, fila): cerca nella lista il posto corrispondente al numero e alla fila indicati e, se lo trova,
 invoca il metodo prenota() sul posto.
stampa_posti_occupati(): stampa tutti i posti che risultano occupati.'''
puccini=Teatro(100)
puccini.stampa(False)
postovip=PostoVip(10,'f',False,100,'bagnovip')
postovip.setprenota(10,'f','bagnovip')
posto1=PostoStandard(1,'a',False,2)
posto1.getposto(1,'a',2)
puccini.aggiungi(5,'d')
        