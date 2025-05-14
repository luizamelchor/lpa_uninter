# Enunciado: Você e sua equipe de programadores foram contratados para
# desenvolver um app de vendas para uma loja que vende Açaí e Cupuaçu.
# Você ficou com a parte de desenvolver a interface
# do cliente para retirada do produto.
# A Loja possui seguinte relação:
# Tamanho P de Cupuaçu (CP) custa 9 reais e o Açaí (AC) custa 11 reais;
# Tamanho M de Cupuaçu (CP) custa 14 reais e o Açaí (AC) custa 16 reais;
# Tamanho G de Cupuaçu (CP) custa 18 reais e o Açaí (AC) custa 20 reais;
# ATÉ A AULA 4
print('Bem vindo(a) a Sorveteria da Luíza Melchor Bisson da Costa')
print('Nosso cardápio:\n--------------------------------------------')
print('|  TAMANHO  |   AÇAÍ (AC)  |  CUPUAÇU (CP) |')
print('|',' ' * 3,'P',' ' * 3,'|',' ' * 3,'R$11',' ' * 3,'|',' ' * 3,'R$9',' ' * 5,'|')
print('|',' ' * 3,'M',' ' * 3,'|',' ' * 3,'R$16',' ' * 3,'|',' ' * 3,'R$14',' ' * 4,'|')
print('|',' ' * 3,'G',' ' * 3,'|',' ' * 3,'R$20',' ' * 3,'|',' ' * 3,'R$18',' ' * 4,'|')
print('--------------------------------------------')
total = 0 #acumulador
while True:
    sabor = input('Qual o sabor (AC ou CP)? ')
    if sabor == 'AC' or sabor == 'CP':
        pass #se válido, continue
    else:
        print('Sabor inválido. Tente novamente')
        continue #se inválido, o laço recomeça

    tam = input('Qual o tamanho (P, M ou G)? ')
    if tam == 'P' or tam == 'M' or tam == 'G':
        if tam == 'P':
            if sabor == 'AC':
                preco = 11
                total += preco
            elif sabor == 'CP':
                preco = 9
                total += preco
        if tam == 'M':
            if sabor == 'AC':
                preco = 16
                total += preco
            elif sabor == 'CP':
                preco = 14
                total += preco
        if tam == 'G':
            if sabor == 'AC':
                preco = 20
                total += preco
            elif sabor == 'CP':
                preco = 18
                total += preco
        print(f'Você pediu um {sabor} tamanho {tam}: R${preco}')
    else:
        print('Tamanho inválido. Tente novamente')
        continue #se inválido, o laço recomeça para escolha de sabor

    continuar = input('Deseja pedir mais alguma coisa (S/N)? ')
    if continuar == 'S':
        pass
        continue #se válido, o laço recomeça para escolha de sabor
    else: #qualquer tecla além de "S"
        print('Sua compra foi finalizada!')
        print(f'O total da sua compra foi: R${total}')
        break


