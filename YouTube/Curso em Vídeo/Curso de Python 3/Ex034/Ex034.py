# Aumentos múltiplos
sal = float(input('Qua lé o salário do funcionário? R$'))
if sal <= 1250:
    novo = sal + (sal * 15 / 100)
else:
    novo = sal + (sal * 10 / 100)
print('Quem ganhava {:.2f} passa a ganhar R${:.2f} agora'.format(sal, novo))
