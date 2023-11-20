from FilaEncadeada import Fila as FilaEncadeada
from FilaEncadeada import FilaException
from Painel import Painel
from Paciente import Paciente
from Senha import Senha

class Clinica:
    def __init__(self):
        self.__proximaSenha = 1
        self.__filaDeCadastro = FilaEncadeada()
        self.__filaDoConsultorio = FilaEncadeada()
        self.__painel = Painel()

    def printPainel(self):
        print(self.__painel)

    def gerarSenha(self) -> str:
        novaSenha = Senha(self.__proximaSenha)
        self.__filaDeCadastro.enfileirar(novaSenha)
        self.__proximaSenha += 1
        print("Senha gerada com sucesso.", novaSenha)

    def cadastrar(self):
        try:
            senha = self.__filaDeCadastro.desenfileirar()
        except FilaException as fe:
            print(fe)
            return
        self.__painel.chamarParaCadastro(senha)
        paciente = Paciente(senha, input("[cadastro]\nNome:  "), input("[cadastro]\nPlano: "))
        self.__filaDoConsultorio.enfileirar(paciente)
        print("Paciente cadastrado com sucesso.")

    def atender(self):
        try:
            paciente = self.__filaDoConsultorio.desenfileirar()
        except FilaException as fe:
            print(fe)
            return
        self.__painel.chamarParaConsulta(paciente)
        print("Chamando", paciente)

    def consultarPosicao(self):
        chave = input("[consulta posição]\nChave: ")
        try:
            print("Você está na ", self.__filaDeCadastro.busca(chave),"ª posição na fila de atendimento.")
            return
        except FilaException:
            pass
        try:
            print("Você está na ", self.__filaDoConsultorio.busca(chave),"ª posição na fila do consultório.")
            return
        except FilaException as fe:
            print(fe)
