from random import randint
from time import sleep
palp = int(input('Digite quantos papiltes quer sortear para mega sena: '))
final = []
sorteios = []
for a in range(0,palp):
    for b in range(0,6):
        numero = randint(1,60)
        while numero in sorteios:
            numero = randint(1,60)
        sorteios.append(numero)
    final.append(sorteios[:])
    sorteios.clear()
print('=-'*30)
cont = 1
for c in final:
    sleep(1)
    print(f'{cont}° jogo: {sorted(c)}')
    cont += 1
print('=-'*30)  
print('FIM')