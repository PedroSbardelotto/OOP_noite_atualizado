pesquisa = {}

class Relevancia:

  def __init__(self):
    self.__desemprego = None
    self.__etica = None
    self.__seguranca = None
    self.__regulamentacao = None
    self.__potencial = None


def menu():
  print('='*20)
  print('        Menu')
  print('='*20)
  print('0- Finalizar o Programa')
  print('1- Realizar avaliação')
  print('2- Relatório')
  escolha = input("Escolha: ")
  try:
    escolha = int(escolha)
    if escolha in [0, 1, 2]:
      return escolha
    print("Escolha incorreta.")
  except:
    print("Escolha incorreta.")
  return -1


EstadosOn = {
  'TO': [],
  'RS': [],
  'SC': [],
  'SE': [],
  'SP': [],
  'RR': [],
  'RO': [],
  'RN': [],
  'RJ': [],
  'PI': [],
  'PE': [],
  'PR': [],
  'PB': [],
  'PA': [],
  'MG': [],
  'MS': [],
  'MT': [],
  'MA': [],
  'GO': [],
  'ES': [],
  'DF': [],
  'CE': [],
  'BA': [],
  'AM': [],
  'AP': [],
  'AL': [],
  'AC': [],
}

def votar():
    estado = input("Digite a sigla do estado em que você reside ("+", ".join(EstadosOn) + "): ").upper()

    if estado not in EstadosOn:
        print("Estado inválido. Digite novamente.")
        return

    relevancia = Relevancia()

  
    relevancia._Relevancia__desemprego = int(input("Grau de relevância para Desemprego e Desigualdade (1 a 5): "))
    relevancia._Relevancia__etica = int(input("Grau de relevância para Questões Éticas e Morais (1 a 5): "))
    relevancia._Relevancia__seguranca = int(input("Grau de relevância para Segurança Cibernética e Privacidade (1 a 5): "))
    relevancia._Relevancia__regulamentacao = int(input("Grau de relevância para Controle e Regulamentação (1 a 5): "))
    relevancia._Relevancia__potencial = int(input("Grau de relevância para Potencial Desenvolvimento de IA Superinteligente (1 a 5): "))

    if estado in pesquisa:
        pesquisa[estado].append(relevancia)
  
    else:
        pesquisa[estado] = [relevancia]
 
    print("Avaliação registrada com sucesso!")


def relatorio():
    estado = input("Que estado você pretende acessar o relatório? (" + ", ".join(EstadosOn) + "): \n").upper()
    if estado not in EstadosOn:
        print("Estado inválido. Digite novamente.")
        return
    
    if estado in pesquisa:
        relevancias = pesquisa[estado]
        total_avaliacoes = len(relevancias)

        soma_desemprego = sum(relevancia._Relevancia__desemprego for relevancia in relevancias)
        soma_etica = sum(relevancia._Relevancia__etica for relevancia in relevancias)
        soma_seguranca = sum(relevancia._Relevancia__seguranca for relevancia in relevancias)
        soma_regulamentacao = sum(relevancia._Relevancia__regulamentacao for relevancia in relevancias)
        soma_potencial = sum(relevancia._Relevancia__potencial for relevancia in relevancias)

        percentual_desemprego = round(soma_desemprego / total_avaliacoes, 2)
        percentual_etica = round(soma_etica / total_avaliacoes, 2)
        percentual_seguranca = round(soma_seguranca / total_avaliacoes, 2)
        percentual_regulamentacao = round(soma_regulamentacao / total_avaliacoes, 2)
        percentual_potencial = round(soma_potencial / total_avaliacoes, 2)

        print('='*50)
        print("Relatório de Importância para o Estado:", estado)
        print('='*50)
        print("Desemprego e Desigualdade:", percentual_desemprego)
        print("Questões Éticas e Morais:", percentual_etica)
        print("Segurança Cibernética e Privacidade:", percentual_seguranca)
        print("Controle e Regulamentação:", percentual_regulamentacao)
        print("Potencial Desenvolvimento de IA Superinteligente:", percentual_potencial)
        input('ENTER para continuar...')
    else:
        print("Não há dados disponíveis para o estado informado.")



while True:
  escolha = menu()
  print('\n'*2)
  if escolha == 0:
    break
  if escolha == 1:
    print('\n'*2)
    votar()
    print('\n'*2)
  if escolha == 2:
    print('\n'*2)
    relatorio()
    print('\n'*2)
    pass
