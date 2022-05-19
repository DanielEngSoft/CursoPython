from termcolor import colored

print('\nDigite dois números: ')
n1 = int(input('1º: '))
n2 = int(input('2º: '))
menu = 0
sair = False
while not sair:
    print('[1] SOMAR',
          '\n[2] MULTIPLICAR',
          '\n[3] MAIOR',
          '\n[4] NOVOS NÚMEROS',
          '\n[5] SAIR DO PROGRAMA')
    menu = int(input('----> Digite uma opção: '))
    if menu == 1:
        print(colored(f'{n1} + {n2} = {n1 + n2}', 'yellow'))
    elif menu == 2:
        print(colored(f'{n1} x {n2} = {n1 * n2}', 'yellow'))
    elif menu == 3:
        print(colored(f'O maior número é o {max(n1, n2)}', 'yellow'))
    elif menu == 4:
        n1 = int(input('1º: '))
        n2 = int(input('2º: '))
    elif menu == 5:
        sair = True
    else:
        print('OPÇÃO INVALIDA, TENTE NOVAMENTE!!')
