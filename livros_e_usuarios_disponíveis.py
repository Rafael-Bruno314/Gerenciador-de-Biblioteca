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
    livros = []
    with open("livros.txt", "r", encoding='utf-8') as arquivo:
        for linha in arquivo:
            livros.append(json.loads(linha.strip()))
    print(livros[0])
    return livros[0]

def cadastra_livro_db(livro):
    with open("livros.txt", "r", encoding='utf-8',errors='replace') as arquivo:
        banana = arquivo.read()
        #print("-"*100,banana[:-1])
    with open("livros.txt", "w", encoding='utf-8',errors='replace') as write_arquivo:
        write_arquivo.write(banana[:-1]+ "," + json.dumps(livro, ensure_ascii=False) + "]")



#cadastra_livro_db()
#livros_db()

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