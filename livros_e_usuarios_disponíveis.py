import json

livros = [
    {
        "nome": "Dom Quixote",
        "autor": "Miguel de Cervantes",
        "isbn": "9780199537564",
        "Emprestado por": "Rafael Bruno"
    },
    {
        "nome": "Harry Potter e a Pedra Filosofal",
        "autor": "J.K. Rowling",
        "isbn": "9788532530780",
        "Emprestado por": "Maria Clara"
    },
    {
        "nome": "1984",
        "autor": "George Orwell",
        "isbn": "9780451524935"
    },
    {
        "nome": "Orgulho e Preconceito",
        "autor": "Jane Austen",
        "isbn": "9780141439518"
    },
    {
        "nome": "A Revolução dos Bichos",
        "autor": "George Orwell",
        "isbn": "9780141182704"
    },
    {
        "nome": "A Menina que Roubava Livros",
        "autor": "Markus Zusak",
        "isbn": "9788535912669"
    },
    {
        "nome": "Cem Anos de Solidão",
        "autor": "Gabriel García Márquez",
        "isbn": "9788501017619"
    },
    {
        "nome": "A Culpa é das Estrelas",
        "autor": "John Green",
        "isbn": "9788580572184"
    },
    {
        "nome": "O Pequeno Príncipe",
        "autor": "Antoine de Saint-Exupéry",
        "isbn": "9788576570715"
    },
    {
        "nome": "O Senhor dos Anéis",
        "autor": "J.R.R. Tolkien",
        "isbn": "9780345339706"
    }
]

def livros_db():
    with open("livros.txt", "r", encoding='utf-8') as arquivo:
        conteudo = arquivo.read()
        lista_de_livros = json.loads(conteudo)
        
        #for livro in lista_de_livros:
            #print(livro, type(livro))
    return lista_de_livros


def cadastra_livro_db(livro):
    #print(livro, type(livro))
    with open("livros.txt", "r", encoding='utf-8',errors='ignore') as arquivo:
        db_antes = arquivo.read()
        db_antes = db_antes[:-1]
    with open("livros.txt", "w", encoding='utf-8',errors='ignore') as write_arquivo:
        write_arquivo.write(db_antes + "," + livro + "]")


def exclui_livro(novo_db):
    with open("livros.txt", "w", encoding='utf-8') as write_arquivo:
        write_arquivo.write(str(novo_db))

#livro = json.dumps({"nome": "título", "autor": "autór", "isbn": "ísbn"}, ensure_ascii=False)
#cadastra_livro_db(livro)

usuarios = [
    "Taylor",
    "Bruno",
    "Carlos",
    "Maria Clara",
    "Eduardo",
    "Fernanda",
    "Gabriel",
    "Helena",
    "Igor",
    "Juliana"
]