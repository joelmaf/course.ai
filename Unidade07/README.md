# **UNIDADE 7: Treinando Modelos LLMs**

7.1. Retrieval Augmented Generation  
7.2. Framework LangChain  
7.3. Llama 3  


# Orientação: Caso deseje executar o projeto Nvidia + Llama3 no Google Colab

Faça a importação do notebook e leve também o diretório **data**.

https://colab.research.google.com/

Descrição: Criar um motor de busca em documentos públicos recuperados do site do tribunal.

*  ouvidoria_tjdft.txt
*  sobre_nos.txt
*  canais_comunicacao.txt
*  cartilha_justica_comunitaria.txt
*  carta_servicos.txt
*  comite_distrital_saude.txt
*  atendimento_ao_cidadao.txt
*  regulamentacao.txt

Fontes:

https://www.tjdft.jus.br/ouvidoria

https://www.tjdft.jus.br/informacoes/cidadania/justica-comunitaria/publicacoes/arquivos/Cartilha_JusCom.pdf

# Configuração do ambiente para o projeto Nvidia + Llama3

### Passo 1:

Crie uma conta na Nvidia. Vá ao site da Nvidia https://build.nvidia.com/explore/discover e crie uma conta

![](images/fig32.png)

### Passo 2:

Escolha o modelo que quer usar. No curso usaremos o **meta/llama-3.1-405b-instruct**

![](images/fig34.png)

### Passo 3:

**Gere API Key** e coloque no **Secrets** do Google Colab.

![](images/fig33.png)

Caso esteja executando no Google Colab configure a  **API Key**

Para poder usar a API Key no Google Colab:

*  Abra o Google Colab e vá para Secrets.
*  Digite o Nome e o Valor do segredo. Embora o Valor possa ser alterado, o Nome não pode ser alterado. Neste código sugiro NVIDIA_KEY, mas você pode alterar
*  Ative o acesso ao Notebook.
*  Finalmente, para usá-lo no notebook, use o código fornecido com o nome do seu segredo no lugar de <secretName>


# Configuração do ambiente para o projeto LMStudio + AnythingLLM

## Instalando o LMStudio

### Passo 1: 

Faça download do LMStudio no link https://lmstudio.ai/. Escolhendo o ambiente que deseja usar. Nas aulas todos os exemplos rodarão no Linux Mint, com instalação do Linux **"LM Studio for Linux (Beta)"**

![](images/fig01.png)

Observação: recomendações de hardware/software mínimos

*  Apple Silicon Mac (M1/M2/M3) com macOS 13.6 ou mais recente
*  Windows / Linux PC ou mais recente que suporta AVX2 (tipicamente novos PCs)
*  16GB+ de RAM é recomendado. Para PCs, 6GB+ de VRAM é recomendado
*  Suporte a GPUs:  NVIDIA/AMD

### Passo 2: 

Depois de instalado na Home do LMStudio faça download do modelo LLM que deseja usar na sua aplicação. Nas aulas usaremos o **Llama 3 - 8B Instruct**, para instalar basta cricar em **Download**.

![](images/fig02.png)

### Passo 3: 

No menu a esquerda escolha a opção **Local Server**. Depois em **Select a model to load** escolha o modelo que quer carregar no servidor. Nos exemplos de sala usaremos o "Llama 3 - 8B Instruct" que foi carregado no Passo 2.

Se quiser ter certeza que tudo funcionou, pare o servidor **Stop Server** e reinicie novamente **Start Server**

![](images/fig03.png)

## Instalando o Anything LLM

### Passo 1: 

Faça download do Anything LLM no link https://anythingllm.com/download. Escolhendo o ambiente que deseja usar. Nas aulas todos os exemplos rodarão no Linux Mint, com instalação do Linux 

![](images/fig04.png)





