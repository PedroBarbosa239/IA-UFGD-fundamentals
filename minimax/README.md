# ♟️ Algoritmo Minimax

## 📖 Descrição
Este projeto implementa o **algoritmo Minimax**, um algoritmo clássico de
**Inteligência Artificial para jogos**, utilizado em problemas de tomada de decisão
em ambientes competitivos com dois jogadores.

O Minimax assume que:
- Um jogador (**MAX**) tenta maximizar o valor da jogada
- O outro jogador (**MIN**) tenta minimizar esse valor
- Ambos jogam de forma ótima

---

## 🧠 Conceitos de Inteligência Artificial abordados
- Tomada de decisão em jogos
- Jogos adversariais
- Árvores de decisão
- Algoritmo Minimax
- Estados terminais
- Função de avaliação

---

## 🌳 Representação em árvore
O jogo é modelado como uma **árvore de estados**, onde:
- Cada nó representa um estado do jogo
- Cada aresta representa uma jogada possível
- Folhas representam estados finais

O algoritmo avalia a árvore de baixo para cima, propagando os valores.

---

## 🧮 Funcionamento do algoritmo

1. O jogador MAX escolhe a jogada que maximiza o valor
2. O jogador MIN escolhe a jogada que minimiza o valor
3. O processo continua recursivamente até:
   - um estado terminal, ou
   - a profundidade máxima definida

---

## 📐 Pseudocódigo simplificado
```text
function minimax(estado, profundidade, maximizando):
    se estado for terminal ou profundidade == 0:
        retorna avaliação

    se maximizando:
        retorna o maior valor entre os filhos
    senão:
        retorna o menor valor entre os filhos
```

---

## 🛠 Estrutura do código

### 🔹 Função `minimax`
Parâmetros:
- `estado`: nó atual da árvore
- `profundidade`: limite de busca
- `maximizando`: indica se o jogador atual é MAX ou MIN

O código espera que o estado possua:
- `estado.terminal()` → verifica se o jogo terminou
- `estado.avaliacao()` → retorna valor heurístico
- `estado.sucessores()` → gera próximos estados

---

## 🛠 Tecnologias utilizadas
- Python

---

## ⚙️ Como executar
Este algoritmo é genérico e pode ser integrado a qualquer jogo baseado em turnos,
como:
- Jogo da velha
- Xadrez (simplificado)
- Damas
- Jogos de tabuleiro em geral

---

## 🧠 Aprendizados obtidos
- Modelagem de jogos como árvores de decisão
- Raciocínio adversarial
- Importância de funções de avaliação
- Limitações do Minimax sem poda

---

## 🚀 Possíveis melhorias futuras
- Implementar poda Alpha-Beta
- Criar um jogo completo (ex: Jogo da Velha)
- Comparar desempenho com e sem poda
- Implementar profundidade adaptativa

---

## 👤 Autor
Pedro Barbosa de Souza  
GitHub: https://github.com/PedroBarbosa239  
LinkedIn: https://www.linkedin.com/in/pedro-barbosa-de-souza/
