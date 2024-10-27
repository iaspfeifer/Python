# Sortear nome em lista
import random

nome1 = input('Digite um nome: ')
nome2 = input('Digite outro nome: ')
nome3 = input('Digite outro nome: ')
nome4 = input('Digite outro nome: ')

lista = [nome1, nome2, nome3, nome4]
escolha = random.choice(lista)
print(escolha)

# Sortear ordem na lista

random.shuffle(lista)
print(lista)
