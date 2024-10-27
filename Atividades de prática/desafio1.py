# Desafio do curso de python do curso em vídeo

# Descrição: Respondendo ao usuário. Inserir nome e retornar uma mensagem de boas-vindas.

nome = input('Digite seu nome: ')
genero = input('Com qual pronome você se identifica? (ela, ele ou elu): ')
if genero == 'ela':
    print('Seja bem-vinda, {}!'.format(nome))
elif genero == 'ele':
    print('Seja bem-vindo, {}!'.format(nome))
else:
    print('Seja bem-vinde, {}!'.format(nome))