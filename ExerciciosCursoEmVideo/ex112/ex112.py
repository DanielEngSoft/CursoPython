from utilidadesCeV import moeda, dado

while True:
    try:
        p = dado.leiaDinheiro('Digite o preço: R$')
        moeda.resumo(p, 6, 23)
    except ValueError:
        print('Informe um valor válido! ')
    else:
        break
