#fare la spesa

listadellaspesa = ['pane','mele','latte']
carrello =[]

def decoratore(carrello):
    def wrapper():
        print('aggiungere al carrello')
        carrello()
        print('aggiunta riuscita')
    return wrapper

@decoratore
def aggiungi_item(nome:str):
    nuovo_prodotto =[]
    carrello.append(nuovo_prodotto) 

    for i in listadellaspesa:
        if i in listadellaspesa:
            yield carrello
        else:
            print('non fa parte della lista')
    return aggiungi_item
x = input('quale item stai prendendo dallo scaffale?')
aggiungi_item()

    


    