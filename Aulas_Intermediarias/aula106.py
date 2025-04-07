"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""


def soma(x, y, z):
    # Definição
    print(f'{x=} {y=} {z=}', ' | ', 'x + y + z =', x + y + z, '\n')


soma(1, 2, 3)
soma(1, 2, 5)
soma(2, 3, 6)

print( 1, 2, 3, sep='-')