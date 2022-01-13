casa = float(input('Digite o valor da casa: '))
sal = float(input('Digite o seu salario mensal: '))
ano = int(input('Numero de parcela em anos: '))
prest_mes = casa/(ano*12)
cores = {'limpa':'\033[m','vermelho':'\033[1;31m','verde':'\033[1;32m'}
print('-=-='*10)
if sal < prest_mes * 0.3:
    print('{}EMPRESTIMO RECUSADO!!{} O valor da prestação é muito alto para seu salario'
    .format(cores['vermelho'],cores['limpa']))
else:
    print('{}EMPRESTIMO APROVADO!!{}'.format(cores['verde'],cores['limpa']))
print('O valor da prestação mensal será de {:.2f} R$'.format(prest_mes))