class Porta:
    def __init__(self, material, largura=100):
        self.altura = 210
        self.largura = largura
        self.material = material
        self.cor = "Azul"
        self.estatus = True  #True=Aberta  False=Fechada

    def pintar(self, nova_cor):
        self.cor = nova_cor

    def abrir(self):
        self.estatus = True

    def fechar(self):
        self.estatus = False

    def imprimir_dados(self):
        print(
            f"""
            Altura= {self.altura}  Largura= {self.largura}
            Material= {self.material}  Cor= {self.cor}
            Estatus= {self.estatus}
            """)

def ler_material():
    return input("Material: ")

def ler_largura():
    while True:
        try:
            return int(input("Largura: "))
        except:
            input("Valor não válido!")


lista = []
def adicionar(lista, porta):
    lista.append(porta)

def consultar(lista:list) -> None:
    if type(lista) == list:
        for porta in lista:
            porta.imprimir_dados()

def ler_dados():
    for x in range(4):
        adicionar(lista, Porta(ler_material(), ler_largura()))

ler_dados()
consultar(lista)

"""
Você deverá continuar esse exercício implementando uma fechadura na porta.
Para isso você deverá:
- adicionar uma propriedade na porta: fechadura
- adicionar uma nova classe chamada Fechadura, com um atributo segredo. Esse atributo deverá ser uma string ou int e servirá para podermos chavearmos ou deschavearmos a fechadura.
- crie um método para instalar a fechadura na porta
Obs.: Validar a situação de poder abrir a porta somente se estiver deschaveada. 

"""