import pandas as pd
from Modelos.classes import Dados


def main():
    base_de_dados = ("C:\\Users\\User\\Desktop\\ficheirosMiguel\\Python\\MiguelQueiros\\AulasAvançadasIEFP\\Aulas\\#2 "
                     "- Pandas - Biblioteca\\imoveis.csv")
    analise = Dados(base_de_dados)

    print('----- Ler tabela completa -----')
    print(analise.dados)

    print('----- Ler Inicio da tabela -----')
    print(analise.ler_inicio(10))

    print('----- Ler Final da tabela -----')
    print(analise.ler_final(10))

    print('----- Ler Tipo da tabela -----')
    print(analise.ler_tipo())

    print('----- Ler Colunas da tabela -----')
    print(analise.ler_colunas())

    print('----- Ler Tipo dado do Cabeçalho -----')
    print(analise.tipo_dado_cabecalho('Tipo'))

    print('----- Ver Média de Rendas POR TIPO DE IMOVEL -----')
    print(analise.media_rendas('Tipo', 'Valor'))

    print('----- Valor Percentual de Rendas POR TIPO DE IMOVEL -----')
    print(analise.percentagem_tipo())

    print('----- MOSTRAR VALORES NULOS -----')
    print(analise.mostrar_valores_nuloes().head(15))

    print('----- Remover VALORES NULOS -----')
    analise.remover_valores_nulos(0)

    print('----- MOSTRAR VALORES NULOS -----')
    print(analise.mostrar_valores_nuloes().head(15))

    print('----- Encontar VALORES A 0 -----')
    print(analise.encontrar_valores_zero())

    print('----- Remover VALORES A 0 -----')
    analise.remover_valores_zero()

    print('----- Encontar VALORES A 0 -----')
    print(analise.encontrar_valores_zero())

    print('----- > 1 Quarto, Valor < 500 -----')
    print(analise.filtros('Quartos == 1 and Valor < 500').head(15))

    print('----- > Filtros de quartos igual A -----')
    print(analise.filtro_quarto(1).head(15))

    print('----- > Filtros de Alguer igual A -----')
    print(analise.filtro_quarto(500).head(15))

    print('----- > Filtros Quarto igual a 1 e alguer inferior a 500 -----')
    print(analise.filtro_quarto_aluguer())

    print('----- > Filtros Quarto pelo menos 2 quartos e alguer inferior a 750 e area maior que 70 -----')
    print(analise.filtro_quarto_aluguer_area())

    print('----- > CRIAR COLUNA DE DESPESAS MENSAIS -----')
    print(analise.despesas_mensais())

    print('----- > CRIAR COLUNA DE DESPESAS ANUAIS -----')
    print(analise.despesas_anuais())

    #analise.guardar('test123.csv', separador=";")


if __name__ == "__main__":
    main()
