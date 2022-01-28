lista = []
while True:
    dicio = {}
    dicio['nome'] = str(input('Digite o nome do jogador: '))
    
    lista_gol = []

    partidas = int(input(f'Quantas partidas {dicio["nome"]} jogou? '))

    total_gols = 0

    for a in range(1,partidas+1):
        g = int(input(f'Quantos gols na {a} partida: '))
        lista_gol.append(g)
        total_gols += g

    dicio['gols'] = lista_gol.copy()
    dicio['totalgols'] = total_gols

    lista.append(dicio.copy())
    dicio.clear()

    continuar = str(input('Quer continuar?[S/N) ')).lower()
    while continuar not in 'sn':
        continuar = str(input('Quer continuar?[S/N) ')).lower()
    if continuar == 'n':
        break

print('-=-'*20)
cont = 0
print(f'{"cod"}{"nome":^10}{"gols":^10}{"total":^10}')
for a in lista:
    print(f"""{f'{cont}':^3}{f'{a["nome"]}':^10}{f'{a["gols"]}':^10}{f'{a["totalgols"]}':^10}""")
    cont += 1
dados = 0
while dados != 999:
    print('Digite 999 para interromper!')
    dados = int(input('Digite o codigo do jogador que quer analisar: '))
    print()
    if dados > len(lista)-1:
        print('Jogador invalido')
    else:
        print(f'---LEVANTAMENTO do jogador {lista[dados]["nome"]}')
        for i,g in enumerate(lista[dados]['gols']):
            print(f'Na partida {i+1} {lista[dados]["nome"]} fez {g} gols')
            print('-=-'*20)
    