lista = []
cont = 0
while True:
    lista.append(int(input('Digite um valor: ')))
    cont += 1
    continuar = str(input('Quer continuar?[S/N] ')).lower()
    while continuar not in 'sn':
        continuar = str(input('Quer continuar?[S/N] ')).lower()
    if continuar == 'n':
        break
print('-=-'*20)
print(f"""Foram digitados {cont} numeros!
A lista ordenada de forma decrecente: {sorted(lista, reverse=True)}""")
if 5 in lista:
    print('O numero 5 esta presente na lista')
else:
    print('O numero 5 não esta presente na lista') 