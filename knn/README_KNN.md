# 📊 K-Nearest Neighbors (KNN)

## 📖 Descrição
Este projeto implementa o algoritmo **K-Nearest Neighbors (KNN)**, um método clássico de
**aprendizado de máquina supervisionado**, utilizado para **classificação** e **regressão**.

O KNN classifica um novo dado com base nos **k vizinhos mais próximos** do conjunto de
treinamento, utilizando uma métrica de distância.

---

## 🧠 Conceitos de Inteligência Artificial abordados
- Aprendizado supervisionado
- Classificação baseada em instância
- Algoritmo KNN (K-Nearest Neighbors)
- Métrica de distância (Distância Euclidiana)
- Votação por maioria

---

## 📐 Funcionamento do algoritmo
1. Calcula a distância entre o ponto de teste e todos os pontos do conjunto de treino
2. Ordena os pontos pela distância
3. Seleciona os **k vizinhos mais próximos**
4. Realiza uma votação entre as classes dos vizinhos
5. A classe mais frequente é atribuída ao ponto de teste

---

## 📏 Métrica de distância
Neste projeto é utilizada a **Distância Euclidiana**, definida como:

d(p, q) = √(Σ (pᵢ − qᵢ)²)

---

## 🛠 Estrutura do código

### 🔹 `distancia_euclidiana`
Responsável por calcular a distância entre dois pontos no espaço n-dimensional.

### 🔹 `knn`
Função principal do algoritmo, responsável por classificar um novo ponto com base
nos k vizinhos mais próximos.

Parâmetros:
- `treino_X`: dados de treinamento
- `treino_y`: rótulos dos dados
- `ponto_teste`: novo ponto a ser classificado
- `k`: número de vizinhos

---

## 🛠 Tecnologias utilizadas
- Python
- NumPy

---

## ⚙️ Como executar

```bash
pip install numpy
python knn.py
```

---

## 🧪 Exemplo de saída
```text
Classe prevista para o ponto [4 4]: A
```

---

## 🧠 Aprendizados obtidos
- Implementação de algoritmos de Machine Learning sem bibliotecas prontas
- Importância da escolha de k
- Uso de métricas de distância
- Classificação baseada em similaridade

---

## 🚀 Possíveis melhorias futuras
- Implementar KNN para regressão
- Normalização dos dados
- Comparar diferentes valores de k
- Comparar com implementação do Scikit-Learn

---

## 👤 Autor
Pedro Barbosa de Souza  
GitHub: https://github.com/PedroBarbosa239  
LinkedIn: https://www.linkedin.com/in/pedro-barbosa-de-souza/
