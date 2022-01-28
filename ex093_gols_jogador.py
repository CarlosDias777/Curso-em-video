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
print('-=-'*20)

for k,v in dicio.items():
    print(f'O campo {k} tem o valor {v}')
print('-=-'*20)

print(f'O jogador {dicio["nome"]} jogou {partidas} partidas')
for a in range(0,partidas):
    print(f'Na {a+1}° partida, fez {dicio["gols"][a]} gols')
print(f'Fez um total de {total_gols} gols')