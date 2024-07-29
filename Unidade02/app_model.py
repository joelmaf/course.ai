import streamlit as st
import joblib
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

st.title("Sucessão em Cargo de Liderança")

Idade = st.number_input('Idade do funcionário', min_value=18, max_value=75, value=45)
Nivel_educacao = st.selectbox('Nível de educação', ['Superior', 'Médio', 'Doutorado', 'Especialização'])
Avaliacao_desempenho = st.number_input('Avaliação de desempenho', min_value=0, max_value=5, value=3)
Experiencia_cargos_lideranca = st.number_input('Experiencia_cargos_lideranca', min_value=0, max_value=1, value=0)
Habilidades_competencias = st.number_input('Habilidades e competências', min_value=0, max_value=10, value=5)
Treinamento_lideranca = st.selectbox('Participação em treinamentos de liderança', ['S', 'N'])
Feedback_supervisores= st.slider('Feedback de supervisores', 0.0, 1.0, 0.5)
Satisfacao_trabalho = st.number_input('Satisfação no trabalho', min_value=0, max_value=5, value=3)
Coach = st.selectbox('É um bom coach', ['S', 'N'])
Empodera = st.selectbox('Empodera a equipe e não faz microgestão', ['S', 'N'])
Sucesso_membros  = st.selectbox('Exprime interesse e preocupação pelo sucesso e bem-estar pessoal dos membros da equipe ', ['S', 'N'])
Orientado_resultados = st.selectbox('É produtivo e orientado para os resultados', ['S', 'N'])
Comunicador  = st.selectbox('É bom comunicador - escuta e compartilha informações', ['S', 'N'])
Desenvolvimento_carreira = st.selectbox('Ajuda com desenvolvimento de carreira', ['S', 'N'])
Estrategia_equipe = st.selectbox('Tem uma visão clara e estratégia para a equipe', ['S', 'N'])
Habilidades_tecnicas = st.selectbox('Possui habilidades técnicas fundamentais que o ajudam a aconselhar a equipe', ['S', 'N'])




############################################################################################################################
#FAZENDO AS TRANSFORMAÇÕES IMPOSTAS NO TREINAMENTO

# Codificando variáveis categóricas
mapeamento_educacao = {
    'Superior': 4,
    'Médio': 2,
    'Doutorado': 0,
    'Especialização': 1,
    'Não Especifica':3
}
mapeamento_educacao_encoded = mapeamento_educacao.get(Nivel_educacao, -1)

mapeamento_SN = {
    'S': 1,
    'N': 0
}
mapeamento_treinamento_encoded = mapeamento_SN.get(Treinamento_lideranca, -1)
mapeamento_coach_encoded = mapeamento_SN.get(Coach, -1)
mapeamento_empodera_encoded = mapeamento_SN.get(Empodera, -1)
mapeamento_sucesso_membros_encoded = mapeamento_SN.get(Sucesso_membros, -1)
mapeamento_orientado_resultados_encoded = mapeamento_SN.get(Orientado_resultados, -1)
mapeamento_comunicador_encoded = mapeamento_SN.get(Comunicador, -1)
mapeamento_desenvolvimento_carreira_encoded = mapeamento_SN.get(Desenvolvimento_carreira, -1)
mapeamento_estrategia_equipe_encoded = mapeamento_SN.get(Estrategia_equipe, -1)
mapeamento_habilidades_tecnicas_encoded = mapeamento_SN.get(Habilidades_tecnicas, -1)

Indice_lideranca = (Experiencia_cargos_lideranca + mapeamento_treinamento_encoded + Feedback_supervisores) / 3
Indice_competencias = (Habilidades_competencias + Avaliacao_desempenho) / 2
Engajamento_desenvolvimento = (mapeamento_treinamento_encoded + Feedback_supervisores + Avaliacao_desempenho) / 3

# Dados de entrada para predição
input_data = {
    'Idade': Idade,
    'Nivel_educacao': mapeamento_educacao_encoded,
    'Avaliacao_desempenho': Avaliacao_desempenho,
    'Experiencia_cargos_lideranca': Experiencia_cargos_lideranca,
    'Habilidades_competencias': Habilidades_competencias,
    'Treinamento_lideranca': mapeamento_treinamento_encoded,
    'Feedback_supervisores': Feedback_supervisores,
    'Satisfacao_trabalho': Satisfacao_trabalho,
    'Indice_lideranca':Indice_lideranca,
    'Indice_competencias':Indice_competencias,
    'Engajamento_desenvolvimento':Engajamento_desenvolvimento,
    'Indice_lideranca':Indice_lideranca,
    'Indice_competencias':Indice_competencias,
    'Engajamento_desenvolvimento':Engajamento_desenvolvimento,
    'Coach':mapeamento_coach_encoded,
    'Empodera':mapeamento_empodera_encoded,
    'Sucesso_membros':mapeamento_sucesso_membros_encoded,
    'Orientado_resultados':mapeamento_orientado_resultados_encoded,
    'Comunicador':mapeamento_comunicador_encoded,
    'Desenvolvimento_carreira':mapeamento_desenvolvimento_carreira_encoded,
    'Estrategia_equipe':mapeamento_estrategia_equipe_encoded,
    'Habilidades_tecnicas':mapeamento_habilidades_tecnicas_encoded
}

# Adicionando as categorias de idade ao dicionário
categorias_idade = {
    'Idade_18-29': (18, 29),
    'Idade_30-39': (30, 39),
    'Idade_40-49': (40, 49),
    'Idade_50-59': (50, 59),
    'Idade_60-69': (60, 69),
    'Idade_70-79': (70, 79),
    'Idade_80-89': (80, 89)
}
def categorizar_idade(idade):
    categoria_adicionada = {}
    for categoria, (inicio, fim) in categorias_idade.items():
        if inicio <= idade <= fim:
            categoria_adicionada[categoria] = 1
        else:
            categoria_adicionada[categoria] = 0
    return categoria_adicionada
    
input_data.update(categorizar_idade(Idade))
del input_data["Idade"]

ordem_colunas = [
   'Nivel_educacao', 'Avaliacao_desempenho',
       'Experiencia_cargos_lideranca', 'Habilidades_competencias',
       'Treinamento_lideranca', 'Feedback_supervisores', 'Satisfacao_trabalho',
       'Coach', 'Empodera', 'Sucesso_membros', 'Orientado_resultados',
       'Comunicador', 'Desenvolvimento_carreira', 'Estrategia_equipe',
       'Habilidades_tecnicas', 'Idade_18-29', 'Idade_30-39', 'Idade_40-49',
       'Idade_50-59', 'Idade_60-69', 'Idade_70-79', 'Idade_80-89',
       'Indice_lideranca', 'Indice_competencias',
       'Engajamento_desenvolvimento'
]



############################################################################################################################
# NORMALIZANDO OS DADOS CONFORME NO TREINAMENTO

scaler = joblib.load('../models/scaler.pkl')

df_servidor = pd.DataFrame([input_data])
df_servidor = df_servidor[ordem_colunas]

df_normalizado = pd.DataFrame(scaler.transform(df_servidor), columns=df_servidor.columns)
df_normalizado = df_normalizado[ordem_colunas]



############################################################################################################################
# CARREGANDO O MODELO TREINADO
def predict(input_data):
    model = joblib.load('../models/model.joblib')
    prediction = model.predict(input_data)
    return prediction




if st.button('Classificação de Sucessão em Cargo de Liderança'):
    predicao = predict(df_normalizado)
    resultado = "Sim" if predicao == 1 else "Não"
    st.metric(label="Possui perfil para Cargo de Liderança baseado nos dados de cadastro:", value=f"{resultado}")

    acuracia = 0.995832
    st.info(f"Métrica de acurácia do modelo: {acuracia:.4f}")


