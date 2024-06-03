import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

st.write('**Municipios do Brasil po população**')
st.sidebar.header('Região Sudeste')

engine = create_engine('sqlite:///populacaosudeste.db', echo=True)
conn = engine.connect()
dados = pd.read_sql('populacaosudeste.db',con=conn )
df = pd.DataFrame(dados)

região = df['unidade_federativa'].drop_duplicates()
escolha_região = st.sidebar.selectbox('Escolha_região', região)

df2 = df[df['unidade_federativa']==escolha_região]

st.write('')
fig = px.box(df2, x='populacao')
st.plotly_chart(fig)

figpiz = px.pie(data_frame=df2, values='populacao', names='municipio')

st.plotly_chart(figpiz, use_container_width=True)
st.plotly_chart(figpiz,use_container_width=True)
