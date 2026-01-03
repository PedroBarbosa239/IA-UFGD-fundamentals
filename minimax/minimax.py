def minimax(estado, profundidade, maximizando):
    '''
    estado: estado atual do jogo (nó da árvore)
    profundidade: profundidade máxima de busca
    maximizando: booleano que indica se o jogador atual é MAX ou MIN
    '''
    if profundidade == 0 or estado.terminal():
        return estado.avaliacao()

    if maximizando:
        melhor_valor = float('-inf')
        for filho in estado.sucessores():
            valor = minimax(filho, profundidade - 1, False)
            melhor_valor = max(melhor_valor, valor)
        return melhor_valor
    else:
        melhor_valor = float('inf')
        for filho in estado.sucessores():
            valor = minimax(filho, profundidade - 1, True)
            melhor_valor = min(melhor_valor, valor)
        return melhor_valor
