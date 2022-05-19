print('----------10 termos de uma P.A--------------\n')

inicio = int(input('Primeiro termo: '))
soma = inicio
razao = int(input('Razão: '))
for c in range(inicio, inicio + 10):
    print(soma, end=' -> ')
    soma = soma + razao
print('ACABOU')