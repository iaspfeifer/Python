# Ler comprimento de 3 retas e diga se podem ou não formar um triângulo

r1 = float(input('Digite o primeiro segmento: '))
r2 = float(input('Digite o segundo segmento: '))
r3 = float(input('Digite o terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[32mPodem formar um triângulo')
else:
    print('\033[31mNão podem formar um triângulo')