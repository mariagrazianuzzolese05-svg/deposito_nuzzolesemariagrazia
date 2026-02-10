'''Esercizio 2 (Facile):

Crea una classe chiamata Libro. Questa classe dovrebbe avere:

Tre attributi: titolo, autore e pagine.

Un metodo descrizione che restituisca una stringa del tipo "Il libro 'titolo' è stato scritto da 'autore' e ha 'pagine' pagine.".'''

class Libro:

    def __init__ (self, titolo, pagine):
        self.titolo =titolo
        self.pagine =pagine
    def descrizione(self, titolo, pagine):
        self.titolo =titolo  
        self.pagine =pagine
        print("il libro", self.titolo, "e ha", self.pagine)

libro1=Libro('da mettere',0)
t =True

while t==True:
    if t==True:
     titolo=input('titolo libro da inserire')
     pagine=int(input("uante pagine ha"))
    libro1.descrizione(titolo, pagine)
    print("il libro",titolo,"ha" ,pagine)
    scelta = input("Vuoi continuare? ")
    if scelta == 'no':
        t = False