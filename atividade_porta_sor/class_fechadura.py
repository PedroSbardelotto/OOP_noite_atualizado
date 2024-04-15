
class Fechadura:
    def __init__(self, chave):
        self.segredo = chave
        self.status = False #True=Chaveada  False=Deschaveada

    def chavear(self, chave:str)-> None:
        if chave == self.segredo:
            self.status = True  # Chaveada

    def deschavear(self, chave:str) -> None:
        if chave == self.segredo:
            self.status = False

    def is_chaveada(self):
        if self.status:
            return "CHAVEADA"
        return "DESCHAVEADA"

    def imprimir(self) -> str:
        return f""" {self.segredo}  {self.is_chaveada()}"""

# fechadura = Fechadura("1234")
# fechadura.chavear("1234")
# # fechadura.deschavear()
# print(fechadura.imprimir())
#

