# Escreva uma função que calcule o fatorial de um número recebido como parâmetro e retorne o seu resultado
# Faça uma validação dos dados por meio de uma outra função, permitindo que somente valores positivos sejam aceitos
# Crie o help da sua função
def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while((x < min) or (x > max)):
        x = int(input(pergunta))
    return x

def fatorial (num):
    """
    Função que calcula o fatorial de um número inteiro
    Args:
        num: número inteiro a ser calculado

    Returns:
        retorna num
    """
    fat = 1
    if num == 0:
        return fat # pois fatorial de 0 é 1, como no início da função
    # esta parte só executa caso num > 0
    for i in range(1, num + 1, 1):
        fat *= i
    return fat

x = valida_int('Digite um valor para calcular o fatorial: ', 0, 999999)
print(f'{x}! = {fatorial(x)}')