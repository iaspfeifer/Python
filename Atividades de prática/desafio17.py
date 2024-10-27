# Ler 3 números e mostrar qual é o maior e o menor

val1 = int(input('Primeiro valor: '))
val2 = int(input('Segundo valor: '))
val3 = int(input('Terceiro valor: '))

# Menor
menor = val1
if val2<val1 and val2<val3:
    menor = val2
if val3<val1 and val3<val2:
    menor = val3

# Maior
maior = val3
if val1>val3 and val1>val2:
    maior = val1
if val2>val3 and val2>val1:
    maior = val2

print('O menor número é {} e o maior é {}'.format(menor, maior))
