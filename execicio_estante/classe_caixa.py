class Caixa: 
    def __init__(self, qntd_caneta:int, id_caixa:int, chave_sala:bool, controle_projetor:bool ) -> None:
        self.qntd_caneta = 3
        self.id_caixa = 703
        self.chave_sala = True
        self.controle_projetor = False
        #self.status = self.nome # locador algum usuário 
        pass
    
    def conferir(self):
      
        pass
    def imprimir_caixa(self):
        return f"""\nID CAIXA: {self.id_caixa}\nCHAVE SALA: {self.chave_sala}\nCONTROLE PROJETOR: {self.controle_projetor}"""
