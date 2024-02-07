from datetime import date


def VerificarAno(ano):
    ano_atual = date.today().year
    while True:
        try:
            ano = int(ano)
            if 1900 <= ano <= ano_atual:
                return ano
            else:
                ano = int(input(f"Insira um ano entre 1900 e {ano_atual}: "))

        except Exception as E:
            print("O número introduzio nao é um numero inteiro")
            ano = input("Insira um novo ano: ")


def VerificarString(string, key):
    while True:
        if isinstance(string, str) and string != '':
            return string
        else:
            print(f"O/A {key} tem de ser string e não pode ser vazio!!")
            string = input(f"Insira um/a novo/a {key}: ")