# 🧭 Busca em Labirinto usando BFS e DFS

## 📖 Descrição
Este projeto implementa algoritmos clássicos de **Inteligência Artificial baseada em busca**
para encontrar um caminho entre um estado inicial e um estado final em um **labirinto
representado por uma matriz**.

São utilizados conceitos de **busca em espaço de estados**, com reconstrução do caminho
solução e **visualização gráfica** do resultado por meio da biblioteca Matplotlib.

---

## 🧠 Conceitos de Inteligência Artificial abordados
- Busca em espaço de estados
- Busca não informada
- Busca em Largura (BFS – Breadth-First Search)
- Busca em Profundidade (DFS – Depth-First Search)
- Expansão de estados
- Reconstrução de caminho com predecessores
- Representação de problemas com matrizes

---

## 🧩 Representação do problema
O labirinto é representado por uma matriz bidimensional onde cada célula possui um significado:

| Valor | Significado |
|------|------------|
| '0' | Espaço livre |
| '1' | Estado inicial |
| '2' | Obstáculo |
| '3' | Estado final |

### Exemplo de labirinto
```python
matriz = [
    ['1','0','0','0'],
    ['2','2','0','2'],
    ['0','0','0','0'],
    ['0','2','2','3']
]
```

---

## 🚀 Algoritmos utilizados

### 🔹 Busca em Largura (BFS)
- Explora o espaço de estados nível por nível
- Garante encontrar o menor caminho em número de passos (custos uniformes)
- Utiliza fila (FIFO)

### 🔹 Busca em Profundidade (DFS)
- Explora um caminho até o fim antes de retroceder
- Utiliza pilha (LIFO)
- Pode não encontrar o menor caminho

📌 A diferença entre BFS e DFS neste projeto está na forma como o próximo estado é removido
da estrutura de dados utilizada.

---

## 🔄 Movimentos permitidos
O agente pode se mover para:
- Cima
- Baixo
- Esquerda
- Direita
- Diagonais (4 direções diagonais)

Totalizando **8 possíveis movimentos**, desde que não haja obstáculos.

---

## 🛠 Tecnologias utilizadas
- Python
- NumPy
- Matplotlib

---

## 📊 Funcionamento geral
1. Identificação do estado inicial e do estado final
2. Aplicação do algoritmo de busca (BFS ou DFS)
3. Expansão dos estados sucessores válidos
4. Armazenamento de predecessores para reconstrução do caminho
5. Reconstrução e visualização do caminho solução

---

## 📈 Visualização
O projeto gera um gráfico onde:
- Branco: espaço livre
- Verde: estado inicial
- Preto: obstáculos
- Vermelho: estado final
- Azul: caminho encontrado

Essa visualização facilita a análise do comportamento do algoritmo.

---

## ⚙️ Como executar
```bash
pip install numpy matplotlib
python labirinto_busca.py
```

---

## 🧪 Exemplo de saída
- Impressão do estado inicial
- Impressão do estado final
- Exibição gráfica do labirinto com o caminho solução
- Caminho retornado como lista de coordenadas

---

## 🧠 Aprendizados obtidos
- Modelagem de problemas como espaço de estados
- Implementação de algoritmos clássicos de busca
- Diferenças práticas entre BFS e DFS
- Importância da visualização para compreensão de algoritmos

---

## 🚀 Possíveis melhorias futuras
- Implementar A* com heurística
- Comparar desempenho entre BFS, DFS e A*
- Restringir ou parametrizar movimentos diagonais
- Calcular número de estados expandidos e custo do caminho

---

## 👤 Autor
Pedro Barbosa de Souza  
GitHub: https://github.com/PedroBarbosa239  
LinkedIn: https://www.linkedin.com/in/pedro-barbosa-de-souza/
