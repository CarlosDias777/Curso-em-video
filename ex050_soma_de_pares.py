soma = 0
for a in range(1,7):
    valor = int(input('Digite um valor: '))
    if valor % 2 == 0:
         soma += valor
print('A soma dos valores PARES digitados é de {}'.format(soma))
