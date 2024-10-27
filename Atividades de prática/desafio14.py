# Cálcular possível multa

veloc = float(input('Digite a velocidade do seu carro: '))

if veloc > 80:
    print('Você está acima da velocidade permitida e receberá uma multa!')
    multa = (veloc - 80) * 7
    print('O valor da sua multa é R$ {}'.format(multa))
else:
    print('Você está dentro da velocidade permitida!')

# Mostrar se a velocidade é par ou ímpar

if veloc%2 == 0:
    print('Esta velocidade é par')
else:
    print('Esta velocidade é ímpar')
