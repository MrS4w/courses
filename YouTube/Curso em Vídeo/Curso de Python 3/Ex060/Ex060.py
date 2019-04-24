# Cálculo do Fatorial
n = int(input('Digite um número para calcular seu fatorial: '))
c = n
f = 1
print('Calculando {}! '.format(n))
while c > 0:
    print('{}'.format(c), end='')
    if c > 1:
        print(' x ', end="")
    else:
        print(' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
