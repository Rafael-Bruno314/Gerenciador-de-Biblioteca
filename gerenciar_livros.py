import time
import livros_e_usuarios_disponíveis
from gerenciar_usuarios import Usuarios

class Visualizar():

    def exibir_livros():
        print("-"*50)
        print("Listando os livros cadastrados na base de dados:")
        print("-"*50)
        for indice, livro in enumerate(livros_e_usuarios_disponíveis.livros, start=1):
            print(f"{indice} - Título: {livro['nome']} \n Autor: {livro['autor']} - ISBN: {livro['isbn']}\n")

    def listar_emprestimos():
        print("-"*50)
        print("Listando todos os livros com empréstimo:")
        print("-"*50)
        for indice, livro in enumerate(livros_e_usuarios_disponíveis.livros, start=1):
            if(livro.get("Emprestado por") != None):
                print(f"{indice} - Título: {livro['nome']} \n Autor: {livro['autor']} - ISBN: {livro['isbn']}\n Emprestado para: {livro['Emprestado por']}\n")

    def listar_disponibilidade():
        for indice, linha in enumerate(livros_e_usuarios_disponíveis.livros, start=1):
            if(linha.get("Emprestado por") == None):
                print(f"{indice} - Título: {linha['nome']} \n Autor: {linha['autor']} - ISBN: {linha['isbn']}\n")

    def procurar_livros(info):
        resultado = []
        for indice, livro in enumerate(livros_e_usuarios_disponíveis.livros):
            for chave, valor in livro.items():
                if(info == valor):
                    resultado.append(indice)
        return resultado
    
    def buscar_livros(info):
        resultados = []
        for livro in livros_e_usuarios_disponíveis.livros:
            for chave, valor in livro.items():
                if(info == valor):
                    resultados.append(livro)
        print(f"Foram encontrados {len(resultados)} resultados para a busca:") if len(resultados)>1 else print(f"Foi encontrado {len(resultados)} resultado para a busca:")
        for resultado in resultados:
            print(f"Título: {resultado['nome']} \n Autor: {resultado['autor']} - ISBN: {resultado['isbn']}\n")


class Livros():   

    def adicionar_livro(titulo, autor, isbn):
        print("Adicionando novo livro")
        livros_e_usuarios_disponíveis.livros.append({"nome": titulo, "autor": autor, "isbn": isbn})
        time.sleep(1)
        print(f"Livro '{titulo}' de {autor} com ISBN {isbn} adicionado com sucesso.")
        time.sleep(3)

    def atualizar_livro(info):
        time.sleep(0.5)
        indice = Visualizar.procurar_livros(info)[0]
        print("Qual dado deseja atualizar? ", end=" ")
        dado = input()
        print("Qual o novo valor? ", end=" ")
        valor = input()   
        livros_e_usuarios_disponíveis.livros[indice][dado] = valor
        print(f" Livro atualizado com sucesso para {livros_e_usuarios_disponíveis.livros[indice][dado]}")

    def excluir_livro(info):
        indice = Visualizar.procurar_livros(info)[0]
        livros_e_usuarios_disponíveis.livros.pop(indice)
        print("Removendo livro...")
        time.sleep(2)


class Biblioteca:

    def emprestar_livro(usuario):
        print("Empréstimo de um livro")
        Visualizar.listar_disponibilidade()     
        print("Qual livro deseja pegar emprestado?", end=" ")
        info = input()
        if(info.isdigit() and int(info) <= 999):
            indice = int(info, base=10)-1
        else:
            indice = Visualizar.procurar_livros(info)[0]       
        livros_e_usuarios_disponíveis.livros[indice]["Emprestado por"] = usuario
        print(f"Livro {livros_e_usuarios_disponíveis.livros[indice]['nome']} emprestado para {usuario}")

    def devolver_livro():
        Visualizar.listar_emprestimos()
        print("Qual livro deseja devolver (Digite o índice)?")
        indice = int(input())
        del livros_e_usuarios_disponíveis.livros[indice]["Emprestado por"]
        print(f"O livro {livros_e_usuarios_disponíveis.livros[indice]['nome']} de {livros_e_usuarios_disponíveis.livros[indice]['autor']} foi devolvido com sucesso!")
