from PilhaEncadeada import Pilha
from Senha import Senha
from Paciente import Paciente

class Painel:
    def __init__(self):
        self.__cadastro = Pilha()
        self.__consulta = Pilha()

    def chamarParaCadastro(self, senha : Senha):
        if not isinstance(senha, Senha):
            return
        self.__cadastro.empilha(senha)

    def chamarParaConsulta(self, paciente : Paciente):
        if not isinstance(paciente, Paciente):
            return
        self.__consulta.empilha(paciente)

    def __str__(self):
        tamanhoCadastro = len(self.__cadastro)
        cadastroAtual = "" if tamanhoCadastro < 1 else self.__cadastro.topo()
        ultimoCadastro = "" if tamanhoCadastro < 2 else self.__cadastro.elemento(tamanhoCadastro - 1)
        penultimoCadastro = "" if tamanhoCadastro < 3 else self.__cadastro.elemento(tamanhoCadastro - 2)

        tamanhoConsulta = len(self.__consulta)
        consultaAtual = "" if tamanhoConsulta < 1 else self.__consulta.topo()
        ultimaConsulta = "" if tamanhoConsulta < 2 else self.__consulta.elemento(tamanhoConsulta - 1)
        penultimaConsulta = "" if tamanhoConsulta < 3 else self.__consulta.elemento(tamanhoConsulta - 2)

        return '''\
       Painel de Atendimento
Cadastro                Consultório Médico
============            ======================
> {:>4}                  > {}
{:>6}                    {}
{:>6}                    {}'''.format(
        str(cadastroAtual), str(consultaAtual), # Topo
        str(ultimoCadastro), str(ultimaConsulta), # Topo -1
        str(penultimoCadastro), str(penultimaConsulta)) # Topo -2
