# Calculando Descontos
preco = float(input('Qual o preço do produto? R$'))
desconto = (preco * 5) / 100
print('O produto que custava {} na promoção de 5% de desconto irá custar: {:.2f}'.format(preco, (preco - desconto)))