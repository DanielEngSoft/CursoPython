def fat(num, show=False):
    """
    :param num: Número a ser realizao o fatorial
    :param show: (Opcional) Caso verdadeiro mostra as somas do fatorial
    :return: Retorna o resultado final do fatorial
    """
    fat = 1
    for c in range(num, 0, -1):
        fat *= c
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
    return fat


n = int(input('Deseja ver o fatorial de qual número? '))
print(fat(n, True))
# print(fat.__doc__)
