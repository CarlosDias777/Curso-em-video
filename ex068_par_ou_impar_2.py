from random import randint
cor = ['\033[m','\033[1;31m','\033[1;32m','\033[1;35m']
print(f'{cor[3]}Vamos jogar par ou impar, quero ver vc ganhar!!!{cor[0]}')
contagem = 0
print('=!='*20)
while True:
    computador = randint(0,10)
    jogador = int(input('Digite sua escolha: '))
    #while parouimpar not in 'PpIi: para obrigador o usuario a digitar um str valido'
    parouimpar = str(input('Par ou impar?[P/I] ')).strip().upper()
    print('=!='*20)
    if 'P' in parouimpar:
        if (jogador + computador) % 2 == 0:
            contagem += 1
            print(f'{cor[3]}Voce jogou {jogador} e o computador jogou {computador}{cor[0]}')
            print(f'{cor[2]}Voce GANHOU de mim (ㆆ_ㆆ) , Vamos novamente!{cor[0]}') 
            print('=!='*20)
        else:
            print(f'{cor[3]}Voce jogou {jogador} e o computador jogou {computador}{cor[0]}')
            print(f'{cor[1]}Voce PERDEU{cor[0]} ( •_•)>⌐■-■ (⌐■_■)')
            break
    elif 'I' in parouimpar:
        if (jogador + computador) % 2 == 0:
            print(f'{cor[3]}Voce jogou {jogador} e o computador jogou {computador}{cor[0]}')
            print(f'{cor[1]}Voce PERDEU{cor[0]} ( •_•)>⌐■-■ (⌐■_■)')
            break
        else:
            contagem += 1
            print(f'{cor[3]}Voce jogou {jogador} e o computador jogou {computador}{cor[0]}')
            print(f'{cor[2]}Voce GANHOU de mim (ㆆ_ㆆ) , Vamos novamente!{cor[0]}')
            print('=!='*20)
    else:
        print(f'{cor[1]}Opção invalida (•`_´•){cor[0]}')
print(f'A quantidade de vitorias consecutivas que vc teve foi de {contagem}')