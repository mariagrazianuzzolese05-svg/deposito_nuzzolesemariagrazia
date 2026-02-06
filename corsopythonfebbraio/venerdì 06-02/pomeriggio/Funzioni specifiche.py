#generatori
def fibonacci(n):
    # Generatore Fibonacci: produce n numeri
    a, b = 0, 1
    count = 0
    while count < n:
        yield a #riporta indietro a e aspetta le altre funzioni
        a, b = b, a + b
        count += 1
print(list(fibonacci(10)))
'''for x in list[fibonacci(10)]:
    print(x)'''




# 6) yield from: un generatore che "delega" a un altro
# ==============================================================

def catena_generatori():
    # Prima produce 1..3, poi 10..12
    yield from range(1, 4)
    yield from range(10, 13)
    print(catena_generatori)

#pari
def pari(n):
    for i in range(n):
        if i % 2==0:
            yield i
    print(i)

    #decoratore
def decoratore(funzione):
    def wrapper():
        print('yy')
        funzione()
        print('oo')
    return wrapper

@decoratore
def saluta():
    print('ciao')
saluta()

#dec
def decoratore_con_argomenti(funzione):
    def wrapper(*args, **kwargs):
        print("Prima")
        risultato = funzione(*args, **kwargs)
        print("Dopo")
        return risultato
    return wrapper

@decoratore_con_argomenti
def somma(a, b):
    print(a+b)
    return a + b

print("risultato è", somma(3, 4))

#wrapper
'''def logger(funzione):
    def wrapper(*args, **kwargs):
    print(f"Chiamata a {funzione.__name__} con argomenti: {args} e {kwargs}")
    risultato = funzione(*args, **kwargs)
    print(f"Risultato di {funzione.__name__}: {risultato}")
    return risultato
return wrapper

@logger
def moltiplica(a, b):
    return a * b

# Chiamata alla funzione decorata
print(moltiplica(3, 4))'''

