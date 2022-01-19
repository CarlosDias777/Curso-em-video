mais18cont = homenscont = muiecont = 0
print('===== Cadastre uma pessoa =====')
print('=!='*20)
while True:
    idade = int(input('Digite a idade da pessoa: '))
    sexo = str(input('Digite o sexo da pessoa:[M/F] ')).strip().lower()

    sexo = str(input('Digite o sexo da pessoa:[M/F] ')).strip().lower()
    if sexo != 'm' and sexo != 'f':
        while sexo != 'm' and sexo != 'f':
            sexo = str(input('Digite o sexo da pessoa:[M/F] ')).strip().lower()
    print('=!='*20)

    if idade > 18:
        mais18cont += 1
    elif sexo == 'm':
        homenscont += 1
    elif sexo == 'f' and idade < 20:
        muiecont += 1

    print('')
    continuar = str(input('Quer continuar?[S/N] ')).strip().lower()
    if continuar != 'n' and continuar != 's':
        continuar = str(input('Quer continuar?[S/N] ')).strip().lower()
    if continuar == 's':
        print()
    elif continuar == 'n':
        break 
    print('=!='*20)
print('Finalizando...')
print(f"""Total de pessoas com mais de 18 anos: {mais18cont}
Ao todo temos {homenscont} homens cadastrados
E temos {muiecont} mulheres com menos de 20 anos""")
