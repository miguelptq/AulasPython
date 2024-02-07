from Modelos.funcoes import VerificarAno
from Modelos.classes import Livro, Ebook


def main():
    ebook = Ebook()
    ebook.titulo = input("Nome do Livro: ")
    ebook.autor = input("Nome do Autor: ")
    ebook.ano = input("Ano de Publicação: ")
    ebook.tamanho_arquivo = input("Tamaho do Arquivo: ")

    print(ebook)


if __name__ == "__main__":
    main()
