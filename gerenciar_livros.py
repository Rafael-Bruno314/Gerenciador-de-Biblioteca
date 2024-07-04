from livros_e_usuarios_disponíveis import *
from gerenciar_usuarios import Usuarios

class Visualizar():

    def exibir_livros():
        print("-"*50)
        print("Listando os livros cadastrados na base de dados:")
        print("-"*50)
        for indice, livro in enumerate(livros_db(), start=1):
            print(f"{indice} - Título: {livro['nome']} \n Autor: {livro['autor']} - ISBN: {livro['isbn']}\n")

    def listar_emprestimos():
        print("-"*50)
        print("Listando todos os livros com empréstimo:")
        print("-"*50)
        for indice, livro in enumerate(livros_db(), start=1):
            if(livro.get("Emprestado por") != None):
                print(f"{indice} - Título: {livro['nome']} \n Autor: {livro['autor']} - ISBN: {livro['isbn']}\n Emprestado para: {livro['Emprestado por']}\n")

    def listar_disponibilidade():
        for indice, linha in enumerate(livros_db(), start=1):
            if(linha.get("Emprestado por") == None):
                print(f"{indice} - Título: {linha['nome']} \n Autor: {linha['autor']} - ISBN: {linha['isbn']}\n")

    def procurar_livros(info):
        indice = []
        #print(type(livros_db()))
        #print(len(livros_db()))
        str_db = str(livros_db())
        print(type(str_db))
        db_split = str_db.split('},')
        db_final = []
        for item in db_split:
            item = item + '}'
            db_final.append(item)
        #print(db_final, type(db_final))
        for key, livro in enumerate(db_final):
            print(livro)
            pass
        



        """
        for key, livro in enumerate(livros_db()[0]):
            novo_livro = eval(livro)
            print(novo_livro,type(novo_livro))
            print("aaaaaaaaaa",type(livro))
            i+=1
            print(livro, i)
            for chave, valor in novo_livro.items():
                if(info == valor):
                    indice.append(key)
        return indice[0]
        """

    def buscar_livros(info):
        resultados = []
        for livro in livros_db():
            for chave, valor in livro.items():
                if(info == valor):
                    resultados.append(livro)
        print(f"Foram encontrados {len(resultados)} resultados para a busca:") if len(resultados)>1 else print(f"Foi encontrado {len(resultados)} resultado para a busca:")
        for resultado in resultados:
            print(f"Título: {resultado['nome']} \n Autor: {resultado['autor']} - ISBN: {resultado['isbn']}\n")


class Livros():   

    def adicionar_livro(titulo, autor, isbn):
        print("Adicionando novo livro")
        livro = json.dumps({"nome": titulo, "autor": autor, "isbn": isbn}, ensure_ascii=False)
        cadastra_livro_db(livro)
        print(f"Livro '{titulo}' de {autor} com ISBN {isbn} adicionado com sucesso.")

    def atualizar_livro(info):
        indice = Visualizar.procurar_livros(info)[0]
        print("Qual dado deseja atualizar? ", end=" ")
        dado = input()
        print("Qual o novo valor? ", end=" ")
        valor = input()   
        livros_db()[indice][dado] = valor
        print(f" Livro atualizado com sucesso para {livros_db()[0][indice][dado]}")

    def excluir_livro(info):
        indice = Visualizar.procurar_livros(info)
        nova_lista = livros_db()
        nova_lista.pop(indice)
        print("Removendo livro...")
        exclui_livro(nova_lista)


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
        livros_db()[0][indice]["Emprestado por"] = usuario
        print(f"Livro {livros_db()[0][indice]['nome']} emprestado para {usuario}")

    def devolver_livro():
        Visualizar.listar_emprestimos()
        print("Qual livro deseja devolver (Digite o índice)?")
        indice = int(input())
        del livros_db()[0][indice]["Emprestado por"]
        print(f"O livro {livros_db()[0][indice]['nome']} de {livros_db()[0][indice]['autor']} foi devolvido com sucesso!")
