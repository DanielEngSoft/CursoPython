def db(op):
    num = int(input('Decimal -> '))
    x = []
    while num != 0:
        x.insert(0, num % 2)  # x.insert(0,) inclui na posiçao 0 da lista x o valor indicado após a virgula
        num = num // 2  # num recebe a divisão inteira de num por 2
    result = ''  # result é o caractere que vai substituir as virgulas da lista, somente por estética

    print('Binário ->', result.join(map(str, x)))  # map(,) transforma todos os elementos da lista no tipo escolhido
def bd(op):
    num = input('Binário ->')
    print('Decimal ->', int(num, 2))
def dh(op):
    hexa = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']
    r = []
    num = int(input('Decimal ->'))
    while num != 0:
        r.insert(0, hexa[num % 16])
        num = num // 16
    a = ''
    print('Hexadecimal ->', a.join(map(str, r)))
def hd(op):
    num = input('Hexadecimal -> ')
    print('Decimal ->', int(num, 16))
def bh(op):
    numb = input('Binário -> ')
    numd = int(numb, 2)
    numh = format(numd, 'x')
    print('Hexadecimal ->', numh)
def hb(op):
    num = input('Hexadecimal ->')
    numd = int(num, 16)
    numb = format(numd, 'b')
    print('Binário ->', numb)
def menu(op):
    print('''#    01* Decimal -> Binário                  04* Hexadecimal -> Decimal      # 
#    02* Binário -> Decimal                  05* Binário -> Hexadecimal      #
#    03* Decimal -> Hexadecimal              06* Hexadecimal -> Binário      #''')
saida = 2
op = 0

while saida == 2:
    menu(op)
    op = int(input('Digite a operação que deseja fazer: '))
    if op == 1:
        db(op)
    elif op == 2:
        bd(op)
    elif op == 3:
        dh(op)
    elif op == 4:
        hd(op)
    elif op == 5:
        bh(op)
    elif op == 6:
        hb(op)
    saida = int(input('Sair? 1 = SIM     2 = NÃO\n'))