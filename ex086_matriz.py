matriz = [[],[],[]]
for a in range(0,3):
    for b in range(0,3):
        matriz[a].append(int(input(f'Digite um numero para ({a},{b}): ')))

#forma q eu fiz
"""print(f""[ {matriz[0][0]} ] [ {matriz[0][1]} ] [ {matriz[0][2]} ]
[ {matriz[1][0]} ] [ {matriz[1][1]} ] [ {matriz[1][2]} ]
[ {matriz[2][0]} ] [ {matriz[2][1]} ] [ {matriz[2][2]} ]"")"""

#printar por codigo
for a in range(0,3):
        for b in range(0,3):
            print(f'[{matriz[a][b]:^5}]',end='')
        print()