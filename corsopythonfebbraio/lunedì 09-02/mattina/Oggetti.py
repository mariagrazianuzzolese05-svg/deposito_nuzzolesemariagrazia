#class
class Automobile:
    numero_di_ruote =4
    def __init__(self,marca,modello):
        self.marca=marca
        self.modello =modello
    def stampa_info(self):
        print("l'auto è una",self.marca,self.modello)
auto1=Automobile("fiat","500")
auto1.stampa_info()

class Persona():
    x=10
    def __init__(self):
        mirko_OBJ=Persona()
        print(mirko_OBJ.x)
Persona.x=20
veronica_OBJ=Persona()

#tipi basilari
print(type(10))
print(type(1.2))
print("test")
print(type([1, 2]))

#tipi non basilari
class MioOggetto:
    def __init__(self):
        pass
    def __str__(self):
        pass
obj=MioOggetto(20)
print(type(obj))

#metodo statico
class Calcolatrice:
    @staticmethod
    def somma(a,b):
        return a+b
risultato=Calcolatrice.somma(5,3)
print(risultato)

#metodo decorato
class Contatore:
    numero_istanze=0
    def __init__(self):
        Contatore.numero_istanze+=1
    @classmethod
    def mostra_numero_istanze(cls):
        print({cls.numero_istanze})
    def __str__(self):
        # Viene richiamato quando facciamo: print(istanza_di_Persona)
        return f"Persona(nome={self.nome}, eta={self.eta})"
c1=Contatore() 

#to string
