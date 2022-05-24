def ajuda(op, c):
    print(cor[c], end='')
    help(op)
    print(cor['p'], end='')


def titulo(op, c='p'):
    print(cor[c], end='')
    print('='*128)
    print(f'{op:^127}'.upper())
    print('='*128)
    print(cor['p'], end='')


# Programa principal
cor = {
    'p': '\033[m',
    'vermelho': '\033[0;30;41m',
    'verde': '\033[0;30;42m',
    'amarelo': '\033[0;30;43m',
    'azul': '\033[0;30;44m',
    'roxo': '\033[0;30;45m',
    'branco': '\033[7;48m'
}
while True:
    titulo('SISTEMA DE AJUDA DO DANIEL', 'azul')
    opc = str(input('DIGITE UMA BIBLIOTECA OU FUNÇÃO: '))
    if opc.upper().strip() == 'FIM':
        break
    else:
        titulo(opc, 'verde')
        ajuda(opc, 'amarelo')
titulo('Até logo!!', 'branco')
