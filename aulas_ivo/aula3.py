class Person:
    def __init__(self, marca, ano) -> None:
        self.marca = marca
        self.ano = ano 
        
        
        pass

ka = Person(marca = "ka")
class Caneta:
    def __init__(self, cor, tam):
        self.cor = cor
        self.tamanho = tam
        self.tampa = True

    def escrever(self):
        if not self.tampa:
            print(f"A caneta {self.cor} está escrevendo...")

    def destampar(self):
        self.tampa = False

    def tampar(self):
        self.tampa = True

caneta = Caneta("Azul", 15)
caneta2 = Caneta("Vermelha", 20)

caneta.escrever()
caneta2.destampar()
caneta2.escrever()