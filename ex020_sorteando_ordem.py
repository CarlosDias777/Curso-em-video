from random import shuffle
print('Ordem de apresentação dos alunos!')
print('=' * 50)
aluno1 = input('Digite o nome do aluno: ')
aluno2 = input('Digite o nome do aluno: ')
aluno3 = input('Digite o nome do aluno: ')
aluno4 = input('Digite o nome do aluno: ')
aluno5 = input('Digite o nome do aluno: ')
r = [aluno1,aluno2,aluno3,aluno4,aluno5]
shuffle(r)
print('A ordem dos alunos sorteados foi',r)
