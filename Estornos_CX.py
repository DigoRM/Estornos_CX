import pandas as pd
import streamlit as st
import plotly_express as px
import plotly.graph_objects as go
import base64
from io import BytesIO


# Config Uploader
st.set_option('deprecation.showfileUploaderEncoding', False)


# Title of the app
st.set_page_config(page_title="Estornos/Chargebacks", page_icon=":bar_chart:", layout="wide")
st.title('Estornos Geral')
st.markdown('Esse é o arquivo que estou analisando:')

# Sidebar
st.sidebar.subheader("GERAL")
# Setup file upload
uploaded_file = st.sidebar.file_uploader(label="Insira o arquivo de estornos gerais", type=['csv','xlsx'])

global df
if uploaded_file is not None:

	print(uploaded_file)

	try:
		df = pd.read_csv(uploaded_file)



	except Exception as e:
		print(e)
		df = pd.read_excel(uploaded_file,engine='openpyxl')


try:
	st.dataframe(data=df,width=2000,height=150)
except Exception as e:
	print(e)

total_estornos = round(df['Valor do Estorno'].sum(),2)
maximo_estorno = df['Valor do Estorno'].max() 
quantidade_estornos = len(df)

st.subheader(f"**Total de estornos da plataforma:** R$ {total_estornos}")
st.subheader(f"**Maior valor estornado:** R$ {maximo_estorno}")
st.subheader(f"**Quantidade de Estornos:** {quantidade_estornos} estornos")

estornos_semana=df
estornos_semana['Data do Estorno'] = estornos_semana['Data do Estorno'].astype(str)
estornos_semana['Data do Estorno'] = estornos_semana['Data do Estorno'].str[:10]
estornos_semana['Data do Estorno'] =pd.to_datetime(estornos_semana['Data do Estorno'],format="%Y/%m/%d") 
estornos_semana ['Quantidade Estorno']=1


# Grafico por datas
agrupa_datas = df.groupby('Data do Estorno').sum()
agrupa_datas






st.title('Estornos CX')
st.markdown('Esse é o arquivo que estou analisando:')

# Sidebar
st.sidebar.subheader("CX")
# Setup file upload
uploaded_file = st.sidebar.file_uploader(label="Insira o arquivo Estornos de CX", type=['csv','xlsx'])

global df2
if uploaded_file is not None:

	print(uploaded_file)

	try:
		df2 = pd.read_csv(uploaded_file)



	except Exception as e:
		print(e)
		df2 = pd.read_excel(uploaded_file,engine='openpyxl')


try:
	st.dataframe(data=df2,width=2000,height=150)
except Exception as e:
	print(e)

# processo para poder efetuar operações matematicas com o horario
df2['Valor do Estorno'] = df2['Valor do Estorno'].astype(str)
df2['Valor do Estorno'] = df2['Valor do Estorno'].str.replace(r',', '.')
df2['Valor do Estorno'] = df2['Valor do Estorno'].str[3:]

df2
df2['Valor do Estorno'] = df2['Valor do Estorno'].astype(float)


total_estornos2 = df2['Valor do Estorno'].sum()
maximo_estorno2 = df2['Valor do Estorno'].max()
quantidade_estornos2 = len(df2)

influencia_valor_CX = total_estornos2/total_estornos
influencia_valor_CX = round(influencia_valor_CX * 100,2)

influencia_quantidade_CX = quantidade_estornos2/quantidade_estornos
influencia_quantidade_CX = round(influencia_quantidade_CX * 100,2)

st.subheader(f"**Total de estornos realizados por CX:** R$ {total_estornos2}")
st.subheader(f"**Maior valor Estornado:** R$ {maximo_estorno2}")
st.subheader(f"**Quantidade de Estornos:** {quantidade_estornos2} estornos")

st.markdown('##')

st.subheader(f"**Influência de CX em valores:** {influencia_valor_CX} %")

st.subheader(f"**Influência de CX em quantidade de pedidos:** {influencia_quantidade_CX} %")

estornos_semana2=df2
estornos_semana2['Data de Resolução'] = estornos_semana2['Data de Resolução'].astype(str)
estornos_semana2['Data de Resolução'] = estornos_semana2['Data de Resolução'].str[:10]
estornos_semana2['Data de Resolução'] =pd.to_datetime(estornos_semana2['Data de Resolução'],format="%d/%m/%Y") 
estornos_semana2 ['Quantidade Estorno']=1


# Grafico por datas
agrupa_datas2 = df2.groupby('Data de Resolução').sum()
agrupa_datas2

Grafico_agrupa_datas2 = px.bar(agrupa_datas2,x=agrupa_datas2.index,y='Valor do Estorno',orientation="v",title="<b>Estornos</b>")

st.plotly_chart(Grafico_agrupa_datas2,use_container_width=True)


# Agente

agrupa_agentes2 = df2.groupby('Solicitante').sum()
agrupa_agentes2

Grafico_agrupa_responsavel2 = px.bar(agrupa_agentes2,x=agrupa_agentes2.index,y='Valor do Estorno',orientation="v",title="<b>Estornos</b>")

st.plotly_chart(Grafico_agrupa_responsavel2,use_container_width=True)
