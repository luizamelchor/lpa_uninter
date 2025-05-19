# Enunciado: Imagina-se que você é um dos programadores responsáveis pela construção de um app de vendas
# para uma determinada empresa X que vende em atacado. Uma das estratégias de vendas dessa empresa X é dar
# desconto maior conforme o valor da compra, conforme a listagem abaixo:
# Se valor for menor que 2500 o desconto será de 0%;
# Se valor for igual ou maior que 2500 e menor que 6000 o desconto será de 4%;
# Se valor for igual ou maior que 6000 e menor que 10000 o desconto será de 7%;
# Se valor for igual ou maior que 10000 o desconto será de 11%;
# ATÉ A AULA 3
print('Bem vindo(a) a Loja da Luíza Melchor Bisson da Costa ')
preco = int(input('Digite aqui o valor do produto: '))
qtd = int(input('Digite aqui a quantidade do produto: '))
total = qtd * preco

if (total >= 2500) and (total < 6000):
    desconto = total * 0.04 #desconto de 4%
elif (total >= 6000) and (total < 10000):
    desconto = total * 0.07 #desconto de 7%
elif (total >= 10000):
    desconto = total * 0.11 #desconto de 11%
else: #menor que 2500 reais
    desconto = 0
print(f'O valor total sem desconto é de: R${total}')
print(f'O valor total com desconto é de: R${total - desconto}')
print(f'Você obteve um desconto de: R${desconto}')