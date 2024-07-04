import json

def livros_db() -> list:
    with open("livros.txt", "r", encoding='utf-8') as arquivo:
        conteudo = arquivo.read()
        lista_de_livros = json.loads(conteudo)
    return lista_de_livros


def cadastra_livro_db(livro:str):
    with open("livros.txt", "r", encoding='utf-8',errors='ignore') as arquivo:
        db_antes = arquivo.read()
        db_antes = db_antes[:-1]
    with open("livros.txt", "w", encoding='utf-8',errors='ignore') as write_arquivo:
        write_arquivo.write(db_antes + "," + livro + "]")


def atualiza_livro(novo_db:list):
    with open("livros.txt", "w", encoding='utf-8') as write_arquivo:
        write_arquivo.write(json.dumps(novo_db, ensure_ascii=False))


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