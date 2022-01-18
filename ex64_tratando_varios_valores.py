print('Caso digite 999 o programa ira finalizar!')
acumulador = contador = n = 0
while n != 999:
    n = int(input('Digite qualquer numero entre 0 e 998: '))
    if n != 999:
        acumulador += n
        contador += 1
    else:
        print('Fim do programa!')
print('Foram {} numeros digitados e a soma entre eles resulta em {}'.format(contador,acumulador))