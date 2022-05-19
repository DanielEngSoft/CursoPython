from random import randint
pc = randint(0, 10)
palpites = 0
acertou = False
print('Em que número pensei? ')
while not acertou:
    escolha = int(input('Foi o '))
    if escolha != pc:
        print('NÃO!!')
        if escolha < pc:
            print('É mais')
        else:
            print('É menos -')
    else:
        acertou = True
    palpites += 1
print('SIM!!!')
print(f'Você acertou na {palpites} tentativa!')