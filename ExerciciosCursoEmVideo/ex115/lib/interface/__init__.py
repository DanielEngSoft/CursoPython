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


def linha(tam=40):
    return "-" * tam


def cabeçalio(txt):
    print('\033[0;30;44m', txt.center(40), '\033[m')


def menu(itens):
    cabeçalio("Menu Principal")
    for i, c in enumerate(itens):
        print(f'{i+1}- {c}')
    print(linha())
    return leiaInt('Sua opção: ')
