nome = str(input('Digite seu nome completo: ')).strip() #strip serve para remover os espaços antes e depois do nome
M = nome.upper() #transfora toda a string em maiúscula
m = nome.lower() #transfora toda a string em minúscula
separa = nome.split() #split separa em listas uma cadeia de caracteres separada por espaços
print(f'Seu nome em maiúsculas é: {M}')
print(f'Seu nome em minúsculas é: {m}')
print(f'Seu nome tem ao todo {len(nome)-nome.count(" ")} letras') #count conta quantas vezes aparece o caractere escolhido
print(f'Seu primeiro nome é {separa[0]} e ele tem  letras {len(separa[0])}')