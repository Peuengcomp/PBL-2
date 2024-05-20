# A primeira parte do código consiste em importar as bibliotecas necessárias para programar: uma para ler e modificar o arquivo csv
# outra para implementar as dadas

import csv
from datetime import datetime, timedelta

# Este bloco de funções é responsável por ler o arquivo csv e retornar o conjunto de listas e o cabeçalho

# Retorna o conjunto de listas
def matriz_de_dados():
    with open ('entrada.csv', 'r') as entrada:
        leitor = csv.reader(entrada)
        dados = []
        for linha in leitor:
            dados.append(linha)
        return dados
# Retorna o cabeçalho
def cabecalho():
    head = matriz_de_dados()[0]
    return head


# Este bloco de funções é responsável exclusivamente pelo incremento de novos dados

# Esta função é responsável por ler a última data e incrementar o dia seguinte para ser implementada juntamente aos novos dados
def ultima_data(data):
    recente = data[-1][0]
    data_recente = datetime.strptime(recente, "%d/%m/%Y")
    nova = data_recente + timedelta(days=1)
    nova_data = nova.strftime("%d/%m/%Y")
    return nova_data
# Esta função é responsável por incrementar os novos dados; ela também valida os dados anteriores para evitar incoerẽncia de resultados,
# como números negativos e excedentes de casos em relação aos dados possíveis
def modificar_dados(matriz):
    hoje = ultima_data(matriz)
    novos_dados = []
    for lista in range(1, 26):
        print("Para o Bairro %s" % matriz[-lista][1])
        novos_casos_positivos_aux = int(input("Digite a quantidade de novos casos positivados\n"))
        novos_casos_negativos_aux = int(input("Digite a quantidade de novos casos negativados\n"))
        novos_casos_suspeitos_aux = int(input("Digite a quantidade de novos casos suspeitos\n"))
        novos_casos_positivos = int(matriz[-lista][4]) + novos_casos_positivos_aux
        novos_casos_negativos = int(matriz[-lista][5]) + novos_casos_negativos_aux
        novos_casos_suspeitos = int(matriz[-lista][3]) + novos_casos_suspeitos_aux - (novos_casos_positivos_aux + novos_casos_negativos_aux)
        soma_aux1 = novos_casos_positivos_aux + novos_casos_negativos_aux
        soma_aux2 = novos_casos_positivos + novos_casos_negativos + novos_casos_suspeitos
        while soma_aux1 > int(matriz[-lista][3]) or soma_aux2 > int(matriz[-lista][2]):
            print("Há apenas %s habitantes, não pode haver excedente nos novos dados" % matriz[-lista][2])
            print("Há apenas %s casos suspeitos no bairro, não pode haver excedente de novos positivos e negativos\n" % matriz[-lista][3])
            print("Para o bairro %s, digite valores válidos:\n" % matriz[-lista][1])
            novos_casos_positivos_aux = int(input("Digite a quantidade de novos casos positivados\n"))
            novos_casos_negativos_aux = int(input("Digite a quantidade de novos casos negativados\n"))
            novos_casos_suspeitos_aux = int(input("Digite a quantidade de novos casos suspeitos\n"))
            novos_casos_positivos = int(matriz[-lista][4]) + novos_casos_positivos_aux
            novos_casos_negativos = int(matriz[-lista][5]) + novos_casos_negativos_aux
            novos_casos_suspeitos = int(matriz[-lista][3]) + novos_casos_suspeitos_aux - (novos_casos_positivos_aux + novos_casos_negativos_aux)
            soma_aux1 = novos_casos_positivos_aux + novos_casos_negativos_aux
            soma_aux2 = novos_casos_positivos + novos_casos_negativos + novos_casos_suspeitos
        insert_dados = []
        insert_dados.append(hoje)
        insert_dados.append(matriz[-lista][1])
        insert_dados.append(matriz[-lista][2])
        insert_dados.append(str(novos_casos_suspeitos))
        insert_dados.append(str(novos_casos_positivos))
        insert_dados.append(str(novos_casos_negativos))
        novos_dados.append(insert_dados)
    novos_dados.reverse()
    for lista in novos_dados:
        matriz.append(lista)
    return matriz
# Esta função é responsável por reescrever o conjunto de listas, isto é, os dados de volta ao arquivo csv, para ser lido depois
def atualizar_csv(novos_dados):
    with open('entrada.csv', 'w', newline='') as entrada:
        implantar = csv.writer(entrada)
        implantar.writerows(novos_dados)


# Bloco exclusivo para funções de busca de dados solicitados pelo usuário

# Esta função é responsável por criar um dicionário que relaciona um número a um bairro,
# o valor retornado é o código referente ao bairro de escolha do usuário
def codex(matriz):
    code_dict = {}
    for item in range(1,26):
        print("%d - %s\n" % (item, matriz[item][1]))
    for bairro in range(1,26):
        code_dict[bairro] = matriz[bairro][1]
    code = int(input("Digite o código do bairro\n"))
    while code < 1 or code > 25:
        print("Digite valores válidos\n")
        code = int(input("Digite o código do bairro\n"))
    return code_dict[code]
# Esta função é responsável por solicitar e validar a data inserida pelo usuário
def validar_implementar_data():
    dia = int(input("Digite o dia:\n"))
    mes = int(input("Digite o mês:\n"))
    ano = int(input("Digite o ano:\n"))
    while (dia < 1 or dia > 31) or (mes < 1 or mes > 12):
        print("Digite valores válidos\n")
        dia = int(input("Digite o dia:\n"))
        mes = int(input("Digite o mês:\n"))
        ano = int(input("Digite o ano:\n"))
    data = "{:02d}/{:02d}/{:04d}".format(dia, mes, ano)
    return data
# Esta função calcula a porcentagem de casos suspeitos, negativos e positivos por bairro
def tratar_dado(lista):
    percentil_casos_suspeitos = str(round(int(lista[3])/int(lista[2])*100, 2)) + "%"
    percentil_casos_negativos = str(round(int(lista[4])/int(lista[2])*100, 2)) + "%"
    percentil_casos_positivos = str(round(int(lista[5])/int(lista[2])*100, 2)) + "%"
    imprimir = print("Percentual de casos suspeitos é: %s\n"
                    "Percentual de casos negativos é: %s\n" 
                    "Percentual de casos positivos é: %s\n" % (percentil_casos_suspeitos, percentil_casos_negativos, percentil_casos_positivos))
    return None
# Esta função retorna o bairro em todas as datas
def buscar_bairro(bairro):
    dados = []
    dados.append(cabecalho())
    for lista in matriz_de_dados():
        if lista[1] == bairro:
            dados.append(lista)
    return dados
# Esta função retorna a data inserida para todos os bairros
def buscar_data(data):
    dados = []
    dados.append(cabecalho())
    for lista in matriz_de_dados():
        if lista[0] == data:
            dados.append(lista)
    return dados
# Esta função retorna os dados referentes a um bairro em determinada data
def buscar_bairro_data(data, bairro):
    dados = []
    dados.append(cabecalho())
    for lista in matriz_de_dados():
        if lista[0] == data and lista[1] == bairro:
            dados.append(lista)
    return dados
# Esta função retorna os dados de datas iniciais e finais para todos os bairros
def buscar_intervalo_datas(data1, data2):
    dados = []
    dados.append(cabecalho())
    for lista in matriz_de_dados():
        if lista[0] == data1 or lista[0] == data2:
            dados.append(lista)
    return dados
def buscar_intervalo_datas_bairro(data1, data2, bairro):
    dados = []
    dados.append(cabecalho())
    for lista in matriz_de_dados():
        if (lista[0] == data1 or lista[0] == data2) and lista[1] == bairro:
            dados.append(lista)
    return dados
# Esta função exibe o menu e retorna a opção escolhida
def opcao_busca():
    print("[1] - Buscar para um único bairro\n")
    print("[2] - Buscar para uma única data\n")
    print("[3] - Buscar para data e bairro\n")
    print("[4] - Buscar para intervalo entre datas\n")
    print("[5] - Buscar intervalo entre datas para um único bairro\n")
    opcao = int(input())
    return opcao

# O bloco de funções abaixo são caracterizados por serem responsáveis pelo layout do software

def visualizar(matriz):
    for linha in matriz:
        print("|".join(f"{campo:^18}" for campo in linha))
    return None

def exibir_menu():
    print("Bem vindo ao menu de sistemas de dengue\n")
    print("[1] - Informações sobre a Dengue\n")
    print("[2] - Acessar o relatório\n")
    print("[3] - Sair do Sistema\n") 
    print("Selecione sua opção:")
    entrada = int(input())
    return entrada

def msg():
    print("[1] - Visualizar relatório\n")
    print("[2] - Modificar relatório\n")
    print("[3] - Buscar informações no relatório\n") 
    opcao = int(input())
    return opcao

def info():
    print("""A dengue é uma doença viral transmitida pelo mosquito Aedes aegypti,
com cerca de 50 a 100 milhões de casos ocorrendo anualmente,
de acordo com a Organização Mundial da Saúde (OMS).
Os sintomas da dengue são:
1 - febre alta
2 - dor de cabeça intensa
3 - dor atrás dos olhos
4 - dores musculares e articulares
5 - náuseas e vômitos
6 - erupções cutâneas
A doença muitas vezes pode ser fatal\n
para mais informações, pode-se acessar o seguinte site:\n
https://www.gov.br/saude/pt-br/assuntos/saude-de-a-a-z/d/dengue\n""")

# Programa principal

inicializador = True
while inicializador:
    escolha = exibir_menu()
    if escolha == 1:
        info()
    elif escolha == 2:
        opcao = msg()
        if opcao == 1:
            visualizar(matriz_de_dados())
        elif opcao == 2:
            atualizar_csv(modificar_dados(matriz_de_dados()))
        elif opcao == 3:
            opcao_buscar = opcao_busca()
            if opcao_buscar == 1:
                bairro = codex(matriz_de_dados())
                dado = buscar_bairro(bairro)
                visualizar(dado)
            elif opcao_buscar == 2:
                data = validar_implementar_data()
                dado = buscar_data(data)
                visualizar(dado)
            elif opcao_buscar == 3:
                data = validar_implementar_data()
                bairro = codex(matriz_de_dados())
                dado = buscar_bairro_data(data, bairro)
                visualizar(dado)
                tratar_dado(dado[1])
            elif opcao_buscar == 4:
                print("Digite a primeira data:\n")
                data1 = validar_implementar_data()
                print("Digite a segunda data\n:")
                data2 = validar_implementar_data()
                dado = buscar_intervalo_datas(data1, data2)
                visualizar(dado)
            elif opcao_buscar == 5:
                print("Digite a primeira data:\n")
                data1 = validar_implementar_data()
                print("Digite a segunda data\n:")
                data2 = validar_implementar_data()
                bairro = codex(matriz_de_dados())
                dado = buscar_intervalo_datas_bairro(data1, data2, bairro)
                visualizar(dado)
        else:
            print("Número inválido\n")
    elif escolha == 3:
        inicializador = False
    else:
        print("Digite valores válidos\n")
