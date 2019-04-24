# Par ou Ímpar?
num = int(input('Me diga um número: '))
result = num % 2
if result == 0:
    print('O número {} é: PAR'.format(num))
else:
    print('O número {} é: ÍMPAR'.format(num))
