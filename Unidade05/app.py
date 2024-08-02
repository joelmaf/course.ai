import streamlit as st
import joblib
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
from neuralNet import NeuralNet 
import torch

st.title("Predição de Tempo de Atravessamento")
rito = st.selectbox('Rito', ['trabalhista', 'sumaríssimo'])
tempo_servico = st.number_input('Tempo de Serviço do Reclamante (meses)', min_value=0, max_value=600, value=12)
salario = st.number_input('Último salário do reclamante', min_value=0.0, value=1000.0)
profissao = st.selectbox('Profissão do reclamante', ['comércio', 'indústria', 'serviço'])
cargo = st.selectbox('Cargo do reclamante', ['direção', 'execução'])
objeto_processo = st.selectbox('Objeto do processo', [
    'falta de registro em carteira', 'diferença salarial', 'verbas rescisórias', 'multa do Art. 477',
    'multa do Art. 467', 'horas extras e reflexos', 'fundo de garantia por tempo de serviço',
    'indenização por danos morais', 'seguro desemprego', 'vale transporte', 'adicional de insalubridade',
    'adicional noturno', 'plano de saúde'
])
quantidade_depoimento = st.number_input('Quantidade de depoimentos em cada audiência', min_value=1, max_value=200, value=10)
acordo = st.selectbox('Acordo', ['presença', 'ausência'])
pericia = st.selectbox('Necessidade de perícia', ['S', 'N'])
recurso_ordinario = st.selectbox('Solicitação de recurso ordinário', ['S', 'N'])
recurso_revista = st.selectbox('Solicitação de recurso de revista', ['S', 'N'])
audiencias = st.number_input('Número de audiências até a emissão da sentença', min_value=1, max_value=200, value=5)
tempo_audiencia = st.number_input('Tempo médio de cada audiência (minutos)', min_value=30, max_value=1000, value=120)

# Codificando variáveis categóricas
mapeamento_rito = {
    'trabalhista': 0,
    'sumaríssimo': 1
}
rito_encoded = mapeamento_rito.get(rito, -1)

mapeamento_profissao = {
    'comércio': 0,
    'indústria': 1,
    'serviço': 2
}
profissao_encoded = mapeamento_profissao.get(profissao, -1)

mapeamento_cargo = {
    'direção': 0,
    'execução': 1
}
cargo_encoded = mapeamento_cargo.get(cargo, -1)

mapeamento_objeto_processo = {
    'adicional de insalubridade': 0,
    'adicional noturno': 1,
    'diferença salarial': 2,
    'falta de registro em carteira': 3,
    'fundo de garantia por tempo de serviço': 4,
    'horas extras e reflexos': 5,
    'indenização por danos morais': 6,
    'multa do Art. 467': 7,
    'multa do Art. 477': 8,
    'plano de saúde': 9,
    'seguro desemprego': 10,
    'vale transporte': 11,
    'verbas recisórias': 12
}
objeto_processo_encoded = mapeamento_objeto_processo.get(objeto_processo, -1)


mapeamento_acordo = {
    'presença': 0,
    'ausência': 1
}
acordo_encoded = mapeamento_acordo.get(acordo, -1)

mapeamento_pericia = {
    'S': 1,
    'N': 0
}
pericia_encoded = mapeamento_pericia.get(pericia, -1)

mapeamento_recurso_ordinario = {
    'S': 1,
    'N': 0
}
recurso_ordinario_encoded = mapeamento_recurso_ordinario.get(recurso_ordinario, -1)

mapeamento_recurso_revista = {
    'S': 1,
    'N': 0
}
recurso_revista_encoded = mapeamento_recurso_revista.get(recurso_revista, -1)

# Dados de entrada para predição
input_data = {
    'rito': rito_encoded,
    'tempo_servico': tempo_servico,
    'salario': salario,
    'profissao': profissao_encoded,
    'cargo': cargo_encoded,
    'objeto_processo': objeto_processo_encoded,
    'quantidade_depoimento': quantidade_depoimento,
    'acordo': acordo_encoded,
    'pericia': pericia_encoded,
    'recurso_ordinario': recurso_ordinario_encoded,
    'recurso_revista': recurso_revista_encoded,
    'audiencias': audiencias,
    'duracao_processo':0,
    'tempo_audiencia': tempo_audiencia
}


# Normalizando os dados
scaler = joblib.load('../models/scaler.pkl')

df_servidor = pd.DataFrame([input_data])
df_normalizado = pd.DataFrame(scaler.transform(df_servidor), columns=df_servidor.columns)
df_normalizado = df_normalizado.drop(columns=['duracao_processo'])

ordem_colunas = [
       'rito', 'tempo_servico', 'salario', 'profissao', 'cargo',
       'objeto_processo', 'quantidade_depoimento', 'acordo', 'pericia',
       'recurso_ordinario', 'recurso_revista', 'audiencias', 'tempo_audiencia'
]
df_normalizado = df_normalizado[ordem_colunas]


def predict(input_data):
    model = torch.load('../models/model.pth')
    model.eval()  # Modo de avaliação
    with torch.no_grad():  # Desativa a autograd durante a predição
        input_tensor = torch.tensor(input_data.values, dtype=torch.float32)
        prediction = model(input_tensor).numpy()
    return prediction



if st.button('Prever Duração do processo (meses)'):
    predicao = predict(df_normalizado)

    # Desnormalizar a predição
    min_valor = scaler.data_min_[13]  # Obter o mínimo da última coluna, que é 'duracao_processo'
    max_valor = scaler.data_max_[13]  # Obter o máximo da última coluna, que é 'duracao_processo'
    predicao_desnormalizada = predicao[0] * (max_valor - min_valor) + min_valor
    st.metric(label="Estimativa de Duração do processo (meses)", value=f"{int(predicao_desnormalizada)}")
