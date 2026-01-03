import numpy as np
from collections import Counter

def distancia_euclidiana(p1, p2):
    """
    Calcula a distância Euclidiana entre dois pontos.
    """
    return np.sqrt(np.sum((p1 - p2) ** 2))
 

def knn(treino_X, treino_y, ponto_teste, k):
    """
    treino_X: conjunto de dados de treinamento (features)
    treino_y: rótulos/classes do conjunto de treinamento
    ponto_teste: ponto que será classificado
    k: número de vizinhos mais próximos
    """

    distancias = []

    # Calcula a distância do ponto de teste para todos os pontos de treino
    for i in range(len(treino_X)):
        dist = distancia_euclidiana(treino_X[i], ponto_teste)
        distancias.append((dist, treino_y[i]))

    # Ordena as distâncias
    distancias.sort(key=lambda x: x[0])

    # Seleciona os k vizinhos mais próximos
    k_vizinhos = distancias[:k]

    # Obtém as classes dos vizinhos
    classes = [classe for _, classe in k_vizinhos]

    # Retorna a classe mais comum
    classe_mais_comum = Counter(classes).most_common(1)[0][0]
    return classe_mais_comum



if __name__ == "__main__":
    X_treino = np.array([
        [1, 2],
        [2, 3],
        [3, 3],
        [6, 5],
        [7, 7]
    ])

    y_treino = ['A', 'A', 'A', 'B', 'B']

    ponto = np.array([4, 4])
    k = 3

    resultado = knn(X_treino, y_treino, ponto, k)
    print(f"Classe prevista para o ponto {ponto}: {resultado}")
