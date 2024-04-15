class Porta:
    # iniciando a instancia do objeto 
    def __init__(self, material:str, largura=100) -> None:
        self.altura = 210
        self.largura = largura
        self.material = material
        self.cor = "Azul"
        self.fechadura = None
        self.status = None #True=Aberto | False=Fechado

    def instalar(self,fechadura): # Passando a instância da classe fechadura encapsulada com todos os seus atributos e metodos. 
        self.fechadura = fechadura 
    
    def trancar(self, chave):
        self.fechadura.chavear(chave) # usando o metodo de uma instância para chavear a porta 
    
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
        Altura: {self.altura} Largura: {self.largura}
        Material: {self.altura} Cor {self.cor}
        Fechadura: {self.fechadura.imprir()} Status: {self.is_aberta()}
"""
    