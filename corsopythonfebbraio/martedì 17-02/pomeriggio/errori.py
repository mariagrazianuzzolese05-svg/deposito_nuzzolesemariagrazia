n=input('n:')
try:
    print(int(n))
except TypeError as e:
    print('erroere')
except ValueError as e:
    print('erroere')
except:
    print('errore')