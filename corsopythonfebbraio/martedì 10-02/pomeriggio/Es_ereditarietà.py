'''Classe Prodotto:
Attributi:
nome (stringa che descrive il nome del prodotto)
costo_produzione (costo per produrre il prodotto)
prezzo_vendita (prezzo a cui il prodotto viene venduto al pubblico)
Metodi:
calcola_profitto: restituisce la differenza tra il prezzo di vendita e il costo di produzione.

Classi parallele:
Creare almeno due classi parallele a Prodotto, per esempio Elettronica e Abbigliamento.
Aggiungere attributi specifici per ciascun tipo di prodotto, come materiale per Abbigliamento e garanzia per Elettronica.

Classe Fabbrica:
Attributi:
inventario: un dizionario che tiene traccia del numero di ogni tipo di prodotto in magazzino.
Metodi:
aggiungi_prodotto: aggiunge prodotti all'inventario.
vendi_prodotto: diminuisce la quantità di un prodotto in inventario e stampa il profitto realizzato dalla vendita.
resi_prodotto: aumenta la quantità di un prodotto restituito in inventario.'''

class Prodotto:
    def __init__(self, nome, costo_produzione, prezzo):
        self.nome=nome
        self.costo_produzione=costo_produzione
        self.prezzo=prezzo
#calcola_profitto: restituisce la differenza tra il prezzo di vendita e il costo di produzione.
    def calcola_profitto(self):
        return self.prezzo - self.costo_produzione
class Elettronica(Prodotto):
    def __init__(self, nome, costo_produzione, prezzo, garanzia):
        super().__init__(nome, costo_produzione, prezzo)
        self.garanzia=garanzia
    def calcola_profitto(self):
        return super().calcola_profitto()
class Abbigliamento(Prodotto):
    def __init__(self, nome, costo_produzione, prezzo,tessuto):
        super().__init__(nome, costo_produzione, prezzo)
        self.tessuto=tessuto
    def calcola_profitto(self):
        return super().calcola_profitto()
class Fabbrica:
#inventario: un dizionario che tiene traccia del numero di ogni tipo di prodotto in magazzino.
    def __init__(self,quantità):
        self.quantità=quantità
        self.quantità= {"telefono":10,"maglie":5}
#aggiunge prodotti all'inventario.
    def aggiungi(self):
        x=input('cosa vuoi aggiungere')
        y=int(input('quantità'))
        self.quantità[x] = {"quantità": y}
        print(self.quantità)
#vendi_prodotto: diminuisce la quantità di un prodotto in inventario
# e stampa il profitto realizzato dalla vendita.
    def vendi(self):
        x=input('da cosa togliere')
        y=int(input('di quanto'))
        self.quantità[x]=y
        profitto = cuffie.calcola_profitto() * y #ci voleva un if per le opzioni
        print(profitto)
#resi_prodotto: aumenta la quantità di un prodotto restituito in inventario.'''
    def reso(self):
        x=input('da cosa aggiungere')
        y=int(input('di quanto'))
        self.quantità[x]=y
        print(self.quantità)
fab=Fabbrica(1000)
prodotti=Prodotto('prodott', 100, 10)
cuffie =Elettronica('cuffie', 3, 2, 1)
scarpe=Abbigliamento('scarpe', 5,7,'lana')
def main():
    while True:
        prodotti.calcola_profitto()
        fab.vendi()
        fab.reso()
        fab.aggiungi()
        continuare=input('continuare?')
        if continuare=='no':
            break

main()

        
    
