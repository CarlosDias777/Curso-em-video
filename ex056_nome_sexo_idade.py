cont_idade = 0
idade_mais_velho = 0
nome_mais_velho = ''
cont_muie = 0
for a in range(1,5):
    print('{}° Pessoa'.format(a))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    cont_idade += idade
    if sexo.upper() == 'M':
        if a == 1:
            idade_mais_velho = idade
            nome_mais_velho = nome
        elif idade > idade_mais_velho:
            idade_mais_velho = idade
            nome_mais_velho = nome
    elif sexo.upper() == 'F':
        if idade <= 20:
            cont_muie += 1
print('A media de idade de todos é de {}!'.format(cont_idade/4))
print('O nome do homem mais velho é {} e ele tem {} anos!'.format(nome_mais_velho,idade_mais_velho))
print('São {} mulheres que tem menos que 20 anos'.format(cont_muie))

