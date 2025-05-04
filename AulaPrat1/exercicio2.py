# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo
# usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o
# preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado
#
# CÓDIGO DO PROFESSOR ----------
# km = int(input('Quantos Km foram percorridos? '))
# dias = int(input('Quantos dias foram percorridos? '))
# preco = 60 * dias + 0.15 * km
# print(f'Km = {km}. Dias: {dias}.')
# print(f'Valor a ser pago: {preco}')
#
# MEU CÓDIGO ----------
km = int(input('Quantos quilômetros o carro percorreu? '))
dias = int(input('Por quantos dias o carro foi alugado? '))
cal = (km * 0.15) + (dias * 60)
print(f'Você alugou o carro por {dias} dias e percorreu {km} quilômetros.')
print(f'Você terá que pagar um valor de {cal} reais pelos dias e km.')