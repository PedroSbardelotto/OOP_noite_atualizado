from class_estante import Estante
from class_user import User
from classe_caixa import Caixa

########-TESTES-###############
list_user = [{"Nome":"ivo","ID":19},{"Nome":"Pedro","ID":10}]
id_user = 0
nome = ""
#instancia CAIXA
caixas = [0] 
caixas = caixaTeste = Caixa(3,703,True, False)



### PROGRAMA PRINCIPAL ###
while True:
    print("\n1 - Classe User\n2 - Classe Caixa\n3 - Classe Estante\n4 - Sair do sistema ")
    entrada = input("Escolha uma opção: ")
    if entrada == "1":
        user_obj = User(nome)
        while True:
            print("\nTestes User\n1 - cadastrar\n2 - listar")
            opcao = input("Escolha uma opção: ")
            if opcao == "1" :
                user_obj.cadastrar_user(list_user)
            if opcao == "2" :
                user_obj.imprimir_user(list_user)
            if  opcao == "3":
                print(caixaTeste.imprimir_caixa())
                pass
            if  opcao == "4":
                break
    if entrada == "2":
        while True: 
            print("\nTestes Caixa\n1 - cadastrar caixa\n2 - listar caixas\n4 - voltar ao menu anterior!")
            opcao2 = input("Escolha uma opção: ")
            if opcao2 == "1" :
                pass
            if opcao2 == "2" :
                print(caixaTeste.imprimir_caixa())
            if entrada == "3":
                pass
            if entrada == "4":
                break    
    if entrada == "3":
        while True:
            print("\ntestes Estante\n1 - cadastrar caixa\n2 - listar caixas\n4 - voltar ao menu anterior!")
            opcao3 = input("Escolha uma opção: ")
            if opcao3 == "1" :
                pass
            if opcao3 == "2" :
                pass
            if opcao3 == "3":
                pass
            if opcao3 == "4":
                break
    if entrada == "4":
                break        