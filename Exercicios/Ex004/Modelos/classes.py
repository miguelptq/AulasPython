from Modelos.funcoes import VerificarAno, VerificarString


class Biblioteca:
    def __init__(self):
        self._livros = []

    @property
    def livros(self):
        return self._livros

    @livros.setter
    def livros(self, novo_livro):
        self._livros.append(novo_livro)

    def __str__(self):
        return '\n'.join(str(livro) for livro in self._livros)


class Livro:
    def __init__(self):
        self._titulo = ""
        self._autor = ""
        self._ano = 0
        self._tipo = "Livro"
        self._tamanho_arquivo = 0

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, ebook):
        self._titulo = VerificarString(ebook, 'Título')

    @property
    def autor(self):
        return self._autor

    @autor.setter
    def autor(self, novo_autor):
        self._autor = VerificarString(novo_autor, 'Autor')

    @property
    def ano(self):
        return self._ano

    @ano.setter
    def ano(self, novo_ano):
        novo_ano = VerificarAno(novo_ano)
        self._ano = novo_ano

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, novo_tipo):
        self._tipo = novo_tipo

    @property
    def tamanho_arquivo(self):
        return self._tamanho_arquivo

    @tamanho_arquivo.setter
    def tamanho_arquivo(self, novo_tamanho):
        self._tamanho_arquivo = novo_tamanho

    def __str__(self):
        if self.tipo == 'Livro':
            return (f'Título: {self._titulo}\n'
                    f'Autor: {self._autor}\n'
                    f'Ano: {self._ano}\n'
                    f'Tipo de Livro: {self._tipo}\n'
                    f'_______________')
        else:
            return (f'Título: {self._titulo}\n'
                    f'Autor: {self._autor}\n'
                    f'Ano: {self._ano}\n'
                    f'Tamanho do Arquivo: {self._tamanho_arquivo} MB\n'
                    f'Tipo de Livro: {self._tipo}\n'
                    f'_______________')
