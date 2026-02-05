#break
numeri = [1, 2, 3, 4, 5]
for n in numeri:
    break
print(n)

#continue
for n in numeri:
    if n==3:
        continue
    print(n)

#splat
c = [*range(1, 11, 3)]
print(c)

print(*'ciao')