from ModCurso.gerencia_cursos import gerenciaCurso
from ModAluno.gerencia_aluno import gerenciaAluno


def main():

    x = 9

    while x != 0:

        opcoes = {
            1: gerenciaCurso,
            2: gerenciaAluno,
        }

        print("Digite 1 para gerenciar cursos: ")
        print("Digite 2 para gerenciar Alunos: ")
        print("Digite 0 para sair: ")

        try:
            x = int(input("Digite a opção desejada: "))
            if x<=3 and x>=1:
                opcoes[x]()

        except ValueError:
            print("Valor inválido! ")


main()
