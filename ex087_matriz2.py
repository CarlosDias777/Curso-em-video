matriz = [[],[],[]]
pares = maior = 0
for a in range(0,3):
    for b in range(0,3):
        n = int(input(f'Digite um valor na posição ({a},{b}): '))
        matriz[a].append(n)
        if n % 2 == 0:
            pares += n

        if a == 1:
            if b == 0:
                maior = n
            else:
                if n > maior:
                    maior = n

print('-='*30)
print(f"""[ {matriz[0][0]} ] [ {matriz[0][1]} ] [ {matriz[0][2]} ]
[ {matriz[1][0]} ] [ {matriz[1][1]} ] [ {matriz[1][2]} ]
[ {matriz[2][0]} ] [ {matriz[2][1]} ] [ {matriz[2][2]} ]""")
print(f'A soma dos valores pares é de {pares}')
print(f'A soma dos valores da terceira coluna resulta em {matriz[0][2]+matriz[1][2]+matriz[2][2]}')
print(f'O maior valor da segunda linha é {maior}')