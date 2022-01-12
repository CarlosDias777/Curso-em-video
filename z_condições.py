nome = str(input('Digite seu nome: ')).strip()
bool_nome = 'carlos' in nome.lower()
print('Bom dia, boa tarde, boa noite {}'.format(nome))
if bool_nome == True:
    print('Seu nome é muito lindo!')
else:
    print('Seu nome é tão normal!')
