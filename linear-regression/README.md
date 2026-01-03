# 📈 Regressão Linear com Scikit-Learn

## 📖 Descrição
Este projeto implementa um modelo de **Regressão Linear** utilizando a biblioteca
**Scikit-Learn**, com o objetivo de compreender os fundamentos do
**aprendizado de máquina supervisionado**.

O modelo aprende uma relação linear entre uma variável independente (`x`)
e uma variável dependente (`y`), ajustando uma reta que melhor representa
os dados fornecidos.

---

## 🧠 Conceitos de Inteligência Artificial abordados
- Aprendizado supervisionado
- Regressão Linear
- Ajuste de modelo (model fitting)
- Previsão de valores numéricos
- Interpretação de parâmetros do modelo
- Visualização de dados

---

## 📐 Modelo matemático
A regressão linear busca aprender a seguinte equação:

y = a + b · x

Onde:
- **a** → intercepto (valor de y quando x = 0)
- **b** → coeficiente angular (inclinação da reta)

Esses parâmetros são aprendidos automaticamente durante o treinamento do modelo.

---

## 🛠 Tecnologias utilizadas
- Python
- NumPy
- Scikit-Learn
- Matplotlib

---

## 📊 Funcionamento do código

1. Define-se um conjunto de dados de entrada (`x`)
2. Define-se um conjunto de valores reais (`y`)
3. O modelo de regressão linear é treinado utilizando o método `fit`
4. São extraídos os parâmetros da reta (`intercept_` e `coef_`)
5. O modelo realiza previsões para novos valores
6. Os dados reais e a reta aprendida são exibidos em um gráfico

---

## ▶️ Exemplo de código

```python
from sklearn.linear_model import LinearRegression
import numpy as np

x = np.array([0, 25, 50, 75, 100])
y = np.array([0, 30, 60, 90, 120])

model = LinearRegression()
model.fit(x.reshape(-1, 1), y)

print("Intercepto (a):", model.intercept_)
print("Coeficiente (b):", model.coef_)

```
## 📈 Visualização dos resultados

O projeto gera um gráfico contendo:
* Pontos reais do conjunto de dados
* Reta de regressão ajustada pelo modelo
Essa visualização facilita a interpretação do comportamento do modelo
e a qualidade do ajuste.

## Como executar o projeto
```python
pip install numpy matplotlib scikit-learn
python linear_regression_sklearn.py
```
## 🧪 Aprendizados obtidos
* Uso prático de modelos de Machine Learning
* Preparação de dados para treinamento
* Interpretação dos parâmetros aprendidos
* Importância da visualização para análise de modelos
* Aplicação de IA para problemas de previsão numérica

## 👤 Autor
Pedro Barbosa de Souza
🔗 GitHub: https://github.com/PedroBarbosa239   
🔗 LinkedIn: https://www.linkedin.com/in/pedro-barbosa-de-souza/