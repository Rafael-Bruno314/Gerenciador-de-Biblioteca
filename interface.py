import sys
import gerenciar_livros

def interface(repeteco):
    if(repeteco == 0):
        print("Bem vindo ao gerenciador de bibliotecas!")

        print("Cadastro de Livros")
        print("1 - Adicionar novo livro")
        print("2 - Remover livro existente")
        print("3 - Atualizar informações de um livro")
        print("4 - Listar todos os livros disponíveis")
        print("-"*60)
        print("5 - Registrar o empréstimo de um livro")
        print("6 - Registrar a devolução de um livro")
        print("7 - Listar todos os empréstimos ativos")
        print("-"*60)
        print("Consulta de Livros")
        print("8 - Procurar livro por título, autor ou ISBN")
        print("9 - Filtrar livros por categoria ou disponibilidade")
        print("0 - Sair")
        
        escolha_do_usuario = input("O que você deseja fazer?")
    else:
        escolha_do_usuario = input("O que mais você deseja fazer?")

    if(escolha_do_usuario == "1"):
        gerenciar_livros.adicionar_livro()
        interface(1)

    elif(escolha_do_usuario == "2"):
        gerenciar_livros.excluir_livro()
        interface(1)
    
    elif(escolha_do_usuario == "3"):
        gerenciar_livros.atualizar_livro()
        interface(1)
    
    elif(escolha_do_usuario == "4"):
        gerenciar_livros.exibir_livros()
        interface(1)
    
    elif(escolha_do_usuario == "5"):
        gerenciar_livros.emprestar_livro()
        interface(1)

    elif(escolha_do_usuario == "6"):
        gerenciar_livros.devolver_livro()
        interface(1)
    
    elif(escolha_do_usuario == "7"):
        gerenciar_livros.listar_emprestimos()
        interface(1)

    elif(escolha_do_usuario == "8"):
        gerenciar_livros.procurar_livros()
        interface(1)

    elif(escolha_do_usuario == "9"):
        gerenciar_livros.listar_disponibilidade()
        interface(1)

    elif(escolha_do_usuario == "0"):
        sys.exit()

    else:
        print("Valor digitado inválido. Digite um valor válido")
        interface(0)

interface(0)