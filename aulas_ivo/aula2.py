# def lenthg(palavra):
#     count = 0 
#     for letter in range(len(palavra)):
#          count += 1 
#     total = count 
    
#     return print(total) 


# lenthg(palavra = "pedro")

# def nome():
#      return len("Eu sou o mais brabo do curso e vai tu te fude!")

# def count_string(mensagem):
#      return len()
# print(f"Quant:{count_string(input("frase: "))}")

# def num(a):
#     b = str(a)
#     count = 0
#     for digito in b: 
#         count += 1 
#     dig = count
#     return dig

# def ler_numero():
#     return input("digite o numero: ")

# print(num(ler_numero()))

# def qt_digitos(numero):
#     return len(str(numero))

# def ler_int():
   
#    try:
#     num = int(input("Numero: "))
#     return num
#     input("Erro")
#    except: 
#     return int("Valor invalido")


# def ler_int2():
#     try: 
#         num = int(input("Numero: "))
    
#         return num if num > 0 else input("Erro")

#     except: 
#         return int ("valor invalido")
    
# def ler_int(num):
#    while 

# def list_int(list):
    
#     return 
# [30,40,50, 500,600,70,66, 90, 101, 230]


""""
crie uma função que receba uma lista com vários numeros e retorne a soma de todos os numeros desta lista, o menor num,
o maior num e a media dos valores dalista.
"""


def retorna_dados(lista_entrada):
    soma = sum(lista_entrada)
    menor = min(lista_entrada)
    maior = max(lista_entrada)
    media = soma/ len(lista_entrada)
    return soma, menor, maior, media

print(retorna_dados([1,2,3,45,34]))