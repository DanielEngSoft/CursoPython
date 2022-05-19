import random
import time
from termcolor import colored

PC = ('PEDRA', 'PAPEL', 'TESOURA', 'PEDRA','PAPEL')
escolha = str('1')
while escolha != '0':
    escolhaPC = random.randint(1, 3)
    escolha = str(input(colored('Pedra, Papel ou Tesoura?.............digite 0 para sair\n','blue'))).strip().upper()
    if escolha == '0':
        print('SAINDO...')
        time.sleep(1)
        break
    if escolha == PC[escolhaPC]:
        print(colored(f'{escolha} com {PC[escolhaPC]} dá empate','yellow'))
    elif escolha == PC[escolhaPC - 1]:
        print(colored(f'Você Perdeu!!\n{escolha} com {PC[escolhaPC]} {escolha} perde.','red'))
    elif escolha == PC[escolhaPC + 1]:
        print(colored(f'Parabens!!\n{escolha} com {PC[escolhaPC]} {escolha} ganha.','green'))
    else:
        print(f'DIGITE UMA OPÇÃO VÁLIDA')
    time.sleep(1)
