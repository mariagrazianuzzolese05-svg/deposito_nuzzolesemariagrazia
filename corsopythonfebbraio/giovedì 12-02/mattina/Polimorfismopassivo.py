class Cane:
    def parla(self):
        return "Bau!"


class Gatto:
    def parla(self):
        return "Miao!"


def fai_parlare(animale):
    # Non importa di che tipo sia l'animale,
    print(animale.parla())

cane = Cane()
gatto = Gatto()

fai_parlare(cane)  # Output: Bau!
fai_parlare(gatto)  # Output: Miao!

#duck typing
class Cerchio:
    def disegna(self):
        print("Disegno un cerchio")


class Rettangolo:
    def disegna(self):
     print("Disegno un rettangolo")

def disegna_figura(figura):
    # Anche qui, basta che 'figura' abbia il metodo 'disegna'
    figura.disegna()
figure = [Cerchio(), Rettangolo()]     # figure[0]=Cerchio() / figure[1]=Rettagolo()

# Iteriamo e disegniamo ogni figura
for figura in figure:
    disegna_figura(figura)

#len
# Lista
print(len([1, 2, 3]))  
# Stringa
print(len("Ciao"))    
# Dizionario
print(len({"a": 1, "b": 2})) 

#main
if __name__ == "__main__":
    print("main")
else:
    print("import")



