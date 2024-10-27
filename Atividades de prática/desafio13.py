# Jogo de adivinha com o computador

import random
from time import sleep

num = random.randint(0, 5)
print('Pensei em um número entre 0 e 5, tente adivinhar!')

chute = int(input('Digite o seu chute: '))

print('Processando...')
sleep(2) # Usado para ter um "delay" entre um print e outro

if chute == num:
    print('Parabéns, você adivinhou!')
else:
    print('Errouuuuuuu, eu pensei no número {}'.format(num))
