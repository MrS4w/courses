# Conversor de Bases Numéricas
num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para converão: 
[1] converter para binário
[2] converter para octal
[3] converter para hexadecimal''')
op = int(input('Sua opção: '))
if op == 1:
   print('{} convertido para binário é igual a {}'.format(num,bin(num) [2:]))
elif op==2:
    print('{} convertido para octal é igual a {}'.format(num, oct(num)[2:]))
elif op==3:
    print('{} convertido para hexadecimal é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida')