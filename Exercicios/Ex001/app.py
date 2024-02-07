from Modelos.classes import Livro


def main():
    livro = Livro()
    livro.titulo = input("Nome do Livro: ")
    livro.autor = input("Nome do Autor: ")
    livro.ano = input("Ano de Publicação: ")

    print(livro.titulo)
    print(livro.autor)
    print(livro.ano)


if __name__ == "__main__":
    main()
