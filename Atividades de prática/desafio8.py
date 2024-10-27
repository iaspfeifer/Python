import math

# Cálculo da hipotenusa

cat1 = float(input('Digite o cateto oposto: '))
cat2 = float(input('Digite o cateto adjacente: '))

hip = math.hypot(cat1, cat2)

print(hip)

# Cálculo de seno, cosseno e tangente 

ang = float(input('Digite o ângulo: '))

sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))

print('O seno, cosseno e tangente de {} é, respectivamente, {}, {} e {}'.format(ang, sen, cos, tan))