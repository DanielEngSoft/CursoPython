print(f'{"Tabuada":^35}')
while True:
    num = int(input('Digite um número: '))
    if num < 0:
        print(f'{"FIM":.^35}')
        break
    print('-'*35)
    for c in range(1, 11):
        print(f'{num}  x {c:>2} = {num * c:.>27}')
    print('-'*35)