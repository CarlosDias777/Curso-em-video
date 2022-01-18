from random import randint
num = randint(1,10)
escolha = 0
tentativas = 1
print('Estou pensando em um numero entre 1 e 10, DUVIDO vc acertar!!')
while num != escolha:
    escolha = int(input('Sua escolha: '))
    if num != escolha:
        tentativas += 1
    if num > escolha:
        print('Mais... tente novamente!')
    elif num < escolha:
        print('Menos... tente novamente!')
print('Parabens voce acertou o numero que estava pensando e levou {} tentativas ate descobrir'.format(tentativas))
