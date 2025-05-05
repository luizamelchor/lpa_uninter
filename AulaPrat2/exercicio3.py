# Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica. Pergunte
# a quantidade de kWh consumida e o tipo de instalação: R para residências, I para indústrias e C para comércios
# Calcule o preço de acordo com a tabela a seguir:
# ----------------------------------------------------------
#  Preço por tipo e faixa de consumo
# ----------------------------------------------------------
# Tipo         | Faixa (kWh)      | Preço (R$)
# ----------------------------------------------------------
# Residencial  | Até 500          | 0,40
# Residencial  | Acima de 500     | 0,65
# Comercial    | Até 1000         | 0,55
# Comercial    | Acima de 1000    | 0,60
# Industrial   | Até 5000         | 0,55
# Industrial   | Acima de 5000    | 0,60
# ----------------------------------------------------------
# CÓDIGO DO PROFESSOR ----------------
# kwh = float(input('Quantos kWh? '))
# tipo = input('Qual o tipo da instalação? (R, C ou I)' )
# if (tipo == 'R'):
#   if kwh >= 500:
#       preco = 0.65
#   else:
#       preco = 0.4
#   print(f'Total a pagar: {kwh * preco}')
# elif (tipo == 'C'):
#   if kwh >= 1000:
#       preco = 0.60
#   else:
#       preco = 0.55
#   print(f'Total a pagar: {kwh * preco}')
# elif (tipo == 'I'):
#   if kwh >= 5000:
#       preco = 0.6
#   else:
#       preco = 0.55
#   print(f'Total a pagar: {kwh * preco}')
#
# MEU CÓDIGO ----------------
print('CALCULADORA DE ENERGIA ELÉTRICA')
con = int(input('Quantos kWh foram consumidos no último mês? '))
print('Qual é o tipo da sua instalação? ')
print('R - Residencial')
print('C - Comercial')
print('I - Industrial')
tipo = input('Qual dessas acima é a sua? ')
if (con <= 500 and tipo == 'R'):
    preco = con * 0.4
    print(f'O preço a se pagar é de {preco}')
elif (con > 500 and tipo == 'R'):
    preco = con * 0.65
    print(f'O preço a se pagar é de {preco}')
elif (con <= 1000 and tipo == 'C'):
    preco = con * 0.55
    print(f'O preço a se pagar é de {preco}')
elif (con > 1000 and tipo == 'C'):
    preco = con * 0.60
    print(f'O preço a se pagar é de {preco}')
elif (con <= 5000 and tipo == 'I'):
    preco = con * 0.55
    print(f'O preço a se pagar é de {preco}')
elif (con > 5000 and tipo == 'I'):
    preco = con * 0.60
    print(f'O preço a se pagar é de {preco}')
else:
    print('Instalação Inválida. Encerrando...')