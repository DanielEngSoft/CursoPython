def leiaInt(msgm):
    num = str(input(msgm))
    if num.isnumeric():
        num = int(num)
    else:
        num = leiaInt('ERRO, DIGITE UM NÚMERO INTEIRO!!\nDigite um número: ')
    return num


n = leiaInt('Didite um número: ')
print(f'Voce digitou o número {n}')

