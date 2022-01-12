n1 = float(input('Digite um numero: '))
n2 = float(input('Digite outro numero: '))
soma = n1 + n2
divisao = n1 / n2
divisao_inteira = n1 // n2
resto_divisao = n1 % n2
multiplicação = n1 * n2
potencia = n1 ** n2
raiz = n1 ** (1/n2)
print('A soma de {} e {} resulta na valor {} \nA divisão de {} por {} resulta no valor {} \n'.format(n1,n2,soma,n1,n2,divisao))
print('A divisão inteita de {} por {} resulta em {} \nO resto da divisão de {} por {} resulta em {}'.format(n1,n2,divisao_inteira,n1,n2,resto_divisao))
print('A multiplicação de {} por {} resulta em {} \nA potencia de {} por {} resulta em {} \n'
'A raiz de {} por {} resulta em {}'.format(n1,n2,multiplicação,n1,n2,potencia,n1,n2,raiz))