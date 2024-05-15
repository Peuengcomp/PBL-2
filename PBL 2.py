import csv
from datetime import datetime, timedelta

def matriz_de_dados():
    with open ('entrada.csv', 'r') as leitura:
        leitor = csv.reader(leitura)
        dados = []
        for linha in leitor:
            dados.append(linha)
        return dados
    
def ultima_data(data):
    last = data[-1][0]
    last_time = datetime.strptime(last, "%d/%m/%Y")
    new = last_time + timedelta(days=1)
    new_data = new.strftime("%d/%m/%Y")
    return new_data
    
def modificar_dados(matriz):
    hoje = ultima_data(matriz)
    new_data = []
    for elemento in range(1, 26):
        print("Para o Bairro %s" % matriz[-elemento][1])
        novos_casos_positivos_aux = int(input("Digite a quantidade de novos casos positivados\n"))
        novos_casos_negativos_aux = int(input("Digite a quantidade de novos casos negativados\n"))
        novos_casos_suspeitos_aux = int(input("Digite a quantidade de casos suspeitos\n"))
        soma_aux = novos_casos_positivos_aux + novos_casos_negativos_aux
        while soma_aux > int(matriz[-elemento][3]):
            print("Há apenas %s casos suspeitos, não pode haver excedente de novos positivos e negativos\n" % matriz[-elemento][3])
            print("Para o Bairro %s, digite valores válidos:\n" % matriz[-elemento][1])
            novos_casos_positivos_aux = int(input("Digite a quantidade de novos casos positivados\n"))
            novos_casos_negativos_aux = int(input("Digite a quantidade de novos casos negativados\n"))
            soma_aux = novos_casos_positivos_aux + novos_casos_negativos_aux
        novos_casos_positivos = str(int(matriz[-elemento][4]) + novos_casos_positivos_aux)
        novos_casos_negativos = str(int(matriz[-elemento][5]) + novos_casos_negativos_aux)
        novos_casos_suspeitos = str(int(matriz[-elemento][3]) - soma_aux + novos_casos_suspeitos_aux)
        insert_dados = []
        insert_dados.append(hoje)
        insert_dados.append(matriz[-elemento][1])
        insert_dados.append(matriz[-elemento][2])
        insert_dados.append(novos_casos_suspeitos)
        insert_dados.append(novos_casos_positivos)
        insert_dados.append(novos_casos_negativos)
        new_data.append(insert_dados)
    new_data.reverse()
    for elemento in new_data:
        matriz.append(elemento)
    return matriz

def atualizar_csv(novos_dados):
    with open('entrada.csv', 'w', newline='') as entrada:
        implantar = csv.writer(entrada)
        implantar.writerows(novos_dados)

# O bloco de funções abaixo são caracterizados por serem responsáveis pelo layout do software

def visualizar():
    with open('entrada.csv','r') as entrada:
        view = csv.reader(entrada)
        for linha in view:
                print("|".join(f"{campo:^18}" for campo in linha))
        sair = int(input(("Digite 1 para sair\n")))
        while sair != 1:
           sair = int(input(("Digite 1 para sair\n")))

def exibir_menu():
    print("Bem vindo ao menu de sistemas de dengue\n")
    print("[1] - Informações sobre a Dengue\n")
    print("[2] - Acessar o relatório\n")
    print("[3] - Sair do Sistema") 
    print("Selecione sua opção:")
    entrada = int(input())
    return entrada

def menu():
    inicializador = True
    while inicializador:
        escolha = exibir_menu()
        if escolha == 1:
            print("A dengue é uma doença viral transmitida pelo mosquito Aedes aegypti,\n")
            print("com cerca de 50 a 100 milhões de casos ocorrendo anualmente,\n")
            print("de acordo com a Organização Mundial da Saúde (OMS).\n")
            print("Os sintomas da dengue são:\n1 - febre alta\n2 - dor de cabeça intensa\n3 - dor atrás dos olhos\n4 - dores musculares e articulares\n5 - náuseas e vômitos\n6 - erupções cutâneas\n")
            print("A doença muitas vezes pode ser fatal\n")
            sair = int(input(("Digite 1 para sair\n")))
            while sair != 1:
               sair = int(input(("Digite 1 para sair\n")))
        elif escolha == 2:
            opcao = int(input("Deseja visualizar, modificar ou buscar informações no relatório? Digite 1 para visualizar; 2 para modificar; 3 para buscar\n"))
            if opcao == 1:
                visualizar()
            elif opcao == 2:
                atualizar_csv(modificar_dados(matriz_de_dados()))
            elif opcao == 3:
                print("buscar")
        elif escolha == 3:
            inicializador = False

menu()
