
class User: 
    def __init__(self, nome:str,):
        self.nome = nome 
        self.id_user = 0
        self.caixa = None
        pass


    def cadastrar_user(self,list_user): #tá funcionando
        # Instanciando um obj USER com atributo nome, caixa entra como parametro vazio para poder instanciar o obj só com nome 
        while True:  
            nome = input("digite o valor do atributo nome do obj: ")
            if not nome.isalpha(): # valida se o dado inserido é string
                print("digite um nome válido!")
                continue
            break   
        self.id_user +=1 #cada user criado gera um ID unico
        list_user.append({"Nome":nome,"ID":self.id_user}) # salva na lista com formato de dict
        return list_user 

    def retirar(self):
        pass

    def devolver(self):
        pass

    def imprimir_user(self, list_user):# tá funcionando 
        for user in list_user:
            print(f"\nNome: {user['Nome']}\nID: {user['ID']}")





