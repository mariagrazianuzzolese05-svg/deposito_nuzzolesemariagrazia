#lambda
#esempio di una funzione
def doppNumero(x):
    return x*x

lambda x:x*x #si scrive lambda,l'elemnto che accetta e : l'elaborazione che fa
#se riprendiamo l'esercizio di prima
numero = [1,2,3,4,5]
#prima nell'eserizio di prima potevamo fare
numeri = list(map(lambda x:x*3, numero))
print(numeri)