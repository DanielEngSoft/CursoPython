tupla = (
    'Lápis', 1.50,
    'Caneta', 2.00,
    'Borracha', 2.00,
    'Caderno', 15.00,
    'Estojo', 19.90,
    'Apontador', 3.50,
    'Mochila', 150.00,
)
for c in range(0, len(tupla)-1, 2):
    print(f'{tupla[c]:.<25}R${tupla[c+1]:>6.2f}')
