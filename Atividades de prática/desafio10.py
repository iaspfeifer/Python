# Programa que leia nome completo e mostre: nome com todas as letras maiúsculas e minúsculas, quantas letras ao todo, quantas letras tem o primeiro nome

nome_completo = str(input('Digite seu nome completo: ')).strip()

print(nome_completo.upper())
print(nome_completo.lower())

print(len(nome_completo) - nome_completo.count(' '))

print(nome_completo.find(' '))

# O nome possui o sobrenome Silva?

print('SILVA' in nome_completo.upper())

# Contar quantas vezes a letra A aparece, em qual posição aparece primeiro e em qual aparece por ultimo

print('A letra A aparece {} vezes em seu nome'.format(nome_completo.count('a')))

print('A letra A aparece pela primeira vez na posição {}'.format(nome_completo.find('a')+1))

print('A letra A aparece pela última vez na posição {}'.format(nome_completo.rfind('a')+1))

# Mostrar o primeiro e o último nome separadamente

nome = nome_completo.split()

print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))

