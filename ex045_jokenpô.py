from random import randint
print("""Vamos jogar JOKENPÔ
1 = pedra
2 = papel
3 = tesoura""")
cores = {'limpa':'\033[m', 'vermelho':'\033[1;31m', 'verde':'\033[1;32m', 'roxo':'\033[1;35m'}
jogador = int(input('Qual a sua escolha? '))
maquina = randint(1,3)
if jogador < 1 and jogador > 3:
    print('{}Jogada infalida!!!{}'.format(cores['vermelho'],cores['limpa']))
elif jogador == 1 and maquina == 1:
    print('Voce jogou: {}PEDRA{} e a maquina jogou: {}PEDRA{}!'.format(cores['verde'],cores['limpa'],cores['verde'],cores['limpa']))
    print('Foi um {}EMPATE!!!{}'.format(cores['roxo'],cores['limpa']))
elif jogador == 1 and maquina == 2:
    print('Voce jogou: {}PEDRA{} e a maquina jogou: {}PAPEL{}!'.format(cores['vermelho'],cores['limpa'],cores['verde'],cores['limpa']))
    print('Voce {}PERDEU!!!{}'.format(cores['vermelho'],cores['limpa']))
elif jogador == 1 and maquina == 3:
    print('Voce jogou: {}PEDRA{} e a maquina jogou: {}TESOURA{}!'.format(cores['verde'],cores['limpa'],cores['vermelho'],cores['limpa']))
    print('Voce {}GANHOU!!!{}'.format(cores['verde'],cores['limpa']))
elif jogador == 2 and maquina == 2:
    print('Voce jogou: {}PAPEL{} e a maquina jogou: {}PAPEL{}!'.format(cores['verde'],cores['limpa'],cores['verde'],cores['limpa']))
    print('Foi um {}EMPATE!!!{}'.format(cores['roxo'],cores['limpa']))
elif jogador == 2 and maquina == 3:
    print('Voce jogou: {}PAPEL{} e a maquina jogou: {}TESOURA{}!'.format(cores['vermelho'],cores['limpa'],cores['verde'],cores['limpa']))
    print('Voce {}PERDEU!!!{}'.format(cores['vermelho'],cores['limpa']))
elif jogador == 2 and maquina == 1:
    print('Voce jogou: {}PAPEL{} e a maquina jogou: {}PEDRA{}!'.format(cores['verde'],cores['limpa'],cores['vermelho'],cores['limpa']))
    print('Voce {}GANHOU!!!{}'.format(cores['verde'],cores['limpa']))
elif jogador == 3 and maquina == 3:
    print('Voce jogou: {}TESOURA{} e a maquina jogou: {}TESOURA{}!'.format(cores['verde'],cores['limpa'],cores['verde'],cores['limpa']))
    print('Foi um {}EMPATE!!!{}'.format(cores['roxo'],cores['limpa']))
elif jogador == 3 and maquina == 1:
    print('Voce jogou: {}TESOURA{} e a maquina jogou: {}PEDRA{}!'.format(cores['vermelho'],cores['limpa'],cores['verde'],cores['limpa']))
    print('Voce {}PERDEU!!!{}'.format(cores['vermelho'],cores['limpa']))
else:
    print('Voce jogou: {}TESOURA{} e a maquina jogou: {}PAPEL{}!'.format(cores['verde'],cores['limpa'],cores['vermelho'],cores['limpa']))
    print('Voce {}GANHOU!!!{}'.format(cores['verde'],cores['limpa']))