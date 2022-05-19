import time

def formaDePagamento():
    print('***** FORMAS DE PAGAMENTO *****\n'
          '[1] à vista DINHEIRO / CHEQUE\n'
          '[2] à vista CARTÃO\n'
          '[3] 2x CARTÃO\n'
          '[4] 3x ou mais no CARTÃO')
    forma = int(input('Qual a forma de pagamento?\n'))
    if forma == 1:
        print(f'O valor final da compra À VISTA ficou R${preco - preco * 0.10:.2f}')
    elif forma == 2:
        print(f'O valor final da compra 1X NO CARTÃO ficou R${preco - preco * 0.05:.2f}')
    elif forma == 3:
        print(f'Sua compra de R${preco:.2f} será parcelada em 2x de R${preco / 2:.2f} sem juros')
    elif forma == 4:
        parcela = int(input('Quantas parcelas? '))
        if parcela >= 3:
            precoC = preco * 1.2
            print(f'Sua compra será parcelada em {parcela}x de R${precoC / parcela:.2f} COM JUROS')
            print(f'Sua comra de {preco:.2f} custará {precoC:.2f} no final.')
        else:
            print('Parcelas inválidas!!!')
            time.sleep(1.5)
            print('Escolha outra forma de pagamento!')
            time.sleep(1.5)
            formaDePagamento()
    else:
        print('Opção inválida!!!')
        time.sleep(1.5)
        formaDePagamento()


print('====_=- LOJA Daniel -=_====')
preco = float(input('QUAL O VALOR DA COMPRA? R$'))
formaDePagamento()
