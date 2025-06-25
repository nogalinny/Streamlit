import streamlit as st
import pandas as pd
import plotly.express as px

@st.cache_data
def load_data():
    return pd.read_excel('ecommerce_estatistica.xlsx')

# Carregar os dados primeiro
df = load_data()

# Mostrar mensagem e as primeiras linhas para debug
st.write("Dados carregados com sucesso!")
st.write(df.head())

# Título do app
st.title('Dashboard Interativo - E-commerce')

# Gráfico 1 - Histograma das Notas dos Produtos
fig1 = px.histogram(df, x='Nota', nbins=10, title='Distribuição das Notas dos Produtos')
st.plotly_chart(fig1, use_container_width=True)

# Gráfico 2 - Histograma do Número de Avaliações
fig2 = px.histogram(df, x='N_Avaliações', nbins=20, title='Distribuição do Número de Avaliações')
st.plotly_chart(fig2, use_container_width=True)

# Gráfico 3 - Heatmap de Densidade: Avaliações x Notas
fig3 = px.density_heatmap(df, x='N_Avaliações', y='Nota', 
                          title='Produtos avaliados e suas notas', 
                          marginal_x='histogram', marginal_y='histogram')
st.plotly_chart(fig3, use_container_width=True)

# Gráfico 4 - Mapa de Calor de Correlação
df_corr = df[['Desconto', 'N_Avaliações', 'Preço', 'Qtd_Vendidos_Cod']].corr()
fig4 = px.imshow(df_corr, text_auto=True, title='Mapa de Calor - Correlação entre Variáveis')
st.plotly_chart(fig4, use_container_width=True)

# Gráfico 5 - Barra Quantidade Vendida por Temporada
fig5 = px.bar(df, x='Temporada_Cod', y='Qtd_Vendidos_Cod', 
              title='Quantidade Vendida na Temporada', color_discrete_sequence=['#90ee70'])
st.plotly_chart(fig5, use_container_width=True)

# Gráfico 6 - Pizza Quantidade Vendida por Gênero
genero_counts = df.groupby('Gênero')['Qtd_Vendidos_Cod'].sum().reset_index()
fig6 = px.pie(genero_counts, names='Gênero', values='Qtd_Vendidos_Cod', 
              title='Quantidade de Produtos Vendidos por Gênero')
st.plotly_chart(fig6, use_container_width=True)

# Gráfico 7 - Densidade de Preços
fig7 = px.density_contour(df, x='Preço_MinMax', title='Densidade de Preços')
st.plotly_chart(fig7, use_container_width=True)

# Gráfico 8 - Scatter Regressão Quantidade Vendida x Desconto
fig8 = px.scatter(df, x='Qtd_Vendidos_Cod', y='Desconto', 
                  title='Regressão de Quantidade Vendida pelo Desconto')
st.plotly_chart(fig8, use_container_width=True)
