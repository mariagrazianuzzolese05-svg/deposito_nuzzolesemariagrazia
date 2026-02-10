'''Esercizio 1 (Facile):
Crea una classe chiamata Punto. Questa classe dovrebbe avere:
Due attributi: x e y, per rappresentare le coordinate del punto nel piano.
Un metodo muovi che prenda in input un valore per dx e un valore per dy e modifichi le coordinate del punto di questi valori.
Un metodo distanza_da_origine che restituisca la distanza del punto dall'origine (0,0) del piano.'''
#creato classe
class Punto:
    def __init__(self, x, y):
        self.x=x
        self.y=y
        
    def muovi(self, dx, dy):
        self.dx=dx
        self.dy=dy
        self.x += dx
        self.y +=dy
    def distanza_origine(self):
        return (self.x**2 + self.y**2)**0.5
#aggiunto oggetto alla classe
p1 = Punto(0, 0)
t =True
while t==True:
    if t==True:
        
        dx=int(input('di quanto ti vuoi muovere con x'))
        dy=int(input('di quanto tivuoi muovere con y'))
        p1.muovi(dx, dy)
        d = p1.distanza_origine()
        print(d)
    
    scelta = input("Vuoi continuare? ")
    if scelta == 'no':
        t = False




