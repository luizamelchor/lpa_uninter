# EXPRESSÕES BOOLEANAS
# if (2 + 2 < 4) -> False
# if (7 // 3 == 1 + 1) -> True
# if (3 ** 2 + 4 ** 2 == 25) -> True
# if (2 + 4 + 6 > 12) -> False, é igual
# if (1387 % 19 == 0) -> True
# if (31 % 2 == 0 ) -> False, se é par
# if (min(34, 29, 31) < 30) -> True, se o menor valor é menor que 30
#
# CONDICIONAIS SIMPLES
# idade = 62
# if (idade > 60):
#   print('Você tem direito aos benefícios')
#
# dano = 12
# escudo = 0
# if (dano > 10 and escudo == 0):
#   print('Você está morto!')
#
# norte = True
# sul = False
# leste = False
# oeste = False
# if(norte == True or sul == True or leste == True or oeste == True):
#   print('Você escapou!')
#
# ano = 2025
# if (ano % 4 == 0):
#   print('Pode ser um ano bissexto')
# else:
#   print('Definitivamente não é um ano bissexto')
#
cima = True
baixo = False
if(cima == True and baixo == True):
    print('Decida-se!')
else:
    print('Você escolheu um caminho')
