# Crie um programa para ler o nome, ano de nascimento e sexo de diferentes pessoas
# Armazene os dados em um dicionário com listas
# Ao encerrar o cadastro, apresente:
# O total de cadastros efetuados;
# A média das idades das pessoas;
# Uma lista de mulheres com menos de 30 anos;
# Uma lista de homens com idade acima da média.
cadastro = {'nome':[], 'sexo': [], 'ano': []}

while True:
    terminar = input('Deseja cadastrar uma pessoa? [S/N]')
    if terminar.upper() in 'N':
        break
    if terminar.upper() not in 'S':
        print('Digite S par SIM ou N para NÃO.')
        continue
    nome = input('Qual o nome?')
    sexo = input('Qual o sexo?')
    ano = input('Qual o ano de nascimento? ') # sem necessidade de converter nesse exercício
    cadastro['nome'].append(nome)
    cadastro['sexo'].append(sexo.upper())
    cadastro['ano'].append(ano)

# FINALIZAR ESTE EXERCÍCIO
