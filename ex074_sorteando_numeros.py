#forma que eu fiz sem tuplas
from random import randint
"""
maior = menor = 0
for a in range(1,6):
    rand = randint(0,10)
    print(rand, end=' → ')
    if a == 1:
        menor = rand
        maior = rand
    else:
        if rand > maior:
            maior = rand
        elif rand < menor:
            menor = rand
print('Fim\n')
    
print(f'O maior valor foi {maior} e o menor valor foi {menor}')"""

numeros = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
print(f'O valores sorteados foram: ', end ='')
for n in numeros:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')