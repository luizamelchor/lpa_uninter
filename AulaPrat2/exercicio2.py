# Escreva um algoritmo que leia dois valores numéricos e que pergunte ao usuário qual operação ele deseja realizar:
# adição (+), subtração (-), multiplicação (*) ou divisão (/), Exiba na tela o resultado da operação desejada
print('CALCULADORA')
print('+ Adição')
print('- Subtração')
print('* Multiplicação')
print('/ Divisão')
print('Pressione qualquer outra tecla para sair.')

op = input('Qual será a operação? ')
x = int(input('Qual será o primeiro valor? '))
y = int(input('Qual será o segundo valor? '))

if (op == '+'):
    res = x + y
    print(f'O valor da soma de {x} e {y} é: {res}')
elif (op == '-'):
    res = x - y
    print(f'O valor da subtração de {x} e {y} é: {res}')
elif (op == '*'):
    res = x * y
    print(f'O valor da multiplicação de {x} e {y} é: {res}')
elif (op == '/'):
    res = x / y
    print(f'O valor da divisão de {x} e {y} é: {res}')
else:
    print('Encerrando o programa...')






