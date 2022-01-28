def ficha(jog ,gols):
    if jog == '':
        jog = '<Desconhecido>'
    if gols.isnumeric() :
        gols = int(gols)
    else:
        gols = 0
    return f'O jogador {jog}, fez um total de {gols} gols no campeonato'


jo = str(input('Qual o nome do jogador? ')).strip()
gol = str(input('Quantos gols ele fez? ')).strip()
print(ficha(jo,gol))