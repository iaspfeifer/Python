# Desafio do curso de python do curso em vídeo

# Continha de bhaskara

a = int(input('Digite o valor de a: '))
b = int(input('Digite o valor de b: '))
c = int(input('Digite o valor de c: '))

delta = b ** 2 - 4 * a * c

print('O valor de delta é {}'.format(delta))

if delta < 0:
    print('A equação não possui raízes reais')
    
elif delta == 0:
    print('A equação possui uma raíz real')

else:
    print('A equação possui duas raízes reais')

x1 = (- b + delta ** 0.5) / (2 * a)

print('O valor de x 1 é {}'.format(x1))

x2 = (-b - delta ** 0.5) / (2 * a)

print('O valor de x 2 é {}'.format(x2))

