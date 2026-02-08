#fare la spesa

listadellaspesa = ['pane','mele','latte']
carrello =[]

def decoratore(aggiungi_item):
    def wrapper():
        print('aggiungere al carrello')
        aggiungi_item()
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
def decspesafatta(spesa_fatta):
    def wrapper():
        print('manca qualcosa?')
        spesa_fatta()
        print('spesa fatta')
    return wrapper

@decspesafatta 
def spesa_fatta(*args):
    a =input('spesa finita?') 
    if args=='si':
        print('spesa completata')
spesa_fatta()
 
