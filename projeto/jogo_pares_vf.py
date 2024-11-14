from os import *
from random import *
from time import *
from dados import *

def escolher_jogador(lista: list[str, str]) -> list:
    '''
    A função é responsável por escolher o jogador a iniciar atráves do sorteio de um índice.

    PARAMÊTROS: 
        - lista: a lista dos índices (0, 1)

    RETURN: 
        - retorna o valor do índice sorteado
    '''
    sorteado = lista[randint(0, 1)]
    return sorteado

def separar_carta_inicial(baralho: list[list[str, list[str]]]) -> tuple[str, str]:
    '''
    A função é responsável por sortear uma carta e a tirá-la do baralho, essa carta não é revelada durante o jogo.

    Primeiramente sorteia um número entre 0 e 3, que corresponde ao índice (nome) do naipe em 'baralho', e o guarda em 'naipe'. Depois sorteia um valor de uma carta dentro da lista correspondente à 'naipe' e o guarda em 'valor'. Por útlimo, percorre 'baralho' no índice do naipe e procura o elemento correspondente a valor e o remove de 'baralho', então retona o nome do naipe e o seu valor.

    - PARÊMTROS: 
        - baralho: corresponde à lista de cartas

    - RETURN: 
        - retorna o naipe da carta e o seu valor
    '''
    naipe = randint(0, 3)
    valor = choice(baralho[naipe][1])
    for i in baralho[naipe][1]:
        # se "i" for igual à "valor", que corresponde a carta sorteada, ele remove de baralho naquele naipe
        if i == valor:
            baralho[naipe][1].remove(valor)
    
    return baralho[naipe][0], valor

def separar_baralhos(baralho: list[list[str, list[str]]], res: str) -> tuple[list[list], list[list]]:
    '''
    É responsável por separar os baralhos do jogador e do computador.

    Cria duas listas (baralho1 e baralho2) e cria um laço que é interrompido quando não houver mais cartas em 'baralho'. Enquanto houver cartas: são sorteados naipes (naipe1 e naipe2), se na lista que está dentro do naipe sorteado houver elementos (cartas), são sorteados valores (valor) e adicionados a baralho1 e baralho2 na lista que corresponde ao naipe sorteado. Após isso, 'baralho' na lista dentro do naipe sorteado é percorrido e se o valor 'i' for igual ao valor sorteado, o valor é removido de 'baralho'. Após o fim do laço, verifica-se o tamanho dos baralhos, aquele que tiver menos carta é retornado primeiro conforme 'res', que representa o jogador ao qual devera receber menos cartas.

    - PARÂMETROS:
        - baralho: lista das cartas.

    - RETURN:
        - retorna baralho1 e baralho2 conforme as verificações.
    '''
    baralho1 = [['paus', []], ['ouro', []], ['copas', []], ['espada', []]]
    baralho2 = [['paus', []], ['ouro', []], ['copas', []], ['espada', []]]

    while True:
        if contar_cartas(baralho) > 0:
            naipe1 = randint(0, 3)
            if len(baralho[naipe1][1]) > 0:
                valor = choice(baralho[naipe1][1]) # adiciona no baralho1, na lista do naipe sorteado o valor também sorteado
                baralho1[naipe1][1] += [valor] # adiciona ao baralho1 no naipe1 o valor sorteado
                for i in baralho[naipe1][1]: # percorre o baralho do naipe sorteado
                    if i == valor: # se "i" for igual à "valor", o remove de baralho
                        baralho[naipe1][1].remove(valor)
            naipe2 = randint(0, 3)
            if len(baralho[naipe2][1]) > 0:
                valor = choice(baralho[naipe2][1]) # adiciona no baralho2, na lista do naipe sorteado o valor também sorteado
                baralho2[naipe2][1] += [valor] # adiciona ao baralho2 no naipe2 o valor sorteado
                for i in baralho[naipe2][1]: # percorre o baralho do naipe sorteado
                    if i == valor: # se "i" for igual à "valor", o remove de baralho
                        baralho[naipe2][1].remove(valor)
        else:
            break
                    
    # analisar qual foi o jogador que venceu e separar o menor número de cartas para ele
    if contar_cartas(baralho1) > contar_cartas(baralho2): # se o baralho1 tiver mais cartas que o baralho2:
        if res == 'COMPUTADOR': # se o computador tiver ganho
            return baralho2, baralho1 # retorna baralho2 para o computador, pois tem menos cartas, e baralho1 para o jogador
        return baralho1, baralho2 # se não, retorna baralho1 para o computador e baralho2 para o jogador
    else: # se o baralho2 tiver mais cartas que o baralho1:
        if res == 'COMPUTADOR': # se o computador tiver ganho ele recebe o baralho1, se não, recebe o baralho2
            return baralho1, baralho2
        return baralho2, baralho1

def guardar_cartas_repetidas(baralho: list[list[str, list[str]]]) -> tuple[list, list, int, int, int, int]:
    '''
    A função guarda as cartas em comum dos naipes em listas: naipes de ouro e copas estão em comum e naipes de paus e espada estão em comum.

    Primeiramente, ela percorre 'baralho' e o índice correspondente ao índice de 'espada' é guadado em 'idx_e', faz o mesmo processo para 'idx_c', mas compara a 'copas' ao ínves de 'espada'. Depois percorre 'baralho', verifica se o índice é igual ao índice de 'paus', guarda em 'idx_p' e percorre a lista. Verifica se o elemento está na lista de 'idx_e', se sim, adiciona a 'repetidos_paus_espada'. Faz o mesmo processo para adicionar os elementos a 'repetidos_copas_ouro', mas guarda o índice de copas (idx_c) ao ínves de 'paus' e utiliza 'idx_o' para verificação.

    - PARÂMETROS: 
        - baralho: lista de cartas

    - RETURN: 
        - retorna 'repetidos_paus_espada' (elementos em comum entre paus e espada), 'repetidos_copas_ouro' (elementos em comum entre copas e ouro) e retorna os índices de paus (idx_p), espada (idx_e), ouro (idx_o) e copas (idx_c).
    '''
    idx_e = 0
    for i in range(len(baralho)): # percorre cada naipe do baralho
        if baralho[i][0] == 'espada': # verifica se a carta é "espada" e guarda o índice em 'idx_e'
            idx_e = i

    idx_c = 0 
    for i in range(len(baralho)): # percorre cada naipe do baralho
        if baralho[i][0] == 'copas': # verifica se a o naipe é "copas"
            idx_c = i # se for copas, a variável "idx_c" recebe "i"
    
    repetidos_paus_espada = [] # guardar as cartas de paus e espadas em comum
    idx_p = 0 
    for c in range(len(baralho)): # percorrer cada naipe do baralho
        if baralho[c][0] == 'paus': # verificar se o índice corresponde ao elemento "paus", se sim, o guarda em 'idx_p'
            idx_p = c
            for i in baralho[c][1]: # Percorre as cartas do baralho no naipe "paus"
                # verifica se a carta está dentro da lista de cartas no naipe espada, se sim, as adiciona na lista "repetidos_paus_espada"
                if i in baralho[idx_e][1]:
                    repetidos_paus_espada += [i]
    
    #faz o mesmo processo para as cartas de copas e ouro
    repetidos_copas_ouro = [] # guardar as cartas de copas e ouro em comum
    idx_o = 0
    for c in range(len(baralho)): 
        if baralho[c][0] == 'ouro': 
            idx_o = c 
            for i in baralho[c][1]: 
                if i in baralho[idx_c][1]: 
                    repetidos_copas_ouro += [i] 
                    
    return repetidos_paus_espada, repetidos_copas_ouro, idx_p, idx_e, idx_o, idx_c

def separar_pares(baralho: list[list[str, list[str]]], naipe=0, valor=0) -> tuple[list[list[str]], bool]:
    '''
    É responsável por retirar do baralho as cartas de paus e espada presente nas listas da função 'guardar_cartas_repetidas'.

    A função cria variáveis que receberação o return de 'guardar_cartas_repetidas'. A partir disso, ela percorre o tamanho de 'repetidos_paus_espada', verifica se em 'baralho' nas listas dentro do índice 'idx_e' e 'idx_p' há o elemento no índice "c", se sim, o remove de 'baralho' e a variável 'houve_par' recebe True. Depois, faz o mesmo processo percorrendo o tamanho da lista 'repetidos_copas_ouro' e utilizando as variáveis 'idx_c' e 'idx_c' para verificação. Por último, retorna o baralhi=o sem os pares e a variável 'houve_par'.

    - PARÂMETROS: 
        - baralho: lista com as cartas

    - RETURN: 
        - retorna o baralho sem os pares e a variável 'houve_par' igual a True ou False
    '''
    houve_par = False
    repetidos_paus_espada, repetidos_copas_ouro, idx_p, idx_e, idx_o, idx_c = guardar_cartas_repetidas(baralho)
    for c in range(len(repetidos_paus_espada)): # percorre a lista de cartas de paus e espadas em comum
        # verifica se no baralho de paus e espadas tem alguma carta que está na lista de cartas repetidas e as remove do respectivo naipe em "baralho", além de 'houve_par' receber True, o que significa que formou par
        if repetidos_paus_espada[c] in baralho[idx_e][1] and repetidos_paus_espada[c] in baralho[idx_p][1]: 
            houve_par = True
            baralho[idx_e][1].remove(repetidos_paus_espada[c])
            baralho[idx_p][1].remove(repetidos_paus_espada[c])
            
    # percorre a lista de cartas de copas e ouro repetidas
    for c in range(len(repetidos_copas_ouro)):
        if repetidos_copas_ouro[c] in baralho[idx_c][1] and repetidos_copas_ouro[c] in baralho[idx_o][1]:
            houve_par = True
            baralho[idx_c][1].remove(repetidos_copas_ouro[c])
            baralho[idx_o][1].remove(repetidos_copas_ouro[c])

    return baralho, houve_par

def cartas_desviradas(baralho: list[list[str, list[str]]]) -> None:
    '''
    É responsável por exibir as cartas desviradas.

    A função cria um dicionário "naipes" com as chaves correspondentes ao nome do naipe e o seu valor corresponde ao simbolo do naipe. Depois, cria um laço que percorre o tamanho de 'baralho', se a lista que está dentro do índice "i" tiver elementos: criamos a váriável "n" onde será guardado o símbolo do naipe que corresponde a chave em "naipes", printamos as linhas da carta com seus devidos símbolos multiplicando-as pelo tamanho da lista dentro de "i". Para exibir a linha do meio, a função cria um laço para percorrer a lista dentro do índice "i" e verifica se o elemento é maior ou igual à 10, se for, é preciso diminuir a largura do meio da carta, após isso, o meio da carta é printado sem quebras de linha.

    - PARÂMETROS:
        - baralho: lista com a cartas

    - RETURN:
        - None.
    '''
# a função serve para exibir as carta do jogador, com os naipes e valores
    naipes = {'paus': '♣', 'ouro': '♦', 'copas': '♥', 'espada': '♠'}
    # percorre a cartas do baralho do jogador
    for i in range(len(baralho)):
        # se nesse naipe ([i][1]) houver cartas:
        if len(baralho[i][1]) > 0:
            # "n" guarda o símbolo do naipe
            n = naipes[baralho[i][0]]
            # printa as cartas conforme a quantidade de cartas no naipe
            print('╭ — — ╮'*len(baralho[i][1]))
            print(f'|{n}    |'*len(baralho[i][1]))
            # percorre os valores das cartas no naipe (i) e os printa
            for c in baralho[i][1]:
                if c == '10':
                    print(f'|  {c} |',end='')
                else:
                    print(f'|  {c}  |',end='')
            print()
            print(f'|    {n}|'*len(baralho[i][1]))
            print('╰ — — ╯'*len(baralho[i][1]))

def cartas_viradas(baralho: list[list[str, list[str]]]) -> None:
    '''
    É responsável por printar as cartas viradas.

    A função cria as variáveis "cont" (serve para controlar o número de cartas em cada linha) e "num_carta" (número correspondente a carta). Após isso, cria um laço e percorre o tamanho de "baralho" iniciando do 1. A cada rodada do laço, "cont" é somado a 1, depois a função verifica se "i" é divisível por 20, se for: exibi cada linha da carta que é multiplicada por "cont". Para exibir o meio da carta, a função cria um laço que inicia de 0 à "cont", a cada rodada, "num_carta" é somado a 1, depois verifica-se se "num_carta" é igual à 10, se for, exibi o meio da carta com seu número corresponte e com a largura ajustada. Por último, retira 20 de "cont". Após isso, verifica se "i" é igual ao tamanho de "baralho" (final do laço), se for: exibi as cartas da mesma maneira mas sem subtrair 20 de "cont'.

    - PARÂMETROS:
        - baralho: lista de cartas.

    - RETURN:
        - None.
    '''
    cont = num_carta = 0 
    for i in range(1, contar_cartas(baralho) + 1):
        cont += 1
        if i % 20 == 0: # sempre que "i" for divisível por 20 exibimos 20 cartas a cada linha e depois subtraimos de "cont" o valor 20:
            print('╭ — — ╮'*cont) # a representação de cada linha da carta é multiplicada por 'cont'
            print('| ⧫ ⧫ |'*cont)
            for c in range(cont): # o laço serve para exibir o meio da carta com um número ao meio correspondente a "num_cartas"
                num_carta += 1
                if num_carta == 10: # o tamanho do número influencia a representação da carta, para números maiores ou iguais a 10, a largura da carta precisa ser menor
                    print(f'|  {num_carta} |', end='') # exibimos o meio da carta sem quebras de linha para garantir que elas fiquem abaixo das linhas de cima
                else:
                    print(f'|  {num_carta}  |', end='')
            print() # quebra de linha para deixar de exibir um ao lado do outro
            print('| ⧫ ⧫ |'*cont)
            print('╰ — — ╯'*cont)
            cont -= 20
        elif i == contar_cartas(baralho): # se for a ultima rodada do laço, exibimos a carta mas não subtraimos 20 de cont
            print('╭ — — ╮'*cont)
            print('| ⧫ ⧫ |'*cont)
            for c in range(cont):
                num_carta += 1
                if num_carta >= 10: 
                    print(f'|  {num_carta} |', end='')
                else:
                    print(f'|  {num_carta}  |', end='')
            print() 
            print('| ⧫ ⧫ |'*cont)
            print('╰ — — ╯'*cont)

def carta_puxada(naipe: str, valor: str) -> None:
    '''
    Exibi somente uma carta desvirada.

    A função cria um dicionário "naipes" com as chaves correspondentes ao nome do naipe e o seu valor corresponde ao simbolo do naipe. Depois, cria uma variável "n" que guarda o símbolo do naipe correspondente a chave dentro de "naipes". Por último, exibi as linhas da carta com seus devidos símbolos. Para exibir o meio da carta, verifica se "valor" é igual à 10, se sim, exibi o meio da carta com seu devido valor e tamanho ajustado.

    - PARÂMETROS:
        - carta: nome do naipe.
        - valor: valor da carta.

    - RETURN:
        - None.
    '''
    # a função irá exibir apenas uma carta virada, onde carta representa o nome do naipe e valor o valor da carta
    naipes = {'paus': '♣', 'ouro': '♦', 'copas': '♥', 'espada': '♠'}
    # "n" guarda o símbolo do naipe

    n = naipes[naipe]
    print('╭ — — ╮')
    print(f'|{n}    |')
    if valor == '10':
        print(f'|  {valor} |')
    else:
        print(f'|  {valor}  |')
    print(f'|    {n}|')
    print('╰ — — ╯')

def descobrir_carta_par(naipe, valor):
    print('\nCarta que formou par:')
    if naipe == 'copas':
        carta_puxada('ouro', valor)
    elif naipe == 'ouro':
        carta_puxada('copas', valor)
    elif naipe == 'espada':
        carta_puxada('paus', valor)
    else:
        carta_puxada('espada', valor)

def puxar_carta_computador(baralho_c: list[list[str, list[str]]], baralho_j: list[list[str, list[str]]]) -> tuple[list[list[str]], list[list[str]]]:
    '''
    É responsável para o computador puxar uma carta do jogador.

    A função cria uma variável "naipe" que guarda um número de 0 à 3, depois, verifica se o tamanho da lista dentro de "baralho_j" correspondente ao índice "naipe" é igual à 0, se sim, sorteia números até que a condição seja falsa. Após isso, cria uma variável "n" e cria um laço que percorre o tamanho de "baralho_j". Se o índice "c" for igual à "naipe": a variável "n" recebe o nome do naipe e é criado uma variável "valor" que guarda um valor sorteado dentro da lista de "naipe". Após isso, cria um laço para percorrer o tamanho de "baralho_c", se o nome do naipe dentro de "baralho_c" for igual à "n": a lista de elementos recebe "valor", depois é exibido a carta puxada e por último "baralho_c" é embaralhado e "valor" é removido de "baralho_j".

    - PARÂMETROS:
        - baralho_c: lista de cartas do computador.
        - baralho_j: lista de cartas do jogador.
    
    - RETURN:
        - Retorna "baralho_c" e "baralho_j" respectivamente.
    '''
    sleep(1)
    naipe = randint(0, 3) # sortea um naipe
    while len(baralho_j[naipe][1]) == 0:
        naipe = randint(0, 3)
    n = 0 # "n" sevirá para guardar o nome do naipe
    for c in range(len(baralho_j)): # percorre o baralho do jogador
        if c == naipe: # verifica se o indice foi igual ao naipe que foi sorteado e guarda em n
            n = baralho_j[naipe][0]
            valor = choice(baralho_j[naipe][1])
            for i in range(len(baralho_c)): # percorre o baralho do computador
                # verifica se "n" é igual ao naipe na posição "i"
                if baralho_c[i][0] == n:
                    # se for, o adiciona ao baralho do computador
                    baralho_c[i][1] += [valor]
                    print('\nCarta puxada pelo computador:')
                    carta_puxada(n, valor)
            shuffle(baralho_c) # embaralha o baralho do computador
            baralho_j[naipe][1].remove(valor) # remove a carta sorteado no naipe que também foi sorteado no baralho do jogado

    return baralho_c, baralho_j, n, valor # retorna os novos baralhos

def puxar_carta_jogador(baralho_c: list[list[str, list[str]]], baralho_j: list[list[str, list[str]]]) -> tuple[list[list[str]], list[list[str]]]:
    '''
    É responsável por pedir ao jogador uma carta para puxar do computador.

    A função exibi as cartas do computador viradas, após isso, pede um número de 1 até o tamanho de "baralho_c" e o guarda em "num", se esse número não estiver dentro do intervalo, o usuário digita o número novamente até que a condição seja falsa. Após isso, a função cria uma variável "cont" e um laço que percorre o tamanho de "baralho_c". A cada rodada, "cont" é somado à 1, depois, verifica se o tamanho da lista que está dentro do índice "i" é maior que 0, se sim, cria uma variável "naipe" que guarda o nome do naipe correspondente, depois a lista dentro de "i" é percorrido, se "cont" for igual à "num": é exibido a carta puxada pelo jogaodr e depois é criado um laço que percorre o tamanho de "baralho_j", se o nome do naipe dentro de "x" for igual à "naipe", a lista dentro de "x" recebe "c" (valor da carta) e por último, o elemento é removido de "baralho_c".

    - PARÂMETROS:
        - baralho_c: lista de cartas do baralho do computador.
        - baralho_j: lista de cartas do baralho do jogador.

    - RETURN:
        - retorna "baralho_j" e "baralho_c" respectivamente.
    '''
    sleep(1)
    print('\nPUXE UMA CARTA:\n\nA ordem das cartas correspondem aos números: ')
    cartas_viradas(baralho_c) # exibi o baralho do computador e utiliza o cont da funcão
    
    # pede ao usuário um número e verifica se esse número está no intevalo de 1 até o valor de num_cartas que corresponde ao cont
    num = int(input(f'\nEscolha uma carta de 1 à {contar_cartas(baralho_c)} para puxar: '))
    while num <= 0 or num > contar_cartas(baralho_c):
        num = int(input(f'Escolha somente números entre 1 e {contar_cartas(baralho_c)}: '))
    system('cls')
    cont = 0 # o cont servirá para comparar com "num" digitado pela pessoa
    for i in range(len(baralho_c)): # percorre o baralho do computador
        # verifica se há cartas naquele naipe para não correr o risco de o computador utilizar um naipe que não tem cartas
        if len(baralho_c[i][1]) > 0:  
            naipe = baralho_c[i][0] # guarda os naipes de cada índice
            for c in baralho_c[i][1]: # percorre a lista de valores em cada índice
                cont += 1 # a cada carta, cont é somado à 1
                if cont == num: 
                    print('\nVocê puxou essa carta: ')
                    # chama a função "exibir_carta_puxada" que recebe os parâmetros "naipe" e "c", onde naipe vai ser o naipe da carta que o jogador escolher e "c" será o valor da carta escolhida
                    carta_puxada(naipe, c)
                    for x in range(len(baralho_j)): # percorre o baralho do jogador
                        # se o índice 0 daquele naipe (x) for igual à "naipe", o baralho do jogador recebe "c"
                        if baralho_j[x][0] == naipe:
                            baralho_j[x][1] += [c]
                            valor = c
                    # remove do baralho do computador a carta escolhida
                    baralho_c[i][1].remove(c)
    
    return baralho_j, baralho_c, naipe, valor

def puxar_ultima_carta(baralho1: list[list[str, list[str]]], baralho2: list[list[str, list[str]]]) -> list[list[str]]:
    '''
    Puxa a última carta de "baralho1".

    A função cria as variáveis "naipe" e "valor", depois cria um laço que percorre o tamanho de "baralho1", se a lista dentro do índice "i" tiver o tamanho igual à 1: "naipe" recebe o nome do valor dentro de "i" e "valor" recebe o elemento dentro da lista de "i". Por último, a função cria um laço que percorre "baralho2", se o nome do naipe dentro do índice "j" for igual à "naipe": baralho2 na lista correspondente à "j" recebe "valor". Por último, chama a função "separar_pares" para retirar as cartas pares de "baralho2".

    - PARÂMETROS:
        - baralho1: baralho que têm somente uma carta.
        - baralho2: baralho que receberá a última carta.

    - RETURN:
        - retorna "baralho2".
    '''
    naipe = 0
    valor = 0
    for i in range(len(baralho1)):
        if len(baralho1[i][1]) == 1:
            naipe = baralho1[i][0]
            valor = baralho1[i][1][0]
    for j in range(len(baralho2)):
        if baralho2[j][0] == naipe:
            baralho2[j][1] += [valor]
    separar_pares(baralho2)
    return baralho2

    
def contar_cartas(baralho: list[list[str, list[str]]]) -> int:
    '''
    A função serve para contar o tamanho de "baralho". Cria uma variável "total", depois percorre o tamanho de "baralho". A cada rodada total é somado ao tamanho da lista dentro do índice "i". 

    - PARÂMETROS:
        - baralho: lista de cartas.

    - RETURN:
        - retorna "total" que corresponde a quantidade de cartas no baralho.
    '''
    # A função verifica a quantidade de cartas do baralho e guarda o resultado em "total"
    total = 0
    # percorre o indices do baralho
    for i in range(len(baralho)):
        # soma a função total o tamanho da lista naquele índice
        total += len(baralho[i][1])
    # retorna o total
    return total

def puxar_cartas_jogadores(baralho_c: list[list[str, list[str]]], baralho_j: list[list[str, list[str]]]) -> str:
    '''
    Serve para ambos jogadores puxarem cartas um do outro.

    A função cria um laço que é interrompido quando algum dos baralhos tiver somente uma carta. Primeiro, verifica se o tamanho de "baralho_c" é maior que 1, se sim, chama a função "puxar_carta_jogador", depois chama a função "separar_pares", guarda o teste lógico em "houve_par" e exibi mensagens para formação de pares ou não conforme as condições. Se "baralho_c" tiver apenas uma carta, exibi uma mensagem de que o jogador perdeu, chama "puxar_ultima_carta", exibi a última carta do jogador e retorna "COMPUTADOR". Depois, verifica se o tamanho de "baralho_j" é maior que 1, se sim, faz o mesmo processo descrito anteriomente mas adicionando a exibição do baralho do jogador ao final através da função "cartas_desviradas", se não, exibi a mensagem de que o jogador ganhou, chama "puxar_ultima_carta", exibi a última carta do computador e retorna "JOGADOR".

    - PARÂMETROS:
        - baralho_c: lista com as cartas do computador.
        - baralho_j: lista com as cartas do jogador.

    - RETURN:
        - retorna "COMPUTADOR", se o computador tiver ganho, ou "JOGADOR", se o jogador tiver ganho.
    '''
    while True:
        if contar_cartas(baralho_c) > 1: # se o computador tiver mais que uma carta, o jogador puxa uma carta, forma o par se possível e exibi o novo baralho
            baralho_j, baralho_c, naipe, valor = puxar_carta_jogador(baralho_c, baralho_j)
            baralho_j, houve_par = separar_pares(baralho_j)
            sleep(1)
            if houve_par: # verifica se foi possível a formação
                descobrir_carta_par(naipe, valor)
            else:
                print('\nNão foi possível formar um par...')
        else: # se o computador não tiver mais de uma carta, significa que ele ganhou o jogador perdeu
            print('\nO computador ficou só com uma carta... Você perdeu...\n\nSua carta restante:')
            puxar_ultima_carta(baralho_c, baralho_j)
            cartas_desviradas(baralho_j)
            return 'COMPUTADOR'
        if contar_cartas(baralho_j) > 1: # se o jogador tiver mais que uma carta, o computador puxa uma carta, forma o par se possível e exibi o novo baralho do jogador
            baralho_c, baralho_j, naipe, valor = puxar_carta_computador(baralho_c, baralho_j)
            baralho_c, houve_par = separar_pares(baralho_c)        
            if houve_par:
                descobrir_carta_par(naipe, valor)
            else:
                print('\nO computador não fez um par...')
            sleep(1)
        else: # se o jogador não tiver mais de uma carta, significa que ele ganhou e o computador perdeu 
            puxar_ultima_carta(baralho_j, baralho_c)
            print('\nVocê ficou só com uma carta... Você ganhou!\n\nCarta restante do computador:')
            cartas_desviradas(baralho_c)
            sleep(1)
            return 'JOGADOR'
        if contar_cartas(baralho_j) > 1:
            print('\nSEU NOVO BARALHO:')
            cartas_desviradas(baralho_j)

def ponto_ponto() -> None:
    for i in range(3):
        sleep(0.8)
        print('.', end='', flush=True)
    print()

def jogar(nome: str) -> str | None:
    '''
    Serve para iniciar uma partida.

    A função cria uma variável chamada "cartas", onde estão todas as cartas do baralho. Depois, sortea o jogador que terá mais cartas através da função "escolher_jogador", retira uma carta de "cartas" através da função "separar_carta_inicial", separa os baralhos para cada jogador e retira os pares através das função "separar_baralhos" e "separar_pares", exibi as cartas do jogador através da função "cartas_desviradas", inicia a parte de puxxar as cartas através da função "puxar_carta_jogadores" e por último revela a carta retirada no início e retorna "ganhou" se o jogador tiver ganho.

    - PARÂMETROS:
        - nome: nome do jogador.

    - RETURN:
        - retona a mensagem "ganhou".
    '''
    cartas = [
        ['paus', ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Q', 'J', 'K']],
        ['ouro', ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Q', 'J', 'K']],
        ['copas', ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Q', 'J', 'K']],
        ['espada', ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Q', 'J', 'K']]
    ]
    sleep(1)
    system('cls')
    print('-='*10, end=' ')
    print('JOGO DOS PARES', end=' ')
    print('-='*10)
    sorteio = escolher_jogador([nome, 'COMPUTADOR'])
    print('\nRETIRANDO UMA CARTA', end='')
    naipe, valor = separar_carta_inicial(cartas)
    ponto_ponto()
    print('\nSEPARANDO OS BARALHOS', end='')
    ponto_ponto()
    sleep(0.8)
    cartas_c, cartas_j = separar_baralhos(cartas, sorteio)
    separar_pares(cartas_c)
    separar_pares(cartas_j)
    print('\nSEU BARALHO:')
    cartas_desviradas(cartas_j)
    sleep(1)
    vencedor = puxar_cartas_jogadores(cartas_c, cartas_j)
    print('\nCARTA RETIRADA NO INÍCIO:')
    carta_puxada(naipe, valor)
    sleep(3)
    system('cls')
    if vencedor == 'JOGADOR': 
        return 'ganhou'

def regras() -> None:
    '''
    Exibi as regras do jogo.

    Na função não há parâmetros e retorna "None".
    '''
    print('-='*30, end=' ')
    print('REGRAS', end=' ')
    print('-='*30)
    print('''\nO jogo de baralho "Jogo dos Pares", conhecido popularmento como "Cagado" é um jogo de cartas disputado\npor dois jogadores onde o objetivo é não ficar com nenhuma carta ao final.

    1. No início do jogo, é separada uma carta aleátoria que não pode ser revelada.
    2. Cada jogador recebe uma quantidade de cartas a partir da divisão do baralho.
    3. Ao receber o baralho, as cartas são separadas para formarem pares, onde os naipes de cores em comum e com valores em comum fazem um par.
    4. Após ser formado todos os pares possíveis, os jogadores vão puxar carta um do outro e continua o processo de formação de par se não \nfor possível, a carta permanece na mão do jogador que a puxou.
    5. O jogador que ficar com nenhuma carta na mão é o vencedor, já que o oponente ficou com a carta par separada no início.''')

def menu() -> None:
    '''
    Exibi o menu.

    Na função não há parâmetros e retorna "None".
    '''
    print('-='*20)
    print(f'{"MENU":^{40}}')
    print('''1- Iniciar\n2- Regras\n3- Ranking\n4- Sair''')
    print('-='*20)

def opções() -> None:
    '''
    Serve para o usuário escolher alguma das opções.

    A função cria as variáveis "ja_ganhou", "partidas_ganhas" e "nome". Depois cria um laço que é interrompido quando a opção escolhida pelo jogador for igual à 4. A função cria um laço que pede ao usuário uma opção e a guarda em "opção" se o valor digitado pelo usuário não estiver no intervalo de 1 à 4, o usuário digita novamente um número, se estiver, o laço é interrompido. Quando a opção for igual a 1: "ja_jogou" é somada à 1, depois verifica se "já_jogou" é igual à 1, se sim, chama a função "cadastro" e guarda em "nome". Fora da condição, chama a função "jogar" e guarda em "resultado", se resultado for igual à "ganhou", "partidas_ganhas" é somada à 1. Quando a opção for igual à 2: chama a função "regras". Quando a função for igual à 3: chama a função "ranking". E, quando a função for igual a 4: o laço é interrompido e "nome" e "partidas_ganhas" são cadastrados através da função "cadastro_ranking".

    - PARÂMETROS:
        - não contém parâmetros.

    - RETURN:
        - retorna None.
    '''
    ja_jogou = 0
    nome = ''
    while True:
        menu()
        while True:
            opção = int(input('\nEscolha um número entre 1 e 4: '))
            if 1 <= opção <= 4:
                break
        if opção == 1:
            ja_jogou += 1
            if ja_jogou == 1:
                nome = cadastro()
            resultado = jogar(nome[:-1])
            if resultado == 'ganhou':
                cadastro_ranking(nome, 100)
        elif opção == 2:
            system('cls')
            regras()
            input('\nAperte ENTER para voltar: ')
        elif opção == 3:
            system('cls')
            cadastro_ranking(nome, 0)
            ranking()
            input('\nAperte ENTER para voltar: ')
        else:
            print('-='*10, end=' ')
            print('SAINDO', end=' ') 
            print('-='*10)
            break
    
# PROGRAMA PRINCIPAL
if __name__ == '__main__':
    opções()