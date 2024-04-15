from class_porta import Porta
from class_fechadura import Fechadura
from estoque import *

def popular_estoque():
    gambiarra = ["Madeira", "PVC", "Ferro"]
    for p in range(3):
        adicionar(Porta(gambiarra)) #def que veio do módulo estoque, estamos add a list gambiarra dentro do estoque com valores já setados

def ler_material():
    return input("Material: ")

popular_estoque()

# instanciando os opbjetos porta e fechadura

porta = estoque[0] #obj porta do indice zero da lista 
fechadura = Fechadura("12345")
porta.instalar(fechadura)
porta.trancar("12345")
porta.abrir()
porta.fechar()
print(fechadura.imprimir())

imprimir_estoque()