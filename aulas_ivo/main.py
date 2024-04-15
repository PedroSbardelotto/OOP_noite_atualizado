from class_porta import Porta
from estoque import *

# porta.abrir()
# porta.fechar()
# print(porta.immprimir)

def popular_estoque():
    for p in  range(3):
        adcionar(Porta(ler_material()))
def ler_material():
    return input("Material: ")

popular_estoque()
porta = estoque[0]
fechadura = Fechadura("1234")

porta.instalar(fechadura)
imprimir_estoque()