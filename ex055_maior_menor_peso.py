maior = 0
menor = 0
for a in range(1,6):
    massa = float(input('Digite a massa(peso) da {} pessoa: '.format(a)))
    if a == 1:
        maior = massa
        menor = massa
    else:
        if massa > maior:
            maior = massa
        elif massa < menor:
            menor = massa
print('A maior massa foi de {} e a menor massa foi de {}'.format(maior,menor))