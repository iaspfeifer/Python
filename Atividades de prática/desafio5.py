# Cálculo de área de uma parede e quantidade de tinta necessária

larg = float(input('Digite a largura: '))
alt = float(input('Digite a altura: '))
area = larg * alt

print('Sua área é de {}m^2'.format(area))

tinta = area / 2

print('Para pintá-la, é necessário comprar {} litros de tinta'.format(tinta))

# Preço total da tinta e com desconto de 5%

preco_litro = 10.49
preco_tinta = tinta * preco_litro
desconto = preco_tinta * 0.05
tinta_desconto = preco_tinta - desconto

print('O valor total da tinta é {}, mas, com desconto de 5%, fica {}'.format(preco_tinta, tinta_desconto))

# Conversão em dólar

dolar = preco_tinta / 5.45

print('Você irá pagar {:.2f} dólares comprando a tinta de {} reais'.format(dolar, preco_tinta))
