# Alistamento militar
from datetime import date

atual = date.today().year
nasc = int(input('Em qual ano você nasceu? '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
if idade == 18:
    print('Você completou 18 anos, é hora de se alistar')
elif idade < 18:
    saldo = 18 - idade
    print('Você ainda nao tem idade para o alistamento militar e faltam {} anos para você se alistar'.format(saldo))
elif idade > 18:
    saldo = idade - 18
    print('Você ja deveria ter se alistado a {} anos'.format(saldo))
