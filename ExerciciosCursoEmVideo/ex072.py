lista = ('zero', 'um', 'dois', 'trêz', 'quatro', 'cinco',
         'seis', 'sete', 'oito', 'nove', 'dez',
         'onze', 'doze', 'treze', 'catoze', 'quinze',
         'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um número de 0 a 20: '))
    if 0 <= num <= 20:
        print(f'Você digitou o número {lista[num]}')
        sair = ' '
        while sair not in 'NS':
            sair = str(input('Deseja sair? ')).strip().upper()[0]
            if sair not in 'NS':
                print('Opção inválida! ')
    else:
        print('Número inválido')
    if sair == 'S':
        break