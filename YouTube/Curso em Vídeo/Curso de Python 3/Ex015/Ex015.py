# Aluguel de Carros - Calcular o preço a pagar,
# sabendo que o carro custa R$60 por dia e 0.15R$ por KM rodado
dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
total = (dias * 60) + (0.15 * km)
print('O total a pagar é de R${:.2f}'.format(total))
