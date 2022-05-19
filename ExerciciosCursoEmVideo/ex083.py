parent_aberto = 0
expressão = str(input('Digite a expressão: ')).strip()
for c in expressão:
    if c == '(':
        parent_aberto += 1
    elif c == ')':
        parent_aberto -= 1
    if parent_aberto < 0:
        break
print('Expressão válida!' if parent_aberto == 0 else 'Expressão inválida!')
