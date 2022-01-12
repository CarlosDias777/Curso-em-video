r1 = float(input('Digite o valor da primeira reta: '))
r2 = float(input('Digite o valor da segunda reta: '))
r3 = float(input('Digite o valor da terceira reta: '))
maior = ''
menor1 = ''
menor2 = ''
if r1 > r2 and r1 > r3:
    maior = r1
    menor1 = r2
    menor2 = r3
elif r2 > r1 and r2 > r3:
    maior = r2
    menor1 = r1
    menor2 = r3
else:
    maior = r3
    menor1 = r1
    menor2 = r2
soma = (menor1+menor2) >= maior
print('-' * 46)
if soma == True:
    print('É possivel formar um triangulo com as retas!')
else:
    print('Não é possivel formar um triangulo com as retas!')
