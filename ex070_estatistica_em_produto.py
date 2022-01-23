total = maisdemil= maisbarato = 0
prod_nome = ''
while True:
    nome = str(input('Digite o nome do produto: ')).strip()
    preço = float(input('Digite o preço do produto: '))
    
    total += preço

    if preço > 1000:
        maisdemil += 1

    if maisbarato == 0:
        maisbarato = preço
        prod_nome = nome
    elif preço < maisbarato:
        maisbarato = preço
        prod_nome = nome

    continuar = str(input('Quer continuar?[S/N] ')).strip().lower()
    while continuar not in 'sn':
        continuar = str(input('Quer continuar?[S/N] ')).strip().lower()

    if continuar == 's':
        print('=!='*25)
    elif continuar == 'n':
        break
print(f"""O total gasto com produtos foi {total:.2f} R$.
{maisdemil} produtos custam mais que mil reais.
O nome do produto mais barato é {prod_nome}""")