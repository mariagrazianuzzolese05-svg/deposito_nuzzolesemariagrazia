'''creare una classe base MetodoPagamento e diverse classi derivate che rappresentano diversi metodi di pagamento. Questo scenario permetterà di vedere il polimorfismo in azione, permettendo alle diverse sottoclassi di implementare i loro specifici comportamenti di pagamento, pur aderendo all'interfaccia comune definita dalla classe base.

Classe MetodoPagamento:
Metodi:
effettua_pagamento(importo): un metodo che ogni sottoclasse dovrà implementare.
Classi Derivate:
CartaDiCredito:
Metodi come effettua_pagamento(importo) che simula un pagamento tramite carta di credito.
PayPal:
Metodi come effettua_pagamento(importo) che simula un pagamento tramite PayPal.
BonificoBancario:
Metodi come effettua_pagamento(importo) che simula un pagamento tramite bonifico bancario.
GestorePagamenti:
Una classe che usa un'istanza di MetodoPagamento per effettuare pagamenti, senza preoccuparsi del dettaglio del metodo di pagamento.'''

'''Classe MetodoPagamento:
Metodi:
effettua_pagamento(importo): un metodo che ogni sottoclasse dovrà implementare.
Classi Derivate:'''

class MetodoPagamento:
    def setsaldo(self,nuovosaldo):
        self.saldo+=nuovosaldo
        print('importo avvenuto con successo')
        print("l'importo totale ora è:",self.saldo)

'''CartaDiCredito:
Metodi come effettua_pagamento(importo) che simula un pagamento tramite carta di credito.'''
class CartaDiCredito(MetodoPagamento):
    def __init__(self, codice,saldototale):
        self.__codice=codice
        self.__saldototale=saldototale
    def setsaldo(self,nuovosaldo):
        self.saldo=nuovosaldo
        super().setsaldo(55)
        print('pagamento fatto con carta di credito')
        
'''PayPal:
Metodi come effettua_pagamento(importo) che simula un pagamento tramite PayPal.'''
class Paypal(MetodoPagamento):
    def __init__(self, codice, saldototale):
        self.__codice=codice
        self.__saldototale=saldototale
    def setsaldo(self,nuovosaldo):
        self.saldo=nuovosaldo
        super().setsaldo(100)
        print('pagamento fatto con paypal',self.saldo)
    
'''BonificoBancario:
Metodi come effettua_pagamento(importo) che simula un pagamento tramite bonifico bancario.'''
class BonificoBancario(MetodoPagamento):
    def __init__(self, codice, saldototale):
        self.__codice=codice
        self.__saldototale=saldototale
    def setsaldo(self,nuovosaldo):
        self.saldo=nuovosaldo
        super().setsaldo(90)
        print('pagamento fatto con bonifico',self.saldo)

'''GestorePagamenti:
Una classe che usa un'istanza di MetodoPagamento per effettuare pagamenti, senza preoccuparsi del dettaglio del metodo di pagamento.'''
class GestorePagamenti(MetodoPagamento):
    def __init__(self, codice, saldototale):
        self.__codice=codice
        self.__saldototale=saldototale
    def setsaldo(self,nuovosaldo):
        self.saldo=nuovosaldo
        super().setsaldo(80)
        print('pagamento fatto',self.saldo)

conto_con_paypal=Paypal(1234,111)
bonifico=BonificoBancario(5678,999)
indipendente=GestorePagamenti(4444,10)

conto_con_paypal.setsaldo(100)
bonifico.setsaldo(100)
indipendente.setsaldo(100)


    
    

    
