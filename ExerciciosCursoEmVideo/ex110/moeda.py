def aumentar(preco=0, v=0, f=True):
    preco = preco + (preco * (v / 100))
    if f:
        return moeda(preco)
    else:
        return preco


def diminuir(preco=0, v=0, f=True):
    preco = preco - (preco * (v / 100))
    if f:
        return moeda(preco)
    else:
        return preco


def dobro(preco=0, f=True):
    preco *= 2
    if f:
        return moeda(preco)
    else:
        return preco


def metade(preco=0, f=True):
    preco /= 2
    if f:
        return moeda(preco)
    else:
        return preco


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')


def resumo(preco, v1, v2):
    print('-'*35)
    print(f"{'RESUMO':^35}")
    print('-'*35)
    print(f'{"Preço analisado":.<20}{preco:.>15}')
    print(f'{"DOBRO":.<20}{dobro(preco):.>15} ')
    print(f'{"METADE":.<20}{metade(preco):.>15} ')
    print(f'{f"AUMENTANDO {v1}%":.<20}{aumentar(preco, 10):.>15} ')
    print(f'{f"REDUZINDO {v2}%":.<20}{diminuir(preco, 13):.>15} ')
    print('-'*35)
