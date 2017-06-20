import os
from ModAluno.Aluno import Aluno
from pymongo import MongoClient
import time

client = MongoClient()
db = client['Escola']
alunos = db['alunovis']
cursos = db['cursos']

def gerenciaAluno():

    os.system('clear')

    opcoes = {
        1: addaluno,
        2: removealuno,
        3: editaraluno,
        4: addcurso,
        5: editarcurso,
        6: removercurso,
        7: listaalunos,
        8: grade,
    }

    print("Digite 1 para adicionar um aluno: ")
    print("Digite 2 para remover um aluno: ")
    print("Digite 3 para editar um aluno: ")
    print("Digite 4 para adicionar um curso para o aluno: ")
    print("Digite 5 para editar um curso para o aluno: ")
    print("Digite 6 para remover um curso de um aluno: ")
    print("Digite 7 para listar todos os alunos: ")
    print("Digite 8 para listar a grade do curso de um aluno: ")

    try:
        x = int(input("Digite a opção desejada: "))
        if x<=8 and x>=1:
            opcoes[x]()

    except ValueError:
        print("Valor inválido! ")

def addaluno():

    os.system('clear')
    n = str(input("Digite o nome do aluno: "))
    i = int(input("Digite a idade do aluno: "))
    m = int(input("Digite o numero da matricula: "))
    aluno = Aluno(n, i, m)

    aluno_id = alunos.insert_one(aluno.__dict__).inserted_id

    print("Aluno cadastrado! ")
    time.sleep(2)
    gerenciaAluno()


def removealuno():

    print("Lista de Alunos")
    for x in alunos.find():
        print("\t\t" + x['_Aluno__nome'])

    no = str(input("\n\nDigite o nome do aluno que deseja remover: "))
    alunos.remove({'_Aluno__nome': no})
    gerenciaAluno()


def editaraluno():

    print("Lista de alunos")

    for x in alunos.find():
        print("\tAlunos: " + x['_Aluno__nome'])

    noo = str(input("Digite o nome do aluno que deseja editar: "))

    no = str(input("Digite o novo nome do aluno: "))
    id = int(input("Digite a nova idade: "))
    ma = int(input("Digite a nova matricula: "))

    alunos.update(
        {'_Aluno__nome': noo},
        {
            '_Aluno__nome': no,
            '_Aluno__idade': id,
            '_Aluno__matricula': ma,
        }
    )
    gerenciaAluno()

def addcurso():

    print("Lista de alunos")

    for x in alunos.find():
        print("\tAlunos: " + x['_Aluno__nome'])

    noo = str(input("Digite o nome do aluno que deseja adicionar o curso: "))

    for x in cursos.find():
        print("\tCursos: " + x['_Curso__nome'])

    cu = str(input("Digite o curso para o aluno: "))

    obj = alunos.find_one({'_Aluno__nome': noo})

    alunos.update(

        {'_Aluno__nome': noo},
        {
            '_Aluno__nome': noo,
            '_Curso__nome': cu,
            '_Aluno__idade': obj['_Aluno__idade'],
            '_Aluno__matricula': obj['_Aluno__matricula'],
        }

    )
    gerenciaAluno()


def editarcurso():

    print("Lista de alunos")

    for x in alunos.find():
        print("\tAlunos: " + x['_Aluno__nome'])

    noo = str(input("Digite o nome do aluno que deseja editar o curso: "))

    for x in cursos.find():
        print("\tCursos: " + x['_Curso__nome'])

    cu = str(input("Digite o curso para o aluno: "))

    obj = alunos.find_one({'_Aluno__nome': noo})

    alunos.update(

        {'_Aluno__nome': noo},
        {
            '_Aluno__nome': noo,
            '_Curso__nome': cu,
            '_Aluno__idade': obj['_Aluno__idade'],
            '_Aluno__matricula': obj['_Aluno__matricula'],
        }

    )
    gerenciaAluno()


def removercurso():

    print("Lista de alunos")

    for x in alunos.find():
        print("\tAlunos: " + x['_Aluno__nome'])

    noo = str(input("Digite o nome do aluno que deseja remover o curso: "))

    obj = alunos.find_one({'_Aluno__nome': noo})

    alunos.update(

        {'_Aluno__nome': noo},
        {
            '_Aluno__nome': noo,
            '_Aluno__idade': obj['_Aluno__idade'],
            '_Aluno__matricula': obj['_Aluno__matricula'],
        }

    )
    gerenciaAluno()

def listaalunos():

    print("Lista de Alunos")
    for x in alunos.find():
        print("\t\t" + x['_Aluno__nome'])

    time.sleep(5)
    gerenciaAluno()


def grade():

    print("Lista de Alunos")
    for x in alunos.find():
        print("\t\t" + x['_Aluno__nome'])

    noo = str(input("Digite o nome do aluno que deseja mostrar a grade: "))

    obj = alunos.find_one({'_Aluno__nome': noo})

    obj = cursos.find_one(
         {'_Curso__nome': obj['_Curso__nome']}
    )

    for x in obj['_Curso__disciplinas']:
        print("Disciplina: " + x)

    time.sleep(5)
    gerenciaAluno()
