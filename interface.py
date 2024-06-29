import adicionar_livro

print("Bem vindo ao gerenciador de bibliotecas!")

print("Cadastro de Livros")
print("1 - Adicionar novo livro")
print("2 - Remover livro existente")
print("3 - Atualizar informações de um livro")
print("4 - Listar todos os livros disponíveis")
print("-"*60)
print("Cadastro de Usuários")
print("5 - Adicionar novo usuário")
print("6 - Remover usuário existente")
print("7 - Atualizar informações de um usuário")
print("8 - Listar todos os usuários registrados")
print("-"*60)
print("9 - Empréstimo e Devolução de Livros")
print("10 - Registrar o empréstimo de um livro")
print("11 - Registrar a devolução de um livro")
print("12 - Listar todos os empréstimos ativos")
print("-"*60)
print("13 - Consulta de Livros")
print("14 - Procurar livro por título, autor ou ISBN")
print("15 - Filtrar livros por categoria ou disponibilidade")

escolha_do_usuario = input("O que você deseja fazer?")

if(escolha_do_usuario == "1"):
    print("Adicionando novo livro")
    nome_livro = input("Qual o nome do livro?")
    autor_livro = input("Qual o autor do livro?")
    isbn_livro = input("Qual o ISBN do livro?")
    
    adicionar_livro.adicionar_livro(nome_livro, autor_livro,isbn_livro)


