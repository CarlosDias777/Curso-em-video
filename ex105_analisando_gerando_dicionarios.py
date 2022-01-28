dicio = {}
def notas(*n,sit=False):
    dicio['total de notas'] = qnotas = len(n)
    
    snotas = 0
    for a in n:
        snotas += a
    dicio['media notas'] = mnotas = snotas/qnotas

    #max(n) min(n) é a forma mais facil de ser feita mas n a mais bonita
    for k,v in enumerate(n):
        if k == 0:
            maior = v
            menor = v
        else:
            if v > maior:
                maior = v
            elif v < menor:
                menor = v
    dicio['maior nota'] = maior
    dicio['menor nota'] = menor

    if sit == True:
        if mnotas < 5:
            dicio['situação'] = 'Ruim'
        elif mnotas > 5 and mnotas < 7:
            dicio['situação'] = 'Razoavel'
        else:
            dicio['situação'] = 'Boa'
 
notas(5,7,9,sit=True)
print(dicio)