class Fechadura:
    def __init__(self, chave):
        self.segredo = chave # Um atributo recebendo uma var!
        self.status = False #True= Chaveada | False = Deschaveada
        pass
    def chavear(self, chave:str) -> None:
        if chave == self.segredo:
            self.status = True # chaveada
    def deschavear(self, chave:str) -> None:
        if chave == self.segredo:
            self.status = False # deschaveada
    def is_chaveada(self):
        if self.status:
            return "CHAVEADA"
        return "DESCHAVEADA"
    def imprimir(self) -> str:
        return f"""{self.segredo} | {self.is_chaveada()} """ 
    

# CHAMADAS 

# fechadura = Fechadura("12345")
# fechadura.chavear("12345")
# print(fechadura.imprimir()) 
# fechadura.deschavear("12345")
# print(fechadura.imprimir())