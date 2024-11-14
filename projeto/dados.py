open('cadastro.txt', 'a', encoding='utf-8').close() # cria o arquivo "cadastro.txt"
def cadastro():
    '''
    É responsável por fazer os cadastros das pessoas, adicionando seus nomes em 'cadastro.txt'.

    A função acessa o arquivo 'cadastro.txt' e guarda as linhas em 'lista_nomes'. Verifica o tamanho de 'listas_nomes', se for maior que 0: pede ao usuário o seu nome, verifica se ele existe em 'lista_nomes', se sim, pede ao úsuario que digite seu nome novamente até que ele digite um nome ainda não cadastrado, se não, apenas o escreve no arquivo. Se o tamanho de 'lista_nomes' não for maior que 0: pede o nome do usuário e o escreve no arquivo.

    - PARÂMETROS: não contém parâmetros

    - RETURN: retorna o nome do usuário
    '''
    arq = open('cadastro.txt', encoding='utf-8') # Lê o arquivo e o guarda em "arq"
    lista_nomes = arq.readlines() # cria uma lista e adiciona as linhas de arquivo
    arq.close() # fecha o arquivo
    if len(lista_nomes) > 0: # se "lista_nomes" tiver o tamanho maior que 0:
        nome = input('\nDigite seu nome: ').upper().strip() # pede ao usuário que digite seu nome
        while nome == '':
            nome = input('\nNome inválido...Digite seu nome: ').upper().strip() # pede ao usuário que digite seu nome
        nome = nome + '\n' # para garantir que a verficação considere a quebra de linha
        if nome not in lista_nomes: # se o nome não estiver em "lista_nomes", abre o arquivo e o guarda em "arq", escreve o nome da pessoa e fecha o aquivo
            arq = open('cadastro.txt', 'a', encoding='utf-8')
            arq.write(nome)
            arq.close()
        else: # se já existir esse nomes em "lista_nomes":
            while nome in lista_nomes: # pede o nome ao usuário enquanto ele existir em "lista_nome"
                nome = input('\nEsse nome já está cadastrado! Tente novamente: ').upper().strip()
                nome = nome + '\n'
            # depois da verificação ser falsa, abre o arquivo e guarda em "arq", escreve o nome e fecha o arquivo
            arq = open('cadastro.txt', 'a', encoding='utf-8')
            arq.write(nome)
            arq.close()
    else: # se "lista_nomes" não tiver elementos apenas pede o nome do usuário e o escreve no arquivo
        nome = input('\nDigite seu nome: ').upper().strip()
        nome = nome + '\n'
        arq = open('cadastro.txt', 'a', encoding='utf-8')
        arq.write(nome)
        arq.close()
    
    print('\nNome cadastrado com sucesso!')

    return nome

open('ranking.txt', 'a', encoding='utf-8').close()
def cadastro_ranking(nome: str, pontuação: int):
    '''
    É responsável por adicionar o nome do usuário e a sua pontuação em 'ranking.txt'.

    A função verifica se há um nome e se as partidas foram diferentes de 0, se sim, acessa o arquivo 'ranking.txt' e esreceve o nome e a pontuação do usuário, que é o número de partidas ganhas (partidas) vezes 100 (valor que o jogador acumula cada vez que ganha).

    - PARÂMETROS: 
        - nome: nome do usuário;
        - partidas: quantidade de partidas ganhas pelo usuário

    - RETURN:
        - None.
                 
    '''
    # abre o arquivo 'ranking.txt' e o guarda em "arq"
    arq = open('ranking.txt', 'a', encoding='utf-8')
    # escreve o nome do usuário
    if nome != '':
        arq.write(nome)
    # escreve a pontuação no arquivo
        arq.write(str(pontuação) + '\n')
    # fecha o arquivo
    arq.close()

def ranking():
    '''
    É responsável por organizar o ranking em ordem decrescente e o exibi-lo.

    A função acessa 'ranking.txt' e guarda as linhas em 'lista_ranking'. Verifica o tamanho de 'lista_ranking', se for maior que 0:
    cria um laço e percorre o tamanho de 'lista_ranking' iniciando do 0 e pulando de 2 em 2, o índice 'i' representa o nome do usuário e é guardado em 'nome'; o índice 'i+1' representa a pontuação do usuário e é guardada em 'pontuação'. Adiciona os nomes ao dicionário 'ranking_dict' e verifica se há uma chave com aquele nome, se sim, ele faz o somatório da pontuação. Por último, guarda as chaves e os valores em um lista, a qual recebe uma lista de dois elementos correspondente a cada jogador onde o índice 0 corresponde a pontuação e o índice 1 corresponde o nome, depois a organiza em ordem crescente e exibi o ranking através da função "exibir_ranking".

    - PARÂMETROS: 
        - Sem parâmetros.

    - RETURN:
        - None.
    '''
    # abre o arquivo 'ranking.txt' e o guarda em "arq"
    arq = open('ranking.txt', encoding='utf-8')
    # guarda as linhas do arquivo em "lista_ranking"
    lista_ranking = arq.readlines()
    # fecha o arquivo
    arq.close()
    ranking_dict = {} # cria uma lista para guardar os nomes e as pontuações do usuário
    ranking = []
    if len(lista_ranking) > 0: # se "lista_ranking" tiver o tamanho maior que 0:
        for i in range(0, len(lista_ranking), 2):
            nome = lista_ranking[i][:-1]
            pontuação = int(lista_ranking[i+1][:-1])
            if nome not in ranking_dict:
                ranking_dict[nome] = pontuação
            else:
                ranking_dict[nome] += pontuação

        for nome, pont in ranking_dict.items():
            ranking += [[pont, nome]]

        ranking.sort(reverse=True)
    
    # exibi o ranking
    exibir_ranking(ranking)

def exibir_ranking(ranking: list[list[str, str]]):
    '''
    É responsável por exibir o ranking.

    Exibi um menu com a palavra 'RANKING' e organiza os dados como uma tabela: a primeira linha são o nome e a pontuação e a primeira coluna são as posições, as linhas/colunas correspondentes são os dados.

    - PARÂMETROS:
        - ranking: a lista do ranking organizada em ordem decrescente.

    - RETURN
        - None.
    '''
    print('-='*20, end=' ')
    print('RANKING', end=' ') 
    print('-='*20)
    print()
    print(22*' ' + 'Nome', end='')
    print(36*' ' + 'Pontuação')
    print('-'*89)
    # percorre o tamanho de raning
    for i in range(len(ranking)):
        if i == 4: # garante que só exiba 5 posições
            break
        nome = ranking[i][1]
        pontuação = ranking[i][0]
        print(f'{i+1}° Posição =', end=' ')
        print(nome, end='')
        print((31 - len(nome))*' ' + '|', end=' ')
        print(pontuação)
