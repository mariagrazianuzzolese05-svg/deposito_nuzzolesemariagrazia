class Prodotto:
    def __init__(self, nome, prezzo):
        self.nome = nome
        self.prezzo = prezzo

    # Il metodo "To String"
    def __str__(self):
        return self.nome +' ciao' # Decidiamo che stampando l'oggetto vedremo il nome

# --- PROVA IL RISULTATO ---

p1 = Prodotto("Computer", 1000)

# SENZA __str__ vedresti: <__main__.Prodotto object at 0x0000...>
# CON __str__ vedi:
print(p1)