completo = [[],[]]
for a in range(0,7):
    n = (int(input(f'Digite o {a} valor: ')))
    if n % 2 == 0:
        completo[0].append(n)
    else:
        completo[1].append(n)
print(f'A lista de pares: {sorted(completo[0])}') 
print(f'A lista de impares: {sorted(completo[1])}')  