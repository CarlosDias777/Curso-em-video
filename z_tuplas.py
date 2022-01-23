lanche = ('hamburguer','suco','pizza','pudim')
print(lanche)

print(lanche[-1::-1]) #-1 do inicio referencia onde vai começar, no caso o pudim, e o -1 final é voltando de 1 em 1

for pos, c in enumerate(lanche):
    print(f'Eu vou comer {c}, na posição {pos}')

print(sorted(lanche))

print(lanche.index('suco'))
