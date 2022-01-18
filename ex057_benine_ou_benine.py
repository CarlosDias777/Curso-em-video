sexo = ''

# while sexo not in 'mf':
while sexo != 'm' and sexo != 'f':
    sexo = str(input('Qual o seu sexo?[M/F] ')).lower().strip()
    if sexo != 'm' and sexo != 'f':
        print('Sexo invalido')
    else:
        if sexo == 'm':
            print('Sexo Masculino, registrado com sucesso!')
        else:
            print('Sexo Feminino, resgistrado com sucesso!')
    