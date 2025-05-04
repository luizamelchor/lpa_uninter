# Desenvolva um algoritmo que solicite ao usuário o preço de um produto e um percentual de desconto
# a ser aplicado a ele. Calcule-o e exiba o valor do desconto e o preço final do produto.
#
# CÓDIGO DO PROFESSOR ----------
# preco = float(input('Digite o preço do produto: '))
# percentual = float(input('Digite o percentual de desconto (0-100%)'))
# desconto = preco * (percentual / 100)
# final = preco - desconto
# print(f'O preço do produto é {preco}. Desconto de {percentual}%')
# print(f'Valor calculado de desconto: {desconto}. Valor final do produto: {final}')
#
# MEU CÓDIGO ----------
preco = float(input('Qual é o preço do produto? '))
percentual = float(input('Qual é percentual do desconto? (0 a 100%) '))
desconto = preco * (percentual / 100)
final = preco - desconto
# para fazer isso em uma linha desconto = preco * (1 - percentual / 100)
print(f'O desconto recebido foi de {desconto} reais sobre o produto.')
print(f'Resultando em um preço final de: {final}.')