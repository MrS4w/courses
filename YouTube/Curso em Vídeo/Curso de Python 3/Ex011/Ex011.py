# Calcular quantidade de tinta para pintar uma parede sabendo que 1l de tinta = 2m
largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
area = largura * altura
print('Sua parede tem dimensão de {}x{} e sua área é de {}m².'.format(largura, altura, area))
tinta = area / 2
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(tinta))