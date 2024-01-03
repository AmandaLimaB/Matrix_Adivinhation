# /*******************************************************************************
# Autor: Amanda Lima Bezerra
# Componente Curricular: MI - Algoritmos I
# Concluido em: 20/05/2022
# Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
# trecho de código de outro colega ou de outro autor, tais como provindos de livros e
# apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
# de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
# do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
# ******************************************************************************************/

# Professora, alguns comentários nesse PBL foram para eu mesma não me perder dentro do meu código. Então se achar muitos comentários 
# repetidos saiba que foram para me orientar kkkkkkk.

# Biblioteca responsável pela geração de números aleatórios.
import random

# Biblioteca responsável pela cópia profunda da matriz/tabuleiro das respostas do jogo e do dicionário do histórico das jogadas. 
# A importância dessa biblioteca é duplicar algumas estruturas e alterar suas cópias sem afetar a estrutura original. 
import copy

# Função responsável pela entrada de dados do jogo.
def menu():
    print('\t\tJOGO DA SOMA\nInicio')
    nome_1 = input('Nome do jogador 1 -----> ')
    nome_2 = input('Nome do jogador 2 -----> ')
    nome_1, nome_2 = validacao_nomes(nome_1, nome_2)
    
    quant_tabuleiro = input('Quantidade de tabuleiros: \n1. Um tabuleiro\n2. Dois tabuleiros\n-----> ')
    quant_tabuleiro = validacao_1(quant_tabuleiro)
    
    nivel = input('Nível do jogo: \n1. Fácil\n2. Médio\n3. Difícil\n-----> ')
    nivel = validacao_2(nivel)

    # Coletando as informações sobre o tamanho do tabuleiro.
    linhas, colunas, limite, quant_numeros = tamanho_tabuleiro(nivel)
    
    termino = input('Encerramento da partida\n1. Número de rodadas\n2. Tabuleiro completamente revelado\n-----> ')
    termino = validacao_1(termino)
    if termino == 1:
        rodadas = input('Qual o números de rodadas?\n-----> ')
        rodadas = validacao_3(rodadas)
        # Nessa parte do código será chamada as funções de cada tipo de jogo. Foi dividido desse jeito pois ficou mais fácil a organização
        # do código.
        if quant_tabuleiro == 1:
            tabuleiro1_rodadas(nome_1, nome_2, quant_tabuleiro, linhas, colunas, limite, quant_numeros, rodadas)
        else:
            tabuleiro2_rodadas(nome_1, nome_2, quant_tabuleiro, linhas, colunas, limite, quant_numeros, rodadas)
    else:
        # Nessa parte do código será chamada as funções de cada tipo de jogo.
        if quant_tabuleiro == 1:
            tabuleiro1_rodadas0(nome_1, nome_2, quant_tabuleiro, linhas, colunas, limite, quant_numeros)
        else:
            tabuleiro2_rodadas0(nome_1, nome_2, quant_tabuleiro, linhas, colunas, limite, quant_numeros)

# Função que determina o tamanho do tabuleiro.
# Em todos os casos o tabuleiro terá duas linhas e 
# colunas a mais para armazenar o resultado da soma.

# Fácil = 3x3
# Médio 4x4
# Díficil 5x5

# O limite é para definir o intervalo dos números aleatórios e 
# a quant_numeros é para definir quantos números aleatórios irá precisar.
def tamanho_tabuleiro(nivel):
    if nivel == 1:
        linhas = 5
        colunas = 5
        limite = 30
        quant_numeros = 9
    elif nivel == 2:
        linhas = 6
        colunas = 6
        limite = 60
        quant_numeros = 16
    else:
        linhas = 7
        colunas = 7
        limite = 100
        quant_numeros = 25
    return linhas, colunas, limite, quant_numeros

# Função que organiza a criação do/dos tabuleiro(s) do jogo.
def montando_tabuleiro(linhas, colunas, limite, quant_numeros):
    tabuleiro_vazio = criar_matriz(linhas, colunas)
    tabuleiro = montar_tabuleiro(tabuleiro_vazio, linhas, colunas)
    # Cópia profunda do tabuleiro pois eu tenho que alterar o tabuleiro
    # resposta ao longo do jogo sem que o tabuleiro seja alterado.
    copia = copy.deepcopy(tabuleiro)
    tabuleiro_resp = colocar_numeros(copia, limite, quant_numeros, linhas, colunas)    
    return tabuleiro, tabuleiro_resp 

# Funções que montam o/os tabuleiro(s).
def criar_matriz(linhas, colunas):
    return [ [0 for j in range(colunas)] for i in range(linhas) ]

def montar_tabuleiro(tabuleiro, linhas, colunas):
    for i in range(linhas):
        for j in range(colunas):
            # Os elementos que não serão usados no jogo estarão o tempo todo com 0.
            if (i == 0 or i == colunas - 1) and (j == 0 or j == colunas - 1):
                tabuleiro[i][j] = 0
            # As colunas estão devidamente identificadas
            elif i == 0 and j != 0 and j != colunas - 1:
                tabuleiro[0][j] = ('C',j)
            # As linhas estão devidamente identificadas
            elif i != 0 and i != colunas - 1 and j == 0:
                tabuleiro[i][0] = ('L',i)
            # O restante das células estão com a sigla J.S., ou seja, jogo da soma
            else:
                tabuleiro[i][j] = 'J.S.'               
                
    return tabuleiro

def colocar_numeros(tabuleiro_resp, limite, quant_numeros, linhas, colunas):
    lista_aleatorios = random.sample(range(1, limite + 1), quant_numeros)
    # Contador para colocar cada elemento da lista_aleatorios no tabuleiro.
    contador = 0 
    for num_linha in range(linhas):
        for num_coluna in range(colunas):
            if num_linha != 0 and num_linha != colunas - 1 and num_coluna != 0 and num_coluna != colunas - 1:
                tabuleiro_resp[num_linha][num_coluna] = lista_aleatorios[contador]
                contador += 1
    # Fazendo o looping para a soma das linhas
    for num_linha in range(linhas):
        soma = 0
        for num_coluna in range(colunas):
            if num_linha != 0 and num_coluna != 0 and num_linha != linhas - 1 and num_coluna != colunas - 1:
                soma += tabuleiro_resp[num_linha][num_coluna]
        tabuleiro_resp[num_linha][colunas - 1] = soma
    # Fazendo o looping para a soma das colunas
    for num_linha in range(linhas):
        soma = 0
        for num_coluna in range(colunas):
            if num_linha != 0 and num_coluna != 0 and num_linha != linhas - 1 and num_coluna != colunas - 1:
                soma += tabuleiro_resp[num_coluna][num_linha]
        tabuleiro_resp[colunas - 1][num_linha] = soma

    return tabuleiro_resp

def mostrar_matriz(matriz, linhas, colunas):
    for num_linha in range(linhas):
        for num_coluna in range(colunas):
            # Parte responsável pela primeira linhas.
            if num_linha == 0:
                # Primeiro 0 da matriz
                if num_coluna == 0:
                    print(matriz[num_linha][num_coluna], end = '')
                # Último 0 da matriz
                elif num_coluna == colunas - 1:
                    print('\t',matriz[num_linha][num_coluna])
                else:
                    # Parte responsável por mostrar as indicações das colunas
                    print('\t',*matriz[num_linha][num_coluna], end = '')
            
            # Parte responsável pelas linhas intermediárias
            elif num_linha != 0 and num_linha != colunas - 1:
                # Primeira coluna responsável pela indicação das linhas
                if num_coluna == 0:
                    print(*matriz[num_linha][num_coluna], end = '')
                # ÚLtima coluna
                elif num_coluna == colunas - 1:
                    print('\t',matriz[num_linha][num_coluna])
                # Partes intermediarias
                else:
                    print('\t',matriz[num_linha][num_coluna], end = '')
            # Última linha
            else:
                # Primeiro 0 da última linha
                if num_coluna == 0:
                    print(matriz[num_linha][num_coluna], end = '')
                # Último 0 da última linha
                elif num_coluna == colunas - 1:
                    print('\t',matriz[num_linha][num_coluna])
                else:
                    print('\t',matriz[num_linha][num_coluna], end = '')
    print('\n')

# Funções para cada tipo de jogo. 
# Como é basicamente a mesma jogabilidade a estrutura é a mesma, são poucas as diferenças.  
def tabuleiro1_rodadas0(nome_1, nome_2, quant_tabuleiro, linhas, colunas, limite, quant_numeros):
    tabuleiro, tabuleiro_resp = montando_tabuleiro(linhas, colunas, limite, quant_numeros)
    mostrar_matriz(tabuleiro, linhas, colunas)
    iniciador = True
    # Variáveis vazias para acumular a pontuação e o histórico.
    historico1 = []
    historico2 = []
    pontuacao1 = 0
    pontuacao2 = 0
    while iniciador:
        # Variável auxiliar para parar o loop assim que o tabuleiro estiver completo usando uma verificação se ainda existem células
        # na matriz que estão com a sigla J.S. 
        aux = 0
        for linha in range(linhas):
            for coluna in range(colunas):
                if tabuleiro[linha][coluna] == 'J.S.':
                    aux += 1
                    dicionario_jogadas = escolher_jogadas(nome_1, nome_2, linhas)
                    # Estrutura do dicionario_jogadas: Nome: [indicação da linha/coluna, valor chutado]                    
                    soma1, soma2 = achar_soma(tabuleiro_resp, dicionario_jogadas, nome_1, nome_2, linhas, colunas)
                    # Estrutura do dicionario_comparacao: Nome: [posição, valor chutado, maior/menor/acertou]
                    dicionario_jogadas = comparar(nome_1, nome_2, soma1, soma2, dicionario_jogadas)
                    pontuacao1, pontuacao2, lista_ganhador = ganhador(dicionario_jogadas, nome_1, nome_2, soma1, soma2, pontuacao1, pontuacao2)
                    mostrar_vencedor(lista_ganhador)
                    print('Pontuação jogador {}: {} ponto(s)\nPontuação jogador {}: {} ponto(s)\n'.format(nome_1, pontuacao1, nome_2, pontuacao2))
                    # Cópia profunda das jogadas para colocar no histórico.
                    copia_historico = copy.deepcopy(dicionario_jogadas)
                    historico1, historico2 = historico(copia_historico, nome_1, nome_2, historico1, historico2)
                    mostrar_historico(nome_1, nome_2, historico1, historico2)
                    dicionario_revelacao = achar_posicao(lista_ganhador, dicionario_jogadas, tabuleiro_resp, linhas, colunas)
                    tabuleiro, tabuleiro_resp = trocar_numeros(dicionario_revelacao, tabuleiro, tabuleiro_resp, linhas, colunas)
                    mostrar_matriz(tabuleiro, linhas, colunas) 
        # Quebra do loop.
        if aux == 0:
            iniciador = False
    # Apresentando o vencendor.
    if pontuacao1 > pontuacao2:
        print('O vencendor foi o jogador {}\n'.format(nome_1))
    elif pontuacao2 > pontuacao1:
        print('O vencendor foi o jogador {}\n'.format(nome_2))
    else:
        print('Os vencedores foram os jogadores {} e {}\n'.format(nome_1, nome_2))
    print('Parabéns, o agente Smith foi derrotado!\nAutora: Amanda Lima Bezerra')

def tabuleiro2_rodadas0(nome_1, nome_2, quant_tabuleiro, linhas, colunas, limite, quant_numeros):
    # Como esse modo de jogo tem dois tabuleiros a função de criar o tabuleiro é chamada duas vezes.
    tabuleiro1, tabuleiro_resp1 = montando_tabuleiro(linhas, colunas, limite, quant_numeros)
    tabuleiro2, tabuleiro_resp2 = montando_tabuleiro(linhas, colunas, limite, quant_numeros)
    print('Tabuleiro do jogador {}'.format(nome_1))
    mostrar_matriz(tabuleiro1, linhas, colunas)
    print('Tabuleiro do jogador {}'.format(nome_2))
    mostrar_matriz(tabuleiro2, linhas, colunas)
    iniciador = True
    historico1 = []
    historico2 = []
    pontuacao1 = 0
    pontuacao2 = 0
    # A estrutura para o loop foi a mesma usada para o modo do jogo com somente um único tabuleiro e sem o número de rodadas definida.
    while iniciador:
        aux = 0
        for linha in range(linhas):
            for coluna in range(colunas):
                if tabuleiro1[linha][coluna] == 'J.S.' and tabuleiro2[linha][coluna] == 'J.S.':
                    aux += 1
                    dicionario_jogadas = escolher_jogadas(nome_1, nome_2, linhas)
                    # Estrutura do dicionario_jogadas = Nome: [indicaçao linha/coluna, valor chutado]
                    # Função de achar a soma é a única que foi diferente entre os jogos com 1 ou 2 tabuleiros.
                    soma1, soma2 = achar_soma2(tabuleiro_resp1, tabuleiro_resp2, dicionario_jogadas, nome_1, nome_2, linhas, colunas)
                    # Estrutura do dicionario_jogadas = Nome: [indicaçao linha/coluna, valor chutado]
                    dicionario_jogadas = comparar(nome_1, nome_2, soma1, soma2, dicionario_jogadas)
                    pontuacao1, pontuacao2, lista_ganhador = ganhador(dicionario_jogadas, nome_1, nome_2, soma1, soma2, pontuacao1, pontuacao2)
                    mostrar_vencedor(lista_ganhador)
                    print('Pontuação jogador {}: {} ponto(s)\nPontuação jogador {}: {} ponto(s)\n'.format(nome_1, pontuacao1, nome_2, pontuacao2))
                    # Cópia profunda das jogadas para colocar no histórico.
                    copia_historico = copy.deepcopy(dicionario_jogadas)
                    historico1, historico2 = historico(copia_historico, nome_1, nome_2, historico1, historico2)
                    mostrar_historico(nome_1, nome_2, historico1, historico2)
                    # Em caso de empate será revelada o número em dois tabuleiros diferentes. Por isso é necessário separar 
                    # para chamar cada uma com seus respectivos tabuleiros.
                    if len(lista_ganhador) == 1:
                        if lista_ganhador[0] == nome_1:
                            dicionario_revelacao = achar_posicao(lista_ganhador, dicionario_jogadas, tabuleiro_resp1, linhas, colunas)
                            tabuleiro1, tabuleiro_resp1 = trocar_numeros(dicionario_revelacao, tabuleiro1, tabuleiro_resp1, linhas, colunas)
                        else:
                            dicionario_revelacao = achar_posicao(lista_ganhador, dicionario_jogadas, tabuleiro_resp2, linhas, colunas)
                            tabuleiro2, tabuleiro_resp2 = trocar_numeros(dicionario_revelacao, tabuleiro2, tabuleiro_resp2, linhas, colunas)
                    else:
                        # Em caso de empate é necessário separar a lista dos ganhadores em duas listas distintas 
                        # para chamar a função achar a posição e trocar os números, pois são dois taduleiros diferentes.
                        lista_nome1 = []
                        lista_nome2 = []
                        lista_nome1.append(lista_ganhador[0])
                        lista_nome2.append(lista_ganhador[1])
                        dicionario_revelacao1 = achar_posicao(lista_nome1, dicionario_jogadas, tabuleiro_resp1, linhas, colunas)
                        tabuleiro1, tabuleiro_resp1 = trocar_numeros(dicionario_revelacao1, tabuleiro1, tabuleiro_resp1, linhas, colunas)
                        dicionario_revelacao2 = achar_posicao(lista_nome2, dicionario_jogadas, tabuleiro_resp2, linhas, colunas)
                        tabuleiro2, tabuleiro_resp2 = trocar_numeros(dicionario_revelacao2, tabuleiro2, tabuleiro_resp2, linhas, colunas)
                    print('Tabuleiro do jogador {}'.format(nome_1))
                    mostrar_matriz(tabuleiro1, linhas, colunas)
                    print('Tabuleiro do jogador {}'.format(nome_2))
                    mostrar_matriz(tabuleiro2, linhas, colunas)
        # Quebra do loop.
        if aux == 0:
            iniciador = False
    if pontuacao1 > pontuacao2:
        print('O vencendor foi o jogador {}\n'.format(nome_1))
    elif pontuacao2 > pontuacao1:
        print('O vencendor foi o jogador {}\n'.format(nome_2))
    else:
        print('Os vencedores foram os jogadores {} e {}\n'.format(nome_1, nome_2))
    print('Parabéns, o agente Smith foi derrotado!\nAutora: Amanda Lima Bezerra')

def tabuleiro1_rodadas(nome_1, nome_2, quant_tabuleiro, linhas, colunas, limite, quant_numeros, rodadas):
    tabuleiro, tabuleiro_resp = montando_tabuleiro(linhas, colunas, limite, quant_numeros)
    mostrar_matriz(tabuleiro, linhas, colunas)
    historico1 = []
    historico2 = []
    pontuacao1 = 0
    pontuacao2 = 0
    # Variável responsável pelo controle de rodadas, começa com 1 pois ela só vai ser atualizada no final da rodada. A estrutura do 
    # loop para número de rodadas definidas é sempre comparar o número de rodadas com uma variável aux que é atualizada a cada rodada.
    aux = 1
    while aux <= rodadas:
        dicionario_jogadas = escolher_jogadas(nome_1, nome_2, linhas)
        # Estrutura do dicionario_jogadas: Nome: [indicação da linha/coluna, valor chutado]                    
        soma1, soma2 = achar_soma(tabuleiro_resp, dicionario_jogadas, nome_1, nome_2, linhas, colunas)
        # Estrutura do dicionario_comparacao: Nome: [posição, valor chutado, maior/menor/acertou]
        dicionario_jogadas = comparar(nome_1, nome_2, soma1, soma2, dicionario_jogadas)
        pontuacao1, pontuacao2, lista_ganhador = ganhador(dicionario_jogadas, nome_1, nome_2, soma1, soma2, pontuacao1, pontuacao2)
        mostrar_vencedor(lista_ganhador)
        print('Pontuação jogador {}: {} ponto(s)\nPontuação jogador {}: {} ponto(s)\n'.format(nome_1, pontuacao1, nome_2, pontuacao2))
        # Cópia profunda das jogadas para colocar no histórico.
        copia_historico = copy.deepcopy(dicionario_jogadas)
        historico1, historico2 = historico(copia_historico, nome_1, nome_2, historico1, historico2)
        mostrar_historico(nome_1, nome_2, historico1, historico2)
        dicionario_revelacao = achar_posicao(lista_ganhador, dicionario_jogadas, tabuleiro_resp, linhas, colunas)
        tabuleiro, tabuleiro_resp = trocar_numeros(dicionario_revelacao, tabuleiro, tabuleiro_resp, linhas, colunas)
        mostrar_matriz(tabuleiro, linhas, colunas)
        aux += 1
    if pontuacao1 > pontuacao2:
        print('O vencendor foi o jogador {}\n'.format(nome_1))
    elif pontuacao2 > pontuacao1:
        print('O vencendor foi o jogador {}\n'.format(nome_2))
    else:
        print('Os vencedores foram os jogadores {} e {}\n'.format(nome_1, nome_2))
    print('Parabéns, o agente Smith foi derrotado!\nAutora: Amanda Lima Bezerra')

def tabuleiro2_rodadas(nome_1, nome_2, quant_tabuleiro, linhas, colunas, limite, quant_numeros, rodadas):
    # Essa rodada tem a estrutura do loop igual a anterios com o número de rodadas definidas mas foi montado de acordo 
    # com o número de tabuleiros, nesse caso foram dois.
    tabuleiro1, tabuleiro_resp1 = montando_tabuleiro(linhas, colunas, limite, quant_numeros)
    tabuleiro2, tabuleiro_resp2 = montando_tabuleiro(linhas, colunas, limite, quant_numeros)
    print('Tabuleiro do jogador {}'.format(nome_1))
    mostrar_matriz(tabuleiro1, linhas, colunas)
    print('Tabuleiro do jogador {}'.format(nome_2))
    mostrar_matriz(tabuleiro2, linhas, colunas)
    historico1 = []
    historico2 = []
    pontuacao1 = 0
    pontuacao2 = 0
    aux = 1
    while aux <= rodadas:
        dicionario_jogadas = escolher_jogadas(nome_1, nome_2, linhas)
        # Estrutura do dicionario_jogadas = Nome: [indicaçao linha/coluna, valor chutado]
        soma1, soma2 = achar_soma2(tabuleiro_resp1, tabuleiro_resp2, dicionario_jogadas, nome_1, nome_2, linhas, colunas)
        # Estrutura do dicionario_jogadas = Nome: [indicaçao linha/coluna, valor chutado]
        dicionario_jogadas = comparar(nome_1, nome_2, soma1, soma2, dicionario_jogadas)
        pontuacao1, pontuacao2, lista_ganhador = ganhador(dicionario_jogadas, nome_1, nome_2, soma1, soma2, pontuacao1, pontuacao2)
        mostrar_vencedor(lista_ganhador)
        print('Pontuação jogador {}: {} ponto(s)\nPontuação jogador {}: {} ponto(s)\n'.format(nome_1, pontuacao1, nome_2, pontuacao2))
        # Cópia profunda das jogadas para colocar no histórico.
        copia_historico = copy.deepcopy(dicionario_jogadas)
        historico1, historico2 = historico(copia_historico, nome_1, nome_2, historico1, historico2)
        mostrar_historico(nome_1, nome_2, historico1, historico2)
        if len(lista_ganhador) == 1:
            if lista_ganhador[0] == nome_1:
                dicionario_revelacao = achar_posicao(lista_ganhador, dicionario_jogadas, tabuleiro_resp1, linhas, colunas)
                tabuleiro1, tabuleiro_resp1 = trocar_numeros(dicionario_revelacao, tabuleiro1, tabuleiro_resp1, linhas, colunas)
            else:
                dicionario_revelacao = achar_posicao(lista_ganhador, dicionario_jogadas, tabuleiro_resp2, linhas, colunas)
                tabuleiro2, tabuleiro_resp2 = trocar_numeros(dicionario_revelacao, tabuleiro2, tabuleiro_resp2, linhas, colunas)
        else:
            lista_nome1 = []
            lista_nome2 = []
            lista_nome1.append(lista_ganhador[0])
            lista_nome2.append(lista_ganhador[1])
            dicionario_revelacao1 = achar_posicao(lista_nome1, dicionario_jogadas, tabuleiro_resp1, linhas, colunas)
            tabuleiro1, tabuleiro_resp1 = trocar_numeros(dicionario_revelacao1, tabuleiro1, tabuleiro_resp1, linhas, colunas)
            dicionario_revelacao2 = achar_posicao(lista_nome2, dicionario_jogadas, tabuleiro_resp2, linhas, colunas)
            tabuleiro2, tabuleiro_resp2 = trocar_numeros(dicionario_revelacao2, tabuleiro2, tabuleiro_resp2, linhas, colunas)
        print('Tabuleiro do jogador {}'.format(nome_1))
        mostrar_matriz(tabuleiro1, linhas, colunas)
        print('Tabuleiro do jogador {}'.format(nome_2))
        mostrar_matriz(tabuleiro2, linhas, colunas)        
        aux += 1
    if pontuacao1 > pontuacao2:
        print('O vencendor foi o jogador {}\n'.format(nome_1))
    elif pontuacao2 > pontuacao1:
        print('O vencendor foi o jogador {}\n'.format(nome_2))
    else:
        print('Os vencedores foram os jogadores {} e {}\n'.format(nome_1, nome_2))
    print('Parabéns, o agente Smith foi derrotado!\nAutora: Amanda Lima Bezerra')

# Funções para a jogabilidade.
def escolher_jogadas(nome1, nome2, linhas):
    # Estrutura de dicionário para armazenar as jogadas a cada rodada.
    dicionario_jogadas = {}
    lista1 = []
    lista2 = []

    # Entrada de dados do jogador 1.
    print('Jogador {} escolha a sua linha ou coluna e o número correspondente.'.format(nome1))
    linha_coluna, numero = [x for x in input('-----> ').split()]
    escolha_linhacoluna = validacao_opcao_linhacoluna(linha_coluna, numero, linhas)
    lista1.append(escolha_linhacoluna)
    chute1 = input('Qual a soma da {} {} jogador {}\n-----> '.format(escolha_linhacoluna[0], escolha_linhacoluna[1], nome1))
    chute1 = validacao_chute(chute1)
    lista1.append(chute1)
    dicionario_jogadas[nome1] = lista1
    
    # Entrada de dados do jogador 2.
    print('Jogador {} escolha a sua linha ou coluna e o número correspondente.'.format(nome2))
    linha_coluna, numero = [x for x in input('-----> ').split()]
    escolha_linhacoluna = validacao_opcao_linhacoluna(linha_coluna, numero, linhas)
    lista2.append(escolha_linhacoluna)
    chute2 = input('Qual a soma da {} {} jogador {}\n-----> '.format(escolha_linhacoluna[0], escolha_linhacoluna[1], nome2))
    chute2 = validacao_chute(chute2)
    lista2.append(chute2)
    dicionario_jogadas[nome2] = lista2
    return dicionario_jogadas

# Função para um único tabuleiro.
def achar_soma(tabuleiro_resp, dicionario_jogadas, nome_1, nome_2, linhas, colunas):
    # Função para achar a soma da linha/coluna correspondente a jogada de cada jogador. Função usada somente quando o jogo 
    # é em um único tabuleiro.
    for nome in dicionario_jogadas.keys():
        if nome == nome_1:
            for linha in range(1, linhas):
                for coluna in range(1, colunas):
                    if dicionario_jogadas[nome_1][0][0] == 'C' and dicionario_jogadas[nome_1][0][1] == coluna and linha == linhas - 1:
                        soma1 = tabuleiro_resp[linha][coluna]
                    elif dicionario_jogadas[nome_1][0][0] == 'L' and dicionario_jogadas[nome_1][0][1] == linha and coluna == colunas - 1:
                        soma1 = tabuleiro_resp[linha][coluna]
        else:
            for linha in range(linhas):
                for coluna in range(colunas):
                    if dicionario_jogadas[nome_2][0][0] == 'C' and dicionario_jogadas[nome_2][0][1] == coluna and linha == linhas - 1:
                        soma2 = tabuleiro_resp[linha][coluna]
                    elif dicionario_jogadas[nome_2][0][0] == 'L' and dicionario_jogadas[nome_2][0][1] == linha and coluna == colunas - 1:
                        soma2 = tabuleiro_resp[linha][coluna]
    return soma1, soma2
        
# Função para dois tabuleiros.
def achar_soma2(tabuleiro_resp1, tabuleiro_resp2, dicionario_jogadas, nome_1, nome_2, linhas, colunas):
    # Função de achar a soma da linha/coluna da jogada feita para dois tabuleiros. A diferença da anterior é que nessa função 
    # a segunda parte é feita no tabuleiro resposta 2.
    for nome in dicionario_jogadas.keys():
        if nome == nome_1:
            for linha in range(1, linhas):
                for coluna in range(1, colunas):
                    if dicionario_jogadas[nome_1][0][0] == 'C' and dicionario_jogadas[nome_1][0][1] == coluna and linha == linhas - 1:
                        soma1 = tabuleiro_resp1[linha][coluna]
                    elif dicionario_jogadas[nome_1][0][0] == 'L' and dicionario_jogadas[nome_1][0][1] == linha and coluna == colunas - 1:
                        soma1 = tabuleiro_resp1[linha][coluna]
        else:
            for linha in range(linhas):
                for coluna in range(colunas):
                    if dicionario_jogadas[nome_2][0][0] == 'C' and dicionario_jogadas[nome_2][0][1] == coluna and linha == linhas - 1:
                        soma2 = tabuleiro_resp2[linha][coluna]
                    elif dicionario_jogadas[nome_2][0][0] == 'L' and dicionario_jogadas[nome_2][0][1] == linha and coluna == colunas - 1:
                        soma2 = tabuleiro_resp2[linha][coluna]
    return soma1, soma2

def comparar(nome_1, nome_2, soma1, soma2, dicionario_jogadas):
    # Função feita para comparar o valor da soma da linha/coluna com o chute do jogador.
    for nome in dicionario_jogadas:
        if nome == nome_1:
            if dicionario_jogadas[nome_1][1] > soma1:
                dicionario_jogadas[nome_1].append('Maior')
            elif dicionario_jogadas[nome_1][1] < soma1:
                dicionario_jogadas[nome_1].append('Menor')
            else:
                dicionario_jogadas[nome_1].append('Acertou!')
        else:
            if dicionario_jogadas[nome_2][1] > soma2:
                dicionario_jogadas[nome_2].append('Maior')
            elif dicionario_jogadas[nome_2][1] < soma2:
                dicionario_jogadas[nome_2].append('Menor')
            else:
                dicionario_jogadas[nome_2].append('Acertou!')
    return dicionario_jogadas

def ganhador(dicionario_jogadas, nome_1, nome_2, soma1, soma2, pontuacao1, pontuacao2):
    # Função para definir o ganhador da rodada. Nesse caso eu calculo a diferença, já em módulo 
    # pois uso a indicação do maior/menor para calcular.

    # Estrutura do dicionario_jogadas: Nome: [indicação da linha/coluna, valor chutado, maior/menor/acertou]
    lista_ganhador = []
    for nome in dicionario_jogadas:
        if nome == nome_1:
            if dicionario_jogadas[nome_1][2] == 'Maior':
                diferenca1 = dicionario_jogadas[nome_1][1] - soma1
            elif dicionario_jogadas[nome_1][2] == 'Menor':
                diferenca1 = soma1 - dicionario_jogadas[nome_1][1]
            else:
                diferenca1 = 0   
        elif nome == nome_2:
            if dicionario_jogadas[nome_2][2] == 'Maior':
                diferenca2 = dicionario_jogadas[nome_2][1] - soma2
            elif dicionario_jogadas[nome_2][2] == 'Menor':
                diferenca2 = soma2 - dicionario_jogadas[nome_2][1]
            else:
                diferenca2 = 0
    # O ganhador nesse caso foi o jogador 2.
    if diferenca1 > diferenca2:
        lista_ganhador.append(nome_2)
        pontuacao2 += 1
        return pontuacao1, pontuacao2, lista_ganhador
    # O ganhador nesse caso foi o jogador 1.
    elif diferenca1 < diferenca2:
        lista_ganhador.append(nome_1)
        pontuacao1 += 1
        return pontuacao1, pontuacao2, lista_ganhador
    # Empate.
    else:
        lista_ganhador.append(nome_1)
        lista_ganhador.append(nome_2)
        pontuacao1 += 1
        pontuacao2 += 1
        return pontuacao1, pontuacao2, lista_ganhador

def mostrar_vencedor(lista_ganhador):
    print('\nO(s) ganhador(es) da rodada: \n')
    for nome in lista_ganhador:
        print('Parabéns {}, ganhador da rodada!\n'.format(nome))

def historico(copia_historico, nome_1, nome_2, historico1, historico2):
    # Estrutura da cópia histórico: Nome: [indicação da linha/coluna, valor chutado, maior/menor/acertou]
    for nome in copia_historico:
        if nome == nome_1:
            historico1.append(copia_historico[nome_1])
        else:
            historico2.append(copia_historico[nome_2])
    return historico1, historico2

def mostrar_historico(nome_1, nome_2, historico1, historico2):
    print('Histórico de jogadas do jogador {}\n'.format(nome_1))
    for jogadas in historico1:
        for elementos_jogadas in jogadas:
            if elementos_jogadas == jogadas[0]:
                print(*elementos_jogadas, end = ' - ')
            else:
                print(elementos_jogadas, end = '  ')
        print('\n')
    print('Histórico de jogadas do jogador {}\n'.format(nome_2))
    for jogadas in historico2:
        for elementos_jogadas in jogadas:
            if elementos_jogadas == jogadas[0]:
                print(*elementos_jogadas, end = ' - ')
            else:
                print(elementos_jogadas, end = '  ')
        print('\n')

def achar_posicao(lista_ganhador, dicionario_jogadas, tabuleiro_resp, linhas, colunas):
    # Essa função foi criada para achar a posição exata no tabuleiro resposta para o valor que vai ser revelado.

    # Estrutura do dicionario_jogadas = Nome: [indicação da linha/coluna, valor chutado, maior/menor/acertou]
    dicionario_revelacao = {}
    for nomes in lista_ganhador:
        # Uma gambiarra foi necessária nesse caso pois ao revelar o número no tabuleiro eu coloco um zero para ficar fora 
        # da busca pelo maior ou menor número a ser achadado para revelar. Coloquei um número muito baixo para inicias a comparção com o maior 
        # número e um número muito baixo para iniciar a comparação com o menor número.
        numero_revelado_maior = -10000
        numero_revelado_menor = 10000        
        for linha in range(1, linhas - 1):
            for coluna in range(1, colunas - 1):
                # Foi necessário separar entre maior/menor/acertou e entre linhas/colunas e todas elas tem a condição de ser diferente de 0.
                if dicionario_jogadas[nomes][2] == 'Maior' and dicionario_jogadas[nomes][0][0] == 'L' \
                        and tabuleiro_resp[dicionario_jogadas[nomes][0][1]][coluna] != 0:
                    if numero_revelado_maior < tabuleiro_resp[dicionario_jogadas[nomes][0][1]][coluna]:
                        numero_revelado_maior = tabuleiro_resp[dicionario_jogadas[nomes][0][1]][coluna]
                        lista_revelacao = []
                        lista_revelacao.append(numero_revelado_maior)
                        lista_revelacao.append(dicionario_jogadas[nomes][0][1])
                        lista_revelacao.append(coluna)
                        # Estrutura do dicionario_revelacao = Nome: [numero_revelado, linha, coluna]  
                        dicionario_revelacao[nomes] = lista_revelacao
                elif dicionario_jogadas[nomes][2] == 'Maior' and dicionario_jogadas[nomes][0][0] == 'C' \
                        and tabuleiro_resp[linha][dicionario_jogadas[nomes][0][1]] != 0:
                    if numero_revelado_maior < tabuleiro_resp[linha][dicionario_jogadas[nomes][0][1]]:
                        numero_revelado_maior = tabuleiro_resp[linha][dicionario_jogadas[nomes][0][1]]
                        lista_revelacao = []
                        lista_revelacao.append(numero_revelado_maior)
                        lista_revelacao.append(linha)
                        lista_revelacao.append(dicionario_jogadas[nomes][0][1])
                        # Estrutura do dicionario_revelacao = Nome: [numero_revelado, linha, coluna]  
                        dicionario_revelacao[nomes] = lista_revelacao
                elif dicionario_jogadas[nomes][2] == 'Menor' and dicionario_jogadas[nomes][0][0] == 'L' \
                        and tabuleiro_resp[dicionario_jogadas[nomes][0][1]][coluna] != 0:
                    if numero_revelado_menor > tabuleiro_resp[dicionario_jogadas[nomes][0][1]][coluna]:
                        numero_revelado_menor = tabuleiro_resp[dicionario_jogadas[nomes][0][1]][coluna]
                        lista_revelacao = []
                        lista_revelacao.append(numero_revelado_menor)
                        lista_revelacao.append(dicionario_jogadas[nomes][0][1])
                        lista_revelacao.append(coluna)
                        # Estrutura do dicionario_revelacao = Nome: [numero_revelado, linha, coluna]  
                        dicionario_revelacao[nomes] = lista_revelacao
                elif dicionario_jogadas[nomes][2] == 'Menor' and dicionario_jogadas[nomes][0][0] == 'C' \
                        and tabuleiro_resp[linha][dicionario_jogadas[nomes][0][1]] != 0:
                    if numero_revelado_menor > tabuleiro_resp[linha][dicionario_jogadas[nomes][0][1]]:
                        numero_revelado_menor = tabuleiro_resp[linha][dicionario_jogadas[nomes][0][1]]
                        lista_revelacao = []
                        lista_revelacao.append(numero_revelado_menor)
                        lista_revelacao.append(linha)
                        lista_revelacao.append(dicionario_jogadas[nomes][0][1])
                        # Estrutura do dicionario_revelacao = Nome: [numero_revelado, linha, coluna]  
                        dicionario_revelacao[nomes] = lista_revelacao
                # Caso o jogador acerte a jogadas a posição salva vai ser a da indicação da linha/coluna que vai ser revelada.
                elif dicionario_jogadas[nomes][2] == 'Acertou!' and dicionario_jogadas[nomes][0][0] == 'L':
                    numero_revelado = tabuleiro_resp[dicionario_jogadas[nomes][0][1]][0]
                    lista_revelacao = []
                    lista_revelacao.append(numero_revelado)
                    lista_revelacao.append(dicionario_jogadas[nomes][0][1])
                    lista_revelacao.append(0)
                    # Estrutura do dicionario_revelacao = Nome: [numero_revelado, linha, coluna]  
                    dicionario_revelacao[nomes] = lista_revelacao
                elif dicionario_jogadas[nomes][2] == 'Acertou!' and dicionario_jogadas[nomes][0][0] == 'C':
                    numero_revelado = tabuleiro_resp[0][dicionario_jogadas[nomes][0][1]]
                    lista_revelacao = []
                    lista_revelacao.append(numero_revelado)
                    lista_revelacao.append(0)
                    lista_revelacao.append(dicionario_jogadas[nomes][0][1])
                    # Estrutura do dicionario_revelacao = Nome: [numero_revelado, linha, coluna]  
                    dicionario_revelacao[nomes] = lista_revelacao
    return dicionario_revelacao

def trocar_numeros(dicionario_revelacao, tabuleiro, tabuleiro_resp, linhas, colunas):
    # Trocando os números no tabuleiro.

    # Estrutura do dicionario_revelacao = Nome: [numero_revelado, linha, coluna]
    for lista_informacoes in dicionario_revelacao.values():
        for linha in range(1, linhas):
            for coluna in range(1, colunas):
                # Acertou somente um número.
                if lista_informacoes[1] == linha and lista_informacoes[2] == coluna and tabuleiro_resp[linha][coluna] != 0:
                    tabuleiro[linha][coluna] = tabuleiro_resp[linha][coluna]
                    tabuleiro_resp[linha][coluna] = 0
                # Acertou a soma da linha.
                elif lista_informacoes[1] != 0 and lista_informacoes[2] == 0 and linha == lista_informacoes[1] \
                    and tabuleiro_resp[linha][coluna] != 0:
                    tabuleiro[lista_informacoes[1]][coluna] = tabuleiro_resp[lista_informacoes[1]][coluna]
                    tabuleiro_resp[lista_informacoes[1]][coluna] = 0
                # Acertou a soma da coluna.
                elif lista_informacoes[1] == 0 and lista_informacoes[2] != 0 and coluna == lista_informacoes[2] \
                    and tabuleiro_resp[linha][coluna] != 0:
                    tabuleiro[linha][lista_informacoes[2]] = tabuleiro_resp[linha][lista_informacoes[2]]
                    tabuleiro_resp[linha][lista_informacoes[2]] = 0
    return tabuleiro, tabuleiro_resp

# Funções responsáveis pelas validações.
def validacao_nomes(entrada1, entrada2):
    while entrada1 == entrada2:
        entrada2 = input('Nome já cadastrado. Coloque outro: ')
    return entrada1, entrada2

def validacao_1(entrada):
    while not entrada.isnumeric() or isinstance(entrada, float) or 1 > int(entrada) or int(entrada) > 2:
        entrada = input('Resposta inválida\nDigite novamente\n-----> ')
    return int(entrada)

def validacao_2(entrada):
    while not entrada.isnumeric() or isinstance(entrada, float) or 1 > int(entrada) or int(entrada) > 3:
        entrada = input('Resposta inválida\nDigite novamente\n-----> ')
    return int(entrada)

def validacao_3(entrada):
    while not entrada.isnumeric() or isinstance(entrada, float) or int(entrada) % 2 == 0:
        entrada = input('Resposta inválida\nDigite novamente\n-----> ')
    return int(entrada)

def validacao_opcao_linhacoluna(linha_coluna, numero, linhas):
    lista = []
    while linha_coluna.upper() != 'C' and linha_coluna.upper() != 'L'\
        or not numero.isnumeric() or isinstance(numero, float) or int(numero) < 0 or int(numero) > linhas - 2:
        linha_coluna, numero = [x for x in input('Resposta inválida\nDigite novamente\n-----> ').split()]
    lista.append(linha_coluna.upper())
    lista.append(int(numero))
    return tuple(lista)

def validacao_chute(entrada):
    while not entrada.isnumeric() or isinstance(entrada, float):
        entrada = input('Resposta inválida\nDigite novamente\n-----> ')
    return int(entrada)

if __name__ == '__main__':
    menu()