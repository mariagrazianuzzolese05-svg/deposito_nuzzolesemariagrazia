class Biblioteca:
    def __init__(self):
        pass
class Libro:
    def __init__(self, libro):
        self.libro=libro
    def creazione(self,nuovo):
        self.libro=nuovo
libro1=Libro("da mettere")
t=True
while t==True:
    nuovo=input('che libro vuoi aggiungere?')
    libro1.creazione(nuovo)
    print(libro1.libro, "aggiunto")
    scelta = input("Vuoi continuare? ")
    if scelta == 'no':
        t = False
#errori che ho fatto:non mettere tra le parentesi le cose chieste dentro init e non aver messo init a  biblioteca e libro1.creazione no creazione ma libro a  riga 16