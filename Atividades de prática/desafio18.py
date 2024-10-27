# Cálculo de aumento de salário

salario = float(input('Digite o seu salário atual: '))

if salario<=1250:
    aumento = salario * (15/100)
    novo = salario + aumento
    print('Seu aumento foi de {:.2f} e seu novo salário é {}'.format(aumento, novo))
else:
    aumento = salario * (10/100)
    novo = salario + aumento
    print('Seu aumento foi de {:.2f} e seu novo salário é {}'.format(aumento, novo))
