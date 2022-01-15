"""num = float(input('Digite um valor para progessão aritmetica: '))
razao = float(input('Digite a razão da progressão aritmetica: '))
s = 0
print('A progressão de {} por {} resulta em:'.format(num, razao))
for a in range(1,11):
    s += num * razao
    print(s)"""

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao
for a in range(primeiro,decimo + razao,razao):
    print(a, end=' → ')
print('Acabou')
