from FilaSequencial import Fila as FilaSequencial
from Senha import Senha
from Paciente import Paciente

class Painel:
    def __init__(self):
        self.__cadastro = FilaSequencial(3)
        self.__consulta = FilaSequencial(3)

        for _ in range(3):
            self.__cadastro.enfileirar("")
            self.__consulta.enfileirar("")

    def chamarParaCadastro(self, senha : Senha):
        if not isinstance(senha, Senha):
            return
        self.__cadastro.desenfileirar()
        self.__cadastro.enfileirar(senha)

    def chamarParaConsulta(self, paciente : Paciente):
        if not isinstance(paciente, Paciente):
            return
        self.__consulta.desenfileirar()
        self.__consulta.enfileirar(paciente)

    def __str__(self):
        return '''\
       Painel de Atendimento
Cadastro                Consultório Médico
============            ======================
> {:>4}                  > {}
{:>6}                    {}
{:>6}                    {}'''.format(
        str(self.__cadastro.elemento(3)), str(self.__consulta.elemento(3)),
        str(self.__cadastro.elemento(2)), str(self.__consulta.elemento(2)),
        str(self.__cadastro.elemento(1)), str(self.__consulta.elemento(1)))
