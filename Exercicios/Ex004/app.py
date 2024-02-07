from Modelos.funcoes import VerificarAno
from Modelos.classes import Livro, Biblioteca


def main():
    biblioteca = Biblioteca()
    while True:
        tipo_livro = input("Tipo de Livro: [Ebook/Livro]")
        if tipo_livro in ["Livro", "Ebook"]:
            livro = Livro()
            livro.titulo = input(f"Título do {tipo_livro}: ")
            livro.autor = input(f"Autor do {tipo_livro}: ")
            livro.ano = input("Ano de Publicação: ")
            livro._tipo = tipo_livro
            if tipo_livro != "Livro":
                livro.tamanho_arquivo = input("Tamaho do Arquivo: ")
            biblioteca.livros = livro
        else:
            print("Tipo de Livro inválido!!")
        opcao = input("Pretende adicionar mais livros? [S/N]").lower().strip()

        if opcao == 'n':
            break
    print(biblioteca)


if __name__ == "__main__":
    main()
