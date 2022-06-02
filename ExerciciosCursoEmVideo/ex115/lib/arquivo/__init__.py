from ExerciciosCursoEmVideo.ex115.lib.interface import *


def arquivoExiste(nome):
    try:
        arquivo = open(nome, 'rt')
        arquivo.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        arquivo = open(nome, "wt+")
        arquivo.close()
    except:
        print('Erro ao criar arquivo')
    else:
        print('Arquivo criado com sucesso!!')


def lerArquivo(nome):
    try:
        arquivo = open(nome, 'rt')
    except FileNotFoundError:
        print("ERRO ao abrir arquivo")
    else:
        cabeçalio("Pessoas Cadastradas")
        print(arquivo.read())
    finally:
        arquivo.close()


def alterarArquivo(nome):
    try:
        novoCadastro = open(nome, 'at')
    except FileNotFoundError:
        print("ERRO ao ler arquivo")
    else:
        cabeçalio("Cadastrar Pessoa")
        novoCadastro = open(nome, 'at')
        nome = str(input('Digite o nome: ')).strip().capitalize()
        idade = leiaInt('Digite a idade: ')
        try:
            novoCadastro.write(f'{nome:.<35}{idade:.>5}\n')
        except:
            print('Erro ao cadastrar dado!')
        else:
            print(f'{nome} cadastrado com sucesso!')
    finally:
        novoCadastro.close()


