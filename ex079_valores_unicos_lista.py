print('-=-'*25)
lista = []
while True:
    valor = int(input('Digite um valor: '))
    if valor in lista:
        print('Valor repetido, Não foi adicionado a lista')
    else:
        lista.append(valor)
    print('-=-'*25)
    continuar = str(input('Quer continuar?[S/N]')).lower()
    while continuar not in 'sn':
        continuar = str(input('Quer continuar?[S/N]')).lower()
    if continuar == 'n':
        break
print('-=-'*25)
print(f'Voce digitou os valores {sorted(lista)}')