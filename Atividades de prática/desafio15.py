# Preço da viagem
dist = float(input('Qual a distância da sua viagem (em km)? '))

if dist <= 200:
    print('Sua passagem custa R$ {}'.format(dist * 0.50))
else:
    print('Sua passagem custa R$ {}'.format(dist * 0.45))
