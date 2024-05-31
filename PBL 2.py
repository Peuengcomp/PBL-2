'''
Autor: Pedro Lucas Fernandes de Souza
Componente Curricular: Algoritmos I
Concluido em: 30/05/2024

Declaro que este código foi elaborado por mim de forma individual e não contém nenhum trecho de código de outro colega ou de outro autor, 
tais como provindos de livros e apostilas, e páginas ou documentos eletrônicos da Internet. 
Qualquer trecho de código de outra autoria que não a minha está destacado com uma citação para o autor e a fonte do código, 
tais como provindos de livros e apostilas, e páginas ou documentos eletrônicos da Internet. 
Qualquer trecho de código de outra autoria que não a minha está destacado com uma citação para o autor e a fonte do código, 
e estou ciente que estes trechos não serão considerados para fins de avaliação.
'''

# A primeira parte do código consiste em importar as bibliotecas necessárias para programar: uma para ler e modificar o arquivo csv
# outra para implementar as dadas

import csv
from datetime import datetime, timedelta


# Este bloco de funções é responsável por ler o arquivo csv e retornar o conjunto de listas e o cabeçalho

# Retorna o conjunto de listas, conforme o ITEM 2 do problema
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
# como números negativos e excedentes de casos em relação aos dados possíveis. Esta funções satisfaz os ITENS 4 e 5 do problema
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

# Esta função é responsável por reescrever o conjunto de listas, isto é, os dados de volta ao arquivo csv, para ser lido depois, conforme o ITEM 9
def atualizar_csv(novos_dados):
    with open('entrada.csv', 'w', newline='') as entrada:
        implantar = csv.writer(entrada)
        implantar.writerows(novos_dados)
    return None


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
    data = "{:02d}/{:02d}/{:04d}".format(dia, mes, ano)
    data_validar = datetime.strptime(data, '%d/%m/%Y')
    matriz_primeira_data = datetime.strptime(matriz_de_dados()[1][0], '%d/%m/%Y')
    matriz_ultima_data = datetime.strptime(matriz_de_dados()[-1][0], '%d/%m/%Y')
    while data_validar < matriz_primeira_data or data_validar > matriz_ultima_data:
        print("Digite valores válidos para a data\n")
        dia = int(input("Digite o dia:\n"))
        mes = int(input("Digite o mês:\n"))
        ano = int(input("Digite o ano:\n"))
        data = "{:02d}/{:02d}/{:04d}".format(dia, mes, ano)
        data_validar = datetime.strptime(data, '%d/%m/%Y')
    return data

# Este bloco de funções são responsáveis por tratar os dados para cada tipo de busca feita

# Esta função calcula a porcentagem de casos suspeitos e positivos por bairro em relação à sua população conforme ITEM 6 do problema
def tratar_dado_data_bairro(matriz):
    matriz.pop(0)
    suspeitos = int(matriz[0][3])
    positivos = int(matriz[0][5])
    habitantes = int(matriz[0][2])
    percentual_suspeitos = round((suspeitos/habitantes)*100, 2)
    percentual_positivos = round((positivos/habitantes)*100, 2)
    print(f"para a data {matriz[0][0]}, estes são os dados do bairro {matriz[0][1]}:\n")
    print(f"Total de habitantes do bairro é: {habitantes}\n"
          f"Porcentagem de casos suspeitos: {percentual_suspeitos}%\n"
          f"Porcentagem de casos positivos: {percentual_positivos}%\n")
    return None

# Esta função é responsável por calcular valores totais e seus percentuais em uma data específica, podendo ser a última data, conforme o ITEM 7 do problema
def tratar_dado_data(data, matriz):
    matriz.pop(0)
    soma_habitantes = 0
    soma_casos_suspeitos = 0
    soma_casos_negativos = 0
    soma_casos_positivos = 0
    for dados in matriz:
        soma_habitantes += int(dados[2])
        soma_casos_suspeitos += int(dados[3])
        soma_casos_negativos += int(dados[4])
        soma_casos_positivos += int(dados[5])
    casos_notificados = soma_casos_suspeitos + soma_casos_negativos + soma_casos_positivos
    percentual_suspeitos = round((soma_casos_suspeitos/casos_notificados)*100, 2)
    percentual_negativos = round((soma_casos_negativos/casos_notificados)*100, 2)
    percentual_positivos = round((soma_casos_positivos/casos_notificados)*100, 2)
    print(f"Para a data {data} estes são os dados:\n")
    print(f"Total de habitantes cadastrados: {soma_habitantes}\n"
          f"Total de casos suspeitos: {soma_casos_suspeitos}\n"
          f"Total de casos negativos: {soma_casos_negativos}\n"
          f"Total de casos positivos: {soma_casos_positivos}\n"
          f"Total de casos notificados: {casos_notificados}")
    print("\n")
    print(f"Os dados percentuais são:\n"
          f"Percentual de suspeitos: {percentual_suspeitos}%\n"
          f"Percentual de negativos: {percentual_negativos}%\n"
          f"Percentual de positivos: {percentual_positivos}%\n")
    return None

# Esta função retorna os valores de casos positivos e negativos, calcula a diferença entre as datas conforme o ITEM 2 do problema
def tratar_dado_intervalo_data(data1, data2, matriz):
    matriz.pop(0)
    soma_casos_positivos_data1 = 0
    soma_casos_negativos_data1 = 0
    soma_casos_positivos_data2 = 0
    soma_casos_negativos_data2 = 0
    for dados in matriz:
        if data1 == dados[0]:
            soma_casos_negativos_data1 += int(dados[4])
            soma_casos_positivos_data1 += int(dados[5])
        elif data2 == dados[0]:
            soma_casos_negativos_data2 += int(dados[4])
            soma_casos_positivos_data2 += int(dados[5])
    # Este cálculo indicará a diferença, em números absolutos, e o percentual desses valores

    diferenca_total_negativos = (soma_casos_negativos_data2 - soma_casos_negativos_data1)
    diferenca_total_positivos = (soma_casos_positivos_data2 - soma_casos_positivos_data1)
    percebtual_negativos = round((diferenca_total_negativos/soma_casos_negativos_data1)*100,2)
    percebtual_positivos = round((diferenca_total_positivos/soma_casos_positivos_data1)*100,2)

    print(f"Para a data {data1}, estes são os dados:\n")
    print(f"Total de casos negativos: {soma_casos_negativos_data1}\n"
          f"Total de casos positivos: {soma_casos_positivos_data1}\n")
    print(f"Para a data {data2}, estes são os dados:\n")
    print(f"Total de casos negativos: {soma_casos_negativos_data2}\n"
          f"Total de casos positivos: {soma_casos_positivos_data2}\n")
    if (soma_casos_negativos_data1 + soma_casos_positivos_data1 == 0) or (soma_casos_negativos_data2 + soma_casos_positivos_data2 == 0):
        print("""Os dados percentuais não podem ser computados, pois os valores de uma das datas é nulo.
              Isso pode indicar que uma das datas não está na base de dados\n""")
    else:
        print(f"""Para casos negativos, teve uma diferença de {abs(diferenca_total_negativos)} casos em números absolutos entre as datas, 
            tendo {percebtual_negativos}% de alteração entre elas\n"""
            f"""Para casos positivos, teve uma diferença de {abs(diferenca_total_positivos)} casos em núemeros absolutos entre as datas, 
            tendo {percebtual_positivos}% de alteração entre elas\n""")
    return None

# Esta função calcula e retorna a quantidade e percentual de casos suspeitos, negativos e positivos em relação ao total de casos notificados
# Aqui interpretados como a soma de casos suspeitos, negativos e positivos em toda matriz de dados

# Este bloco de funções é responsável por retornar dados para serem computados e impressos aos usuários

# Esta função retorna o bairro para uma data esepecífica
def buscar_bairro_data(data, bairro):
    dados = []
    dados.append(cabecalho())
    for lista in matriz_de_dados():
        if lista[0] == data and lista[1] == bairro:
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
# Esta função retorna os dados de datas iniciais e finais para todos os bairros
def buscar_intervalo_datas(data1, data2):
    dados = []
    dados.append(cabecalho())
    for lista in matriz_de_dados():
        if lista[0] == data1 or lista[0] == data2:
            dados.append(lista)
    return dados

# Esta função exibe o menu e retorna a opção escolhida
def opcao_busca():
    print("[1] - Buscar para um único bairro em data específica\n")
    print("[2] - Buscar para uma única data\n")
    print("[3] - Buscar para intervalo entre datas\n")
    opcao = int(input())
    return opcao


# O bloco de funções abaixo são caracterizados por serem responsáveis pelo layout do software


# Função para visualizar os dados em forma de tabela
def visualizar(matriz):
    for linha in matriz:
        print(f"{linha[0]:^16} \t {linha[1]:^16} \t {linha[2]:^16} \t {linha[3]:^16} \t {linha[4]:^16} \t {linha[5]:^16}")
    return None

# Função para sair ou realizar back
def sair():
    back = 0
    while back != 1:
        back = (int(input("Digite 1 para sair\n")))
    return None

# Função para mostrar um menu conforme o ITEM 1 do problema
def exibir_menu():
    print("Bem vindo ao menu de sistemas de dengue\n")
    print("[1] - Informações sobre a Dengue\n")
    print("[2] - Acessar o relatório\n")
    print("[3] - Sair do Sistema\n") 
    print("Selecione sua opção:")
    entrada = int(input())
    return entrada

# Função para mostrar um menu
def msg():
    print("[1] - Visualizar relatório\n")
    print("[2] - Modificar relatório\n")
    print("[3] - Buscar informações no relatório\n") 
    opcao = int(input())
    return opcao

# FUnção para mostrar informações sobre a dengue
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
        sair()
    elif escolha == 2:
        opcao = msg()
        if opcao == 1:
            visualizar(matriz_de_dados())
            sair()
        elif opcao == 2:
            atualizar_csv(modificar_dados(matriz_de_dados()))
        elif opcao == 3:
            opcao_buscar = opcao_busca()
            if opcao_buscar == 1:
                data = validar_implementar_data()
                bairro = codex(matriz_de_dados())
                dado = buscar_bairro_data(data, bairro)
                visualizar(dado)
                tratar_dado_data_bairro(dado)
                sair()
            elif opcao_buscar == 2:
                data = validar_implementar_data()
                dado = buscar_data(data)
                visualizar(dado)
                tratar_dado_data(data, dado)
                sair()
            elif opcao_buscar == 3:
                print("Digite a primeira data:\n")
                data1 = validar_implementar_data()
                print("Digite a segunda data:\n")
                data2 = validar_implementar_data()
                while data1 == data2:
                    print("Digite datas diferentes\n")
                    print("Digite a primeira data:\n")
                    data1 = validar_implementar_data()
                    print("Digite a segunda data:\n")
                    data2 = validar_implementar_data()
                dado = buscar_intervalo_datas(data1, data2)
                visualizar(dado)
                tratar_dado_intervalo_data(data1, data2, dado)
                sair()
        else:
            print("Número inválido\n")
    elif escolha == 3:
        inicializador = False
    else:
        print("Digite valores válidos:\n")
