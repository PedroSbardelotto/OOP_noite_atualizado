class Estante:
    def __init__(self, caixa) -> None:
        self.dic_slots =  {}
        self.caixa = caixa
        self.status = None # True - cheio | False = Vazio 
        self.id_slot = 0
        pass
     
    def imprimir(self,dict_slots): 
        for slots in dict_slots:
            print(f"\nID SLOT: {self.id_slot}\nID CAIXA: {self.id_caixa}\nCHAVE SALA: {self.chave_sala}\nCONTROLE PROJETOR:{self.controle_pro}")
            pass
    
    def verificar_slot(self, caixa): # Metodo que verifica dentro do dict se tem slot vazio para se colocar uma caixa nova
        pass
    
    
    def colocar_caixa(self,caixa):
        pass 

    
    def retirar_caixa(self,caixa):
        pass
