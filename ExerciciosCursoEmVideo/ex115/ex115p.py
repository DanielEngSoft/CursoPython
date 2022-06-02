from time import sleep
from lib.interface import *
from lib.arquivo import *

while True:
    try:
        arq = "dados.txt"
        if not arquivoExiste(arq):
            criarArquivo(arq)

        opc = menu(["Pessoas Cadastradas", "Cadastrar Pessoas", "Sair do programa"])
        if opc == 1:
            lerArquivo(arq)
            sleep(1)
        elif opc == 2:
            alterarArquivo(arq)
            sleep(1)
        elif opc == 3:
            print('Saindo do sistema...Até logo')
            sleep(1)
            break
        else:
            print('\033[31mOpção inválida!!\033[m')
            sleep(1)
    except ValueError:
        print('ERRO, DIGITE UMA OPÇÃO VÁLIDA')
