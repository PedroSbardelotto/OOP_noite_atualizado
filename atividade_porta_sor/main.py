
from class_porta import Porta
from class_fechadura import Fechadura
from estoque import *


def popular_estoque():
    gambiarra = ["Madeira", "PVC", "Ferro"]
    for p in range(3):
        adicionar(Porta(gambiarra[p]))

def ler_material():
    return input("Material: ")

popular_estoque()

porta = estoque[0]
fechadura = Fechadura("1234")

fechadura.deschavear("1234")

porta.instalar(fechadura)
porta.trancar("1234")
porta.abrir()
porta.fechar()
print(porta.imprimir())




# print(fechadura.imprimir())

# imprimir_estoque()





