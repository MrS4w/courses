# Índice de Massa Corporal
peso = float(input('Qual o seu peso? '))
altura = float(input('Qual sua altura? '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa mede: {:.1f}'.format(imc))
if imc < 18.5:
    print('Abaixo do peso')
elif imc <= 25:
    print('Peso ideal')
elif imc <= 30:
    print('Sobrepeso')
elif imc <= 40:
    print('Obesidade')
else:
    print('Obesidade mórbida!')
