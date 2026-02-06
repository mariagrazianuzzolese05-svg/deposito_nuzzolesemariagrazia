#def senza return (non viene associata  variabile e usi solo una volta
def saluta(nome):
    print('ciao,', nome)
def somma(a, b):
    risultato = a + b
    print('la somma è:' , risultato)
#return
def quadrato(numero):
    return numero * numero
risultato = quadrato(4)
def moltiplicazione(a:int, b:int):
    print(a*b)
moltiplicazione(2,4)