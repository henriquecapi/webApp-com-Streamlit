import streamlit as st
from json import loads
from pandas import read_csv
import base64

# Define o título da aplicação web
st.title('Visualizador de arquivos')

# Cria um widget para upload de arquivos, especificando os tipos permitidos
file = st.file_uploader(
    'Suba seu arquivo aqui!',
    type=['txt', 'json', 'jpg', 'png', 'csv', 'py', 'mp3', 'mp4', 'pdf']
)

# Verifica se um arquivo foi carregado pelo usuário
if file:
    # Verifica o tipo MIME do arquivo para determinar como exibi-lo
    if file.type == 'text/plain':
        # Lê o conteúdo do arquivo, decodifica de bytes para string e exibe
        st.text(file.read().decode())
    elif file.type == 'application/json':
        # Carrega o JSON e exibe de forma formatada
        st.json(loads(file.read()))
    elif file.type.startswith('image'):
        # Exibe a imagem
        st.image(file)
    elif file.type == 'text/csv':
        # Lê o arquivo CSV para um DataFrame do Pandas
        df = read_csv(file)
        # Exibe o DataFrame como uma tabela interativa
        st.dataframe(df)
        # Filtra apenas colunas numéricas para gerar gráficos
        numeric_df = df.select_dtypes(include=['number'])
        if not numeric_df.empty:
            # Exibe gráficos de linha e barra
            st.line_chart(numeric_df)
            st.bar_chart(numeric_df)
    elif file.type == 'text/x-python':
        # Exibe código Python com formatação de sintaxe
        st.code(file.read().decode(), language='python')
    elif file.type == 'audio/mpeg':
        # Reproduz áudio
        st.audio(file)
    elif file.type == 'video/mp4':
        # Reproduz vídeo
        st.video(file)
    elif file.type == 'application/pdf':
        # Codifica o PDF em base64 para exibição em um iframe HTML
        base64_pdf = base64.b64encode(file.read()).decode('utf-8')
        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'
        # Renderiza o HTML (unsafe_allow_html=True é necessário para iframes)
        st.markdown(pdf_display, unsafe_allow_html=True)
    else:
        st.error('Formato de arquivo não suportado!')
else:
    # Exibe um aviso se nenhum arquivo foi carregado
    st.warning('Ainda não tenho arquivo!')
