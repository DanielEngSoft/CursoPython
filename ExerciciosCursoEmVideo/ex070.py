totalgasto = 0
maisde1000 = 0
maisBaratoNome = ' '
while True:
    sair = ' '
    produto = str(input(f'Nome do produto: ')).strip().capitalize()
    preço = float(input('Preço: R$'))
    totalgasto += preço
    if maisBaratoNome == ' ':
        maisBaratoNome = produto
        maisBaratoPreço = preço
    if preço > 1000:
        maisde1000 += 1
    if maisBaratoPreço > preço:
        maisBaratoPreço = preço
        maisBaratoNome = produto
    while sair not in ('SN'):
        sair = str(input('Deseja continuar? [S/N]')).strip().upper()
    if sair == 'N':
        break
print(f'Total gasto: {totalgasto:.>37}\n'
      f'Produtos mais de R$1000,00: {maisde1000:.>22}\n'
      f'Produto mais barato: {maisBaratoNome}, custa R${maisBaratoPreço}')
