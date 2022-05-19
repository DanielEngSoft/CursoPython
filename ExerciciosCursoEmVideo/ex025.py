id = 'SILVA'
nome = str(input('Digite seu nome:')).strip().upper()
x = nome.strip()
print(f'Seu nome tem Silva? {id in x[0::]}')