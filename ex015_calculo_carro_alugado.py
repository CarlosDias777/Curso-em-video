dia = int(input('Quantos dias ficou com o carro alugado? '))
km = float(input('Quantos Km rodou com o carro? '))
vdia = dia * 60
vkm = km * 0.15 
print('O valor a ser pago por dia pelo carro alugado é de {} \nE por Kms rodados é de {} ao total são R${} a pagar'
.format(vdia,vkm,vdia+vkm))