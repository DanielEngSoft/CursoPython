num = int(input('Digite um número inteiro: '))
opção = int(input('1- Binario\n'
      '2- Octal\n'
      '3- Hexadecimal\n'))
if opção == 1:
      print(f'{num} convertido para BINÁRIO é: {format(num, "b")}')
elif opção == 2:
      print(f'{num} convertido para OCTAL é: {format(num, "o")}')
elif opção == 3:
      print(f'{num} convertido para HEXADECIMAL é: {format(num, "x")}')
else:
      print('Opção inválida')