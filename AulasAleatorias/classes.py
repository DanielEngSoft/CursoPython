class Cliente:
    def __init__(self, nome, cpf, idade, senha):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.senha = senha

    def mudarSenha(self):
        while True:
            senha_antiga = input('Digite a senha atual: ')
            if senha_antiga == self.senha:
                self.senha = input('Digite a nova senha: ')
                break
            else:
                print('Senha atual errada!')


nome = str(input('NOME: ')).capitalize()
cpf = int(input('CPF: '))
idade = int(input('IDADE: '))
senha = str(input('Digite uma senha: '))

cliente = Cliente(nome, cpf, idade, senha)
print('Senha atual', cliente.senha)
menu = int(input(f'1- SAIR\n'
                f'2- MUDAR SENHA\n'))
if menu == 1:
    print('OBGD!!')
elif menu == 2:
    cliente.mudarSenha()
print('Nova senha', cliente.senha)
