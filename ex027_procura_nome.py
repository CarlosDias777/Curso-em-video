nome = str(input('Digite seu nome completo: ')).strip()
split_nome = nome.split()
comp_nome = len(split_nome) - 1
print('Seu primeiro nome é {} seu ultimo nome é {}'.format(split_nome[0],split_nome[comp_nome]))