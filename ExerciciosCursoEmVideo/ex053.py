frase = str(input('Digite uma frase: ')).strip().upper().replace(' ', '')
reverso = ''
for c in range(len(frase)-1, -1, -1):
    reverso += frase[c]
junto = (''.join(reverso))
print(f'{frase} \nAo contrário fica \n{junto}')
if frase == junto:
    print('\033[32mTemos um palindromo!')
else:
    print('\033[31mNão temos um palindromo')

