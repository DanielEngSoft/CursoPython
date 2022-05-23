while True:
    opc = str(input('\033[0;30;41mBiblioteca ou função: '))
    if opc == 'fim':
        break
    help(opc)

