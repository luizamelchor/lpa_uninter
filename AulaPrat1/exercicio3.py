# Crie uma variável de string que receba uma frase qualquer. Cria uma segunda variável, agora
# contendo a metade da string digitada. Imprima na tela somente os dois últimos
# caracteres da segunda variável do tipo string
#
# MEU CÓDIGO (ajuda do prof) ----------
frase = input('Digite uma frase qualquer aqui: ')
tan = len(frase)
frase2 = frase[:int(tan/2)]
print(frase2[-2:]) # assim usará os dois últimos caracteres quando não se sabe quais serão

