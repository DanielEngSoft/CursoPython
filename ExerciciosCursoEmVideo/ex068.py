from random import randint
cont = 0
while True:
    player = int(input('Digite um número: '))
    comp = randint(1, 10)
    resultado = player + comp
    ParOuImpar = 'P' if resultado % 2 == 0 else 'I'
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {player} e o computador {comp}, ', end='')
    print(f'Deu Par' if ParOuImpar == 'P' else 'Deu Ímpar')
    print(f'{"Você VENCEU":.^43}' if escolha == ParOuImpar else f'{"Você perdeu":.^43}\nGAME OVER, você venceu {cont}x')
    cont += 1
    if ParOuImpar != escolha:
        break
    print('Vamos jogar de novo')
