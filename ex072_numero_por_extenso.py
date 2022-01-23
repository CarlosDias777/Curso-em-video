numeros = ('Zero','Um','Dois','Tres','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez','Onze','Doze','Treze','Quatorze','Quinze','Dezesseis','Dezessete','Dezoito','Dezenove','Vinte')
while True:
    escolha = int(input('Digite um numero entre 0 e 20: '))
    while escolha not in range(0,21):
        escolha = int(input('Tente novamente, Digite um numero entre 0 e 20: '))  
    print(f'O numero que voce escolheu escrito por extenso é {numeros[escolha]}')
    continuar = str(input('Quer continuar?[S/N] ')).strip().lower()
    while continuar not in 'sn':
        continuar = str(input('Quer continuar?[S/N] ')).strip().lower()
    if continuar == 'n':
        break
        