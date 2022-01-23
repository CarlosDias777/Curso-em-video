lista = []
maior = menor = 0
for a in range(0,5):
    lista.append(int(input(f'Digite um valor na posição {a}: ')))
    
    if a == 0:
        maior = menor = lista[0]
    
    else:
        if lista[a] > lista[a-1]:
                maior = lista[a]
        elif lista[a] < lista[a-1]:
                menor = lista[a]

print('-=-'*20)
contmaior = []
contmenor = []

#outra forma de contar em q posição da lista esta
"""for i,v in enumerate(lista):
        if v == maior
        print(f'{i}')"""

for b in range(0,5):
    if lista[b] == maior:
        contmaior += b,
    if lista[b] == menor:
        contmenor += b,

print(f"""Voce digitou os valores {lista}
O maior valor digitado foi {maior} nas posições {contmaior}
O menor valor digitado foi {menor} nas posições {contmenor}""")
print('-=-'*20)