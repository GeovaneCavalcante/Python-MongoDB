import os
from ModAluno.Aluno import Aluno
from pymongo import MongoClient
import time

client = MongoClient()
db = client['Escola']
alunos = db['alunos']


def gerenciaAluno():

    os.system('clear')

    opcoes = {
        1: None,
    }

    print("Digite 1 para adicionar um aluno: ")
    print("Digite 2 para remover um curso: ")
    print("Digite 3 para editar um curso: ")
    print("Digite 4 para adicionar uma disciplina: ")
    print("Digite 5 para remover uma disciplina: ")
    print("Digite 6 para listar todos os cursos: ")
    print("Digite 7 para listar as disciplinas de um determinado curso: ")
    print("Digite 8 para listar os alunos de um determinado curso: ")

    try:
        x = int(input("Digite a opção desejada: "))
        if x<=8 and x>=1:
            opcoes[x]()

    except ValueError:
        print("Valor inválido! ")