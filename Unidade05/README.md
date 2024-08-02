# **UNIDADE 5: Redes Neurais**

5.1. Estrutura básica de uma rede neural  
5.2. Arquitetura de redes neurais  
  5.2.1. Perceptron  
  5.2.2. Multilayer Perceptron  
5.3. Treinamento de redes neurais  
  5.3.1. Algoritmos de retropropagação  
  5.3.2. Otimização de pesos  
  5.3.3. Função de ativação  
5.4. Arquiteturas de Redes Neurais Profundas  

### Redes Neurais Convolucionais (CNNs)
As Redes Neurais Convolucionais (CNNs) são modelos especialmente eficazes no processamento de dados com uma estrutura de grade, como imagens. Elas utilizam camadas convolucionais para automaticamente e adaptativamente aprenderem hierarquias de características espaciais, permitindo o reconhecimento de padrões complexos. Essas redes são amplamente usadas em tarefas de visão computacional, como reconhecimento de objetos, detecção de rostos e classificação de imagens.

### Redes Neurais Recorrentes (RNNs)
As Redes Neurais Recorrentes (RNNs) são modelos projetados para processar sequências de dados, como séries temporais ou linguagem natural. Elas mantêm um estado oculto que captura informações sobre entradas anteriores, permitindo que aprendam dependências temporais. RNNs são comumente usadas em tarefas como previsão de séries temporais, tradução automática e processamento de linguagem natural.

### LSTM (Long Short-Term Memory)
As LSTM (Long Short-Term Memory) são uma variação das RNNs que abordam o problema de dependências de longo prazo. Elas utilizam uma estrutura de células que podem controlar o fluxo de informações, preservando e esquecendo dados conforme necessário. Isso permite que as LSTM aprendam e lembrem informações em sequências longas, tornando-as ideais para tarefas como tradução de idiomas, modelagem de linguagem e reconhecimento de fala.

### Redes Neurais Generativas

#### Redes Adversariais Generativas (GANs)
As Redes Adversariais Generativas (GANs) consistem em duas redes neurais competindo entre si: um gerador, que cria dados falsos, e um discriminador, que tenta distinguir entre dados reais e falsos. Esse processo adversarial resulta em geradores capazes de criar dados altamente realistas. GANs são amplamente utilizadas na geração de imagens, vídeos e música.

#### Modelo Autorregressivo
Os Modelos Autorregressivos preveem os próximos valores em uma sequência com base nos valores anteriores. Em redes neurais, isso é feito utilizando camadas que consideram entradas anteriores para gerar saídas futuras. Esses modelos são utilizados em tarefas como geração de texto, previsão de séries temporais e síntese de áudio.

#### Redes Geradoras de Momento Variacional (Variational Autoencoders - VAEs)
As Variational Autoencoders (VAEs) são um tipo de rede neural generativa que aprende uma representação latente dos dados de entrada em um espaço contínuo e probabilístico. Elas são compostas por um codificador que mapeia os dados para a representação latente e um decodificador que reconstrói os dados a partir dessa representação. VAEs são usadas para geração de imagens, modelagem de dados complexos e compressão de dados.

### Transformers
Os Transformers são uma arquitetura de rede neural projetada para lidar com sequências de dados, como texto, sem depender de processamento sequencial. Eles utilizam mecanismos de atenção que permitem que o modelo considere todas as partes da entrada simultaneamente, resultando em uma maior eficiência no treinamento. Transformers são a base de muitos modelos de linguagem avançados, como o BERT e o GPT, e são usados em tarefas como tradução automática, resumo de textos e resposta a perguntas.
