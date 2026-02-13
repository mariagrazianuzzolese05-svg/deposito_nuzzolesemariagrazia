#operatori logici
x = 5
y = 10
z = 7
print(x < y and y > z)
print(x < y or z > y)
print(not(x < y))

#lista numerica 
numeri = [1, 2, 3, 4, 5]

#lista di stringhe
nomi = ["alice", "bob", "charlie"]

#lista mista
misto = [1, "due", True, 4.5]

#indici
print(numeri[0])
print(numeri[2])

#lista di liste
ldl = [numeri, nomi,misto]
print(ldl)

#modificare lista
numeri[2] = 10
print(numeri)

#metodi
print(len(numeri))

#aggiungere elemento
numeri.append(7)
print(numeri)

#inserire in una posizione specifica
numeri.insert(2, 10)
print(numeri)

#rimuovere elemento
numeri.remove(4)
print(numeri)

#ordinare lista
numeri.sort()
print(numeri)

#tuple numerica
punto = (5, 4, 0)
print(punto)

#tuple stringhe
info = ("alice", 25, "femmina")
print(info)


#indici tuple
print(punto[0])
print(info[2])

#da tupla a lista
lista = list(info)   

#packing
pippo = 3, 4

#unpacking
g, f =pippo
print(g, f)

#set con ()
set1 = set([1, 2, 2])
print(set1)

#unione
set3 = {1, 4, 6}
set4 = {4, 7, 8 }
print(set3.union(set4))

#intersezione
print(set3.intersection(set4))

#differenza
print(set3.difference(set4))

#differenza simmetrica
print(set3.symmetric_difference(set4))

#add
set3.add("orange")
print(set3)

#remove
set4.remove(4)
print(set4)

#discard
set4.discard(5) #anche se 5 non c'è non dà errore al contrario di remove
print(set4)

#len
len(set3)
print(set3)

#copy
x = set3.copy()
print(x)

