preço = float(input('Qual o valor do produto? '))
print("""Formas de pagamentos
----------------------------------------
1 = A vista no dinheiro, 10% de desconto
2 = A vista no cartão, 5% de desconto
3 = 2 vezes no cartão, sem desconto 
4 = 3 vezes ou mais no cartão, 20% de juros simples
----------------------------------------""")
escolha = int(input('Qual será a forma de pagamento? '))
if escolha < 1 or escolha > 4:
    print('Forma de pagamento invalida!!')
elif escolha == 1:
    print('O valor de {} R$ do produto, com desconto de 10% é de {} R$'.format(preço, preço - preço*0.1))
elif escolha == 2:
    print('O valor de {} R$ do produto, com desconto de 5% é de {} R$'.format(preço, preço - preço * 0.05))
elif escolha == 3:
    print('O valor do produto é de {} R$'.format(preço))
else:
    print('O valor de {} R$ do produto, com juros simples de 20% é de {} R$'.format(preço,preço + preço * 0.2))