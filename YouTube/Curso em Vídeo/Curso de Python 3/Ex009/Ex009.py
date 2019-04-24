# Tabuada
num = int(input('Digite um número para verificar a tabuada: '))
for cont in range(0, 11):
    print('{} X {} = {}'.format(num, cont, (num * cont)))

