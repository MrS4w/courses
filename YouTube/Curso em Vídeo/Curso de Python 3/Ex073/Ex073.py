# Tuplas com Times de Futebol
times = (
    'Corinthians', 'Palmeiras', 'Santos', 'Grêmio',
    'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
    'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia',
    'São Paulo', 'Fluminense', 'Sport Recife',
    'FC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta',
    'Atlético-GO')

# lista de todos os 20 primeiros colocados
print("-=" * 30)
print("Lista dos times do Brasileirão")
print(times[0:5])
print(times[5:10])
print(times[10:15])
print(times[15:20])
print("-=" * 30)

# os 5 primeiros
print("Os 5 primeiros são")
print(times[0:5])
print("-=" * 30)

# os 4 últimos
print("Os 4 últimos são")
print(times[-4:])
print("-=" * 30)

# em ordem alfabética
print("Times em ordem alfabética")
emOrdem = sorted(times)
print(emOrdem[0:5])
print(emOrdem[5:10])
print(emOrdem[10:15])
print(emOrdem[15:20])
print("-=" * 30)

# o Chapecoense está na lista?
print(f"O Chapecoense está na {times.index('Chapecoense')}ª posição")
