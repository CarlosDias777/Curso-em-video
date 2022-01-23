from time import sleep
alunos = []
juntar = []
nomes = []
notas = []
cont = 0

while True:
    #le o nome e adiciona a lista
    nomes.append(str(input('Digite o nome do aluno: ')))
    juntar.append(nomes[:])
    
    #le a nota e adiciona a lista
    notas.append(float(input('Digite a 1° nota do aluno: ')))
    notas.append(float(input('Digite a 2° nota do aluno: ')))
    juntar.append(notas[:])
    
    #adiciona o nome e a nota em uma lista
    alunos.append(juntar[:])
    
    #limpa as listas para o proximo aluno
    juntar.clear()
    nomes.clear()
    notas.clear()
    
    #pergunta se quer continuar
    continuar = str(input('Quer continuar?[s/n] ')).lower()
    while continuar not in 'sn':
        continuar = str(input('Quer continuar?[s/n] ')).lower()
    if continuar == 'n':
        break
print('\033[1;35m-=-\033[m'*20)    

#printa as listas na tela
for nom,nott in alunos:
    print(f'Numero do aluno: {cont}')
    print(f'Nome do aluno: {nom}')
    print(f'Media do aluno: {(nott[0]+nott[1])/2:}')
    print('\033[1;35m-=-\033[m'*20)      
    cont += 1
    sleep(1)

#Ver as notas individualmente
while True:
    print('Digitar 999 interrompe!')
    mostrarnotas = int(input('Mostrar nota de qual aluno pelo numero? '))
    if mostrarnotas == 999:
        break
    else:
        print(f'A notas do aluno {alunos[mostrarnotas][0]} foram de {alunos[mostrarnotas][1]}')
    print('\033[1;35m-=-\033[m'*20)    
print('=-=-= FIM =-=-=')