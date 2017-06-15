

class Curso(object):

    __nome = ""
    __disciplinas = []

    def __init__(self, nome):
        self.__nome = nome
        self.__disciplinas = []

    def getNome(self):
        return self.__nome

    def setNome(self, nome):
        self.__nome = nome

    def getDisciplinas(self):
        return self.__disciplinas

    def addDisciplina(self, disciplina):
        self.__disciplinas.append(disciplina)
