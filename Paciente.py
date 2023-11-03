from Senha import Senha

class Paciente:
    def __init__(self, senha : Senha, nome : str, plano : str):
        self.__nome = nome
        self.__plano = plano
        self.__senha = senha

    def __str__(self):
        return str(self.__senha) + " " + self.__nome

    def __eq__(self, x):
        if self is x:
            return True
        return x == str(self.__senha) or x == self.__senha or x == str(self)
