import pandas as pd


class Dados:
    def __init__(self, dados):
        self._dados = pd.read_csv(dados, sep=';')

    @property
    def dados(self):
        return self._dados

    def ler_inicio(self, linhas=5):
        return self.dados.head(linhas)

    def ler_final(self, linhas=5):
        return self.dados.tail(linhas)

    def ler_tipo(self):
        return type(self.dados)

    def ler_colunas(self):
        return self.dados.columns

    def tipo_dado_cabecalho(self, cabecalho):
        return self.dados[cabecalho]

    def media_rendas(self, agrupador, valor_de_media):
        return self.dados.groupby(agrupador)[valor_de_media].mean().round(2)

    def percentagem_tipo(self):
        return self.dados.Tipo.value_counts(normalize=True) * 100

    def mostrar_valores_nuloes(self):
        return self.dados.isnull().sum()

    def remover_valores_nulos(self, novo_valor):
        self.dados.fillna(novo_valor, inplace=True)

    def encontrar_valores_zero(self):
        return self.dados.query('Valor == 0 | Area == 0 | Quartos == 0 | Condominio == 0')

    def remover_valores_zero(self):
        registos_a_remover = self.dados.query('Valor == 0 | Area == 0 | Quartos == 0 | Condominio == 0').index
        self.dados.drop(registos_a_remover, axis=0, inplace=True)

    def filtros(self, filtragem):
        return self.dados.query(filtragem)

    def filtro_quarto(self, num_quarto):
        return self.dados['Quartos'] == num_quarto

    def fitro_aluguer(self, aluguer):
        return  self.dados['Valor'] == aluguer

    def filtro_quarto_aluguer(self):
        filtro1 = self.dados['Quartos'] == 1
        filtro2 = self.dados['Valor'] < 500
        filtro_composto = filtro1 & filtro2
        return self.dados[filtro_composto]

    def filtro_quarto_aluguer_area(self):
        filtro1 = self.dados['Quartos'] >= 2
        filtro2 = self.dados['Valor'] < 750
        filtro3 = self.dados['Area'] > 70
        filtro_composto = filtro1 & filtro2 & filtro3
        return self.dados[filtro_composto]

    def despesas_mensais(self):
        self.dados['Despesas Mensais'] = self.dados['Valor'] + self.dados['Condominio']
        return self.dados

    def despesas_anuais(self):
        self.dados['Despesas Anauis'] = (self.dados['Valor'] + self.dados['Condominio']) * 12
        return self.dados

    def guardar(self, nome_arquivo, metodo=None, separador=";"):
        # decidir o que guardar
        if metodo:
            df_para_guardar = metodo()
        else:
            df_para_guardar = self.dados
        # guardar o que foi decidido em cima
        df_para_guardar.to_csv(nome_arquivo, sep=separador, encoding='UTF-8-sig', index=False, )
        print(f"{nome_arquivo} guardado com sucesso")

