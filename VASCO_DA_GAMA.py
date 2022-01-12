import Play_mp3
print('Aumente o som!!')
time = input('Digite o time que torce: ')
analise = time.lower().find('vasco')
if analise == 0:
    Play_mp3.play('y_Vasco_da_gama.mp3')
else:
    print('Seu time não tem Graça!')
