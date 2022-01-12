from math import hypot
cat1 = float(input('Digite o valor do cateto oposto: '))
cat2 = float(input('Digite o valor do cateto adjacente: '))
resultado = hypot(cat1,cat2)
print('O cateto oposto que mede {} ao quadrado mais o cateto adjacente que mede {} ao quadrado \nResulta no valor da hipotenusa de {}'
.format(cat1,cat2,resultado))