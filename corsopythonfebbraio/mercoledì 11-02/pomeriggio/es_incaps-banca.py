'''L'obiettivo è utilizzare l'incapsulamento per prevenire accessi non autorizzati o modifiche inappropriate al saldo del conto.

Classe ContoBancario:
Attributi privati:
__titolare (stringa che rappresenta il nome del titolare del conto)
__saldo (decimale che rappresenta il saldo del conto)
Metodi pubblici:
deposita(importo): aggiunge un importo al saldo solo se l'importo è positivo.
preleva(importo): sottrae un importo dal saldo solo se ci sono fondi sufficienti e l'importo è positivo.
visualizza_saldo(): restituisce il saldo corrente senza permettere la sua modifica diretta.
Gestione dei Metodi e Sicurezza:
I metodi deposita e preleva devono controllare che gli importi siano validi (e.g., non negativi).
Aggiungere metodi "getter" e "setter" per gli attributi come _titolare,
applicando validazioni appropriate (e.g., il titolare deve essere una stringa non vuota).'''

'''ss Utente:
class Cliente(Utente):
class Admin(Utente):'''

'''Classe ContoBancario:
Attributi privati:
__titolare (stringa che rappresenta il nome del titolare del conto)
__saldo (decimale che rappresenta il saldo del conto)'''

class Utente:
    def __init__(self,nometitolare,saldo):
        self.__nometitolare=nometitolare
        self.__saldo=saldo

    def setsaldo(self,nuovosaldo):
        self.saldo+=nuovosaldo
    def getsaldo(self,nuovosaldo):
        self.saldo=nuovosaldo
        print(self.saldo)


class Admin(Utente):
    def __init__(self, nometitolare, saldo):
        super().__init__(nometitolare, saldo)
    def viewprivate(self):
        return super().viewprivate()
    
class Cliente(Utente):
    def __init__(self, nometitolare, saldo):
        super().__init__(nometitolare, saldo)
    def viewprivate(self):
        return super().viewprivate()
    
class ContoBancario:
    def __init__(self,nometitolareconto):
        self.__nometitolareconto=nometitolareconto

    def deposito(self,nometitolareconto):
        importo=int(input('quanto aggiungere'))
        if importo>0:
          nometitolareconto.setsaldo(importo)
          print(self.__saldo,'totale')
        else:
            print('non valido')
    def preleva(self):
        importo=int(input('di quanto togliere'))
        if importo<=self.__saldo:#però voglio il saldo da cliente
            self.__saldo-=importo
            print(self.__saldo)
        else:
            print('non valido')

cliente1=Cliente('mariagrazia',99999)
admin1=Admin('paolo',100)
conto=ContoBancario(cliente1)

cliente1.getsaldo(100)
cliente1.setsaldo(100)
conto.deposito(cliente1)
conto.preleva()

        

    
