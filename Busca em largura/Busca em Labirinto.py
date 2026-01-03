def apresenta_solucao(estado, predecessores, matriz, M, N):
    caminho = []
    caminho.append(estado)
    while predecessores[estado] is not None:
        caminho.append(predecessores[estado])
        estado = predecessores[estado]
    caminho = caminho[::-1]

    # Criar matriz para visualização
    labirinto = np.zeros((M, N))
    for i in range(M):
        for j in range(N):
            if matriz[i][j] == '2':
                labirinto[i][j] = 2  # Obstáculo
            elif matriz[i][j] == '1':
                labirinto[i][j] = 1  # Início
            elif matriz[i][j] == '3':
                labirinto[i][j] = 3  # Fim

    # Marcar o caminho
    for pos in caminho:
        if labirinto[pos[0]][pos[1]] not in [1, 3]:  # Não sobrescrever início e fim
            labirinto[pos[0]][pos[1]] = 4  # Caminho

    # Configurar o mapa de cores
    cmap = mcolors.ListedColormap(['white', 'green', 'black', 'red', 'blue'])
    bounds = [0, 1, 2, 3, 4, 5]
    norm = mcolors.BoundaryNorm(bounds, cmap.N)

    # Plotar o labirinto
    plt.figure(figsize=(8, 8))
    plt.imshow(labirinto, cmap=cmap, norm=norm)
    plt.title('Labirinto com Solução')
    plt.grid(True, which='both', color='black', linestyle='-', linewidth=0.5)
    plt.xticks(np.arange(0, N, 1))
    plt.yticks(np.arange(0, M, 1))
    plt.show()

    return caminho
def busca_em_largura(matriz,M,N,estado_inicial,estado_final):
  estados_visitados = []
  estados_expandidos = []
  predecessores = {}

  estados_visitados.append(estado_inicial)
  predecessores[estado_inicial] = None
  solucao_encontrada = False

  while len(estados_visitados) != 0:
    estado = estados_visitados.pop(0)
    if estado in estado_final:
      solucao_encontrada = True
      break
    estados_sucessores = encontra_estados_sucessores(matriz,M,N,estado)
    estados_expandidos.append(estado)
    for sucessor in estados_sucessores:
      if sucessor not in  estados_expandidos and sucessor not in estados_visitados:
        estados_visitados.append(sucessor)
        predecessores[sucessor] = estado

  if solucao_encontrada:
    print("caminho = ",apresenta_solucao(estado,predecessores,matriz,M,N))
  else:
    print("n tem solução")

def encontra_estados_sucessores(matriz, M, N, posicao_atual):
    i = posicao_atual[0]
    j = posicao_atual[1]
    estados_sucessores = []
    if i > 0 and matriz[i-1][j] != '2':
        estados_sucessores.append((i-1, j))
    if i+1 < M and matriz[i+1][j] != '2':
        estados_sucessores.append((i+1, j))
    if j > 0 and matriz[i][j-1] != '2':
        estados_sucessores.append((i, j-1))
    if j+1 < N and matriz[i][j+1] != '2':
        estados_sucessores.append((i, j+1))
    if j > 0 and i > 0 and matriz[i-1][j-1] != '2':
        estados_sucessores.append((i-1, j-1))
    if j > 0 and i+1 < M and matriz[i+1][j-1] != '2':
        estados_sucessores.append((i+1, j-1))
    if j+1 < N and i > 0 and matriz[i-1][j+1] != '2':
        estados_sucessores.append((i-1, j+1))
    if j+1 < N and i+1 < M and matriz[i+1][j+1] != '2':
        estados_sucessores.append((i+1, j+1))
    return estados_sucessores
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


def encontraPosicao(matriz,M,N, elemento):
  posicoes = []
  for i in range(M):
    for j in range(N):
      if matriz[i][j] == elemento:
        posicoes.append((i,j))
  return posicoes

matriz =[
    ['1','0','0','0'],
    ['2','2','0','2'],
    ['0','0','0','0'],
    ['0','2','2','3']
]
M,N = 4,4
estado_inicial = encontraPosicao(matriz,M,N,'1')[0]
estado_final = encontraPosicao(matriz,M,N,'3')

print(estado_inicial)
print(estado_final)

busca_em_largura(matriz,M,N,estado_inicial,estado_final)

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors