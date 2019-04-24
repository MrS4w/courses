# Procurando uma string dentro de outra
nome = str(input('Qual é o seu nome completo? '))
nome2 = nome.upper()
ter = nome2.count('SILVA')
if ter > 0:
    print('Seu nome tem Silva? Sim')
else:
    print('Seu nome tem Silva? Não')
