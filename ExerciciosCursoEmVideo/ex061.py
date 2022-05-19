print('----------10 termos de uma P.A--------------\n')

inicio = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
cont = 0

while cont < 10:
    print(f' ->{inicio}', end=' ')
    inicio += razao
    cont += 1
print(f'ACABOU\n Voce mostrou {cont} termos no final')