nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5:
    print('Voce esta REPROVADO, estude mais no proximo ano!!')
elif media > 5 and media < 7:
    print('Voce esta em RECUPERAÇÃO, tera outra chance para ser aprovado então estude')
else:
    print('Voce esta APROVADO, parabens!!!')