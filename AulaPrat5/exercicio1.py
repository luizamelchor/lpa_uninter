# Escreva um algoritmo que crie uma tupla com 10 palavras. Encontre dentro dessa tupla as vogais de cada palavra.
# Faça um print na tela com o nome da palavra e suas respectivas vogais.
palavras = ('Mario', 'Luigi', 'Peach', 'Yoshi', 'Bowser')

for palavra in palavras: # palavra da tupla palavras
    print(f'\nPalavra: {palavra.upper()}. Vogais: ')
    for letra in palavra: # letra da palavra
        if letra.lower() in 'aeiou':
            print(letra.upper(), end=' ')
