
# classes #
class Fechadura:
    def __init__(self, modelo, material, cor, chave) -> None:
        self.modelo = modelo
        self.material = material
        self.cor = cor
        self.chave = None
        pass
    
    def usa_chave(self):
        # O Trinco só funciona se a chave for inserida, ou seja ele recebe um True
        # True = com chave | False = sem chave 
        if self.chave == True:
            return True
        else:
            return False

# Instanciando objetos da classe Trinco #

fechadura01 = Fechadura(
    modelo="com_chave",
    material= "Ferro",
    cor="Prata",
    chave= None
) 
#
class Macaneta:
    def __init__(self, modelo, material, cor, obj ) -> None:
        self.modelo = modelo
        self.material = material
        self.cor = cor
        self.obj = fechadura01 # Passando o obj FECHADURA01 como atributo da CLASSE MAÇANETA
        pass
    def macaneta_abre(self):
        if self.obj.usa_chave() == True:
            
            return True
        else: 
             return False
            

# Instanciando objetos da classe Maçaneta #

macaneta01 = Macaneta(
    modelo="redondo",
    material = "Ferro",
    cor = "",
    obj = fechadura01
)

#
class Door:
    def __init__(self,cor, altura, largura, formato, material, vazada, obj, obj2 ) -> None:
        
        self.cor = cor
        self.altura = altura
        self.largura = largura
        self.formato = formato
        self.material = material
        self.vazada = vazada
        self.aberto = None
        # Passando os objetos das CLASSES MACANETA e FECHADURA como atributo da CLASSE DOOR
        self.obj = macaneta01 
        self.obj2 = fechadura01 
    
    def abrir(self):
        # a porta abre se a macaneta receber o True do Trinco.
        if self.obj.macaneta_abre() == True:
            return "A porta está destrancada!"
    def fechar(self): 
        # a porta ñ abre se o trinco da macaneta estiver False.
        if self.obj.macaneta_abre() == False:
            return "A porta está trancada!"

# Instanciando objetos da classe Door #

door1 = Door(
            "red",
             2.10,
             0.50, 
             "retangular", 
             "Madeira",
             vazada=True,
             obj= macaneta01,
             obj2 = fechadura01 
             )

### PROGRAMA PRINCIPAL ###

# Perguntando ao usuário se ele quer abrir a porta
resposta = input("Deseja abrir a porta? (s/n): ")

if resposta.lower() == "s":
    # Simulando inserção da chave
    fechadura01.chave = True
    mensagem = door1.abrir()
    print(mensagem)
else:
   mensagem = door1.fechar()
   print(mensagem)