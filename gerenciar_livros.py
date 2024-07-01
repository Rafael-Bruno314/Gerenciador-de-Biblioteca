import livros_e_usuarios_disponíveis
import gerenciar_usuarios

def exibir_livros():
    for livro in livros_e_usuarios_disponíveis.livros:
        print(livros_e_usuarios_disponíveis.livros.index(livro), livro)

def listar_emprestimos():
    for indice, linha in enumerate(livros_e_usuarios_disponíveis.livros):
        if(linha.get("Emprestado por") != None):
            print(indice, linha)

def exibir_usuario():
    for indice, usuario in enumerate(livros_e_usuarios_disponíveis.usuarios):
        print(indice, usuario)

class Livros():

    def adicionar_livro():
        print("Adicionando novo livro")
        titulo = input("Qual o nome do livro?")
        autor = input("Qual o autor do livro?")
        ISBN = input("Qual o ISBN do livro?")
        print(f"Livro '{titulo}' de {autor} com ISBN {ISBN} adicionado.")
        livros_e_usuarios_disponíveis.livros.append({"nome": titulo, "autor": autor, "isbn": ISBN})
        print(livros_e_usuarios_disponíveis.livros[-1])

    def atualizar_livro():
        print("Atualizando dados de um livro")
        exibir_livros()
        print("Qual livro deseja atualizar? (digite o número correspondente)", end=" ")
        indice = int(input())
        print("Qual dado deseja atualizar? ", end=" ")
        dado = input()
        print("Qual o novo valor? ", end=" ")
        valor = input()
        livros_e_usuarios_disponíveis.livros[indice][dado] = valor
        print(livros_e_usuarios_disponíveis.livros[indice])

    def excluir_livro():
        exibir_livros()
        print("Qual livro deseja remover? (digite o número correspondente)", end=" ")
        livros_e_usuarios_disponíveis.livros.pop(int(input()))
        print("Removendo livro...")


class Emprestimo:

    def listar_disponibilidade():
        for indice, linha in enumerate(livros_e_usuarios_disponíveis.livros):
            if(linha.get("Emprestado por") == None):
                print(indice, linha)

    def emprestar_livro():
        print("Empréstimo de um livro")
        exibir_livros()
        print("Qual livro deseja pegar emprestado? (digite o número correspondente)", end=" ")
        indice = int(input())
        print("possui cadastro? (s/n)", end=" ")
        cadastro = input()
        while cadastro != "s" or cadastro != "n":
            if(cadastro == "n"):
                gerenciar_usuarios.adicionar_usuarios()
                usuario = livros_e_usuarios_disponíveis.usuarios[-1]
                livros_e_usuarios_disponíveis.livros[indice]["Emprestado por"] = usuario
                print(f"Livro {livros_e_usuarios_disponíveis.livros[indice]['nome']} emprestado para {usuario}")
                break
            else:
                exibir_usuario()
                print("Quem é você (Digite o índice)?", end=" ")
                indice_user = int(input())
                livros_e_usuarios_disponíveis.livros[indice]["Emprestado por"] = livros_e_usuarios_disponíveis.usuarios[indice_user]
                exibir_livros()
                break

    def devolver_livro():
        listar_emprestimos()
        print("Qual livro deseja devolver (Digite o índice)?")
        indice = int(input())
        del livros_e_usuarios_disponíveis.livros[indice]["Emprestado por"]
        print(f"{livros_e_usuarios_disponíveis.livros[indice]} devolvido com sucesso!")

    def procurar_livros():
        print("Digite alguma informação do livro desejado:")
        entrada = input()
        for livro in livros_e_usuarios_disponíveis.livros:
            for chave, valor in livro.items():
                if(entrada == valor):
                    print(livro)
