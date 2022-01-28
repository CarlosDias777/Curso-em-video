from random import randint
from time import sleep
numeros = []
def sortear(a,b):
    print('Os numeros sorteados foram:')
    for j in range(0,5):
        sort = randint(a,b)
        numeros.append(sort)
        print(sort, end=' ', flush=True)
        sleep(0.5)

   
def par(n):
    s = 0
    for f in n:
        if f % 2 == 0:
            s += f
    print(f'\nA soma dos numeros pares sorteados resulta em {s}')

sortear(1,10)
par(numeros)

