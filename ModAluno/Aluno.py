
class Aluno(object):

    __nome = ""
    __idade = 0
    __matricula = 0

    def __init__(self, nome, idade, matricula):

        self.__nome = nome
        self.__idade = idade
        self.__matricula = matricula

    def getNome(self):
        return self.__nome

    def setNome(self, nome):
        self.__nome = nome

    def getIdade(self):
        return self.__idade

    def setIdade(self, idade):
        self.__idade = idade

    def getMatricula(self):
        return self.__matricula

    def setMatricula(self, matricula):
        self.__matricula = matricula
