soma = cont = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'Números digitados:{cont:->8}\n'
      f'Soma entre eles:{soma:->10}')
