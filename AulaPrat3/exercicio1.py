# Escreva um algoritmo que mostra, na tela quatro produtos a serem comprados em uma lanchonete:
# Coxinha - R$ 5,00
# Pastel - R$ 7,00
# Café - R$ 4,00
# Suco - R$ 6,00
# Faça um algoritmo em que você seleciona o produto que quer comprar e a quantidade.
# Faça isso até que decida encerrar o programa
# Ao final, mostre o valor final do pedido a ser pago
print('LANCHONETE DA LUÍZA')
print('Temos esses itens no nosso cardápio com seus respectivos preços:')
print('1 - Coxinha R$ 5,00')
print('2 - Pastel R$ 7,00')
print('3 - Café R$ 4,00')
print('4 - Suco R$ 6,00')
print('5 - SAIR')
total = 0
while True:
    pedido = int(input('Digite o número do seu pedido: '))
    if (pedido == 1):
        qtd = int(input('Digite a quantidade desejada: '))
        total = total + qtd * 5
    elif (pedido == 2):
        qtd = int(input('Digite a quantidade desejada: '))
        total = total + qtd * 7
    elif (pedido == 3):
        qtd = int(input('Digite a quantidade desejada: '))
        total = total + qtd * 4
    elif (pedido == 4):
        qtd = int(input('Digite a quantidade desejada: '))
        total = total + qtd * 6
    elif (pedido == 5):
        qtd = int(input('Digite a quantidade desejada: '))
        print('Saindo...')
        break
    else:
        print('O item selecionado não existe.')
print(f'O total a ser gasto neste pedido é de R$ {total}.')
