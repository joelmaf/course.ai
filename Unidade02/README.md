# UNIDADE 2: Tratamento dos dados

2.1. Análise exploratória de dados (EDA)

2.2. Limpeza de dados

2.3. Transformação de dados

2.3.1. Divisão dos dados

2.3.2. Balanceamento

2.3.3. Escalonamento

2.3.4. Codificação e criação de features

2.4. Redução de dimensionalidade

## Análise exploratória de dados (EDA)
A Análise Exploratória de Dados (EDA) é um processo crucial para entender a estrutura, características e padrões dos dados brutos. Utilizando técnicas estatísticas e visualizações gráficas, a EDA ajuda a identificar outliers, tendências, distribuições e possíveis relações entre variáveis. Esse passo inicial é fundamental para guiar futuras etapas de modelagem e análise.

### Limpeza e transformação de dados

A limpeza e transformação de dados são passos que garantem a qualidade e a usabilidade dos dados para análises e modelagens subsequentes. Essas etapas ajudam a eliminar ruídos, melhorar a precisão dos modelos.

#### Limpeza de Dados

A limpeza de dados envolve a identificação e correção de inconsistências, erros e valores ausentes nos dados. Esse processo pode incluir a remoção de duplicatas, tratamento de valores nulos, correção de erros tipográficos e ajuste de formatos inconsistentes. A limpeza de dados é essencial para garantir a integridade e a qualidade dos dados antes da análise ou modelagem.

1. **Tratamento de Ausentes**:
    - **Remoção de Linhas/Colunas**: Linhas ou colunas com muitos valores ausentes podem ser removidas.
    - **Imputação**: Valores ausentes podem ser substituídos por valores como a média, mediana, moda ou valores derivados de métodos mais sofisticados, como K-Nearest Neighbors.

2. **Remoção de Duplicatas**:
    - Identificação e remoção de registros duplicados para evitar a contagem redundante de dados.

3. **Correção de Valores Anômalos (Outliers)**:
    - **Remoção**: Outliers que são claramente erros podem ser removidos.
    - **Transformação**: Aplicação de transformações como logarítmica para reduzir o impacto de outliers.
    - **Substituição**: Substituir outliers por valores que estejam dentro de um intervalo aceitável.

4. **Correção de Erros de Digitação**:
    - Identificação e correção de valores que foram inseridos incorretamente devido a erros de digitação ou inconsistências de formato.

5. **Normalização e Padronização**:
    - **Normalização**: Redimensiona os valores para um intervalo fixo, geralmente entre 0 e 1.
    - **Padronização**: Transforma os dados para que tenham média zero e desvio padrão um.

6. **Correção de Inconsistências de Formato**:
    - Uniformização de formatos de datas, unidades de medida e padrões de texto para garantir a consistência dos dados.

#### Transformação de Dados

A transformação de dados refere-se à modificação dos dados brutos em um formato adequado para a análise ou modelagem. Esse processo pode incluir várias etapas, como a divisão dos dados, balanceamento, escalonamento e codificação.

1. **Divisão dos dados**:
A divisão dos dados envolve separar o conjunto de dados em subconjuntos, geralmente em dados de treino e teste. Isso permite avaliar o desempenho dos modelos em dados não vistos durante o treinamento, ajudando a prevenir o overfitting e a garantir a generalização do modelo.

2. **Balanceamento**:
O balanceamento de dados é necessário quando há uma distribuição desigual entre as classes em problemas de classificação. Técnicas como oversampling, undersampling e geração de novos exemplos sintéticos são usadas para equilibrar a distribuição das classes e melhorar a performance 

3. **Codificação de Variáveis Categóricas**:
    - **Label Encoding**: Converte categorias em valores numéricos.
    - **One-Hot Encoding**: Cria colunas binárias para cada categoria, indicando a presença ou ausência da categoria.

4. **Criação de Novas Features (Feature Engineering)**:
    - **Combinação de Variáveis**: Criar novas variáveis combinando variáveis existentes.
    - **Transformações Matemáticas**: Aplicação de transformações como logaritmo, raiz quadrada ou quadrado para criar novas features.

5. **Transformação Logarítmica**:
    - Aplicada para reduzir a variação em dados altamente dispersos e trazer a distribuição mais próxima de uma distribuição normal.

6. **Detecção e Tratamento de Outliers**:
    - Aplicar métodos como o desvio interquartil ou z-score para identificar e tratar valores que se afastam significativamente dos demais dados.

7. **Agregação de Dados**:
    - Resumir dados detalhados em dados agregados, por exemplo, transformando dados diários em dados mensais para análise em nível superior.

8. **Transformações Baseadas em Domínio**:
    - Transformações específicas baseadas no conhecimento do domínio, como transformar vari modelos e fornecer uma base sólida para a tomada de decisões baseada em dados.

9. **Escalonamento de Variáveis**:
    - **Min-Max Scaling (Normalização)**: Escala os dados para que fiquem entre um intervalo específico.
    - **Z-Score Scaling (Padronização)**: Escala os dados com base na média e desvio padrão.
  
### Normalização e Padronização dos dados

* **Normalização (Min-Max Scaling)**: Utilize quando precisar que seus dados estejam em uma faixa específica, como 0 a 1, mantendo a proporcionalidade entre os valores.
  
* **Padronização (Z-score Scaling)**: Use quando for necessário comparar dados com diferentes escalas ou unidades, centralizando os dados em torno de uma média de 0 e um desvio padrão de 1.

#### Padronização (Z-score Scaling)

Padronização é o processo de transformar os dados para que tenham uma média de 0 e um desvio padrão de 1. Isso é útil quando você quer comparar dados que podem ter diferentes escalas ou unidades. Após a padronização, os dados seguem uma distribuição normal padrão.

A fórmula para padronização é:

$z = \frac{x - \mu}{\sigma}$

#### Normalização (Min-Max Scaling)

Normalização é o processo de transformar os dados para que fiquem em uma faixa específica, geralmente entre 0 e 1. Esse método é útil quando você quer manter a proporcionalidade dos dados, ou seja, o relacionamento entre os valores permanece o mesmo.

A fórmula para normalização é:

$z = \frac{x - \min(x)}{\max(x) - \min(x)}$

### Redução de dimensionalidade
A redução de dimensionalidade é o processo de reduzir o número de variáveis (features) em um conjunto de dados, preservando ao máximo a variabilidade e a informação. Técnicas como Análise de Componentes Principais (PCA) e Análise Discriminante Linear (LDA) são utilizadas para simplificar os dados, melhorar a performance dos modelos e reduzir o tempo de processamento.
