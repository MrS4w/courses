# Classificando Atletas
from datetime import date

atual = date.today().year
nascimento = int(input('Digite a data de nascimento: '))
idade = atual - nascimento
print('O atleta tem {} anos de idade'.format(idade))
if idade <= 9:
    print('Classificação: Mirim')
elif idade > 9 and idade <= 14:
    print('Classificação: Infantil')
elif idade <= 19:
    print('Classificação: Junior')
elif idade <= 25:
    print('Classificação: Senior')
else:
    print('Classificação: Master')
