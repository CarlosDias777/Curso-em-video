from math import cos,sin,tan,radians
angulo = float(input('Digite o valor de um angulo: '))
rad = radians(angulo)
print('O angulo de {:.3f}° \nTem o seno de {:.3f} \nO cosseno de {:.3f} \nE a tangente de {:.3f}'
.format(angulo,sin(rad),cos(rad),tan(rad)))
