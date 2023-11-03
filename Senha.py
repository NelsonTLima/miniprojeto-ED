class Senha:
    def __init__(self, n):
        self.__numero = n

    def __str__(self):
        return "N{:03}".format(self.__numero)

    def __eq__(self, x):
        if self is x:
            return True
        return x == str(self)
