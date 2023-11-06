from os import system

class Menu:
    def __init__(self, clinica):
        self.funcao = {
                "exibir" : self,
                "limpar" : self.limpar,
                "1" : clinica.gerarSenha,
                "2" : clinica.cadastrar,
                "3" : clinica.atender,
                "4" : clinica.consultarPosicao,
                "5" : clinica.printPainel,
                "6" : exit
        }

    def escolha(self, comando):
        try:
            self.funcao[comando]()
        except TypeError:
            print(self.funcao[comando])
        except KeyError:
            print("Opção inválida.")

    def limpar(self):
        system("clear")

    def __str__(self):
        return '''\

Clinica Medica - Atendimento
============================
exibir -> exibe o menu.
limpar -> limpa a tela.

1. Obter senha de atendimento
2. Chamar paciente para cadastro
3. Chamar paciente para o consultório
4. Consultar a posição atual
5. Painel de atendimento
6. Sair
'''
