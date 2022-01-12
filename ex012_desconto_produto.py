preço = float(input('Digite o preço do produto: '))
desconto = float(input('Digite o valor do desconto em %: '))
comdesconto = -((preço * desconto) / 100) + preço
print('O valor do produto de {} com desconto de {} é de R${} '.format(preço,desconto,comdesconto))