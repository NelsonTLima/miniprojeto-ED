from Clinica import Clinica
from Menu import Menu

clinica = Clinica()
menu = Menu(clinica)
print(menu)
while True:
    try:
        comando = input("[menu]\n> ")
        menu.escolha(comando)
    except KeyboardInterrupt:
        break
