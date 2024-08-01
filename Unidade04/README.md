# **UNIDADE 4: Otimização e Desempenho**

4.1. Otimização de hiperparâmetros e regularização  
  4.1.1. Técnicas de avaliação de modelos  
    4.1.1.1. Overfitting e underfitting  
    4.1.1.2. Interpretabilidade dos modelos  
    4.1.1.3. Questões éticas e de viés  
  4.1.2. Validação cruzada  
  4.1.3. GridSearchCV  
  4.1.4. Avaliação de métricas 

# Avaliação do Desempenho

Erro de Treinamento é o erro medido no conjunto de dados de treinamento, já o erro de Validação/Teste é medido em dados não vistos durante o treinamento, usado para avaliar a generalização do modelo.

* **Overfitting**: Se o <b>erro</b> no conjunto de <b>treinamento é muito baixo</b>, mas o erro no conjunto de <b>validação/teste é significativamente maior</b>, o modelo pode estar overfitting.
     * Muitas features confundem o modelo.
     * Usar um modelo complexo para um problema simples.
     * Pouca regularização.
</br></br>
* **Underfitting**: Se o <b>erro</b> no conjunto de <b>treinamento e nos conjuntos de validação/teste é alto</b>, o modelo pode estar underfitting.
     * Poucas features perdem detalhes importantes.
     * Usar um modelo simples para um problema complexo.
     * Excessiva regularização limita a flexibilidade do modelo.
  
# Validação Cruzada (Cross-Validation)

Em muitos casos, a divisão simples em treino e teste é expandida com a técnica de validação cruzada. Validação Cruzada é uma técnica de avaliação que **divide o conjunto de dados em múltiplas partes** para validar o desempenho do modelo. Ela ajuda a  <span style="color:red">garantir que o modelo generaliza bem para dados não vistos</span>, ao invés de simplesmente memorizar o conjunto de treino. Nesta abordagem, o conjunto de dados é dividido em múltiplas partes, e o **modelo é treinado e testado várias vezes** em diferentes subdivisões dos dados. 

### Métodos de Validação Cruzada:

* **k-Fold Cross Validation**: Divide os dados em k dobras; em cada iteração, uma dobra é usada para teste e as outras k-1 para treino.
* **Stratified k-Fold**: Similar ao k-Fold, mas preserva a proporção de classes em cada dobra (útil para dados desbalanceados).
* **Time Series Cross Validation**: Para séries temporais, respeita a sequência temporal ao dividir os dados.

# Otimização de Hiperparâmetros

Otimização de Hiperparâmetros é o processo de encontrar a **melhor combinação de hiperparâmetros** para um modelo de aprendizado de máquina. <span style="color:red">Hiperparâmetros</span> são parâmetros que não são aprendidos durante o treinamento do modelo, mas são <span style="color:red">definidos antes do treinamento</span> e influenciam o comportamento do algoritmo.

### Métodos de Otimização:

* **Grid Search**: Explora exaustivamente uma grade de combinações de hiperparâmetros.
* **Random Search**: Seleciona combinações aleatórias de hiperparâmetros.
* **Bayesian Optimization**: Utiliza métodos probabilísticos para explorar o espaço de hiperparâmetros de forma mais eficiente.
* **Genetic Algorithms**: Utiliza princípios de evolução natural para encontrar a melhor combinação de hiperparâmetros.

```
# Definir hiperparâmetros a serem otimizados
param_grid = {
    'n_estimators': [10, 50, 100],
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

# Configurar GridSearchCV
grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=5, scoring='accuracy')

# Treinar o modelo
grid_search.fit(X_train, y_train)

# Melhor combinação de hiperparâmetros
print(f"Melhores Hiperparâmetros: {grid_search.best_params_}")

```

# Aprendizado de Máquina Automatizado (AutoML)

Aprendizado de Máquina Automatizado (AutoML) refere-se ao processo de automatização do fluxo completo de aplicação de aprendizado de máquina a problemas do mundo real. Isso inclui tarefas como pré-processamento de dados, engenharia de características, seleção de modelos, ajuste de hiperparâmetros e implantação de modelos, tudo isso sem necessitar de uma intervenção manual extensa.

Existem frameworks e bibliotecas que facilitam a comparação e avaliação de diferentes algoritmos de aprendizado de máquina. Eles oferecem ferramentas para automatizar o processo de treino, teste, validação e seleção do melhor modelo. 

## Vantagens e Desvantagens do AutoML
Vantagens:
* Mais rápido e exige menos conhecimento especializado.
* Bom para problemas simples ou quando se tem tempo ou recursos limitados.
  
Desvantagens:
* Pode produzir modelos menos precisos ou menos interpretáveis.
* Pode não ser adequado para problemas mais complexos que requerem maior controle e customização.

## Exemplos de Frameworks e Bibliotecas AutoML
* Auto-sklearn: Extensão do scikit-learn com capacidades de AutoML.
* TPOT: Usa algoritmos genéticos para otimizar pipelines de machine learning.
* H2O.ai: Plataforma de machine learning que inclui capacidades de AutoML.

  
  
