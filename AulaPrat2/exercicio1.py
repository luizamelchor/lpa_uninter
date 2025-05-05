# Faça um algoritmo que receba três valores, representando os lados de um triângulo
# fornecidos pelo usuário. Verifique se os valores formam um triângulo e classifique como:
# a) Equilátero (três lados iguais)
# b) Isósceles (dois lados iguais)
# c) Escaleno (três lados diferentes)
# Lembre-se de que, para formar um triângulo, nenhum dos lados pode ser igual a zero,
# e um lado não pode ser maior do que a soma dos outros dois
A = int(input('Digite um valor para o primeiro lado: '))
B = int(input('Digite um valor para o segundo lado: '))
C = int(input('Digite um valor para o terceiro lado: '))

if ((A > 0 and B > 0 and C > 0) and (A + B > C and A + C > B and B + C > A)):
    if (A != B and A != C and B != C):
        print('É um triângulo escaleno')
    else:
        if (A == B and B == C):
            print('É um triângulo equilátero')
        else:
            print('É um triângulo isósceles')
else:
    print('Ao menos um dos valores indicados não servem para formar um triângulo')