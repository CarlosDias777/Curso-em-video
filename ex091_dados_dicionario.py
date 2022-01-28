from random import randint
from time import sleep
from operator import itemgetter
res = {}
ordem = {}
for pos in range(1,5):
    n = randint(1,6)
    res[pos] = n
for k, v in res.items():
    print(f'O jogador{k} tirou {v} no dado')
    sleep(1)
ordem = sorted(res.items(),key=itemgetter(1), reverse=True)
print('-=-'*20)
for cont, a in enumerate(ordem):
    print(f'{cont+1}° lugar: jogardor{a[0]} com {a[1]}')
    sleep(1)