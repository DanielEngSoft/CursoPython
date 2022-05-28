def aumentar(preco, v):
    preco = preco + (preco * (v / 100))
    return preco


def diminuir(x, v):
    x = x - (x * (v/100))
    return x


def dobro(x):
    x *= 2
    return x


def metade(x):
    x /= 2
    return x
