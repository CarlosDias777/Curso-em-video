from random import randint
from Play_mp3 import play
print("""Estou pensando em um numero, Duvido voce acertar!!
Dica: Estou pensando em um numero entre 1 e 5""")
chute = int(input('Valor que acha que estou pensando: '))
numero = randint(1,5)
if numero == chute:
    print('Acertou, voce me venceu ;-;')
else:
    print('Voce errou, tente novamente!')   
    play('y_Errou - Faustao Falando (320 kbps).mp3')
