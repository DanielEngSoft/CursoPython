nome = str(input('Digite seu nome completo:')).strip()
separa = nome.split()
print('Prazer em te conhecer!')
print(f'Seu primeiro nome é {separa[0].capitalize()}\n'
      f'Seu ultimo nome é {separa[len(separa) - 1].capitalize()}')
