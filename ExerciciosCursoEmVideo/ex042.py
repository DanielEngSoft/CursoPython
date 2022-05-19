
texto = 'lado do triangulo: '
texto2 = 'Não forma um triângulo!'
texto3 = 'Forma um triângulo '
l1 = float(input(f'Primeiro {texto}'))
l2 = float(input(f'Segundo {texto}'))
l3 = float(input(f'Terceiro {texto}'))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    if l1 == l2 == l3:
        print(f'{texto3} EQUILÁTERO!')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print(f'{texto3}ISÓCELES!')
    else:
        print(f'{texto3}SCALENO!')
else:
    print(texto2)
