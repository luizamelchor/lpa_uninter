# Enunciado: Você foi contratado para desenvolver um sistema de cobrança de serviços
# de uma copiadora. Você ficou com a parte de desenvolver a interface com o funcionário.
# A copiadora opera da seguinte maneira:
# Serviço de Digitalização (DIG) o custo por página é de um real e dez centavos;
# Serviço de Impressão Colorida (ICO) o custo por página é de um real;
# Serviço de Impressão Preto e Branco (IPB) o custo por página é de quarenta centavos;
# Serviço de Fotocópia (FOT) o custo por página é de vinte centavos;
#
# Se número de páginas for menor que 20 retornar o número de página sem desconto;
# Se número de páginas for igual ou maior que 20 e menor que 200 retornar o número de páginas com o desconto é de 15%;
# Se número de páginas for igual ou maior que 200 e menor que 2000 retornar o número de páginas com o desconto é de 20%;
# Se número de páginas for igual ou maior que 2000 e menor que 20000 retornar o número de páginas com o desconto é de 25%;
# Se número de páginas for maior ou igual à 20000 não é aceito pedidos nessa quantidade de páginas;
#
# Para o adicional de encadernação simples (1) é cobrado um valor extra de 15 reais;
# Para o adicional de encadernação de capa dura (2) é cobrado um valor extra de 40 reais;
# Para o adicional de não querer mais nada (0) é cobrado um valor extra de 0 reais;
#
# O valor final da conta é calculado da seguinte maneira:
# total = (servico * num_pagina) + extra
# ATÉ AULA 5
def escolha_servico(e_servico):
    preco = 0
    servico = input(e_servico)
    while servico not in ['DIG', 'ICO', 'IPB', 'FOT']:
        print('Serviço inválido. Tente novamente.')
        servico = input(e_servico)
    if servico == 'DIG':
        preco += 1.1
    elif servico == 'ICO':
        preco += 1
    elif servico == 'IPB':
        preco += 0.4
    else:
        preco += 0.2
    return preco

def num_pagina(pergunta_pagina, min, max):
    paginas = 0
    while True:
        try:
            paginas = int(input(pergunta_pagina))
            if ((paginas < min) or (paginas >= max)): #invalidar caso esteja fora de 0 a 20000
                print('Não aceitamos esta quantidade de páginas.\nTente novamente usando um valor menor.')
            else:
                if (paginas < 20):
                    paginas = paginas
                elif (paginas >= 20) and (paginas < 200):
                    paginas = paginas * 0.85  # desconto de 15%
                elif (paginas >= 200) and (paginas < 2000):
                    paginas = paginas * 0.8  # desconto de 20%
                else:
                    paginas = paginas * 0.75  # desconto de 25%
                break
        except ValueError: #caso a resposta em forma string
            print('Você digitou usando letras. Tente novamente.')
    return paginas

def servico_extra(s_extra, min, max):
    # lista de serviços
    print('1 - Encadernação simples - R$15')
    print('2 - Encadernação de capa dura - R$40')
    print('0 - Sem serviço adicional')
    extra = 0
    while True:
        try:
            e = int(input(s_extra))
            if (e < 0) or (e > 2):
                print('O serviço escolhido é inválido. Tente novamente.')
            else:
                if e == 1:
                    print('Encadernação simples. Custo: R$15')
                    extra += 15
                elif e == 2:
                    print('Encadernação de capa dura. Custo: R$40')
                    extra += 40
                else:
                    print('Nenhum serviço adicional. Custo: R$0')
                    extra += 0
                break
        except ValueError: #caso a resposta em forma string
            print('Serviço extra inválido. Tente novamente.')
    return extra

# Programa Principal

print('Bem vindo(a) a Copiadora da Luíza Melchor Bisson da Costa')
print('Escolha um dos nossos serviços:')
print('DIG - Serviço de Digitalização')
print('ICO - Serviço de Impressão Colorida')
print('IPB - Serviço de Impressão Preto e Branco')
print('FOT - Serviço de Fotocópia')

servico = escolha_servico('Qual o serviço escolhido? ')
paginas = num_pagina('Qual o número de páginas? ',0,20000)
extra = servico_extra('Você gostaria dos nossos serviços adicionais? ', 0, 2)
total = (servico * paginas) + extra
print(f'Total: R${total} (serviço: {servico} * páginas: {paginas}) + extra: {extra}')


