# Aquele clássico da Média
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
if media >= 7:
    print('Com a média {:.1f} você está aprovado!'.format(media))
elif media < 5:
    print('Com a média {:.1f} você está reprovado!'.format(media))
else:
    print('Com a média {:.1f} você está em recuperação!'.format(media))
