import Play_mp3
time = input('Digite o time que torce: ')
analise = time.lower().find('vasco')
if analise == 0:
    Play_mp3.play('Vasco_da_gama.mp3')
else:
    print('Seu time não tem Graça')
