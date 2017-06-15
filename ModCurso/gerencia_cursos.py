import os
from ModCurso.Curso import Curso
from pymongo import MongoClient
import time

client = MongoClient()
db = client['Escola']
cursos = db['cursos']


def gerenciaCurso():

    os.system('clear')

    opcoes = {
        1: addcurso,
        2: removecurso,
        3: editarcuro,
        4: adddisciplina,
        5: removedisciplina,
        6: listarcurso,
        7: listadisciplina,
    }

    print("Digite 1 para adicionar um curso: ")
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


def addcurso():

    os.system('clear')
    c = Curso(str(input("Digite o nome do curso: ")))

    conclue = cursos.insert_one(c.__dict__).inserted_id
    print("Curso adicionado! ")
    gerenciaCurso()


def editarcuro():

    print("\n\nCursos: ")
    for x in cursos.find():
        print("\t " + x['_Curso__nome'])

    n = str(input("Digite qual curso você quer editar: "))
    nome = str(input("Digite o novo nome: "))

    cursos.update(
        {'_Curso__nome': n},
        {
            '_Curso__nome': nome,
            '_Curso__disciplinas': cursos.find_one(
                {
                    '_Curso__nome': n
                }
            )['_Curso__disciplinas']
        }
    )
    gerenciaCurso()


def removecurso():

    print("\n\nCursos: ")

    for x in cursos.find():
        print("\t " + x['_Curso__nome'])

    n = str(input("Digite o nome do banco que deseja remover: "))

    cursos.remove({'_Curso__nome': n})
    gerenciaCurso()


def listarcurso():

    print("Lista de cursos")

    for x in cursos.find():
        print("\t \t" + x['_Curso__nome'])

    time.sleep(5)
    gerenciaCurso()


def adddisciplina():

    print("\n\nCursos: ")

    for x in cursos.find():
        print("\t " + x['_Curso__nome'])

    z = str(input("Digite o nome do banco que deseja inserir a disciplina: "))
    obj = cursos.find_one({'_Curso__nome': z})
    n = str(input("Digite o nome da disciplina: "))
    obj['_Curso__disciplinas'].append(n)

    cursos.update(
        {'_Curso__nome': z},
        {
            '_Curso__nome': z,
            '_Curso__disciplinas': obj['_Curso__disciplinas']
        }
    )
    gerenciaCurso()


def removedisciplina():

    print("\n\nCursos: ")

    for x in cursos.find():
        print("\t " + x['_Curso__nome'])

    z = str(input("Digite o nome do banco que deseja remover a disciplina: "))
    obj = cursos.find_one({'_Curso__nome': z})
    n = str(input("Digite o nome da disciplina: "))
    obj['_Curso__disciplinas'].remove(n)

    cursos.update(
        {'_Curso__nome': z},
        {
            '_Curso__nome': z,
            '_Curso__disciplinas': obj['_Curso__disciplinas']
        }
    )
    gerenciaCurso()


def listadisciplina():

    print("\n\nCursos: ")

    for x in cursos.find():
        print("\t " + x['_Curso__nome'])

    z = str(input("Digite o nome do banco que deseja listar as disciplinas: "))
    print("\n\n\n")

    obj = cursos.find_one(
        {'_Curso__nome': z}
    )

    for x in obj['_Curso__disciplinas']:
        print("Disciplina: " + x)

    time.sleep(5)
    gerenciaCurso()