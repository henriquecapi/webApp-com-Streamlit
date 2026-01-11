import io
import streamlit as st
from PIL import Image

# Função para converter uma imagem para preto e branco (escala de cinza)
def img_to_black_and_white(image):
    # Abre a imagem enviada usando a biblioteca PIL (Pillow)
    img = Image.open(image)
    # Converte a imagem para o modo 'L' (Luminância/Escala de cinza)
    return img.convert('L')

# Define o título da aplicação
st.title('Conversor de imagens')

# Widget de upload de arquivos, aceitando apenas imagens jpeg e png
file = st.file_uploader(
    'Suba sua imagem aqui!',
    type=['jpeg', 'png']
)

# Verifica se um arquivo foi carregado
if file:
    # Verifica se o tipo do arquivo é JPEG
    if file.type == 'image/jpeg':
        # Chama a função para converter a imagem
        img_bw = img_to_black_and_white(file)

        # Cria duas colunas para organizar o layout
        col_left, col_right = st.columns(2)

        # Coluna da esquerda: exibe a imagem original
        with col_left:
            st.subheader('Imagem original')
            st.image(file)

        # Coluna da direita: exibe a imagem convertida e o botão de download
        with col_right:
            st.subheader('Imagem preto e branco')
            st.image(img_bw)

            # Cria um buffer de bytes em memória (como um arquivo virtual)
            img_bytes = io.BytesIO()
            # Salva a imagem convertida no buffer no formato JPEG
            img_bw.save(img_bytes, format='JPEG')
            
            # Cria um botão para o usuário baixar a imagem processada
            st.download_button(
                label='Baixar imagem preto e branco',
                file_name='img_bw.jpg',
                data=img_bytes,
            )
    else:
        # Exibe erro se o formato não for suportado (neste caso, se não for JPEG)
        st.error('Formato de arquivo não suportado!')
else:
    # Exibe aviso se nenhum arquivo foi enviado
    st.warning('Ainda não tenho arquivo!')
