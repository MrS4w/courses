# Gerenciador de Pagamentos
print('{:=^40}'.format(' PYTHON STORE '))
preco = float(input('Preço das compras: R$ '))
print('''FORMAS DE PAGAMENTO
[ 1 ] À vista no dinheiro/cheque
[ 2 ] À vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    # É descontado 10% por ser á vista
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    # É descontado 10% por ser á vista no cartão
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R$ {:.2f} SEM JUROS.'.format(parcela))
elif opcao == 4:
    # Juros de 20% por dividir mais de duas vezes
    total = preco + (preco * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R$ {:.2f} COM JUROS.'.format(totparc, parcela))
else:
    total = preco
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')
print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final.'.format(preco, total))
