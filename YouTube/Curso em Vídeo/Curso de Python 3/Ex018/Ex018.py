# Seno, Cosseno e Tangente
import math

ang = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(ang))
cosseno = math.cos(math.radians(ang))
tangente = math.tan(math.radians(ang))
print('O ângulo de {} tem o SENO de: {:.2f}'.format(ang, seno))
print('O ângulo de {} tem o COSSENO de: {:.2f}'.format(ang, cosseno))
print('O ângulo de {} tem a TANGENTE de: {:.2f}'.format(ang, tangente))
