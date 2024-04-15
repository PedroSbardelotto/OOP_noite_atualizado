import json
from datetime import datetime

class Veiculo:
    def __init__(self, placa):
        self.placa = placa
        self.hora_entrada = datetime.now()
        self.hora_saida = None

class Estacionamento:
    def __init__(self):
        self.vagas = {i: [] for i in range(1, 41)}

    def estacionar(self, veiculo):
        """
        É feito uma conferencia nos items de vagas e caso não tenha
        registo do carro, registra ele e retorna a vaga registrada.
        """
        for vaga, carros in self.vagas.items():
            if not carros:
                carros.append(veiculo)
                return vaga
        return None

    def saida(self, placa):
        """
        Confere se tem carro nas vagas e quando encontra faz o teste para ver se a placa bate com algum parecido.
        Caso tenha, remove o carro e adiciona o horário de saída do mesmo.
        
        """
        for vaga, carros in self.vagas.items():
            for carro in carros:
                if carro.placa == placa:
                    carro.hora_saida = datetime.now()
                    carros.remove(carro)
                    return vaga
        return None

    def resumo_ocupacao(self):
        """
        Envia o resumo de todas as vagas, confere cada vaga e caso esteja vazia, entrega que ela está livre.
        Caso a vaga esteja preenchida, entrega todos os dados de registro dela.
        """
        for vaga, carros in self.vagas.items():
            print(f"Vaga {vaga}:")
            if not carros:
                print("Vaga livre")
            else:
                for carro in carros:
                    print(f"Placa: {carro.placa} - Entrada: {carro.hora_entrada.strftime('%d/%m/%Y %H:%M:%S')}", end="")
                    if carro.hora_saida is not None:
                        print(f" - Saída: {carro.hora_saida.strftime('%d/%m/%Y %H:%M:%S')}")
                    else:
                        print(" - Ainda estacionado")

estacionamento = Estacionamento()

while True:
    print("=== Estacionamento do Tio Ivo ===")
    print("1- Estacionar")
    print("2- Saída")
    print("3- Resumo de ocupação")
    print('4- Carregar Informações')
    print("9- Fim")
    escolha = input("Escolha: ")

    if escolha == "1":
        placa = input("Digite a placa do veículo: ")
        veiculo = Veiculo(placa)
        vaga = estacionamento.estacionar(veiculo)
        if vaga:
            print(f"O veículo foi estacionado na vaga {vaga}")
        else:
            print("Não há vagas disponíveis")

    elif escolha == "2":
        placa = input("Digite a placa do veículo que deseja retirar: ")
        vaga = estacionamento.saida(placa)
        if vaga:
            print(f"O veículo foi retirado da vaga {vaga}")
        else:
            print("Veículo não encontrado")

    elif escolha == "3":
        estacionamento.resumo_ocupacao()
    
    elif escolha == "4":
        resposta = input("Digite o tipo de arquivo que deseja carregar (TXT ou JSON): ")
        if resposta.upper() == "TXT":
            arquivo = input("Digite o nome do arquivo TXT: ")
            try:
                with open(arquivo, "r") as arquivo_txt:
                    dados = arquivo_txt.readlines()
                    for linha in dados:
                        if linha.startswith("Vaga"):
                            vaga = int(linha.split()[1].strip(":"))
                        elif linha.startswith("Placa"):
                            placa = linha.split(":")[1].strip().split()[0]
                            hora_entrada = datetime.strptime(linha.split("-")[0].strip().split(":")[1].strip(), "%d/%m/%Y %H:%M:%S")
                            veiculo = Veiculo(placa)
                            veiculo.hora_entrada = hora_entrada
                            estacionamento.vagas[vaga].append(veiculo)
            except FileNotFoundError:
                print("Arquivo não encontrado.")
        elif resposta.upper() == "JSON":
            arquivo = input("Digite o nome do arquivo JSON: ")
            try:
                with open(arquivo, "r") as arquivo_json:
                    dados = json.load(arquivo_json)
                    for vaga, carros in dados.items():
                        vaga = int(vaga)
                        for carro in carros:
                            placa = carro['placa']
                            hora_entrada = datetime.strptime(carro['hora_entrada'], "%Y-%m-%d %H:%M:%S")
                            veiculo = Veiculo(placa)
                            veiculo.hora_entrada = hora_entrada
                            if 'hora_saida' in carro:
                                hora_saida = datetime.strptime(carro['hora_saida'], "%Y-%m-%d %H:%M:%S")
                                veiculo.hora_saida = hora_saida
                            estacionamento.vagas[vaga].append(veiculo)
            except FileNotFoundError:
                print("Arquivo não encontrado.")
        else:
            print("Tipo de arquivo inválido.")

    elif escolha == "9":
        resposta = input("Deseja salvar os dados em um arquivo TXT ou JSON? (S/N) ")                    
        if resposta.upper() == "S":
            tipo_arquivo = input("Digite o tipo de arquivo que deseja salvar (TXT ou JSON): ")
            if tipo_arquivo.upper() == "TXT":
                with open("estacionamento.txt", "w") as arquivo_txt:
                    for vaga, carros in estacionamento.vagas.items():
                        arquivo_txt.write(f"Vaga {vaga}:\n")
                        if not carros:
                            arquivo_txt.write("Vaga livre\n")
                        else:
                            for carro in carros:
                                arquivo_txt.write(f"Placa: {carro.placa} - Entrada: {carro.hora_entrada}\n")
                                if carro.hora_saida is not None:
                                    arquivo_txt.write(f" - Saída: {carro.hora_saida}\n")
                                else:
                                    arquivo_txt.write(" - Ainda estacionado\n")
            elif tipo_arquivo.upper() == "JSON":
                with open("estacionamento.json", "w") as arquivo_json:
                    json.dump(estacionamento.vagas, arquivo_json, default=str)
            else:
                print("Tipo de arquivo inválido")
        break

    else:
        print("Opção inválida")