# Catetos e Hipotenusa
from math import hypot

oposto = float(input('Informe o cateto oposto: '))
adj = float(input('Informe o cateto adjacente: '))
hipotenusa = hypot(oposto, adj)
print('A hipotenusa vai medir: {:.2f}'.format(hipotenusa))
