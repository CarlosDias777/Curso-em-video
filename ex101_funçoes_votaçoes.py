def voto(ano):
    global anop
    from datetime import date
    a = date.today().year
    anop = a - ano
    if anop < 16:
        return 'Voce ainda não pode votar'
    elif anop >= 16 and anop < 18:
        return 'Seu voto é opcional'
    elif anop >= 18 and anop < 65:
        return 'Seu voto é obrigatorio' 
    else:
        return 'Seu voto é opcional'

resp = voto(int(input('Digite o seu ano de nascimento: ')))
print(f'Voce tem {anop} anos e {resp}')