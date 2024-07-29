import streamlit as st
import joblib
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

st.title("Predição de Casos Pendentes")
populacao = st.number_input('Tamanho da população da região', min_value=30000, max_value=500000, value=100000)
juizes_ativos = st.number_input('Número de juízes ativos', min_value=1, max_value=20, value=10)
casos_mensais = st.number_input('Número de casos recebidos mensalmente', min_value=150, max_value=800, value=300)
tipos_casos = st.selectbox('Tipo de casos comuns', ['criminal', 'civil', 'trabalhista'])
taxa_crescimento_pop = st.slider('Taxa de crescimento da população', 0.0, 1.0, 0.03)
taxa_criminalidade = st.slider('Taxa de criminalidade na região', 0.0, 1.0, 0.1)
tempo_gasto_meses = st.number_input('Média de tempo gasto em cada tipo de caso (meses)', min_value=1, max_value=24, value=12)
nivel_automacao = st.slider('Nível de automação e eficiência do tribunal', 0, 10, 8)
congestionamento = st.selectbox('Nível de congestionamento do sistema judicial', ['baixo', 'médio', 'alto'])
num_advogados = st.number_input('Número de advogados atuando na região', min_value=1, max_value=100, value=50)
urbanizacao = st.selectbox('Nível de urbanização da região', ['baixo', 'médio', 'alto'])
nivel_educacao = st.slider('Nível de educação da população na região', 0.0, 1.0, 0.8)
habitantes_por_juiz = populacao / juizes_ativos
idh = st.slider('Índice de Desenvolvimento Humano', 0.0, 1.0, 0.85)
idade_juizes = st.number_input('Média de idade dos juízes', min_value=35, max_value=60, value=45)

# Codificando variáveis categóricas
mapeamento_tipos_casos = {
    'civil': 0,
    'criminal': 1,
    'trabalhista': 2
}
tipos_casos_encoded = mapeamento_tipos_casos.get(tipos_casos, -1)

mapeamento_congestionamento = {
    'alto': 0,
    'baixo': 1,
    'medio': 3
}
nivel_congestionamento_encoded = mapeamento_congestionamento.get(congestionamento, -1)

mapeamento_nivel_urbanizacao = {
    'alto': 0,
    'baixo': 1,
    'medio': 3
}
nivel_urbanizacao_encoded = mapeamento_nivel_urbanizacao.get(urbanizacao, -1)


# Dados de entrada para predição
input_data = {
    'populacao': populacao,
    'num_juizes': juizes_ativos,
    'casos_recebidos': casos_mensais,
    'tipo_caso': tipos_casos_encoded,
    'taxa_crescimento_populacao': taxa_crescimento_pop,
    'taxa_criminalidade': taxa_criminalidade,
    'tempo_casos': tempo_gasto_meses,
    'nivel_automacao': nivel_automacao,
    'congestionamento': nivel_congestionamento_encoded,
    'advogados': num_advogados,
    'urbanizacao': nivel_urbanizacao_encoded,
    'nivel_educacao': nivel_educacao,
    'habitantes_por_juiz': habitantes_por_juiz,
    'idh': idh,
    'idade_juizes': idade_juizes,
    'casos_pendentes': 0
}

# Adicionando as categorias de idade ao dicionário
categorias_idade = {
    'idade_juizes_18-29': (18, 29),
    'idade_juizes_30-39': (30, 39),
    'idade_juizes_40-49': (40, 49),
    'idade_juizes_50-59': (50, 59),
    'idade_juizes_60-69': (60, 69),
    'idade_juizes_70-79': (70, 79),
    'idade_juizes_80-89': (80, 89)
}
def categorizar_idade(idade):
    categoria_adicionada = {}
    for categoria, (inicio, fim) in categorias_idade.items():
        if inicio <= idade <= fim:
            categoria_adicionada[categoria] = 1
        else:
            categoria_adicionada[categoria] = 0
    return categoria_adicionada
input_data.update(categorizar_idade(idade_juizes))
del input_data["idade_juizes"]

# Normalizando os dados
scaler = joblib.load('../models/scaler.pkl')

df_servidor = pd.DataFrame([input_data])
df_normalizado = pd.DataFrame(scaler.transform(df_servidor), columns=df_servidor.columns)
df_normalizado = df_normalizado.drop(columns=['casos_pendentes'])

ordem_colunas = [
    'populacao', 'num_juizes', 'casos_recebidos', 'tipo_caso',
    'taxa_crescimento_populacao', 'taxa_criminalidade', 'tempo_casos',
    'nivel_automacao', 'congestionamento', 'advogados', 'urbanizacao',
    'nivel_educacao', 'habitantes_por_juiz', 'idh',
    'idade_juizes_18-29', 'idade_juizes_30-39', 'idade_juizes_40-49',
    'idade_juizes_50-59', 'idade_juizes_60-69', 'idade_juizes_70-79',
    'idade_juizes_80-89'
]
df_normalizado = df_normalizado[ordem_colunas]


def predict(input_data):
    model = joblib.load('../models/model.pkl')
    prediction = model.predict(input_data)
    return prediction
    
if st.button('Prever Número de Casos Pendentes'):
    predicao = predict(df_normalizado)

    # Desnormalizar a predição
    min_valor = scaler.data_min_[14]  # Obter o mínimo da última coluna, que é 'casos_pendentes'
    max_valor = scaler.data_max_[14]  # Obter o máximo da última coluna, que é 'casos_pendentes'
    predicao_desnormalizada = predicao[0] * (max_valor - min_valor) + min_valor
    st.metric(label="Número de Casos Pendentes Previstos", value=f"{int(predicao_desnormalizada)}")

    # Calcular métricas de desempenho
    rmse = 0.07264765812597583
    st.info(f"RMSE: {rmse:.2f}")
