from Modelos.funcoes import VerificarAno, VerificarString


class Livro:
    def __init__(self):
        self._titulo = ""
        self._autor = ""
        self._ano = 0

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, novo_titulo):
        self._autor = VerificarString(novo_titulo, 'Título')

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

    def __str__(self):
        return (f'Título: {self._titulo}\n'
                f'Autor: {self._autor}\n'
                f'Ano: {self._ano}')


class Ebook(Livro):
    def __init__(self):
        super().__init__()
        self._tamanho_arquivo = 0

    @property
    def tamanho_arquivo(self):
        return self._tamanho_arquivo

    @tamanho_arquivo.setter
    def tamanho_arquivo(self, novo_tamanho):
        self._tamanho_arquivo = novo_tamanho

