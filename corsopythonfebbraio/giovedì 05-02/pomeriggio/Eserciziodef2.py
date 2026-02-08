#fibonacci
def fibonacci(n):
    sequenza =[]
    a, b=0,1
    while a<n:
        sequenza.append(a)
        a,b=b,a+b
    return sequenza
risultato= fibonacci(int(input('che numero scegli?')))
print(risultato)