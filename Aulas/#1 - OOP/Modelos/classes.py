class Personagem:
    def __init__(self, nome):
        self._nome = nome.strip().capitalize()
        self._vida = 100
        self._experiencia = 0
        self._nivel = 1

    @property
    def nome(self):
        return f'PERSONAGEM: {self._nome}'

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.strip().capitalize()

    @property
    def nivel(self):
        return f'NÍVEL: {self._nivel}'

    @property
    def vida(self):
        return f'Pontos Vitais: {self._vida}%'

    @property
    def experiencia(self):
        return f'EXPERIÊNCIA: {self._experiencia}'


class Mago(Personagem):
    def __init__(self, nome):
        super().__init__(nome)
        self._poder = None
        self.varinha = "Pau"

    def __str__(self):
        return ('--- Mago ---\n'
                f'Nome: {self._nome}\n'
                f'Vida: {self._vida}\n'
                f'XP: {self._experiencia}\n'
                f'Nível: {self._nivel}\n'
                f'PODER: {self.poder}\n'
                f'VARINHA: {self.varinha}')

    @property
    def poder(self):
        return f'{self._poder}' if self._poder is not None else 'Nenhum poder disponível'

    @poder.setter
    def poder(self, novo_poder):
        self._poder = novo_poder

