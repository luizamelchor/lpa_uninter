# Enunciado: Você e sua equipe de programadores foram contratados por pequena empresa para
# desenvolver o software de gerenciamento de livros. Este software deve ter o seguinte menu e opções:
#
# 1. Cadastrar Livro
# 2. Consultar Livro
#  2.1. Consultar Todos
#  2.2. Consultar por Id
#  2.3. Consultar por Autor
#  2.4. Retornar ao menu
# 3. Remover Livro
# 4. Encerrar Programa
# ATÉ AULA 6

lista_livro = []
id_global = 0
def cadastrar_livro(id):
    global id_global
    id_global += 1 #sempre aumenta o id em 1 automaticamente
    print()
    print('=' * 10, 'Cadastro de livros', '=' * 10)
    print(f'Id do livro: {id_global}')
    dicio = {
        'id': id_global,
        'nome': input('Qual o nome do livro? '),
        'autor': input('Qual o autor do livro? '),
        'editora': input('Qual a editora do livro? ')
    }
    print('=' * 40)
    lista_livro.append(dicio) #adicina as alterações à lista_livro
    print(f'Livro cadastrado com sucesso!')
    return #retorna ao menu principal

def consultar_livro():
    print()
    print('=' * 10, 'Consulta de livros', '=' * 10) #menu de consulta de livros
    print('1 - Consultar todos')
    print('2 - Consultar por id')
    print('3 - Consultar por autor')
    print('4 - Retornar ao menu')
    print('=' * 40)
    consulta = int(input('Qual a consulta desejada? '))

    while True:
        if (consulta < 1) or (consulta > 4): #invalidando respostas
            print('Opção inválida. Tente novamente')
            consulta = int(input('Qual a consulta desejada? '))
        else:
            if consulta == 1: #todos os livros
                for livro in lista_livro:
                    print()
                    print(f"Id: {livro['id']}")
                    print(f"Nome: {livro['nome']}")
                    print(f"Autor: {livro['autor']}")
                    print(f"Editora: {livro['editora']}")
            elif consulta == 2: #livros por id
                id_consulta = int(input('Digite o id do livro: '))
                for id in lista_livro:
                    if id['id'] == id_consulta: #usa o id da lista_livro
                        print()
                        print(f"Id: {id['id']}")
                        print(f"Nome: {id['nome']}")
                        print(f"Autor: {id['autor']}")
                        print(f"Editora: {id['editora']}")
            elif consulta == 3: #livros por autor
                autor_consulta = input('Digite o autor do livro: ')
                for autor in lista_livro:
                    if autor['autor'] == autor_consulta: #usa o autor da lista_livro
                        print()
                        print(f"Id: {autor['id']}")
                        print(f"Nome: {autor['nome']}")
                        print(f"Autor: {autor['autor']}")
                        print(f"Editora: {autor['editora']}")
            else: #voltar ao menu principal
                print('Retornando ao menu principal...')
            break

def remover_livro():
    print()
    print('=' * 10,'Removendo livro(s)','=' * 10) #menu de remoção de livros
    id_remover = int(input('Digite o id do livro a se remover: '))
    for id in lista_livro:
        if id['id'] == id_remover:
            lista_livro.remove(id)
            print(f'Livro removido com sucesso!')
    return #retorna ao menu principal

#Programa Principal
print('Bem vindo(a) a Livraria da Luíza Melchor Bisson da Costa')
while True:
    print()
    print('=' * 12,'Menu Principal','=' * 12)
    print('1 - Cadastrar livro')
    print('2 - Consultar livro(s)')
    print('3 - Remover livro')
    print('4 - Encerrar o programa')
    print('=' * 40)
    resposta = int(input('Qual opção você deseja explorar? '))

    if (resposta < 1) or (resposta > 4): #invalidando respostas
        print('Opção inválida. Tente novamente.')
        resposta = int(input('Qual opção você deseja explorar? '))
    else:
        if resposta == 1:
            cadastrar_livro(id)
        elif resposta == 2:
            consultar_livro()
        elif resposta == 3:
            remover_livro()
        elif resposta == 4:
            print('Encerrando o programa...')
            break

# cadastrar ---------
# nome: O Estranho Destino de Poison
# autor: Chris Wooding
# editora: Arxjovem
# nome: A Maldição de Alaizabel Cray
# autor: Chris Wooding
# editora: Arxjovem
# nome: Do Inferno
# autor: Alan Moore & Eddie Campbell
# editora: Veneta

