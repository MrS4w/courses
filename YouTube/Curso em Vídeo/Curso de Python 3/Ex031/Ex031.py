# Custo da Viagem
dist = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}Km'.format(dist))
if dist <= 200:
    preco = dist * 0.50
else:
    preco = dist * 0.45
print('O preço da passagem será R${:.2f}'.format(preco))
