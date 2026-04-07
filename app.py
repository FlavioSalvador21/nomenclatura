import streamlit as st
import re

def limpar_nome(nome_original):
    # 1. Remove a extensão do arquivo (.mp4, etc)
    nome = re.sub(r'\.[^.]+$', '', nome_original)
    
    # 2. Remove partes específicas (NA_, VID_, POLI_, - )
    # Adicione aqui outros termos que queira deletar
    padroes_remover = [r'_NA_', r'_VID_', r'_POLI_', r'\s-\s']
    for padrao in padroes_remover:
        nome = re.sub(padrao, ' ', nome)
    
    # 3. Substitui os underscores restantes por espaços
    nome = nome.replace('_', ' ')
    
    # 4. Remove espaços duplos extras que podem ter surgido
    nome = re.sub(r'\s+', ' ', nome).strip()
    
    return nome

# Interface Streamlit
st.set_page_config(page_title="Limpador de Nomenclatura", page_icon="📝")

st.title("✂️ Formatador de Nomes de Arquivo")
st.markdown("Cole o nome original abaixo para gerar a versão limpa.")

# Input do usuário
entrada = st.text_input("Digite o nome original:", placeholder="W2Y26_FTO_NA_...")

if entrada:
    resultado = limpar_nome(entrada)
    
    st.subheader("Resultado:")
    st.code(resultado, language=None)
    
    if st.button("Copiar para área de transferência"):
        # O Streamlit não tem acesso direto ao clipboard do sistema por segurança, 
        # mas o componente 'st.code' já oferece um botão de cópia nativo no canto superior direito.
        st.success("Texto pronto para copiar acima!")
