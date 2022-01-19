contagem = n = s = 0

while True:
    if contagem == 0:
        n = int(input('Digite um valor (999 para interromper o programa): '))
    else:
        n = int(input('Digite outro numero (999 para interromper o programa): '))
    if n == 999:
        break
    contagem += 1
    s += n
print(f'A quantidade de numeros digitados foi {contagem}, a soma entre eles resulta em {s}')