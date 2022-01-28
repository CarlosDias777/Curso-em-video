aluno = {}
aluno['Nome'] = str(input('Nome do aluno: '))
aluno['Media'] = float(input('Media do aluno: '))
for a,b in aluno.items():
    print(f'{a} é igual a {b}')
if aluno['Media'] > 6:
    print(f'O aluno {aluno["Nome"]} está aprovado')
else:
    print(f'O aluno {aluno["Nome"]} está reprovado')