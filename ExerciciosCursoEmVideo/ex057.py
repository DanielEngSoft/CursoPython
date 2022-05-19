sexo = ('M','F')
escolha = str(input('Informe seu sexo [M/F]: '))
while escolha not in sexo:
    escolha = input("Dados inválidos, digite M ou F: ").strip().upper()
print(f'Sexo {escolha} registrado com sucesso!')
