num = int(input('Digite um numero inteiro: '))
print('')
print('☭' * 40)
print('')
print("""1 = Binario ৷ Digite 1 para converter para binario! 
2 = Octal ৷ Digite 2 para converter para octal!
3 = Hexadecimal ৷ Digite 3 para converter para hexadecimal!""")
cores = {'limpa':'\033[m', 'vermelho':'\033[1;31m', 'verde':'\033[1;32m'}
print('')
print('☭' * 40)
print('')
escolha = int(input('Para qual base quer converter? '))
print('')
print('☭' * 40)
print('')
bina = bin(num)
octo = oct(num)
hexa = hex(num)
if escolha > 3 or escolha < 1:
    print('{}Escolha invalida!!!{}'.format(cores['vermelho'],cores['limpa'])) 
elif escolha == 1:
    print('Este numero na base binaria é: {}{}{}'.format(cores['verde'],bina[2:],cores['limpa']))
elif escolha == 2:
    print('Este numero na base octal é: {}{}{}'.format(cores['verde'],octo[2:],cores['limpa']))
else:
    print('Este numero na base hexadecimal é: {}{}{}'.format(cores['verde'],hexa[2:],cores['limpa']))
