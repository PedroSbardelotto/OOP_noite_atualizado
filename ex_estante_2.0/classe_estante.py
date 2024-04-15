from classe_caixa import Caixa
from classe_user import User
import os

class Estante:
    def __init__(self):
        self.qntd_slots = {"701" : None, "702" : None, "702" : None, "703" : None, "704" : None, "705" : None}
        self.caixa = None
        
    def verificar(self): # filé
        for caixa in self.qntd_slots:
            if caixa == None:
                print(caixa)

    def imprimir(self): # filé
        for slot, caixa in self.qntd_slots.items():
            if caixa:
                print(f"Slot {slot}: {caixa.nome}")
            else:
                print(f"Slot {slot}: Vazio")

    def colocar_caixa(self, caixa ): # filé  caixa = caixa
       
        for chave in self.qntd_slots.keys():
            if (caixa.id == chave):
                self.qntd_slots[chave] = caixa
                return print("Slot encontrado, caixa adicionada")
            
    def retirar_caixa(self, caixa):
        remover = self.qntd_slots.pop(caixa, None)

        for chave in self.qntd_slots.keys():
            if (caixa.id == chave):
                self.qntd_slots[chave] = remover
                print("Caixa removida")
            elif(caixa.id != chave):
                slot_incorreto = True
        if slot_incorreto == True:
            print("Caixa não encontrada")

    # def criar_slot(self):
        # chaves = int(input("Quantos slots terá: "))
        # for _ in range(chaves):
        #      slot = input("Chave do slot: ")
        #      self.qntd_slots[slot] = None





### TESTES ###

#instancias  
estante = Estante()
caixa = caixa_obj_teste = Caixa("cx701", "701")
caixa_obj2 = Caixa("cx702", "702") # Caixa  c/ C maiusculo é a class

# estante.colocar_caixa(caixa_obj)
# estante.colocar_caixa(caixa_obj2)
# print("-----------------------")
# estante.imprimir()
# print("-----------------------")
# estante.retirar_caixa(caixa_obj)
# estante.imprimir()


print()
entrada = input("aperte ENTER para entrar no sistema: ")
if entrada == "":
        while True:
            print("\ntestes Estante\n1 - verificar\n2 - imprimir\n3 - colocar_caixa\n4 -  retirar_caixa\n5 - sair")
            opcao3 = input("Escolha uma opção: ")
            if opcao3 == "1" :
                print()
                os.system("cls")
                estante.verificar()
            if opcao3 == "2" :
                os.system("cls")
                print()
                estante.imprimir()
            if opcao3 == "3":
                print()
                os.system("cls")
                estante.colocar_caixa(caixa)
            if opcao3 == "4":
                print()
                os.system("cls")    
                estante.retirar_caixa(caixa)
            if opcao3 == "5":
                break







 






