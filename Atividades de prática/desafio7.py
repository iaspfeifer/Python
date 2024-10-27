# Aluguel de carro

valor_dia = 60
valor_km = 0.15

dias = float(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos km foram rodados? '))

preco_final = (dias * valor_dia) + (km * valor_km)

print('O valor total a se pagar é R${}'.format(preco_final))
