from FilaEncadeada import Fila as FilaEncadeada
from FilaEncadeada import FilaException
from FilaSequencial import Fila as FilaSequencial
from Painel import Painel
from Paciente import Paciente
from Senha import Senha

class Clinica:
    def __init__(self):
        self.__proximaSenha = 1
        self.__filaDeCadastro = FilaEncadeada()
        self.__filaDoConsultorio = FilaEncadeada()
        self.__painel = Painel()
        self.__menu = Menu(self)

    @property
    def menu(self):
        return self.__menu

    def printPainel(self):
        print(self.__painel)

    def gerarSenha(self) -> str:
        novaSenha = Senha(self.__proximaSenha)
        self.__filaDeCadastro.enfileirar(novaSenha)
        self.__proximaSenha += 1

    def cadastrar(self):
        try:
            senha = self.__filaDeCadastro.desenfileirar()
        except FilaException as fe:
            print(fe)
            return
        self.__painel.chamarParaCadastro(senha)
        paciente = Paciente(senha, input("Nome\n> "), input("Plano\n> "))
        self.__filaDoConsultorio.enfileirar(paciente)

    def atender(self):
        # colocar paciente atual na fila de consulta do painel.
        try:
            paciente = self.__filaDoConsultorio.desenfileirar()
        except FilaException as fe:
            print(fe)
            return
        self.__painel.chamarParaConsulta(paciente)

    def consultarPosicao(self):
        chave = input("Identificação de senha: ")
        try:
            print("Você está na ", self.__filaDeCadastro.busca(chave),"ª posição na fila de atendimento.")
            return
        except FilaException:
            pass
        try:
            print("Você está na ", self.__filaDoConsultorio.busca(chave),"ª posição na fila de atendimento.")
            return
        except FilaException as fe:
            print(fe)

class Menu:
    def __init__(self, clinica):
        self.funcao = {
                "1" : clinica.gerarSenha,
                "2" : clinica.cadastrar,
                "3" : clinica.atender,
                "4" : clinica.consultarPosicao,
                "5" : clinica.printPainel,
                "6" : exit
        }

    def __str__(self):
        return '''\
Clinica Medica - Atendimento
============================
1. Obter senha de atendimento
2. Chamar paciente para cadastro
3. Chamar paciente para o consultório
4. Consultar a posição atual
5. Painel de atendimento
6. Sair
'''
