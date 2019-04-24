# Aprovando impréstimo
casa = float(input('Valor da casa R$: '))
sal = float(input('Salário do comprador R$: '))
anos = int(input('Em quantos anos deseja pagar? '))
prest = casa / (anos * 12)
min = sal * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end='')
print(' a prestação será de R${:.2f}'.format(prest))
if prest <= min:
    print('Empréstimo pode ser concedido!')
else:
    print('Empréstimo não pode ser concedido!')
