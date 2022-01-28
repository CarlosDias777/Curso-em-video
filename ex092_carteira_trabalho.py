from datetime import date
lista = {}
lista['nome'] = str(input('Seu nome: '))
ano_nasc = int(input('Ano do seu nascimento: '))
lista['idade'] = date.today().year - ano_nasc
carteira = int(input('Sua carteira de trabalho, caso não tenho digite 0: '))
if carteira != 0:
    lista['ctps'] = carteira
    lista['contratação'] = int(input('Digite o ano que foi contratado: '))
    lista['salario'] = float(input('Digite seu salario: '))
    aposenta = 35 -(date.today().year-lista["contratação"])
    print('-=-'*20)
    if aposenta > 0:
        print(f'Sua aposentadoria sai daqui {aposenta} anos!')
    else:
        print(f'Voce ja está aposentado!')
print('-=-'*20)
for k,v in lista.items():
    print(f'{k} tem o valor de {v}')
