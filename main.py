from Clinica import Clinica

c = Clinica()
print(c.menu)
while True:
    comando = input("> ")
    c.menu.funcao[comando]()
