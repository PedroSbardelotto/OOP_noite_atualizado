class Porta:
    def __init__(self, material:str, largura=100) -> None:
        self.altura = 210
        self.largura = largura
        self.material = material
        self.cor = "Azul"
        self.fechadura = None
        self.status = None  # True=Aberta   False=Fechada

    def instalar(self, fechadura):
        self.fechadura = fechadura

    def trancar(self, chave):
        self.fechadura.chavear(chave)

    def abrir(self):
        self.status = True

    def fechar(self):
        self.status = False

    def is_aberta(self):
        if self.status:
            return "ABERTA"
        return "FECHADA"

    def imprimir(self) -> str:
        return f"""
        Altura: {self.altura}  Largura: {self.largura}
        Material: {self.material} Cor: {self.cor}
        Fechadura: {self.fechadura.imprimir()}  Status: {self.is_aberta()}
"""

