def aumentar(preco=0, v=0, f=True):
    preco = preco + (preco * (v / 100))
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
