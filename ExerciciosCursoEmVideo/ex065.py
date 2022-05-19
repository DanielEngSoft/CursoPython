continuar = 'S'
cont = media = soma = 0
while continuar != 'N':
    num = int(input('Digite um número: '))
    if cont == 0:
        maior = menor = num
    continuar = str(input('Quer continuar? [S/N]')).strip().upper()
    cont += 1
    soma += num
    if num > maior:
        maior = num
    if num < menor:
        menor = num

media = soma / cont
print(f'Você digitou {cont} números e a média foi {media:.2f}\n'
      f'o maior valor foi {maior} e o menor foi {menor}')
