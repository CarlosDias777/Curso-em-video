altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))
area = altura * largura
tinta = area / 2
print('A altura da parede é de {} a largura é de {}\n'
'Sua area em m² é de {}, considerando que cada litro de tinta pinta 2m²\n'
'É necessario {} litros de tinta para pintar a parede'.format(altura,largura,area,tinta))