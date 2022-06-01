def leiaInt(msgm):
    while True:
        try:
            num = int(input(msgm))
        except (ValueError, TypeError):
            print('\033[31mERRO, DIGITE UM NÚMERO INTEIRO!!\033[m')
        except KeyboardInterrupt:
            print('\n\033[31mUsuário não quiz informar o valor\033[m')
            return 0
        else:
            return num


def leiaFloat(msgm):
    while True:
        try:
            num = float(input(msgm).replace(',', '.'))
        except ValueError:
            print('\033[31mERRO, DIGITE UM NÚMERO REAL!!\033[m')
        except KeyboardInterrupt:
            print('\n\033[31mUsuário não quiz informar o valor\033[m')
            num = 0
            break
        else:
            break
    return num


i = leiaInt('Didite um número Inteiro: ')
f = leiaFloat('Didite um número Real: ')
print(f'Voce digitou o número {i} e {f}')
